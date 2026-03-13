from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


class JarvisError(Exception):
    pass


PRIORITY_ORDER = {"P1": 1, "P2": 2, "P3": 3, "P4": 4}
RISK_ORDER = {"low": 1, "medium": 2, "high": 3}
ELIGIBLE_BUCKETS = {"broken", "ugly"}
ALLOWED_PROJECT = "WCS"
REQUIRED_TASK_FIELDS = {"task_id", "project", "bucket", "priority", "risk", "status", "title"}
PLACEHOLDER_STATUS = "draft"


ESCALATIONS_JSON_NAME = "escalations.json"
ESCALATIONS_MD_NAME = "ESCALATIONS.md"


def now_local_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def today_local_date() -> str:
    return datetime.now().astimezone().date().isoformat()


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path, expected_type: type | None = None) -> Any:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise JarvisError(f"Required JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise JarvisError(f"Invalid JSON in {path}: {exc}") from exc

    if expected_type is not None and not isinstance(data, expected_type):
        raise JarvisError(
            f"Expected {expected_type.__name__} in {path}, got {type(data).__name__}"
        )
    return data


def read_optional_json(path: Path, default: Any, expected_type: type | None = None) -> Any:
    if not path.exists():
        return default
    return read_json(path, expected_type=expected_type)


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_escalations(escalations_path: Path) -> list[dict[str, Any]]:
    """Load existing escalations, initializing an empty list if the file does not exist."""
    if not escalations_path.exists():
        return []
    data = read_json(escalations_path, expected_type=list)
    # Defensive: ensure list of dict-like items
    cleaned: list[dict[str, Any]] = []
    for item in data:
        if isinstance(item, dict):
            cleaned.append(item)
    return cleaned


def render_escalations_md(records: list[dict[str, Any]]) -> str:
    lines = ["# ESCALATIONS", ""]
    if not records:
        lines.append("_No escalations recorded._")
        return "\n".join(lines)

    for record in records:
        timestamp = normalize_text(record.get("timestamp"))
        reason_code = normalize_text(record.get("reason_code"))
        human_action_required = "yes" if bool(record.get("human_action_required")) else "no"

        lines.extend(
            [
                f"## {timestamp} - {reason_code}",
                "",
                f"- **Task ID:** {normalize_text(record.get('task_id'))}",
                f"- **Project:** {normalize_text(record.get('project'))}",
                f"- **Phase:** {normalize_text(record.get('phase'))}",
                f"- **Severity:** {normalize_text(record.get('severity'))}",
                f"- **Status:** {normalize_text(record.get('status'))}",
                f"- **Human action required:** {human_action_required}",
                f"- **Summary:** {normalize_text(record.get('summary'))}",
                "",
                "- **Details:**",
            ]
        )

        details = record.get("details")
        if isinstance(details, list) and details:
            for detail in details:
                lines.append(f"  - {normalize_text(detail)}")
        else:
            lines.append("  - (none)")

        lines.extend(
            [
                "",
                f"- **Recommended next action:** {normalize_text(record.get('recommended_next_action'))}",
                "",
            ]
        )

    return "\n".join(lines).rstrip()


def append_escalation(
    *,
    state_dir: Path,
    task_id: str,
    phase: str,
    reason_code: str,
    summary: str,
    details: list[str],
    recommended_next_action: str,
) -> None:
    """Append a durable escalation record and render the markdown view."""
    escalations_path = state_dir / ESCALATIONS_JSON_NAME
    escalations_md_path = state_dir / ESCALATIONS_MD_NAME

    records = load_escalations(escalations_path)

    record = {
        "timestamp": now_local_iso(),
        "task_id": normalize_text(task_id).upper(),
        "project": ALLOWED_PROJECT,
        "phase": phase,
        "severity": "error",
        "status": "open",
        "human_action_required": True,
        "reason_code": reason_code,
        "summary": summary,
        "details": details,
        "recommended_next_action": recommended_next_action,
    }
    records.append(record)
    write_json(escalations_path, records)
    write_text(escalations_md_path, render_escalations_md(records))

    print("")
    print("JARVIS: escalation recorded")
    print(f"- JSON: {escalations_path}")
    print(f"- Markdown: {escalations_md_path}")


def parse_task_number(task_id: str) -> int:
    task_id = normalize_text(task_id).upper()
    if not task_id.startswith("WCS-"):
        raise JarvisError(f"Expected task id like WCS-016. Got: {task_id}")
    number_part = task_id.split("-", 1)[1]
    if not number_part.isdigit():
        raise JarvisError(f"Expected numeric WCS task id suffix. Got: {task_id}")
    return int(number_part)


def task_branch_name(task_id: str) -> str:
    return f"jarvis-task-{normalize_text(task_id).lower()}"


def priority_rank(task: dict[str, Any]) -> int:
    return PRIORITY_ORDER.get(normalize_text(task.get("priority")).upper(), 999)


def risk_rank(task: dict[str, Any]) -> int:
    return RISK_ORDER.get(normalize_text(task.get("risk")).lower(), 999)


def validate_task_shape(task: dict[str, Any], *, context: str) -> None:
    missing = [field for field in sorted(REQUIRED_TASK_FIELDS) if not normalize_text(task.get(field))]
    if missing:
        raise JarvisError(f"{context}: task is missing required fields: {', '.join(missing)}")

    task_id = normalize_text(task.get("task_id")).upper()
    parse_task_number(task_id)

    project = normalize_text(task.get("project")).upper()
    if project != ALLOWED_PROJECT:
        raise JarvisError(f"{context}: task project must be {ALLOWED_PROJECT}. Found: {project}")

    bucket = normalize_text(task.get("bucket")).lower()
    if bucket not in ELIGIBLE_BUCKETS:
        raise JarvisError(
            f"{context}: task bucket must be one of {sorted(ELIGIBLE_BUCKETS)}. Found: {bucket}"
        )

    status = normalize_text(task.get("status")).lower()
    if status != "ready":
        raise JarvisError(f"{context}: task status must be ready for execution. Found: {status}")

    priority = normalize_text(task.get("priority")).upper()
    if priority not in PRIORITY_ORDER:
        raise JarvisError(f"{context}: invalid priority: {priority}")

    risk = normalize_text(task.get("risk")).lower()
    if risk not in RISK_ORDER:
        raise JarvisError(f"{context}: invalid risk: {risk}")


def validate_backlog_task_uniqueness(backlog: list[dict[str, Any]], task_id: str) -> None:
    normalized = normalize_text(task_id).upper()
    matches = [
        task for task in backlog
        if isinstance(task, dict) and normalize_text(task.get("task_id")).upper() == normalized
    ]
    if len(matches) != 1:
        raise JarvisError(
            f"Backlog must contain exactly one entry for {normalized}. Found: {len(matches)}"
        )


def is_ready_wcs_task(task: dict[str, Any]) -> bool:
    if normalize_text(task.get("project")).upper() != ALLOWED_PROJECT:
        return False
    if normalize_text(task.get("status")).lower() != "ready":
        return False
    if normalize_text(task.get("bucket")).lower() not in ELIGIBLE_BUCKETS:
        return False
    task_id = normalize_text(task.get("task_id")).upper()
    return task_id.startswith("WCS-")


def select_task(backlog: list[dict[str, Any]]) -> dict[str, Any]:
    eligible = [task for task in backlog if isinstance(task, dict) and is_ready_wcs_task(task)]
    if not eligible:
        raise JarvisError("No eligible ready WCS task found in master_backlog.json.")

    try:
        eligible.sort(
            key=lambda task: (
                priority_rank(task),
                risk_rank(task),
                parse_task_number(normalize_text(task.get("task_id"))),
            )
        )
    except JarvisError:
        raise
    except Exception as exc:
        raise JarvisError(f"Failed to sort eligible tasks: {exc}") from exc

    return eligible[0]


def get_backlog_task_by_id(backlog: list[dict[str, Any]], task_id: str) -> dict[str, Any] | None:
    normalized = normalize_text(task_id).upper()
    for task in backlog:
        if not isinstance(task, dict):
            continue
        if normalize_text(task.get("task_id")).upper() == normalized:
            return task
    return None


def task_selected_today(
    daily_plan: dict[str, Any],
    run_log: list[dict[str, Any]],
    current_date: str,
) -> dict[str, Any] | None:
    selected_task = daily_plan.get("selected_task")
    generated_at = normalize_text(daily_plan.get("generated_at"))

    if isinstance(selected_task, dict) and generated_at.startswith(current_date):
        return selected_task

    for entry in reversed(run_log):
        if not isinstance(entry, dict):
            continue
        if normalize_text(entry.get("event")) != "task_selected":
            continue
        timestamp = normalize_text(entry.get("timestamp"))
        if not timestamp.startswith(current_date):
            continue
        task_id = normalize_text(entry.get("task_id"))
        if task_id:
            return {"task_id": task_id}
    return None


def build_daily_plan(selected_task: dict[str, Any], timestamp: str) -> dict[str, Any]:
    return {
        "generated_at": timestamp,
        "selected_task": selected_task,
        "selection_reason": {
            "rule": "priority_risk_task_id",
            "details": (
                "Selected highest-priority eligible ready WCS task using deterministic "
                "ordering (priority, then risk, then numeric task id)."
            ),
        },
    }


def render_daily_plan_md(plan: dict[str, Any]) -> str:
    selected_task = plan.get("selected_task", {})
    selection_reason = plan.get("selection_reason", {})
    lines = [
        "# DAILY PLAN",
        "",
        f"**Generated at:** {normalize_text(plan.get('generated_at'))}",
        "",
        "## Selected Task",
        "",
        f"- **Task ID:** {normalize_text(selected_task.get('task_id'))}",
        f"- **Project:** {normalize_text(selected_task.get('project'))}",
        f"- **Bucket:** {normalize_text(selected_task.get('bucket'))}",
        f"- **Priority:** {normalize_text(selected_task.get('priority'))}",
        f"- **Risk:** {normalize_text(selected_task.get('risk'))}",
        f"- **Status:** {normalize_text(selected_task.get('status'))}",
        f"- **Title:** {normalize_text(selected_task.get('title'))}",
        f"- **Notes:** {normalize_text(selected_task.get('notes'))}",
        "",
        "## Selection Reason",
        "",
        f"- **Rule:** {normalize_text(selection_reason.get('rule'))}",
        f"- **Details:** {normalize_text(selection_reason.get('details'))}",
    ]
    return "\n".join(lines)


def render_run_log_md(run_log: list[dict[str, Any]]) -> str:
    lines = ["# RUN LOG", ""]
    if not run_log:
        lines.append("_No run log entries yet._")
        return "\n".join(lines)

    for entry in run_log:
        lines.extend(
            [
                f"## {normalize_text(entry.get('timestamp'))} — {normalize_text(entry.get('event'))}",
                "",
                f"- **Task ID:** {normalize_text(entry.get('task_id'))}",
                f"- **Project:** {normalize_text(entry.get('project'))}",
                f"- **Title:** {normalize_text(entry.get('title'))}",
                f"- **Summary:** {normalize_text(entry.get('summary'))}",
            ]
        )
        artifacts = entry.get("artifacts")
        if isinstance(artifacts, list) and artifacts:
            lines.append("- **Artifacts:**")
            for artifact in artifacts:
                lines.append(f"  - {normalize_text(artifact)}")
        lines.append("")
    return "\n".join(lines).rstrip()


def build_run_log_entry(
    *,
    event: str,
    selected_task: dict[str, Any],
    timestamp: str,
    summary: str,
    artifacts: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "timestamp": timestamp,
        "event": event,
        "task_id": normalize_text(selected_task.get("task_id")).upper(),
        "project": normalize_text(selected_task.get("project")).upper(),
        "title": normalize_text(selected_task.get("title")),
        "summary": summary,
        "artifacts": artifacts or [],
    }


def append_run_log_entry(
    run_log_json_path: Path,
    run_log_md_path: Path,
    run_log: list[dict[str, Any]],
    entry: dict[str, Any],
) -> None:
    run_log.append(entry)
    write_json(run_log_json_path, run_log)
    write_text(run_log_md_path, render_run_log_md(run_log))


def task_artifact_paths(workspace: Path, task_id: str) -> dict[str, Path]:
    normalized_task_id = normalize_text(task_id).upper()
    return {
        "task_json": workspace / "tasks" / f"{normalized_task_id}_task.json",
        "task_md": workspace / "tasks" / f"{normalized_task_id}_task.md",
        "worker_result": workspace / "results" / f"{normalized_task_id}_worker_result.json",
        "qa_result": workspace / "qa" / f"{normalized_task_id}_qa_result.json",
        "escalation": workspace / "logs" / f"{normalized_task_id}_escalation.json",
    }


def analyze_artifacts(artifact_map: dict[str, Path]) -> tuple[list[Path], list[Path]]:
    existing = []
    missing = []
    for path in artifact_map.values():
        if path.exists():
            existing.append(path)
        else:
            missing.append(path)
    return existing, missing


def run_packet_generator(workspace: Path, task_id: str, *, force_packet: bool) -> tuple[int, str, str]:
    helper_path = workspace / "scripts" / "generate_task_packet.py"
    if not helper_path.exists():
        raise JarvisError(f"Packet generator not found: {helper_path}")

    cmd = [
        sys.executable,
        str(helper_path),
        "--workspace",
        str(workspace),
        "--task",
        normalize_text(task_id).upper(),
    ]
    if force_packet:
        cmd.append("--force")

    result = subprocess.run(
        cmd,
        cwd=workspace,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )
    return result.returncode, result.stdout, result.stderr


def run_branch_preparer(workspace: Path, task_id: str) -> tuple[int, str, str]:
    helper_path = workspace / "scripts" / "prepare_wcs_task_branch.py"
    if not helper_path.exists():
        raise JarvisError(f"Branch preparer not found: {helper_path}")

    cmd = [
        sys.executable,
        str(helper_path),
        "--workspace",
        str(workspace),
        "--task",
        normalize_text(task_id).upper(),
    ]

    result = subprocess.run(
        cmd,
        cwd=workspace,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )
    return result.returncode, result.stdout, result.stderr


def parse_branch_prep_output(stdout: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for line in stdout.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        parsed[key.strip().upper()] = value.strip()
    return parsed


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def verify_repo_branch_state(repo_path: Path) -> dict[str, str]:
    current_branch_result = run_git(repo_path, ["branch", "--show-current"])
    if current_branch_result.returncode != 0:
        raise JarvisError(
            current_branch_result.stderr.strip() or f"Failed to inspect repo branch at {repo_path}"
        )

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        raise JarvisError(
            status_result.stderr.strip() or f"Failed to inspect repo status at {repo_path}"
        )

    current_branch = current_branch_result.stdout.strip()
    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    return {
        "current_branch": current_branch,
        "dirty": "true" if dirty_lines else "false",
        "dirty_count": str(len(dirty_lines)),
    }


def validate_task_json_contract(path: Path, expected_task: dict[str, Any]) -> None:
    data = read_json(path, expected_type=dict)
    expected_id = normalize_text(expected_task.get("task_id")).upper()

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != expected_id:
        raise JarvisError(f"{path}: task_id mismatch. Expected {expected_id}, found {actual_id}")

    required = ["task_id", "title"]
    missing = [field for field in required if not normalize_text(data.get(field))]
    if missing:
        raise JarvisError(f"{path}: missing required task packet fields: {', '.join(missing)}")


def validate_result_placeholder_contract(path: Path, expected_task_id: str, kind: str) -> None:
    data = read_json(path, expected_type=dict)
    actual_id = normalize_text(data.get("task_id")).upper()
    expected_id = normalize_text(expected_task_id).upper()

    if actual_id != expected_id:
        raise JarvisError(f"{path}: {kind} task_id mismatch. Expected {expected_id}, found {actual_id}")

    status = normalize_text(data.get("status")).lower()
    if status != PLACEHOLDER_STATUS:
        raise JarvisError(
            f"{path}: expected placeholder status '{PLACEHOLDER_STATUS}' before execution. Found: {status}"
        )

    completed_at = data.get("completed_at")
    if normalize_text(completed_at):
        raise JarvisError(f"{path}: placeholder completed_at must be blank before execution")

    if kind == "worker_result":
        for field in ["executor", "summary", "notes"]:
            if field not in data:
                raise JarvisError(f"{path}: missing worker placeholder field: {field}")
        for list_field in ["files_changed", "commands_run", "issues_encountered"]:
            value = data.get(list_field)
            if not isinstance(value, list):
                raise JarvisError(f"{path}: worker placeholder field must be a list: {list_field}")

    if kind == "qa_result":
        for field in ["qa_tool", "summary", "notes"]:
            if field not in data:
                raise JarvisError(f"{path}: missing QA placeholder field: {field}")
        for list_field in ["checks_run", "checks_passed", "checks_failed", "artifacts"]:
            value = data.get(list_field)
            if not isinstance(value, list):
                raise JarvisError(f"{path}: QA placeholder field must be a list: {list_field}")


def validate_existing_artifacts(
    artifact_map: dict[str, Path],
    selected_task: dict[str, Any],
) -> None:
    task_id = normalize_text(selected_task.get("task_id")).upper()

    if not artifact_map["task_md"].exists():
        raise JarvisError(f"Existing packet set is invalid: missing markdown packet: {artifact_map['task_md']}")
    if not artifact_map["escalation"].exists():
        raise JarvisError(
            f"Existing packet set is invalid: missing escalation file: {artifact_map['escalation']}"
        )

    validate_task_json_contract(artifact_map["task_json"], selected_task)
    validate_result_placeholder_contract(artifact_map["worker_result"], task_id, "worker_result")
    validate_result_placeholder_contract(artifact_map["qa_result"], task_id, "qa_result")


def validate_generated_placeholders(
    artifact_map: dict[str, Path],
    selected_task: dict[str, Any],
) -> None:
    for path in artifact_map.values():
        if not path.exists():
            raise JarvisError(f"Expected generated artifact not found after packet generation: {path}")

    validate_existing_artifacts(artifact_map, selected_task)


def print_mode_banner(mode: str) -> None:
    print("=" * 72)
    print(f"JARVIS MODE: {mode}")
    print("=" * 72)


def print_packet_placeholder_warning(task_id: str, artifact_map: dict[str, Path], skipped_existing: bool) -> None:
    print("")
    print("JARVIS: artifact safety warning")
    print(
        "These task packet result files are placeholders until the worker result and QA result are filled truthfully."
    )
    print("They are NOT execution proof and do NOT mean the task is reconcile-ready.")
    print(f"- Worker placeholder: {artifact_map['worker_result']}")
    print(f"- QA placeholder:     {artifact_map['qa_result']}")
    print(f"- Escalation file:   {artifact_map['escalation']}")
    if skipped_existing:
        print("")
        print("JARVIS: packet generation was skipped because all artifacts already exist.")
        print("That does NOT mean the task is complete.")
        print("Existing packet/result artifacts were contract-validated before continuing.")
        print("Inspect existing worker/QA result contents before relying on them.")


def print_result_contracts() -> None:
    print("")
    print("JARVIS: result contracts")
    print("- Worker result status must be one of: worker_complete | blocked | escalated")
    print("- QA result status must be one of: qa_pass | qa_fail | escalated")
    print("- Keep completed_at blank in worker/QA result files until stamp_result_timestamp.py runs")


def print_contract_validation_summary(
    selected_task: dict[str, Any],
    packet_validated: bool,
    task_validated: bool,
) -> None:
    print("")
    print("JARVIS: contract validation")
    print(f"- Selected task execution-eligible: {'yes' if task_validated else 'no'}")
    print(f"- Packet/result placeholder contract valid: {'yes' if packet_validated else 'no'}")
    print(f"- Selected task: {normalize_text(selected_task.get('task_id')).upper()}")


def print_next_steps(
    selected_task: dict[str, Any],
    workspace: Path,
    repo_path: Path,
    artifact_map: dict[str, Path],
    branch_name: str,
) -> None:
    task_id = normalize_text(selected_task.get("task_id")).upper()
    print("")
    print("JARVIS: foreman phase complete")
    print("TASK IS NOT COMPLETE YET")
    print("Do NOT run reconcile until code is committed, worker result is final, QA result is final, and both are stamped.")
    print("")
    print("Next steps:")
    print(f"1. Open repo: {repo_path}")
    print("2. Verify git state:")
    print("   - git branch --show-current")
    print("   - git status")
    print(f"3. Confirm branch is: {branch_name}")
    print("4. Review task packet:")
    print(f"   - {artifact_map['task_json']}")
    print(f"   - {artifact_map['task_md']}")
    print("5. Perform the bounded implementation only")
    print("6. Inspect the diff before commit")
    print(f"   - git diff -- {normalize_text(selected_task.get('notes')) or '<target_file>'}")
    print("7. Commit on the correct task branch")
    print(f"8. Finalize worker result JSON: {artifact_map['worker_result']}")
    print("9. Run QA (current live path):")
    print("   - npm run build")
    print("   - npm run test:e2e:smoke")
    print(f"10. Finalize QA result JSON: {artifact_map['qa_result']}")
    print("11. Stamp timestamps:")
    print(f"   - python .\\stamp_result_timestamp.py ..\\results\\{task_id}_worker_result.json")
    print(f"   - python .\\stamp_result_timestamp.py ..\\qa\\{task_id}_qa_result.json")
    print("12. Reconcile only when ready:")
    print(f"   - python .\\reconcile_task_outcome.py --task {task_id}")
    print("")
    print("Working process/documentation files should be updated whenever a new process rule or hardening change is locked in.")
    print(f"Workspace: {workspace}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Jarvis foreman v6: select or reuse one WCS task, validate task/artifact contracts, generate packet artifacts, prepare the correct repo branch, and print operator-safe handoff guidance."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow a new selection even if a WCS task was already selected today.",
    )
    parser.add_argument(
        "--force-packet",
        action="store_true",
        help="Force overwrite of existing task packet/result/qa/escalation files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    script_path = Path(__file__).resolve()
    workspace = script_path.parent.parent
    state_dir = workspace / "state"

    backlog_path = state_dir / "master_backlog.json"
    project_status_path = state_dir / "project_status_wcs.json"
    daily_plan_json_path = state_dir / "daily_plan.json"
    daily_plan_md_path = state_dir / "DAILY_PLAN.md"
    run_log_json_path = state_dir / "run_log.json"
    run_log_md_path = state_dir / "RUN_LOG.md"

    try:
        backlog = read_json(backlog_path, expected_type=list)
        project_status_wcs = read_json(project_status_path, expected_type=dict)
        daily_plan = read_optional_json(daily_plan_json_path, default={}, expected_type=dict)
        run_log = read_optional_json(run_log_json_path, default=[], expected_type=list)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id="",
            phase="jarvis_state_load",
            reason_code="invalid_json_state",
            summary="Jarvis failed to load required JSON state during startup.",
            details=[str(exc)],
            recommended_next_action="Inspect the referenced JSON file, repair or restore it, then rerun jarvis.py.",
        )
        print("JARVIS: hard failure while loading required JSON state.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    current_date = today_local_date()
    current_timestamp = now_local_iso()

    used_existing_selection = False
    mode_banner = "NEW_SELECTION_NO_EXISTING_TODAY_TASK"

    try:
        if not args.force:
            existing_today = task_selected_today(daily_plan, run_log, current_date)
            if existing_today:
                existing_task_id = normalize_text(existing_today.get("task_id"))
                backlog_match = get_backlog_task_by_id(backlog, existing_task_id)
                if not backlog_match:
                    raise JarvisError(
                        f"Daily plan references task {existing_task_id}, but that task was not found in master_backlog.json."
                    )
                selected_task = backlog_match
                used_existing_selection = True
                mode_banner = "REUSING_ALREADY_SELECTED_TASK"
            else:
                selected_task = select_task(backlog)
        else:
            selected_task = select_task(backlog)
            mode_banner = "FORCED_FRESH_SELECTION"

        task_id = normalize_text(selected_task.get("task_id")).upper()
        validate_backlog_task_uniqueness(backlog, task_id)
        validate_task_shape(selected_task, context=f"Selected task {task_id}")
        task_validated = True
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=locals().get("task_id", ""),
            phase="jarvis_selection",
            reason_code="invalid_selected_task",
            summary="Jarvis failed to select a valid execution-eligible WCS task.",
            details=[str(exc)],
            recommended_next_action="Inspect the backlog entry and project status for this task, correct invalid fields or duplicates, then rerun jarvis.py.",
        )
        print("JARVIS: task selection/validation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    if not used_existing_selection:
        plan = build_daily_plan(selected_task, current_timestamp)
        selection_entry = build_run_log_entry(
            event="task_selected",
            selected_task=selected_task,
            timestamp=current_timestamp,
            summary="Jarvis selected task for current daily plan.",
        )

        write_json(daily_plan_json_path, plan)
        write_text(daily_plan_md_path, render_daily_plan_md(plan))
        append_run_log_entry(run_log_json_path, run_log_md_path, run_log, selection_entry)
    else:
        plan = daily_plan

    artifact_map = task_artifact_paths(workspace, task_id)
    existing_artifacts, missing_artifacts = analyze_artifacts(artifact_map)

    packet_generated = False
    packet_skipped_existing = False
    packet_contract_validated = False

    if existing_artifacts and missing_artifacts and not args.force_packet:
        message = (
            "Partial packet artifact state detected. Some packet files already exist, but not all of them. "
            "Inspect the task artifacts and rerun with --force-packet only if overwrite is intentional.\n"
            + "\n".join(f"- existing: {path}" for path in existing_artifacts)
            + "\n"
            + "\n".join(f"- missing: {path}" for path in missing_artifacts)
        )
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_packet_validation",
            reason_code="partial_packet_artifacts",
            summary="Jarvis detected partial packet artifact state for the selected task.",
            details=[message],
            recommended_next_action="Inspect existing/missing packet artifacts, decide whether to clean up or rerun with --force-packet, then rerun jarvis.py.",
        )
        print("JARVIS: partial packet artifact state detected.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    try:
        if existing_artifacts and not missing_artifacts and not args.force_packet:
            validate_existing_artifacts(artifact_map, selected_task)
            packet_contract_validated = True
            packet_skipped_existing = True
        else:
            returncode, packet_stdout, packet_stderr = run_packet_generator(
                workspace,
                task_id,
                force_packet=args.force_packet,
            )

            if returncode != 0:
                append_escalation(
                    state_dir=state_dir,
                    task_id=task_id,
                    phase="jarvis_packet_validation",
                    reason_code="packet_contract_mismatch",
                    summary="Jarvis packet generator reported a non-zero exit code.",
                    details=[
                        f"Return code: {returncode}",
                        f"STDERR: {packet_stderr.strip() or '(no stderr output)'}",
                    ],
                    recommended_next_action="Inspect generate_task_packet.py output, fix the underlying issue, then rerun jarvis.py (optionally with --force-packet).",
                )
                print("JARVIS: packet generation failed.", file=sys.stderr)
                print("An escalation record was written for operator follow-up.", file=sys.stderr)
                raise SystemExit(returncode)

            validate_generated_placeholders(artifact_map, selected_task)
            packet_contract_validated = True
            packet_generated = True
            packet_event = build_run_log_entry(
                event="task_packet_generated",
                selected_task=selected_task,
                timestamp=now_local_iso(),
                summary="Jarvis generated task packet and contract-valid placeholder execution artifacts.",
                artifacts=[str(path) for path in artifact_map.values()],
            )
            append_run_log_entry(run_log_json_path, run_log_md_path, run_log, packet_event)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_packet_validation",
            reason_code="packet_contract_mismatch",
            summary="Jarvis detected invalid or mismatched packet/result placeholder contracts.",
            details=[str(exc)],
            recommended_next_action="Inspect the generated packet and result placeholder files, correct the contract shape, then rerun jarvis.py (optionally with --force-packet).",
        )
        print("JARVIS: packet/result placeholder contract validation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    branch_returncode, branch_stdout, branch_stderr = run_branch_preparer(workspace, task_id)

    if branch_returncode != 0:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_preparation",
            reason_code="branch_prepare_failed",
            summary="Jarvis branch preparer reported a non-zero exit code.",
            details=[
                f"Return code: {branch_returncode}",
                f"STDERR: {branch_stderr.strip() or '(no stderr output)'}",
            ],
            recommended_next_action="Inspect prepare_wcs_task_branch.py output and the WCS repo state, fix issues, then rerun jarvis.py.",
        )
        print("JARVIS: branch preparation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(branch_returncode)

    branch_info = parse_branch_prep_output(branch_stdout)
    target_branch = branch_info.get("TARGET_BRANCH", task_branch_name(task_id))
    repo_path = Path(
        branch_info.get("REPO_PATH") or normalize_text(project_status_wcs.get("repo_path"))
    ).resolve()

    try:
        verified_repo_state = verify_repo_branch_state(repo_path)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_verification",
            reason_code="repo_inspection_failed",
            summary="Jarvis failed to inspect the WCS repo branch/status after preparation.",
            details=[str(exc)],
            recommended_next_action="Inspect the WCS repo manually (branch and status), resolve issues, then rerun jarvis.py.",
        )
        print("JARVIS: repo branch/status inspection failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    branch_mode = branch_info.get("MODE", "")
    if branch_mode in {"switched_to_existing_target", "created_new_target_from_main"}:
        branch_event = build_run_log_entry(
            event="task_branch_prepared",
            selected_task=selected_task,
            timestamp=now_local_iso(),
            summary=f"Jarvis prepared repo branch for task execution: {target_branch}",
            artifacts=[target_branch, str(repo_path)],
        )
        append_run_log_entry(run_log_json_path, run_log_md_path, run_log, branch_event)

    print_mode_banner(mode_banner)

    if used_existing_selection:
        print("JARVIS: using existing task selected today")
    else:
        print("JARVIS: task selected")
        print(f"Workspace: {workspace}")
        print(f"Priority: {normalize_text(selected_task.get('priority'))}")
        print(f"Risk: {normalize_text(selected_task.get('risk'))}")
        print(f"Bucket: {normalize_text(selected_task.get('bucket'))}")
        print(f"daily_plan.json: {daily_plan_json_path}")
        print(f"DAILY_PLAN.md: {daily_plan_md_path}")
        print(f"run_log.json: {run_log_json_path}")
        print(f"RUN_LOG.md: {run_log_md_path}")

    print(f"Task ID: {task_id}")
    print(f"Title: {normalize_text(selected_task.get('title'))}")

    print("")
    if packet_skipped_existing:
        print("JARVIS: packet generation skipped")
        print("Reason: all packet artifacts already exist for this task. Use --force-packet to overwrite.")
        for path in artifact_map.values():
            print(f"- {path}")
    elif packet_generated:
        print("JARVIS: packet generation complete")
        for path in artifact_map.values():
            print(f"WROTE: {path}")
        print("")
        print("Task packet generation complete.")
        print(f"Task packet markdown: {artifact_map['task_md']}")
        print(f"Task packet JSON:     {artifact_map['task_json']}")

    print("")
    print("JARVIS: branch preparation result")
    for line in branch_stdout.strip().splitlines():
        print(line)

    print("")
    print("JARVIS: final branch verification")
    print(f"VERIFIED_REPO_PATH: {repo_path}")
    print(f"VERIFIED_CURRENT_BRANCH: {verified_repo_state['current_branch']}")
    print(f"VERIFIED_EXPECTED_BRANCH: {target_branch}")
    print(f"VERIFIED_DIRTY: {verified_repo_state['dirty']}")
    print(f"VERIFIED_DIRTY_COUNT: {verified_repo_state['dirty_count']}")

    if verified_repo_state["current_branch"] != target_branch:
        details = [
            "Post-branch-prep verification failed. Repo is not on the expected task branch.",
            f"Expected: {target_branch}",
            f"Actual:   {verified_repo_state['current_branch']}",
        ]
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_verification",
            reason_code="branch_verification_failed",
            summary="Jarvis detected a branch mismatch after branch preparation.",
            details=details,
            recommended_next_action="Switch the WCS repo to the expected task branch or repair the branch state, then rerun jarvis.py.",
        )
        print("JARVIS: post-branch-prep branch verification failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    print_contract_validation_summary(selected_task, packet_contract_validated, task_validated)
    print_packet_placeholder_warning(task_id, artifact_map, packet_skipped_existing)
    print_result_contracts()
    print_next_steps(selected_task, workspace, repo_path, artifact_map, target_branch)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except JarvisError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        # Record a generic escalation when a JarvisError bubbles out that was not already
        # handled by a more specific escalation path.
        script_path = Path(__file__).resolve()
        state_dir = script_path.parent.parent / "state"
        try:
            append_escalation(
                state_dir=state_dir,
                task_id="",
                phase="jarvis_preflight",
                reason_code="invalid_json_state",
                summary="Jarvis encountered an unhandled JarvisError.",
                details=[str(exc)],
                recommended_next_action="Inspect the error message and recent changes, repair the underlying issue, then rerun jarvis.py.",
            )
        except Exception:
            # If escalation writing itself fails, avoid masking the original error.
            pass
        print("JARVIS: an escalation record may have been written for this failure.", file=sys.stderr)
        raise SystemExit(1)
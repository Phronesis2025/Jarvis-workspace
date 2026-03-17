from __future__ import annotations

import argparse
import json
import re
import sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

VALID_STATUSES = {
    "draft",
    "ready",
    "dispatched",
    "in_progress",
    "worker_complete",
    "qa_pass",
    "qa_fail",
    "blocked",
    "escalated",
    "done",
    "deferred",
}

DEFAULT_PROJECT_CONFIG = {
    "WCS": {
        "repo_path": r"C:\dev\wcsv2.0-new",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": [
            "Run npm run build",
            "Start local app with npm run dev",
            "Run Playwright smoke QA if available",
            "Verify the targeted change locally in the browser",
        ],
        "default_stop_conditions": [
            "Required file cannot be found",
            "Build fails for unrelated reasons",
            "Task scope expands beyond the targeted fix",
        ],
    },
    "N8N": {
        "repo_path": "",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": [
            "Validate workflow or prompt output against the task rubric",
            "Confirm no malformed JSON or broken node configuration",
        ],
        "default_stop_conditions": [
            "Required workflow file cannot be found",
            "Task scope expands beyond the targeted fix",
            "Quality cannot be verified with the current rubric",
        ],
    },
}

TASK_MD_TEMPLATE = """# TASK PACKET

## Header
- Task ID: {task_id}
- Project: {project}
- Title: {title}
- Bucket: {bucket}
- Priority: {priority}
- Risk: {risk}
- Status: {status}

## Repo
- Repo Path: `{repo_path}`
- Branch Name: `{branch_name}`

## Problem Summary
{problem_summary}

## Goal
{goal}

## Suspected Files
{suspected_files_md}

## Acceptance Criteria
{acceptance_criteria_md}

## QA Plan
{qa_plan_md}

## System Impact
{system_impact}

## Stop Conditions
{stop_conditions_md}

## Notes
{notes}
"""


def now_local() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


class PacketGenerationError(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PacketGenerationError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PacketGenerationError(f"Invalid JSON in {path}: {exc}") from exc



def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")



def is_path_like(value: str) -> bool:
    """
    Treat only clear repo-path-looking values as bounded file scope.
    Examples: 'src/components/Hero.tsx', 'app/about/page.tsx'.
    """
    v = value.strip()
    if not v:
        return False
    lower = v.lower()
    if "/" in v:
        return True
    for ext in (".tsx", ".ts", ".jsx", ".js", ".css", ".scss", ".md"):
        if lower.endswith(ext):
            return True
    return False



def parse_notes_to_files(notes: str) -> list[str]:
    if not notes:
        return []
    cleaned = notes.replace("`", "").strip()
    parts = [part.strip() for part in re.split(r",|;", cleaned) if part.strip()]
    # Only keep values that clearly look like bounded repo paths.
    return [part for part in parts if is_path_like(part)]



def humanize_title_to_problem(title: str) -> str:
    title = title.strip()
    if not title:
        return "Describe the current issue clearly before execution."
    return f"{title}."



def goal_from_title(title: str) -> str:
    if not title.strip():
        return "Complete the scoped task and verify the result."
    return f"Resolve: {title}, with the smallest safe change that satisfies QA."



def acceptance_from_backlog(item: dict[str, Any], suspected_files: list[str]) -> list[str]:
    project = item.get("project", "")
    title = item.get("title", "")
    criteria = [f"The scoped issue is resolved: {title}"] if title else ["The scoped issue is resolved"]
    if project == "WCS":
        criteria.extend([
            "App builds successfully with npm run build",
            "Local app can be opened for verification",
            "Targeted change is visible or behaves correctly on the relevant page/flow",
        ])
    elif project == "N8N":
        criteria.extend([
            "Workflow or prompt output passes the defined quality/rubric check",
            "No malformed JSON or broken node configuration is introduced",
        ])
    if suspected_files:
        criteria.append("Changes remain tightly limited to the suspected files unless a clearly related helper/config file must also be updated")
    return criteria



def system_impact_from_risk(project: str, risk: str, suspected_files: list[str]) -> str:
    base = {
        "low": "Low risk.",
        "medium": "Medium risk.",
        "high": "High risk.",
    }.get(risk, "Risk level not specified.")
    if suspected_files:
        scope = f" Primary expected scope: {', '.join(suspected_files)}."
    else:
        scope = " Scope should stay tightly bounded to the targeted issue."
    if project == "WCS":
        return base + " This should avoid unrelated production-facing behavior changes unless strictly necessary." + scope
    if project == "N8N":
        return base + " This should avoid unrelated workflow, credential, or publishing changes unless strictly necessary." + scope
    return base + scope



def bulletize(items: list[str], fallback: str) -> str:
    if not items:
        return f"- {fallback}"
    return "\n".join(f"- {item}" for item in items)



def build_packet_json(item: dict[str, Any], project_cfg: dict[str, Any], dispatch: bool) -> dict[str, Any]:
    task_id = item["task_id"]
    project = item["project"]
    notes = str(item.get("notes", "") or "")
    suspected_files = parse_notes_to_files(notes)
    if not suspected_files:
        raise PacketGenerationError(
            f"Unable to derive bounded file scope for task packet generation for {task_id}."
        )
    ts = now_local()
    status = "dispatched" if dispatch else str(item.get("status", "ready") or "ready")
    if status not in VALID_STATUSES:
        raise PacketGenerationError(f"Task {task_id} has unsupported status: {status}")

    packet = {
        "task_id": task_id,
        "project": project,
        "title": str(item.get("title", "") or ""),
        "bucket": str(item.get("bucket", "") or ""),
        "priority": str(item.get("priority", "") or ""),
        "risk": str(item.get("risk", "") or ""),
        "status": status,
        "repo_path": project_cfg.get("repo_path", ""),
        "branch_name": f"{project_cfg.get('branch_prefix', 'jarvis-task-')}{task_id.lower()}",
        "problem_summary": humanize_title_to_problem(str(item.get("title", "") or "")),
        "goal": goal_from_title(str(item.get("title", "") or "")),
        "suspected_files": suspected_files,
        "acceptance_criteria": acceptance_from_backlog(item, suspected_files),
        "qa_plan": deepcopy(project_cfg.get("default_qa_plan", [])),
        "system_impact": system_impact_from_risk(project, str(item.get("risk", "") or ""), suspected_files),
        "stop_conditions": deepcopy(project_cfg.get("default_stop_conditions", [])),
        "notes": notes,
        "created_at": ts,
        "updated_at": ts,
    }
    impl = item.get("implementation_instruction")
    if impl and isinstance(impl, str) and impl.strip():
        packet["implementation_instruction"] = impl.strip()
    return packet



def build_packet_markdown(packet: dict[str, Any]) -> str:
    suspected_files_md = bulletize(packet.get("suspected_files", []), "Confirm the target files before execution")
    acceptance_md = bulletize(packet.get("acceptance_criteria", []), "Add acceptance criteria before execution")
    qa_plan_md = bulletize(packet.get("qa_plan", []), "Add a QA plan before execution")
    stop_md = bulletize(packet.get("stop_conditions", []), "Add stop conditions before execution")
    notes = packet.get("notes") or "No additional notes."

    return TASK_MD_TEMPLATE.format(
        task_id=packet.get("task_id", ""),
        project=packet.get("project", ""),
        title=packet.get("title", ""),
        bucket=packet.get("bucket", ""),
        priority=packet.get("priority", ""),
        risk=packet.get("risk", ""),
        status=packet.get("status", ""),
        repo_path=packet.get("repo_path", ""),
        branch_name=packet.get("branch_name", ""),
        problem_summary=packet.get("problem_summary", ""),
        goal=packet.get("goal", ""),
        suspected_files_md=suspected_files_md,
        acceptance_criteria_md=acceptance_md,
        qa_plan_md=qa_plan_md,
        system_impact=packet.get("system_impact", ""),
        stop_conditions_md=stop_md,
        notes=notes,
    )



def create_blank_result(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "executor": "",
        "summary": "",
        "files_changed": [],
        "commands_run": [],
        "issues_encountered": [],
        "notes": "",
        "completed_at": "",
    }



def create_blank_qa(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "qa_tool": "",
        "summary": "",
        "checks_run": [],
        "checks_passed": [],
        "checks_failed": [],
        "artifacts": [],
        "notes": "",
        "completed_at": "",
    }



def create_blank_escalation(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "reason": "",
        "details": "",
        "recommended_next_action": "",
        "created_at": "",
    }



def maybe_write(path: Path, content: str | dict[str, Any], *, force: bool) -> tuple[bool, str]:
    if path.exists() and not force:
        return False, f"SKIPPED (exists): {path}"
    if isinstance(content, str):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    else:
        save_json(path, content)
    return True, f"WROTE: {path}"



def update_backlog_status(backlog_items: list[dict[str, Any]], task_id: str, new_status: str) -> None:
    for item in backlog_items:
        if item.get("task_id") == task_id:
            item["status"] = new_status
            return
    raise PacketGenerationError(f"Task {task_id} not found while updating backlog status")



def render_master_backlog_md(backlog_items: list[dict[str, Any]]) -> str:
    lines = [
        "# MASTER_BACKLOG",
        "",
        "| Task ID | Project | Bucket | Priority | Risk | Status | Title | Notes |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in backlog_items:
        notes = str(item.get("notes", "") or "")
        lines.append(
            f"| {item.get('task_id','')} | {item.get('project','')} | {item.get('bucket','')} | {item.get('priority','')} | {item.get('risk','')} | {item.get('status','')} | {item.get('title','')} | {notes} |"
        )
    lines.append("")
    return "\n".join(lines)



def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Jarvis task packet files from master_backlog.json")
    parser.add_argument("--task", help="Task ID to generate, e.g. WCS-002")
    parser.add_argument("--workspace", help="Workspace root path. Defaults to script grandparent directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite packet/result/qa/escalation files if they already exist")
    parser.add_argument("--dispatch", action="store_true", help="Mark the backlog item as dispatched when generating files")
    parser.add_argument("--list-ready", action="store_true", help="List ready tasks and exit")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent
    state_dir = workspace / "state"
    tasks_dir = workspace / "tasks"
    results_dir = workspace / "results"
    qa_dir = workspace / "qa"
    logs_dir = workspace / "logs"
    backlog_json_path = state_dir / "master_backlog.json"
    backlog_md_path = state_dir / "MASTER_BACKLOG.md"

    backlog = load_json(backlog_json_path)
    if not isinstance(backlog, list):
        raise PacketGenerationError(f"Expected a JSON array in {backlog_json_path}")

    if args.list_ready:
        ready = [item for item in backlog if str(item.get("status", "")).lower() == "ready"]
        if not ready:
            print("No ready tasks found.")
            return 0
        print("Ready tasks:")
        for item in ready:
            print(f"- {item.get('task_id')}: {item.get('title')}")
        return 0

    if not args.task:
        parser.error("--task is required unless --list-ready is used")

    task_id = args.task.strip().upper()
    item = next((row for row in backlog if str(row.get("task_id", "")).upper() == task_id), None)
    if not item:
        raise PacketGenerationError(f"Task {task_id} not found in {backlog_json_path}")

    project = str(item.get("project", "") or "")
    project_cfg = DEFAULT_PROJECT_CONFIG.get(project, {
        "repo_path": "",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": ["Run the project-appropriate QA checks"],
        "default_stop_conditions": ["Task scope expands beyond the targeted fix"],
    })

    packet = build_packet_json(item, project_cfg, dispatch=args.dispatch)
    packet_md = build_packet_markdown(packet)

    task_json_path = tasks_dir / f"{task_id}_task.json"
    task_md_path = tasks_dir / f"{task_id}_task.md"
    worker_result_path = results_dir / f"{task_id}_worker_result.json"
    qa_result_path = qa_dir / f"{task_id}_qa_result.json"
    escalation_path = logs_dir / f"{task_id}_escalation.json"

    outputs = [
        maybe_write(task_json_path, packet, force=args.force),
        maybe_write(task_md_path, packet_md, force=args.force),
        maybe_write(worker_result_path, create_blank_result(task_id), force=args.force),
        maybe_write(qa_result_path, create_blank_qa(task_id), force=args.force),
        maybe_write(escalation_path, create_blank_escalation(task_id), force=args.force),
    ]

    if args.dispatch:
        update_backlog_status(backlog, task_id, "dispatched")
        save_json(backlog_json_path, backlog)
        backlog_md_path.write_text(render_master_backlog_md(backlog), encoding="utf-8")
        print(f"UPDATED backlog status to dispatched for {task_id}")
        print(f"RENDERED: {backlog_md_path}")

    for _, message in outputs:
        print(message)

    print("\nTask packet generation complete.")
    print(f"Task packet markdown: {task_md_path}")
    print(f"Task packet JSON:     {task_json_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PacketGenerationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)

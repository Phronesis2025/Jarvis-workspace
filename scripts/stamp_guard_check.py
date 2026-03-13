from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}
ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class StampGuardError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise StampGuardError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise StampGuardError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only pre-stamp guardrail for worker and QA result JSON files."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise StampGuardError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise StampGuardError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def load_result(path: Path, kind: str, failures: List[str]) -> Dict[str, Any] | None:
    try:
        data = read_json(path)
    except StampGuardError as exc:
        failures.append(str(exc))
        return None
    if not isinstance(data, dict):
        failures.append(f"{kind} result must be a JSON object: {path}")
        return None
    return data


def check_completed_at_pre_stamp(
    data: Dict[str, Any], kind: str, failures: List[str]
) -> str:
    completed_raw = normalize_text(data.get("completed_at"))
    if completed_raw:
        failures.append(
            f"{kind} result completed_at must be blank before stamping; "
            f"found: {completed_raw!r}."
        )
    return completed_raw


def check_worker_pre_stamp(
    data: Dict[str, Any],
    task_id: str,
    failures: List[str],
) -> None:
    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("Worker result status must not be 'draft' before stamping.")
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. "
            f"Found: {status or '(blank)'}."
        )

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    summary = normalize_text(data.get("summary"))
    if not summary or summary.lower() in {"todo", "tbd", "placeholder"}:
        failures.append(
            "Worker result summary must be present, non-blank, and not a placeholder before stamping."
        )

    executor = normalize_text(data.get("executor"))
    if not executor:
        failures.append(
            "Worker result executor must be present and non-blank before stamping."
        )

    files_changed = data.get("files_changed")
    if not isinstance(files_changed, list):
        failures.append("Worker result files_changed must be a list before stamping.")
        files_changed_list: List[str] = []
    else:
        files_changed_list = [normalize_text(x) for x in files_changed]

    if status == "worker_complete" and not files_changed_list:
        failures.append(
            "Worker result files_changed must contain at least one entry when status is worker_complete before stamping."
        )

    commands_run = data.get("commands_run")
    if not isinstance(commands_run, list):
        failures.append("Worker result commands_run must be a list before stamping.")
        commands_run_list: List[str] = []
    else:
        commands_run_list = [normalize_text(x) for x in commands_run]

    if status == "worker_complete":
        meaningful_commands = [
            cmd
            for cmd in commands_run_list
            if cmd and cmd.lower() not in {"todo", "tbd", "placeholder"}
        ]
        if not meaningful_commands:
            failures.append(
                "Worker result commands_run should contain at least one meaningful entry when status is worker_complete before stamping."
            )


def check_qa_pre_stamp(
    data: Dict[str, Any],
    task_id: str,
    failures: List[str],
) -> None:
    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("QA result status must not be 'draft' before stamping.")
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. "
            f"Found: {status or '(blank)'}."
        )

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    summary = normalize_text(data.get("summary"))
    if not summary or summary.lower() in {"todo", "tbd", "placeholder"}:
        failures.append(
            "QA result summary must be present, non-blank, and not a placeholder before stamping."
        )

    qa_tool = normalize_text(data.get("qa_tool"))
    if not qa_tool:
        failures.append(
            "QA result qa_tool must be present and non-blank before stamping."
        )

    notes = normalize_text(data.get("notes"))
    if notes and notes.lower() in {"todo", "tbd", "placeholder"}:
        failures.append(
            "QA result notes must not be an obvious placeholder before stamping."
        )

    checks_run = data.get("checks_run")
    if not isinstance(checks_run, list):
        failures.append("QA result checks_run must be a list before stamping.")
        checks_run_list: List[str] = []
    else:
        checks_run_list = [normalize_text(x) for x in checks_run]

    checks_failed = data.get("checks_failed")
    if not isinstance(checks_failed, list):
        failures.append("QA result checks_failed must be a list before stamping.")
        checks_failed_list: List[str] = []
    else:
        checks_failed_list = [normalize_text(x) for x in checks_failed]

    if status in {"qa_pass", "qa_fail"} and not checks_run_list:
        failures.append(
            "QA result checks_run must contain at least one entry when status is qa_pass or qa_fail before stamping."
        )

    if status == "qa_pass" and checks_failed_list:
        failures.append(
            "QA result checks_failed must be empty when status is qa_pass before stamping."
        )

    checks_passed = data.get("checks_passed")
    if not isinstance(checks_passed, list):
        failures.append("QA result checks_passed must be a list before stamping.")
        checks_passed_list: List[str] = []
    else:
        checks_passed_list = [normalize_text(x) for x in checks_passed]

    if status == "qa_pass" and not checks_passed_list:
        failures.append(
            "QA result checks_passed must contain at least one entry when status is qa_pass before stamping."
        )


def main() -> int:
    args = parse_args()

    if not args.task:
        print("STAMP GUARD CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except StampGuardError as exc:
        print("STAMP GUARD CHECK: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    worker_path = workspace / "results" / f"{task_id}_worker_result.json"
    qa_path = workspace / "qa" / f"{task_id}_qa_result.json"

    worker_data = load_result(worker_path, "Worker", failures)
    qa_data = load_result(qa_path, "QA", failures)

    worker_completed_raw = ""
    qa_completed_raw = ""

    if worker_data is not None:
        worker_completed_raw = check_completed_at_pre_stamp(
            worker_data, "Worker", failures
        )
        check_worker_pre_stamp(worker_data, task_id, failures)
    if qa_data is not None:
        qa_completed_raw = check_completed_at_pre_stamp(qa_data, "QA", failures)
        check_qa_pre_stamp(qa_data, task_id, failures)

    # Detect uneven / split-stamp states explicitly.
    if worker_data is not None and qa_data is not None:
        worker_completed = bool(worker_completed_raw)
        qa_completed = bool(qa_completed_raw)
        if worker_completed != qa_completed:
            failures.append(
                "Worker and QA results are in a split-stamp state: "
                f"worker completed_at={worker_completed_raw!r}, "
                f"QA completed_at={qa_completed_raw!r}. "
                "Both must be blank before stamping or both stamped consistently."
            )

    # Both artifacts must be present and ready before stamping.
    if worker_data is None or qa_data is None:
        failures.append(
            "Both worker and QA result files must exist and parse successfully before stamping."
        )

    if failures:
        print("STAMP GUARD CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("STAMP GUARD CHECK: PASS")
    print(f"Task: {task_id}")
    print("Worker and QA results are present, pre-stamp, and appear ready for timestamping.")
    print(f"- Worker result: {worker_path}")
    print(f"- QA result: {qa_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


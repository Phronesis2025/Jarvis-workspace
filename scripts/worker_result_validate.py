from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, List, Set


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}


class WorkerResultError(Exception):
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
        raise WorkerResultError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise WorkerResultError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only worker result schema validator for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    parser.add_argument(
        "--mode",
        choices=["pre-stamp", "post-stamp"],
        default="pre-stamp",
        help="Validation mode for completed_at (default: pre-stamp).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise WorkerResultError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise WorkerResultError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def determine_expected_files(task_json_path: Path) -> Set[str]:
    expected: Set[str] = set()
    try:
        data = read_json(task_json_path)
    except WorkerResultError:
        return expected

    if not isinstance(data, dict):
        return expected

    target_files = data.get("target_files")
    if isinstance(target_files, list):
        for item in target_files:
            path = normalize_text(item)
            if path:
                expected.add(path.replace("\\", "/"))

    if not expected:
        for key in ("target_file", "file_path", "file"):
            value = normalize_text(data.get(key))
            if value:
                expected.add(value.replace("\\", "/"))
                break

    if not expected:
        notes = normalize_text(data.get("notes"))
        if notes and ("\\" in notes or "/" in notes) and " " not in notes:
            expected.add(notes.replace("\\", "/"))

    return expected


def check_worker_result(
    worker_path: Path,
    task_id: str,
    mode: str,
    expected_files: Set[str],
    failures: List[str],
) -> None:
    try:
        data = read_json(worker_path)
    except WorkerResultError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {worker_path}")
        return

    # Required fields
    required_fields = [
        "task_id",
        "status",
        "executor",
        "summary",
        "files_changed",
        "commands_run",
        "issues_encountered",
        "notes",
        "completed_at",
    ]
    for field in required_fields:
        if field not in data:
            failures.append(f"Worker result missing required field: {field}")

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("Worker result status must not be 'draft'.")
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. Found: {status or '(blank)'}."
        )

    executor = normalize_text(data.get("executor"))
    if not executor:
        failures.append("Worker result executor must be present and non-blank.")

    summary = normalize_text(data.get("summary"))
    if not summary:
        failures.append("Worker result summary must be present and non-blank.")

    files_changed = data.get("files_changed")
    if not isinstance(files_changed, list):
        failures.append("Worker result files_changed must be a list.")
        files_changed_list: List[str] = []
    else:
        files_changed_list = [normalize_text(x) for x in files_changed]

    commands_run = data.get("commands_run")
    if not isinstance(commands_run, list):
        failures.append("Worker result commands_run must be a list.")

    issues_encountered = data.get("issues_encountered")
    if not isinstance(issues_encountered, list):
        failures.append("Worker result issues_encountered must be a list.")

    # notes field must exist (already checked) but may be blank or non-blank; no extra content rule

    if status == "worker_complete":
        if not files_changed_list:
            failures.append(
                "Worker result files_changed must contain at least one entry when status is worker_complete."
            )

    for entry in files_changed_list:
        if not entry:
            failures.append("Worker result files_changed contains a blank entry.")

    # Simple task-scope consistency if expected scope is known
    if expected_files:
        for entry in files_changed_list:
            normalized_entry = entry.replace("\\", "/")
            if normalized_entry and normalized_entry not in expected_files:
                failures.append(
                    f"Worker result files_changed entry {normalized_entry} is outside expected task scope: {sorted(expected_files)}."
                )

    completed_at_raw = normalize_text(data.get("completed_at"))
    if mode == "pre-stamp":
        if completed_at_raw:
            failures.append("In pre-stamp mode, worker result completed_at must be blank.")
    else:  # post-stamp
        if not completed_at_raw:
            failures.append("In post-stamp mode, worker result completed_at must be non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("WORKER RESULT VALIDATION: FAIL")
        print("Task: (missing)")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except WorkerResultError as exc:
        print("WORKER RESULT VALIDATION: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print(f"Mode: {args.mode}")
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
    task_json_path = workspace / "tasks" / f"{task_id}_task.json"

    if not worker_path.exists():
        failures.append(f"Missing worker result JSON: {worker_path}")

    expected_files = determine_expected_files(task_json_path)

    if worker_path.exists():
        check_worker_result(worker_path, task_id, args.mode, expected_files, failures)

    if failures:
        print("WORKER RESULT VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    # Best-effort display of key fields on pass
    data = read_json(worker_path)
    executor = normalize_text(data.get("executor"))
    status = normalize_text(data.get("status"))
    files_changed = data.get("files_changed") or []
    files_changed_display = [normalize_text(x) for x in files_changed if normalize_text(x)]

    print("WORKER RESULT VALIDATION: PASS")
    print(f"Task: {task_id}")
    print(f"Mode: {args.mode}")
    print(f"Executor: {executor}")
    print(f"Status: {status}")
    print(f"Files changed: {', '.join(files_changed_display) if files_changed_display else '(none)'}")
    print("Passed checks:")
    print("- worker result JSON exists and parses")
    print("- required worker result fields are present")
    print("- executor and summary are non-blank")
    print("- list fields (files_changed, commands_run, issues_encountered) have the correct types")
    print("- files_changed is non-empty for worker_complete (if applicable)")
    print("- completed_at matches the expected mode (pre-stamp or post-stamp)")
    if expected_files:
        print("- files_changed entries are within expected task scope")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


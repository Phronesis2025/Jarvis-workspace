from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}
ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class ValidationError(Exception):
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
        raise ValidationError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only post-reconcile validation for a WCS task."
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


def validate_task_id(task_id_raw: str) -> str:
    task_id = normalize_text(task_id_raw).upper()
    if not task_id.startswith("WCS-"):
        raise ValidationError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise ValidationError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def check_state_files_exist(workspace: Path, failures: list[str]) -> dict[str, Path]:
    state_dir = workspace / "state"
    paths = {
        "backlog_json": state_dir / "master_backlog.json",
        "backlog_md": state_dir / "MASTER_BACKLOG.md",
        "daily_review_md": state_dir / "DAILY_REVIEW.md",
    }
    for key, path in paths.items():
        if not path.exists():
            failures.append(f"Missing state file: {path}")
    return paths


def check_backlog_json(backlog_json_path: Path, task_id: str, failures: list[str]) -> dict[str, Any] | None:
    try:
        data = read_json(backlog_json_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, list):
        failures.append(f"master_backlog.json root must be a list: {backlog_json_path}")
        return None

    matches: list[dict[str, Any]] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        if normalize_text(item.get("task_id")).upper() == task_id:
            matches.append(item)

    if len(matches) == 0:
        failures.append(f"No backlog entry found for task {task_id} in master_backlog.json.")
        return None
    if len(matches) > 1:
        failures.append(f"Expected exactly one backlog entry for {task_id}, found {len(matches)}.")
        return None

    record = matches[0]
    project = normalize_text(record.get("project")).upper()
    status = normalize_text(record.get("status")).lower()

    if project != "WCS":
        failures.append(
            f"Backlog entry for {task_id} has wrong project. Expected WCS, found {project or '(blank)'}."
        )
    if status != "done":
        failures.append(
            f"Backlog entry for {task_id} must have status 'done'. Found {status or '(blank)'}."
        )

    return record


def check_backlog_markdown(
    backlog_md_path: Path,
    task_id: str,
    title: str | None,
    failures: list[str],
) -> None:
    try:
        text = backlog_md_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        failures.append(f"Missing backlog markdown file: {backlog_md_path}")
        return
    except OSError as exc:
        failures.append(f"Failed to read backlog markdown {backlog_md_path}: {exc}")
        return

    if task_id not in text:
        failures.append(f"Task id {task_id} not found in MASTER_BACKLOG.md.")

    if title:
        if title not in text:
            failures.append(f"Task title not found in MASTER_BACKLOG.md: {title}")

    # Simple done indicator: look for a line containing both the task id and 'done' (case-insensitive).
    done_line_found = False
    for line in text.splitlines():
        if task_id in line and "done" in line.lower():
            done_line_found = True
            break
    if not done_line_found:
        failures.append(
            f"MASTER_BACKLOG.md does not show a simple 'done' indicator on the same line as {task_id}."
        )


def check_daily_review(daily_review_path: Path, task_id: str, failures: list[str]) -> None:
    try:
        text = daily_review_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        failures.append(f"Missing DAILY_REVIEW.md: {daily_review_path}")
        return
    except OSError as exc:
        failures.append(f"Failed to read DAILY_REVIEW.md {daily_review_path}: {exc}")
        return

    if task_id not in text:
        failures.append(f"Task id {task_id} not found in DAILY_REVIEW.md.")


def check_worker_result(worker_path: Path, task_id: str, failures: list[str]) -> None:
    if not worker_path.exists():
        failures.append(f"Missing worker result JSON: {worker_path}")
        return

    try:
        data = read_json(worker_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {worker_path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("Worker result completed_at must be present and non-blank.")


def check_qa_result(qa_path: Path, task_id: str, failures: list[str]) -> None:
    if not qa_path.exists():
        failures.append(f"Missing QA result JSON: {qa_path}")
        return

    try:
        data = read_json(qa_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {qa_path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("QA result completed_at must be present and non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("POST-RECONCILE VALIDATION: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except ValidationError as exc:
        print("POST-RECONCILE VALIDATION: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: list[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    paths = check_state_files_exist(workspace, failures)

    backlog_record: dict[str, Any] | None = None
    title: str | None = None

    backlog_json_path = paths["backlog_json"]
    backlog_md_path = paths["backlog_md"]
    daily_review_path = paths["daily_review_md"]

    if backlog_json_path.exists():
        backlog_record = check_backlog_json(backlog_json_path, task_id, failures)
        if backlog_record is not None:
            title = normalize_text(backlog_record.get("title"))

    if backlog_md_path.exists():
        check_backlog_markdown(backlog_md_path, task_id, title, failures)

    if daily_review_path.exists():
        check_daily_review(daily_review_path, task_id, failures)

    worker_path = workspace / "results" / f"{task_id}_worker_result.json"
    qa_path = workspace / "qa" / f"{task_id}_qa_result.json"

    check_worker_result(worker_path, task_id, failures)
    check_qa_result(qa_path, task_id, failures)

    if failures:
        print("POST-RECONCILE VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    status = ""
    if backlog_record is not None:
        status = normalize_text(backlog_record.get("status"))

    print("POST-RECONCILE VALIDATION: PASS")
    print(f"Task: {task_id}")
    if title:
        print(f"Title: {title}")
    if status:
        print(f"Backlog status: {status}")
    print("Passed checks:")
    print("- backlog JSON contains one WCS backlog entry for this task with status done")
    print("- MASTER_BACKLOG.md shows the task id, title, and a done indicator")
    print("- DAILY_REVIEW.md includes the task id")
    print("- worker result exists with matching task_id, allowed status, and non-blank completed_at")
    print("- QA result exists with matching task_id, allowed status, and non-blank completed_at")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, List


ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class QaResultError(Exception):
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
        raise QaResultError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise QaResultError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only QA result schema validator for a WCS task."
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
        raise QaResultError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise QaResultError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def check_qa_result(
    qa_path: Path,
    task_id: str,
    mode: str,
    failures: List[str],
) -> None:
    try:
        data = read_json(qa_path)
    except QaResultError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {qa_path}")
        return

    required_fields = [
        "task_id",
        "status",
        "qa_tool",
        "summary",
        "checks_run",
        "checks_passed",
        "checks_failed",
        "artifacts",
        "notes",
        "completed_at",
    ]
    for field in required_fields:
        if field not in data:
            failures.append(f"QA result missing required field: {field}")

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("QA result status must not be 'draft'.")
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. Found: {status or '(blank)'}."
        )

    qa_tool = normalize_text(data.get("qa_tool"))
    if not qa_tool:
        failures.append("QA result qa_tool must be present and non-blank.")

    summary = normalize_text(data.get("summary"))
    if not summary:
        failures.append("QA result summary must be present and non-blank.")

    checks_run = data.get("checks_run")
    checks_passed = data.get("checks_passed")
    checks_failed = data.get("checks_failed")
    artifacts = data.get("artifacts")

    if not isinstance(checks_run, list):
        failures.append("QA result checks_run must be a list.")
        checks_run_list: List[str] = []
    else:
        checks_run_list = [normalize_text(x) for x in checks_run]

    if not isinstance(checks_passed, list):
        failures.append("QA result checks_passed must be a list.")
        checks_passed_list: List[str] = []
    else:
        checks_passed_list = [normalize_text(x) for x in checks_passed]

    if not isinstance(checks_failed, list):
        failures.append("QA result checks_failed must be a list.")
        checks_failed_list: List[str] = []
    else:
        checks_failed_list = [normalize_text(x) for x in checks_failed]

    if not isinstance(artifacts, list):
        failures.append("QA result artifacts must be a list.")
        artifacts_list: List[str] = []
    else:
        artifacts_list = [normalize_text(x) for x in artifacts]

    # notes must exist (checked above) but can be blank or non-blank; no extra content rule

    if status in {"qa_pass", "qa_fail"} and not checks_run_list:
        failures.append(
            "QA result checks_run must contain at least one entry when status is qa_pass or qa_fail."
        )

    for arr_name, arr in [
        ("checks_run", checks_run_list),
        ("checks_passed", checks_passed_list),
        ("checks_failed", checks_failed_list),
        ("artifacts", artifacts_list),
    ]:
        for entry in arr:
            if not isinstance(entry, str):
                failures.append(f"QA result {arr_name} contains a non-string entry.")
            elif not entry:
                failures.append(f"QA result {arr_name} contains a blank entry.")

    # Simple internal consistency
    if status == "qa_pass":
        if checks_failed_list:
            failures.append("QA result checks_failed must be empty when status is qa_pass.")
        if not checks_passed_list:
            failures.append("QA result checks_passed must contain at least one entry when status is qa_pass.")
    elif status == "qa_fail":
        if not checks_failed_list:
            failures.append("QA result checks_failed must contain at least one entry when status is qa_fail.")
    # status == escalated: no extra requirements for checks_passed / checks_failed beyond type and content shape

    completed_at_raw = normalize_text(data.get("completed_at"))
    if mode == "pre-stamp":
        if completed_at_raw:
            failures.append("In pre-stamp mode, QA result completed_at must be blank.")
    else:  # post-stamp
        if not completed_at_raw:
            failures.append("In post-stamp mode, QA result completed_at must be non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("QA RESULT VALIDATION: FAIL")
        print("Task: (missing)")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except QaResultError as exc:
        print("QA RESULT VALIDATION: FAIL")
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

    qa_path = workspace / "qa" / f"{task_id}_qa_result.json"

    if not qa_path.exists():
        failures.append(f"Missing QA result JSON: {qa_path}")

    if qa_path.exists():
        check_qa_result(qa_path, task_id, args.mode, failures)

    if failures:
        print("QA RESULT VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    data = read_json(qa_path)
    qa_tool = normalize_text(data.get("qa_tool"))
    status = normalize_text(data.get("status"))
    checks_run = data.get("checks_run") or []
    checks_run_display = [normalize_text(x) for x in checks_run if normalize_text(x)]

    print("QA RESULT VALIDATION: PASS")
    print(f"Task: {task_id}")
    print(f"Mode: {args.mode}")
    print(f"QA tool: {qa_tool}")
    print(f"Status: {status}")
    print(f"Checks run: {', '.join(checks_run_display) if checks_run_display else '(none)'}")
    print("Passed checks:")
    print("- QA result JSON exists and parses")
    print("- required QA result fields are present")
    print("- qa_tool and summary are non-blank")
    print("- list fields (checks_run, checks_passed, checks_failed, artifacts) have the correct types")
    print("- checks_run is non-empty for qa_pass/qa_fail (if applicable)")
    print("- internal consistency between status, checks_passed, and checks_failed")
    print("- completed_at matches the expected mode (pre-stamp or post-stamp)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


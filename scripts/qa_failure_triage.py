from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


class QaTriageError(Exception):
    pass


ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


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
        raise QaTriageError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise QaTriageError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only QA failure triage helper for a WCS task."
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
        raise QaTriageError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise QaTriageError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def load_task_packet(workspace: Path, task_id: str) -> Optional[Dict[str, Any]]:
    path = workspace / "tasks" / f"{task_id}_task.json"
    try:
        data = read_json(path)
    except QaTriageError:
        return None
    if not isinstance(data, dict):
        return None
    return data


def load_qa_result(workspace: Path, task_id: str) -> Optional[Dict[str, Any]]:
    path = workspace / "qa" / f"{task_id}_qa_result.json"
    try:
        data = read_json(path)
    except QaTriageError:
        return None
    if not isinstance(data, dict):
        return None
    return data


def classify_failure(
    qa: Optional[Dict[str, Any]],
) -> Tuple[str, str, str, str, bool, Optional[str]]:
    """
    Return:
      (failure_class, confidence, reviewed_status, likely_cause, follow_up_recommended, follow_up_title)
    """
    if qa is None:
        return (
            "ambiguous",
            "low",
            "(missing)",
            "No QA result JSON found; cannot triage without evidence.",
            True,
            "Investigate missing QA result for WCS task",
        )

    status = normalize_text(qa.get("status")).lower()
    summary = normalize_text(qa.get("summary"))
    notes = normalize_text(qa.get("notes"))

    reviewed_status = status if status in ALLOWED_QA_STATUSES else "(invalid)"

    # Environment / setup signatures
    env_markers = [
        "did not become ready",
        "connection refused",
        "ECONNREFUSED",
        "ERR_CONNECTION_REFUSED",
        "Start the app with 'npm run dev'",
        "start the app with 'npm run dev'",
        "server at http://localhost:3000",
        "server at https://localhost:3000",
    ]

    text = f"{summary} {notes}".lower()

    if any(m.lower() in text for m in env_markers):
        failure_class = "environment_setup_failure"
        confidence = "high"
        likely_cause = (
            "Playwright global setup could not reach the local app server "
            "(e.g. localhost:3000 not running or not ready)."
        )
        follow_up_recommended = True
        follow_up_title = (
            "Stabilize local WCS smoke QA server startup for Playwright (npm run dev readiness)."
        )
        return (
            failure_class,
            confidence,
            reviewed_status,
            likely_cause,
            follow_up_recommended,
            follow_up_title,
        )

    # Test harness failures: runner/setup failing before meaningful app checks
    harness_markers = [
        "playwright test was not found",
        "global setup failed",
        "global teardown failed",
        "cannot find module '@playwright/test'",
        "playwright.config",
        "browserType.launch: Failed to launch",
        "browserType.launch: executable doesn't exist",
        "ENV VAR",
        "missing env var",
    ]

    if any(m.lower() in text for m in harness_markers):
        failure_class = "test_harness_failure"
        confidence = "medium"
        likely_cause = (
            "Playwright test harness or global setup/teardown failed before executing meaningful app assertions."
        )
        follow_up_recommended = True
        follow_up_title = "Investigate Playwright harness/global setup failure for WCS smoke QA"
        return (
            failure_class,
            confidence,
            reviewed_status,
            likely_cause,
            follow_up_recommended,
            follow_up_title,
        )

    # Application regression: app reachable but assertions / locators failed
    app_markers = [
        "expect",
        "locator",
        "to be visible",
        "to contain text",
        "AssertionError",
        "Expected",
        "received:",
        "element not found",
        "timed out waiting for selector",
    ]

    if any(m.lower() in text for m in app_markers):
        failure_class = "application_regression"
        confidence = "medium"
        likely_cause = (
            "The app loaded, but one or more smoke assertions/locators failed, "
            "indicating a likely application regression."
        )
        follow_up_recommended = True
        follow_up_title = "Investigate WCS smoke QA regression (home page assertions/locators failing)"
        return (
            failure_class,
            confidence,
            reviewed_status,
            likely_cause,
            follow_up_recommended,
            follow_up_title,
        )

    # No strong signatures matched
    failure_class = "ambiguous"
    confidence = "low"
    likely_cause = (
        "QA result did not match known environment, harness, or regression signatures. "
        "Manual review of QA logs and artifacts is recommended."
    )
    follow_up_recommended = False
    follow_up_title = None
    return (
        failure_class,
        confidence,
        reviewed_status,
        likely_cause,
        follow_up_recommended,
        follow_up_title,
    )


def main() -> int:
    args = parse_args()

    if not args.task:
        print("QA TRIAGE: UNABLE TO CLASSIFY")
        print("Task: (missing)")
        print("Reason: --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except QaTriageError as exc:
        print("QA TRIAGE: UNABLE TO CLASSIFY")
        print(f"Task: {normalize_text(args.task).upper()}")
        print(f"Reason: {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    if not workspace.exists():
        print("QA TRIAGE: UNABLE TO CLASSIFY")
        print(f"Task: {task_id}")
        print(f"Reason: Workspace path does not exist: {workspace}")
        return 1

    task_packet = load_task_packet(workspace, task_id)
    qa_result = load_qa_result(workspace, task_id)

    # Gate behavior by QA status: only triage non-passing or ambiguous QA evidence.
    status_raw = None
    status = ""
    if qa_result is not None:
        status_raw = qa_result.get("status")
        status = normalize_text(status_raw).lower()

    if status == "qa_pass":
        print("QA TRIAGE: NO FAILURE TO TRIAGE")
        print(f"Task: {task_id}")
        print(f"Reviewed QA status: {status}")
        print(
            "Reason: QA triage is intended for failed/escalated/ambiguous QA evidence, "
            "not for qa_pass results."
        )
        return 0

    (
        failure_class,
        confidence,
        reviewed_status,
        likely_cause,
        follow_up_recommended,
        follow_up_title,
    ) = classify_failure(qa_result)

    if failure_class == "ambiguous":
        print("QA TRIAGE: UNABLE TO CLASSIFY" if qa_result is None else "QA TRIAGE: CLASSIFIED")
    else:
        print("QA TRIAGE: CLASSIFIED")

    print(f"Task: {task_id}")
    print(f"Reviewed QA status: {reviewed_status}")
    print(f"Failure class: {failure_class}")
    print(f"Confidence: {confidence}")

    if task_packet is not None:
        title = normalize_text(task_packet.get("title"))
        if title:
            print(f"Task title: {title}")

    if qa_result is not None:
        summary = normalize_text(qa_result.get("summary"))
        if summary:
            print(f"QA summary: {summary}")
        notes = normalize_text(qa_result.get("notes"))
        if notes:
            print(f"QA notes: {notes}")

    print(f"Likely cause: {likely_cause}")
    print(f"Follow-up task recommended: {'yes' if follow_up_recommended else 'no'}")
    if follow_up_title:
        print(f"Suggested follow-up task title: {follow_up_title}")

    # Exit 0 even when classification is ambiguous, as long as processing succeeded.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


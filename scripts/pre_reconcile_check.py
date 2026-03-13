from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Tuple


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}
ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class CheckError(Exception):
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
        raise CheckError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise CheckError(f"Invalid JSON in {path}: {exc}") from exc


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only pre-reconcile readiness check for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016.",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(task_id: str) -> str:
    task_id_norm = normalize_text(task_id).upper()
    if not task_id_norm.startswith("WCS-"):
        raise CheckError(f"Invalid task id (expected WCS-XXX): {task_id_norm}")
    suffix = task_id_norm.split("-", 1)[1]
    if not suffix.isdigit():
        raise CheckError(f"Invalid task id suffix (expected numeric): {task_id_norm}")
    return task_id_norm


def check_artifacts(workspace: Path, task_id: str, failures: list[str]) -> Tuple[Path, Path, Path]:
    task_json = workspace / "tasks" / f"{task_id}_task.json"
    worker_result = workspace / "results" / f"{task_id}_worker_result.json"
    qa_result = workspace / "qa" / f"{task_id}_qa_result.json"

    if not task_json.exists():
        failures.append(f"Missing task packet JSON: {task_json}")
    if not worker_result.exists():
        failures.append(f"Missing worker result JSON: {worker_result}")
    if not qa_result.exists():
        failures.append(f"Missing QA result JSON: {qa_result}")

    return task_json, worker_result, qa_result


def check_worker_result(path: Path, task_id: str, failures: list[str]) -> None:
    try:
        data = read_json(path)
    except CheckError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {path}")
        return

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

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("Worker result completed_at must be present and non-blank.")


def check_qa_result(path: Path, task_id: str, failures: list[str]) -> None:
    try:
        data = read_json(path)
    except CheckError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {path}")
        return

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

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("QA result completed_at must be present and non-blank.")


def resolve_repo_path(workspace: Path, failures: list[str]) -> Path | None:
    project_status_path = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(project_status_path)
    except CheckError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, dict):
        failures.append(f"project_status_wcs.json must be a JSON object: {project_status_path}")
        return None

    repo_raw = normalize_text(data.get("repo_path"))
    if not repo_raw:
        failures.append("project_status_wcs.json is missing repo_path.")
        return None

    repo_path = Path(repo_raw).resolve()
    if not repo_path.exists():
        failures.append(f"Repo path does not exist: {repo_path}")
        return None

    return repo_path


def check_repo_state(repo_path: Path, task_id: str, failures: list[str]) -> tuple[str | None, str | None, int | None]:
    expected_branch = f"jarvis-task-{task_id.lower()}"

    branch_result = run_git(repo_path, ["branch", "--show-current"])
    if branch_result.returncode != 0:
        failures.append(
            f"Failed to read current branch in repo {repo_path}: "
            f"{branch_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, None, None

    current_branch = normalize_text(branch_result.stdout)
    if not current_branch:
        failures.append(f"Current branch is empty in repo {repo_path}.")
    elif current_branch != expected_branch:
        failures.append(
            f"Current branch mismatch. Expected {expected_branch}, found {current_branch}."
        )

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        failures.append(
            f"Failed to inspect repo status in {repo_path}: "
            f"{status_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
        if dirty_lines:
            failures.append(
                f"Repo working tree is not clean in {repo_path}. {len(dirty_lines)} changed path(s) detected."
            )

    base_branch = None
    for candidate in ["main", "master"]:
        rev_parse = run_git(repo_path, ["rev-parse", "--verify", candidate])
        if rev_parse.returncode == 0:
            base_branch = candidate
            break

    if base_branch is None:
        failures.append(f"Neither 'main' nor 'master' branch exists in repo {repo_path}.")
        return expected_branch, current_branch, None

    ahead_result = run_git(repo_path, ["rev-list", "--count", f"{base_branch}..{current_branch or 'HEAD'}"])
    if ahead_result.returncode != 0:
        failures.append(
            f"Failed to compute commits ahead of {base_branch} in {repo_path}: "
            f"{ahead_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, current_branch, None

    ahead_str = normalize_text(ahead_result.stdout)
    try:
        ahead_count = int(ahead_str or "0")
    except ValueError:
        failures.append(
            f"Unexpected rev-list output for {base_branch}..{current_branch or 'HEAD'} in {repo_path}: {ahead_str}"
        )
        return expected_branch, current_branch, None

    if ahead_count < 1:
        failures.append(
            f"Task branch must be ahead of {base_branch} by at least 1 commit. Found: {ahead_count}."
        )

    return expected_branch, current_branch, ahead_count


def main() -> int:
    args = parse_args()

    if not args.task:
        print("PRE-RECONCILE CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except CheckError as exc:
        print("PRE-RECONCILE CHECK: FAIL")
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

    task_json, worker_result, qa_result = check_artifacts(workspace, task_id, failures)

    if worker_result.exists():
        check_worker_result(worker_result, task_id, failures)

    if qa_result.exists():
        check_qa_result(qa_result, task_id, failures)

    repo_path = resolve_repo_path(workspace, failures)
    expected_branch = None
    current_branch = None
    ahead_count: int | None = None

    if repo_path is not None:
        expected_branch, current_branch, ahead_count = check_repo_state(
            repo_path, task_id, failures
        )

    if failures:
        print("PRE-RECONCILE CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("PRE-RECONCILE CHECK: PASS")
    print(f"Task: {task_id}")
    if repo_path is not None and expected_branch is not None and current_branch is not None:
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
        if ahead_count is not None:
            print(f"Commits ahead of main/master: {ahead_count}")
    print("Passed checks:")
    print("- task, worker result, and QA result artifacts present")
    print("- worker result contract and completed_at valid")
    print("- QA result contract and completed_at valid")
    print("- repo path, branch, and clean working tree valid")
    print("- task branch ahead of main/master by at least 1 commit")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


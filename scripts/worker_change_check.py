from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple


class WorkerChangeError(Exception):
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
        raise WorkerChangeError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise WorkerChangeError(f"Invalid JSON in {path}: {exc}") from exc


def run_git(repo_path: Path, args: List[str]) -> subprocess.CompletedProcess[str]:
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
        description="Read-only worker change boundary check for a WCS task."
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
        raise WorkerChangeError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise WorkerChangeError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def determine_expected_files(task_json_path: Path, failures: List[str]) -> Set[str]:
    try:
        data = read_json(task_json_path)
    except WorkerChangeError as exc:
        failures.append(str(exc))
        return set()

    if not isinstance(data, dict):
        failures.append(f"Task packet must be a JSON object: {task_json_path}")
        return set()

    expected: Set[str] = set()

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

    if not expected:
        failures.append(
            f"Unable to determine expected file scope from task packet: {task_json_path}"
        )

    return expected


def resolve_repo_path(workspace: Path, failures: List[str]) -> Path | None:
    project_status_path = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(project_status_path)
    except WorkerChangeError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, dict):
        failures.append(f"project_status_wcs.json must be a JSON object: {project_status_path}")
        return None

    raw = normalize_text(data.get("repo_path"))
    if not raw:
        failures.append("project_status_wcs.json is missing repo_path.")
        return None

    repo_path = Path(raw).resolve()
    if not repo_path.exists():
        failures.append(f"Repo path does not exist: {repo_path}")
        return None

    return repo_path


def gather_changed_files(repo_path: Path, failures: List[str]) -> Set[str]:
    changed: Set[str] = set()

    status_result = run_git(repo_path, ["status", "--short"])
    if status_result.returncode != 0:
        failures.append(
            f"git status --short failed in {repo_path}: "
            f"{status_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in status_result.stdout.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.split(maxsplit=1)
            if len(parts) == 2:
                changed.add(parts[1].replace("\\", "/"))

    diff_result = run_git(repo_path, ["diff", "--name-only"])
    if diff_result.returncode != 0:
        failures.append(
            f"git diff --name-only failed in {repo_path}: "
            f"{diff_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in diff_result.stdout.splitlines():
            path = normalize_text(line)
            if path:
                changed.add(path.replace("\\", "/"))

    return changed


def check_branch(repo_path: Path, task_id: str, failures: List[str]) -> Tuple[str, str | None]:
    expected_branch = f"jarvis-task-{task_id.lower()}"

    branch_result = run_git(repo_path, ["branch", "--show-current"])
    if branch_result.returncode != 0:
        failures.append(
            f"git branch --show-current failed in {repo_path}: "
            f"{branch_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, None

    current_branch = normalize_text(branch_result.stdout)
    if not current_branch:
        failures.append(f"Current branch is empty in repo {repo_path}.")
    elif current_branch != expected_branch:
        failures.append(
            f"Current branch mismatch. Expected {expected_branch}, found {current_branch}."
        )

    return expected_branch, current_branch


def check_diff_sanity(repo_path: Path, changed_files: Set[str], failures: List[str]) -> None:
    if len(changed_files) > 3:
        failures.append(
            f"Too many changed files for a bounded task. Expected at most 3, found {len(changed_files)}."
        )

    for path in sorted(changed_files):
        diff_result = run_git(repo_path, ["diff", "--unified=0", "--", path])
        if diff_result.returncode != 0:
            failures.append(
                f"git diff --unified=0 failed for {path} in {repo_path}: "
                f"{diff_result.stderr.strip() or '(no stderr output)'}"
            )
            continue

        total_changes = 0
        for line in diff_result.stdout.splitlines():
            if not line:
                continue
            if line.startswith("@@"):
                continue
            if line.startswith("+++ ") or line.startswith("--- "):
                continue
            if line[0] in {"+", "-"}:
                total_changes += 1

        if total_changes > 40:
            failures.append(
                f"File {path} has too many changed lines for a bounded task. "
                f"Found {total_changes}, limit is 40."
            )


def main() -> int:
    args = parse_args()

    if not args.task:
        print("WORKER CHANGE CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except WorkerChangeError as exc:
        print("WORKER CHANGE CHECK: FAIL")
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

    task_json_path = workspace / "tasks" / f"{task_id}_task.json"
    expected_files = determine_expected_files(task_json_path, failures)

    repo_path = resolve_repo_path(workspace, failures)
    expected_branch = ""
    current_branch: str | None = None

    changed_files: Set[str] = set()
    if repo_path is not None:
        expected_branch, current_branch = check_branch(repo_path, task_id, failures)
        changed_files = gather_changed_files(repo_path, failures)

        if not changed_files:
            failures.append("No changed files detected in the WCS repo for this task.")

        if expected_files:
            for path in sorted(changed_files):
                if path not in expected_files:
                    failures.append(
                        f"Changed file {path} is outside the expected task scope: {sorted(expected_files)}."
                    )

        if changed_files:
            check_diff_sanity(repo_path, changed_files, failures)

    if failures:
        print("WORKER CHANGE CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("WORKER CHANGE CHECK: PASS")
    print(f"Task: {task_id}")
    if repo_path is not None and expected_branch and current_branch:
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
    if expected_files:
        print(f"Expected file scope: {', '.join(sorted(expected_files))}")
    print(f"Actual changed files: {', '.join(sorted(changed_files))}")
    print("Passed checks:")
    print("- repo path and current branch resolved correctly")
    print("- changed files exist and are within expected task scope")
    print("- number of changed files is within the allowed limit")
    print("- per-file diff size is within the allowed limit")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


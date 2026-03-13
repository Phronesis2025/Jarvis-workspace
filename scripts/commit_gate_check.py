from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple


class CommitGateError(Exception):
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
        raise CommitGateError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise CommitGateError(f"Invalid JSON in {path}: {exc}") from exc


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
        description="Read-only commit-state gate for a single WCS task."
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
        raise CommitGateError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise CommitGateError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def determine_expected_files(task_json_path: Path, failures: List[str]) -> Set[str]:
    """
    Derive expected file scope from the task packet.

    Mirrors the Phase-1 logic used in worker_change_check.py:
    - prefer target_files (list)
    - then target_file / file_path / file
    - finally a notes field that looks like a single path
    """
    try:
        data = read_json(task_json_path)
    except CommitGateError as exc:
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


def resolve_repo_path(workspace: Path, failures: List[str]) -> Optional[Path]:
    project_status_path = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(project_status_path)
    except CommitGateError as exc:
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


def check_branch_and_head(
    repo_path: Path, task_id: str, failures: List[str]
) -> Tuple[str, Optional[str], Optional[str]]:
    expected_branch = f"jarvis-task-{task_id.lower()}"

    branch_result = run_git(repo_path, ["branch", "--show-current"])
    if branch_result.returncode != 0:
        failures.append(
            f"git branch --show-current failed in {repo_path}: "
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

    head_result = run_git(repo_path, ["rev-parse", "HEAD"])
    if head_result.returncode != 0:
        failures.append(
            f"Failed to resolve HEAD in repo {repo_path}: "
            f"{head_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, current_branch, None

    head_sha = normalize_text(head_result.stdout)
    if not head_sha:
        failures.append(f"HEAD rev-parse returned empty output in repo {repo_path}.")
        head_sha = None

    return expected_branch, current_branch, head_sha


def check_ahead_of_base(
    repo_path: Path, current_branch: Optional[str], failures: List[str]
) -> Tuple[Optional[str], Optional[int]]:
    base_branch: Optional[str] = None
    for candidate in ["main", "master"]:
        rev_parse = run_git(repo_path, ["rev-parse", "--verify", candidate])
        if rev_parse.returncode == 0:
            base_branch = candidate
            break

    if base_branch is None:
        failures.append(f"Neither 'main' nor 'master' branch exists in repo {repo_path}.")
        return None, None

    ahead_result = run_git(
        repo_path,
        ["rev-list", "--count", f"{base_branch}..{current_branch or 'HEAD'}"],
    )
    if ahead_result.returncode != 0:
        failures.append(
            f"Failed to compute commits ahead of {base_branch} in {repo_path}: "
            f"{ahead_result.stderr.strip() or '(no stderr output)'}"
        )
        return base_branch, None

    ahead_str = normalize_text(ahead_result.stdout)
    try:
        ahead_count = int(ahead_str or "0")
    except ValueError:
        failures.append(
            f"Unexpected rev-list output for {base_branch}..{current_branch or 'HEAD'} "
            f"in {repo_path}: {ahead_str}"
        )
        return base_branch, None

    if ahead_count < 1:
        failures.append(
            f"Task branch must be ahead of {base_branch} by at least 1 commit. Found: {ahead_count}."
        )

    return base_branch, ahead_count


def check_worktree_clean(repo_path: Path, failures: List[str]) -> None:
    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        failures.append(
            f"Failed to inspect repo status in {repo_path}: "
            f"{status_result.stderr.strip() or '(no stderr output)'}"
        )
        return

    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    if dirty_lines:
        failures.append(
            f"Repo working tree is not clean in {repo_path}. "
            f"{len(dirty_lines)} changed path(s) detected after commit."
        )


def is_within_expected_scope(path: str, expected_files: Set[str]) -> bool:
    for expected in expected_files:
        if not expected:
            continue
        prefix = expected.rstrip("/")
        if path == prefix or path.startswith(prefix + "/"):
            return True
    return False


def gather_head_commit_files_and_changes(
    repo_path: Path, failures: List[str]
) -> Tuple[Set[str], Dict[str, int]]:
    """
    Inspect the HEAD commit.

    - Uses git show to list committed files.
    - Uses git diff-tree --numstat to count changed lines per file.
    """
    committed_files: Set[str] = set()
    line_counts: Dict[str, int] = {}

    show_result = run_git(repo_path, ["show", "--pretty=", "--name-only", "HEAD"])
    if show_result.returncode != 0:
        failures.append(
            f"git show --name-only HEAD failed in {repo_path}: "
            f"{show_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in show_result.stdout.splitlines():
            path = normalize_text(line)
            if path:
                norm = path.replace("\\", "/")
                committed_files.add(norm)

    numstat_result = run_git(
        repo_path, ["diff-tree", "--no-commit-id", "--numstat", "-r", "HEAD"]
    )
    if numstat_result.returncode != 0:
        failures.append(
            f"git diff-tree --numstat HEAD failed in {repo_path}: "
            f"{numstat_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in numstat_result.stdout.splitlines():
            parts = line.split("\t")
            if len(parts) != 3:
                continue
            added_raw, deleted_raw, path = parts
            path = normalize_text(path)
            if not path:
                continue
            norm_path = path.replace("\\", "/")
            try:
                added = int(added_raw) if added_raw.isdigit() else 0
                deleted = int(deleted_raw) if deleted_raw.isdigit() else 0
            except ValueError:
                continue
            total = added + deleted
            line_counts[norm_path] = total
            committed_files.add(norm_path)

    return committed_files, line_counts


def check_commit_boundedness(
    committed_files: Set[str],
    line_counts: Dict[str, int],
    expected_files: Set[str],
    failures: List[str],
) -> None:
    if not committed_files:
        failures.append("HEAD commit has no changed files.")
        return

    # Reuse Phase-1 thresholds from worker_change_check.py.
    if len(committed_files) > 3:
        failures.append(
            f"Too many committed files for a bounded task. Expected at most 3, "
            f"found {len(committed_files)}."
        )

    for path in sorted(committed_files):
        if not is_within_expected_scope(path, expected_files):
            failures.append(
                f"Committed file outside expected task scope: {path}. "
                f"Expected scope derived from task packet: {sorted(expected_files) or '(none)'}."
            )

    for path, total_changes in line_counts.items():
        if total_changes > 40:
            failures.append(
                f"File {path} has too many changed lines in HEAD for a bounded task. "
                f"Found {total_changes}, limit is 40."
            )


def check_commit_message(repo_path: Path, task_id: str, failures: List[str]) -> None:
    log_result = run_git(repo_path, ["log", "-1", "--pretty=%B"])
    if log_result.returncode != 0:
        failures.append(
            f"Failed to read HEAD commit message in {repo_path}: "
            f"{log_result.stderr.strip() or '(no stderr output)'}"
        )
        return

    message = normalize_text(log_result.stdout)
    if not message:
        failures.append("HEAD commit message is empty.")
        return

    if task_id.upper() not in message.upper():
        failures.append(
            f"HEAD commit message must contain the task id {task_id}. "
            f"Found: {message!r}."
        )


def main() -> int:
    args = parse_args()

    if not args.task:
        print("COMMIT GATE CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except CommitGateError as exc:
        print("COMMIT GATE CHECK: FAIL")
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
    if not task_json_path.exists():
        failures.append(f"Missing task packet JSON: {task_json_path}")
        expected_files: Set[str] = set()
    else:
        expected_files = determine_expected_files(task_json_path, failures)

    repo_path = resolve_repo_path(workspace, failures)
    expected_branch = ""
    current_branch: Optional[str] = None
    head_sha: Optional[str] = None
    base_branch: Optional[str] = None
    ahead_count: Optional[int] = None
    committed_files: Set[str] = set()
    line_counts: Dict[str, int] = {}

    if repo_path is not None:
        expected_branch, current_branch, head_sha = check_branch_and_head(
            repo_path, task_id, failures
        )
        base_branch, ahead_count = check_ahead_of_base(
            repo_path, current_branch, failures
        )
        check_worktree_clean(repo_path, failures)
        committed_files, line_counts = gather_head_commit_files_and_changes(
            repo_path, failures
        )
        if expected_files:
            check_commit_boundedness(
                committed_files, line_counts, expected_files, failures
            )
        else:
            failures.append(
                "Unable to determine expected file scope; commit gate cannot validate "
                "that HEAD is bounded to the selected task."
            )
        check_commit_message(repo_path, task_id, failures)

    if failures:
        print("COMMIT GATE CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("COMMIT GATE CHECK: PASS")
    print(f"Task: {task_id}")
    if repo_path is not None:
        print(f"Repo: {repo_path}")
    print(f"Expected branch: {expected_branch or '(unknown)'}")
    print(f"Current branch: {current_branch or '(unknown)'}")
    print(f"Base branch: {base_branch or '(none)'}")
    if ahead_count is not None:
        print(f"Commits ahead of {base_branch}: {ahead_count}")
    print(f"HEAD: {head_sha or '(unknown)'}")

    if committed_files:
        print("Committed files in HEAD:")
        for path in sorted(committed_files):
            changes = line_counts.get(path)
            if changes is not None:
                print(f"- {path} (changed lines: {changes})")
            else:
                print(f"- {path}")

    print("Checks:")
    print("- task packet exists and parses")
    print("- WCS repo path exists")
    print("- current branch matches expected task branch")
    print("- HEAD commit exists")
    print("- branch is ahead of main/master by at least 1 commit")
    print("- worktree is clean after commit")
    print("- HEAD commit message references the task id")
    print("- committed files are within expected task file scope")
    print("- committed file count and changed-line counts are within bounded thresholds")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


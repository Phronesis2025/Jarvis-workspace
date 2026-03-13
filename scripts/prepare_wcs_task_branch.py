from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


class BranchPrepError(Exception):
    pass


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BranchPrepError(f"Required JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise BranchPrepError(f"Invalid JSON in {path}: {exc}") from exc


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


def normalize_task_id(task_id: str) -> str:
    task_id = task_id.strip().upper()
    if not task_id.startswith("WCS-"):
        raise BranchPrepError(f"Expected task id like WCS-009. Got: {task_id}")
    return task_id


def target_branch_name(task_id: str) -> str:
    return f"jarvis-task-{task_id.lower()}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare the correct WCS task branch before execution."
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-009")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root. Defaults to script grandparent directory.",
    )
    parser.add_argument(
        "--repo",
        help="Override WCS repo path. If omitted, use state/project_status_wcs.json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent
    state_dir = workspace / "state"

    task_id = normalize_task_id(args.task)
    target_branch = target_branch_name(task_id)

    if args.repo:
        repo_path = Path(args.repo).resolve()
    else:
        project_status = read_json(state_dir / "project_status_wcs.json")
        repo_path = Path(project_status["repo_path"]).resolve()

    if not repo_path.exists():
        raise BranchPrepError(f"WCS repo path does not exist: {repo_path}")

    git_dir = repo_path / ".git"
    if not git_dir.exists():
        raise BranchPrepError(f"Path is not a git repo: {repo_path}")

    current_branch_result = run_git(repo_path, ["branch", "--show-current"])
    if current_branch_result.returncode != 0:
        raise BranchPrepError(current_branch_result.stderr.strip() or "Failed to detect current branch.")

    current_branch = current_branch_result.stdout.strip()

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        raise BranchPrepError(status_result.stderr.strip() or "Failed to inspect repo status.")

    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    is_dirty = bool(dirty_lines)

    if current_branch == target_branch:
        mode = "already_on_target_dirty" if is_dirty else "already_on_target_clean"
        print(f"MODE: {mode}")
        print(f"CURRENT_BRANCH: {current_branch}")
        print(f"TARGET_BRANCH: {target_branch}")
        print(f"DIRTY: {'true' if is_dirty else 'false'}")
        if dirty_lines:
            print("DIRTY_FILES:")
            for line in dirty_lines:
                print(line)
        return 0

    if is_dirty:
        raise BranchPrepError(
            "Refusing to switch branches because the WCS repo has uncommitted changes on the wrong branch.\n"
            f"Current branch: {current_branch}\n"
            f"Target branch: {target_branch}\n"
            "Dirty files:\n" + "\n".join(dirty_lines)
        )

    branch_exists_result = run_git(repo_path, ["branch", "--list", target_branch])
    if branch_exists_result.returncode != 0:
        raise BranchPrepError(branch_exists_result.stderr.strip() or "Failed to inspect branch list.")

    target_exists = bool(branch_exists_result.stdout.strip())

    if target_exists:
        switch_result = run_git(repo_path, ["switch", target_branch])
        if switch_result.returncode != 0:
            raise BranchPrepError(switch_result.stderr.strip() or f"Failed to switch to {target_branch}.")
        mode = "switched_to_existing_target"
    else:
        main_exists_result = run_git(repo_path, ["branch", "--list", "main"])
        if main_exists_result.returncode != 0:
            raise BranchPrepError(main_exists_result.stderr.strip() or "Failed to inspect main branch.")
        if not main_exists_result.stdout.strip():
            raise BranchPrepError("Cannot create target branch because local 'main' branch was not found.")

        create_result = run_git(repo_path, ["switch", "-c", target_branch, "main"])
        if create_result.returncode != 0:
            raise BranchPrepError(create_result.stderr.strip() or f"Failed to create {target_branch} from main.")
        mode = "created_new_target_from_main"

    print(f"MODE: {mode}")
    print(f"CURRENT_BRANCH: {current_branch}")
    print(f"TARGET_BRANCH: {target_branch}")
    print("DIRTY: false")
    print(f"REPO_PATH: {repo_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BranchPrepError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
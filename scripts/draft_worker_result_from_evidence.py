"""
Draft a truthful worker_result.json from real repo/task evidence.
Does not stamp, reconcile, or fabricate completion.
Operator should review the drafted result before guarded post-worker if appropriate.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, List, Optional, Set, Tuple


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Draft a truthful worker result JSON from task packet and repo evidence. "
            "Does not stamp or fabricate completion."
        )
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-042")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--executor",
        default="cursor_agent",
        help="Executor label (default: cursor_agent).",
    )
    parser.add_argument(
        "--mode",
        choices=["working_tree", "head_auto"],
        default="head_auto",
        help=(
            "working_tree: use uncommitted diff only; "
            "head_auto: working tree if changed, else HEAD commit (default)."
        ),
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write results/WCS-XXX_worker_result.json; without this, dry-run only.",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    t = normalize_text(raw).upper()
    if not re.match(r"^WCS-\d+$", t):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return t


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def run_git(repo_path: Path, args: List[str], timeout: int = 10) -> Tuple[int, str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=str(repo_path),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )
    out = (proc.stdout or "").strip()
    if proc.stderr:
        out = f"{out}\n{proc.stderr.strip()}" if out else proc.stderr.strip()
    return proc.returncode, out


def get_expected_scope(packet: dict) -> Set[str]:
    """Derive expected file scope from task packet (same spirit as worker_result_validate)."""
    expected: Set[str] = set()
    target_files = packet.get("target_files")
    if isinstance(target_files, list):
        for item in target_files:
            path = normalize_text(item)
            if path:
                expected.add(path.replace("\\", "/"))
    if not expected:
        for key in ("target_file", "file_path", "file"):
            value = normalize_text(packet.get(key))
            if value:
                expected.add(value.replace("\\", "/"))
                break
    if not expected:
        suspected = packet.get("suspected_files")
        if isinstance(suspected, list):
            for item in suspected:
                path = normalize_text(item)
                if path:
                    expected.add(path.replace("\\", "/"))
    if not expected:
        notes = normalize_text(packet.get("notes"))
        if notes and ("\\" in notes or "/" in notes) and " " not in notes:
            expected.add(notes.replace("\\", "/"))
    return expected


def get_changed_files_working_tree(repo_path: Path) -> List[str]:
    """Files changed in working tree vs HEAD (repo-relative, forward slashes)."""
    code, out = run_git(repo_path, ["diff", "--name-only", "HEAD"])
    if code != 0:
        return []
    lines = [ln.strip().replace("\\", "/") for ln in out.splitlines() if ln.strip()]
    return lines


def get_changed_files_head_commit(repo_path: Path) -> List[str]:
    """Files changed in HEAD commit (repo-relative, forward slashes)."""
    code, out = run_git(repo_path, ["diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"])
    if code != 0:
        return []
    lines = [ln.strip().replace("\\", "/") for ln in out.splitlines() if ln.strip()]
    return lines


def main() -> int:
    args = parse_args()
    try:
        task_id = validate_task_id(args.task)
    except ValueError as e:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {normalize_text(args.task).upper() or '(missing)'}")
        print(f"Reason: {e}")
        return 1

    script_dir = Path(__file__).resolve().parent
    workspace = Path(args.workspace).resolve() if args.workspace else script_dir.parent
    if not workspace.exists():
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print("Reason: Workspace path does not exist.")
        return 1

    task_packet_path = workspace / "tasks" / f"{task_id}_task.json"
    if not task_packet_path.is_file():
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print("Reason: Task packet does not exist.")
        print(f"Expected: {task_packet_path}")
        return 1

    try:
        packet = read_json(task_packet_path)
    except Exception as e:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Reason: Could not read task packet: {e}")
        return 1

    if not isinstance(packet, dict):
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print("Reason: Task packet must be a JSON object.")
        return 1

    raw_repo = normalize_text(packet.get("repo_path") or "")
    if not raw_repo:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print("Reason: Task packet has no repo_path.")
        return 1
    repo_path = Path(raw_repo).resolve()
    if not repo_path.exists() or not repo_path.is_dir():
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Repo path: {repo_path}")
        print("Reason: Task repo path does not exist or is not a directory.")
        return 1

    expected_branch = normalize_text(packet.get("branch_name") or "")
    if not expected_branch:
        expected_branch = f"jarvis-task-{task_id.lower()}"

    code, branch_out = run_git(repo_path, ["branch", "--show-current"])
    if code != 0 or not branch_out:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Repo path: {repo_path}")
        print("Reason: Could not determine current branch.")
        return 1
    current_branch = branch_out.strip()
    if current_branch != expected_branch:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
        print("Reason: Current branch does not match expected task branch.")
        return 1

    expected_scope = get_expected_scope(packet)
    if not expected_scope:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print("Reason: Could not derive expected file scope from task packet.")
        return 1

    evidence_source: Optional[str] = None
    changed: List[str] = []

    if args.mode == "working_tree":
        changed = get_changed_files_working_tree(repo_path)
        evidence_source = "working_tree" if changed else None
    else:
        changed = get_changed_files_working_tree(repo_path)
        if changed:
            evidence_source = "working_tree"
        else:
            changed = get_changed_files_head_commit(repo_path)
            evidence_source = "head_commit" if changed else None

    if not changed:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
        print("Reason: No changed files detected (no working tree changes and no HEAD commit changes in head_auto mode).")
        return 1

    if evidence_source is None:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print("Reason: No evidence source for changed files.")
        return 1

    for f in changed:
        norm = f.replace("\\", "/")
        if norm not in expected_scope:
            print("DRAFT WORKER RESULT: FAIL")
            print(f"Task: {task_id}")
            print(f"Repo path: {repo_path}")
            print(f"Expected scope: {sorted(expected_scope)}")
            print(f"Changed files: {changed}")
            print(f"Reason: Changed file {norm!r} is outside expected task scope.")
            return 1

    summary = (
        f"Implemented bounded changes for {task_id} in {', '.join(sorted(changed))} on branch {current_branch}."
    )

    notes = f"Evidence from {evidence_source}. Drafted by script; operator should review before post-worker."

    draft = {
        "task_id": task_id,
        "status": "worker_complete",
        "executor": normalize_text(args.executor) or "cursor_agent",
        "summary": summary,
        "files_changed": sorted(changed),
        "commands_run": [],
        "issues_encountered": [],
        "notes": notes,
        "completed_at": "",
    }

    out_path = workspace / "results" / f"{task_id}_worker_result.json"
    written = False
    if args.write:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(draft, indent=2) + "\n", encoding="utf-8")
        written = True

    print("DRAFT WORKER RESULT: PASS")
    print(f"Task: {task_id}")
    print(f"Workspace: {workspace}")
    print(f"Repo path: {repo_path}")
    print(f"Expected branch: {expected_branch}")
    print(f"Current branch: {current_branch}")
    print(f"Evidence source: {evidence_source}")
    print(f"Output path: {out_path}")
    print(f"Written: {'yes' if written else 'no'}")
    print("")
    print(json.dumps(draft, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

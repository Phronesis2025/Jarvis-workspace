"""
Operator-facing wrapper for the current Phase 1 WCS lane.

This consolidates the current prep/post operator entrypoints without
replacing the validated helper scripts underneath.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Sequence, Tuple


class OperatorEntrypointError(Exception):
    pass


def normalize_task_id(raw: str) -> str:
    task_id = raw.strip().upper()
    if not re.match(r"^WCS-\d+$", task_id):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return task_id


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Operator-facing wrapper for the current Phase 1 WCS lane. "
            "Delegates to the existing validated helpers; does not replace them."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    prep = subparsers.add_parser(
        "prep",
        help="Ensure packet exists, run guarded pre_worker, and optionally launch Cursor.",
    )
    prep.add_argument("--task", required=True, help="Task id, e.g. WCS-044")
    prep.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    prep.add_argument(
        "--launch-cursor",
        action="store_true",
        help=(
            "After successful prep, call run_cursor_worker.py for this task "
            "with strict post-launch audit."
        ),
    )

    post = subparsers.add_parser(
        "post",
        help="Delegate to guarded post_worker with existing evidence passthrough flags.",
    )
    post.add_argument("--task", required=True, help="Task id, e.g. WCS-044")
    post.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    post.add_argument(
        "--draft-worker-result",
        action="store_true",
        help="Pass through to run_guarded_task_cycle.py post_worker.",
    )
    post.add_argument(
        "--worker-command",
        action="append",
        default=[],
        metavar="TEXT",
        help="Repeatable truthful worker evidence string.",
    )
    post.add_argument(
        "--worker-executor",
        metavar="TEXT",
        help="Optional worker executor label passthrough.",
    )
    post.add_argument(
        "--draft-qa-result",
        action="store_true",
        help="Pass through to run_guarded_task_cycle.py post_worker.",
    )
    post.add_argument(
        "--build-status",
        choices=["pass", "fail", "skip", "unknown"],
        help="QA evidence: build outcome.",
    )
    post.add_argument(
        "--smoke-status",
        choices=["pass", "fail", "skip", "unknown"],
        help="QA evidence: smoke outcome.",
    )
    post.add_argument(
        "--manual-status",
        choices=["pass", "fail", "skip", "unknown"],
        help="QA evidence: manual verification outcome.",
    )
    post.add_argument(
        "--manual-check",
        action="append",
        default=[],
        metavar="TEXT",
        help="Repeatable manual verification description.",
    )
    post.add_argument(
        "--artifact",
        action="append",
        default=[],
        metavar="PATH",
        help="Repeatable artifact path passthrough.",
    )
    post.add_argument(
        "--qa-note",
        action="append",
        default=[],
        metavar="TEXT",
        help="Repeatable QA note passthrough.",
    )

    return parser.parse_args()


def workspace_from_args(raw_workspace: str | None) -> Path:
    if raw_workspace:
        return Path(raw_workspace).resolve()
    return Path(__file__).resolve().parent.parent


def run_helper(cmd: Sequence[str], cwd: Path) -> Tuple[int, str]:
    proc = subprocess.run(
        list(cmd),
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = ""
    if proc.stdout:
        output += proc.stdout
    if proc.stderr:
        if output:
            output += "\n"
        output += proc.stderr
    return proc.returncode, output.rstrip()


def print_helper_result(cmd: Sequence[str], output: str) -> None:
    print(f"Running helper command: {' '.join(cmd)}")
    if output:
        print("--- helper output begin ---")
        print(output)
        print("--- helper output end ---")


def ensure_workspace_exists(workspace: Path) -> None:
    if not workspace.exists():
        raise OperatorEntrypointError(f"Workspace path does not exist: {workspace}")


def task_paths(workspace: Path, task_id: str) -> dict[str, Path]:
    return {
        "packet_json": workspace / "tasks" / f"{task_id}_task.json",
        "packet_md": workspace / "tasks" / f"{task_id}_task.md",
        "handoff": workspace / "scratch" / "cursor_handoffs" / f"{task_id}_cursor_handoff.md",
        "summary": workspace / "scratch" / "task_cycle_summaries" / f"{task_id}_task_cycle_summary.md",
    }


def handle_prep(args: argparse.Namespace) -> int:
    try:
        task_id = normalize_task_id(args.task)
    except ValueError as e:
        print("WCS OPERATOR ENTRYPOINT: FAIL")
        print("Mode: prep")
        print(f"Reason: {e}")
        return 1

    workspace = workspace_from_args(args.workspace)
    scripts_dir = workspace / "scripts"
    try:
        ensure_workspace_exists(workspace)
    except OperatorEntrypointError as e:
        print("WCS OPERATOR ENTRYPOINT: FAIL")
        print("Mode: prep")
        print(f"Task: {task_id}")
        print(f"Reason: {e}")
        return 1

    paths = task_paths(workspace, task_id)
    packet_state = "already present"

    if not paths["packet_json"].is_file():
        packet_cmd = [
            sys.executable,
            str(scripts_dir / "generate_task_packet.py"),
            "--task",
            task_id,
            "--workspace",
            str(workspace),
        ]
        code, output = run_helper(packet_cmd, workspace)
        print_helper_result(packet_cmd, output)
        if code != 0:
            print("WCS OPERATOR ENTRYPOINT: FAIL")
            print("Mode: prep")
            print(f"Task: {task_id}")
            print("Failed delegated step: generate_task_packet")
            return code
        packet_state = "generated during this run"

    pre_cmd = [
        sys.executable,
        str(scripts_dir / "run_guarded_task_cycle.py"),
        "--task",
        task_id,
        "--workspace",
        str(workspace),
        "--mode",
        "pre_worker",
    ]
    code, output = run_helper(pre_cmd, workspace)
    print_helper_result(pre_cmd, output)
    if code != 0:
        print("WCS OPERATOR ENTRYPOINT: FAIL")
        print("Mode: prep")
        print(f"Task: {task_id}")
        print("Failed delegated step: run_guarded_task_cycle pre_worker")
        return code

    if args.launch_cursor:
        launch_cmd = [
            sys.executable,
            str(scripts_dir / "run_cursor_worker.py"),
            "--task",
            task_id,
            "--workspace",
            str(workspace),
            "--require-auditable-delta",
        ]
        code, output = run_helper(launch_cmd, workspace)
        print_helper_result(launch_cmd, output)
        if code != 0:
            print("WCS OPERATOR ENTRYPOINT: FAIL")
            print("Mode: prep")
            print(f"Task: {task_id}")
            print("Failed delegated step: run_cursor_worker")
            return code

    print("WCS OPERATOR ENTRYPOINT: PASS")
    print("Mode: prep")
    print(f"Task: {task_id}")
    print(f"Task packet: {packet_state}")
    print(f"Task packet JSON: {paths['packet_json']}")
    print(f"Task packet markdown: {paths['packet_md']}")
    print(f"Cursor handoff: {paths['handoff']}")
    print(f"Task cycle summary: {paths['summary']}")
    if args.launch_cursor:
        print("Cursor launch: attempted via run_cursor_worker.py")
    else:
        print("Cursor launch: not attempted")
    print("Worker result: not written by this wrapper")
    print("QA result: not written by this wrapper")
    return 0


def handle_post(args: argparse.Namespace) -> int:
    try:
        task_id = normalize_task_id(args.task)
    except ValueError as e:
        print("WCS OPERATOR ENTRYPOINT: FAIL")
        print("Mode: post")
        print(f"Reason: {e}")
        return 1

    workspace = workspace_from_args(args.workspace)
    scripts_dir = workspace / "scripts"
    try:
        ensure_workspace_exists(workspace)
    except OperatorEntrypointError as e:
        print("WCS OPERATOR ENTRYPOINT: FAIL")
        print("Mode: post")
        print(f"Task: {task_id}")
        print(f"Reason: {e}")
        return 1

    cmd: List[str] = [
        sys.executable,
        str(scripts_dir / "run_guarded_task_cycle.py"),
        "--task",
        task_id,
        "--workspace",
        str(workspace),
        "--mode",
        "post_worker",
    ]
    if args.draft_worker_result:
        cmd.append("--draft-worker-result")
    if args.worker_executor:
        cmd.extend(["--worker-executor", args.worker_executor])
    for item in args.worker_command or []:
        cmd.extend(["--worker-command", item])
    if args.draft_qa_result:
        cmd.append("--draft-qa-result")
    if args.build_status:
        cmd.extend(["--build-status", args.build_status])
    if args.smoke_status:
        cmd.extend(["--smoke-status", args.smoke_status])
    if args.manual_status:
        cmd.extend(["--manual-status", args.manual_status])
    for item in args.manual_check or []:
        cmd.extend(["--manual-check", item])
    for item in args.artifact or []:
        cmd.extend(["--artifact", item])
    for item in args.qa_note or []:
        cmd.extend(["--qa-note", item])

    code, output = run_helper(cmd, workspace)
    print_helper_result(cmd, output)
    if code != 0:
        print("WCS OPERATOR ENTRYPOINT: FAIL")
        print("Mode: post")
        print(f"Task: {task_id}")
        print("Failed delegated step: run_guarded_task_cycle post_worker")
        return code

    print("WCS OPERATOR ENTRYPOINT: PASS")
    print("Mode: post")
    print(f"Task: {task_id}")
    print("Delegation: run_guarded_task_cycle.py --mode post_worker")
    return 0


def main() -> int:
    args = parse_args()
    if args.command == "prep":
        return handle_prep(args)
    if args.command == "post":
        return handle_post(args)
    print("WCS OPERATOR ENTRYPOINT: FAIL")
    print(f"Reason: Unsupported command: {args.command!r}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

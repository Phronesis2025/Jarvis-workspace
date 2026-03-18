"""
Sequential multi-task runner for the live Jarvis/WCS lane.

Runs multiple WCS tasks one after another by reusing run_one_task_full_cycle.py.
No concurrency, no scheduling, no batch preselection. Stops immediately on failure,
blocked result, escalation, or gate failure. Preserves honest manual-verification
checkpoint: interactive operator prompt at each checkpoint.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Sequence, Tuple


def positive_int(raw: str) -> int:
    value = int(raw)
    if value < 1:
        raise argparse.ArgumentTypeError("Value must be a positive integer.")
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run multiple WCS tasks sequentially using the proven single-task flow. "
            "Stops on failure, no ready task, or operator abort. Interactive at checkpoints."
        )
    )
    parser.add_argument(
        "--max-tasks",
        type=positive_int,
        default=3,
        metavar="N",
        help="Maximum tasks to attempt in this session (default: 3).",
    )
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--launch-cursor",
        action="store_true",
        help="Pass through to run_one_task_full_cycle: strict Cursor launch after prep.",
    )
    parser.add_argument(
        "--agent-timeout-seconds",
        type=positive_int,
        metavar="SECONDS",
        help="Pass through for Agent CLI timeout. Used only with --launch-cursor.",
    )
    parser.add_argument(
        "--agent-model",
        metavar="MODEL",
        help="Pass through for Agent CLI model. Used only with --launch-cursor.",
    )
    parser.add_argument(
        "--manage-dev-server",
        action="store_true",
        help="Pass through: manage dev server for smoke/manual.",
    )
    parser.add_argument(
        "--force-restart-dev-server",
        action="store_true",
        help="Pass through: kill process on dev port before starting.",
    )
    parser.add_argument(
        "--dev-port",
        type=positive_int,
        default=3000,
        metavar="PORT",
        help="Pass through: dev server port (default: 3000).",
    )
    parser.add_argument(
        "--capture-screenshot",
        action="store_true",
        help="Pass through: capture screenshot for manual verification.",
    )
    parser.add_argument(
        "--manual-url",
        metavar="URL",
        help="Pass through: URL for manual verification page.",
    )
    parser.add_argument(
        "--commit-message",
        metavar="TEXT",
        help="Pass through: custom commit message template.",
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


def build_passthrough_args(args: argparse.Namespace, workspace: Path) -> List[str]:
    """Build list of flags to pass through to run_one_task_full_cycle."""
    passthrough: List[str] = ["--workspace", str(workspace)]
    if args.launch_cursor:
        passthrough.append("--launch-cursor")
    if args.agent_timeout_seconds is not None:
        passthrough.extend(["--agent-timeout-seconds", str(args.agent_timeout_seconds)])
    if args.agent_model:
        passthrough.extend(["--agent-model", args.agent_model])
    if args.manage_dev_server:
        passthrough.append("--manage-dev-server")
    if args.force_restart_dev_server:
        passthrough.append("--force-restart-dev-server")
    passthrough.extend(["--dev-port", str(args.dev_port)])
    if args.capture_screenshot:
        passthrough.append("--capture-screenshot")
    if args.manual_url:
        passthrough.extend(["--manual-url", args.manual_url])
    if args.commit_message:
        passthrough.extend(["--commit-message", args.commit_message])
    return passthrough


def select_next_task(workspace: Path) -> Tuple[Optional[str], int, str]:
    """Run select_next_ready_task. Returns (task_id, exit_code, output)."""
    scripts_dir = workspace / "scripts"
    cmd = [
        sys.executable,
        str(scripts_dir / "select_next_ready_task.py"),
        "--workspace",
        str(workspace),
        "--project",
        "WCS",
    ]
    code, output = run_helper(cmd, workspace)
    task_id = None
    if code == 0:
        for line in output.splitlines():
            stripped = line.strip()
            if stripped.startswith("Selected task id:"):
                task_id = stripped.split(":", 1)[1].strip().upper()
                break
    return task_id, code, output


# Exit codes from run_one_task_full_cycle (must match run_one_task_full_cycle.EXIT_*)
_EXIT_STOP_COMMIT = 10
_EXIT_STOP_MANUAL = 11


def run_full_cycle(
    workspace: Path,
    task_id: str,
    confirm_commit: bool,
    manual_check: Optional[str],
    finalize: bool,
    passthrough: List[str],
) -> Tuple[int, str]:
    """Run run_one_task_full_cycle for pinned task_id. Returns (exit_code, output)."""
    scripts_dir = workspace / "scripts"
    cmd = [
        sys.executable,
        str(scripts_dir / "run_one_task_full_cycle.py"),
        "--task",
        task_id,
        *passthrough,
    ]
    if finalize:
        cmd.append("--finalize")
        if manual_check:
            cmd.extend(["--manual-check", manual_check])
    else:
        if confirm_commit:
            cmd.append("--confirm-commit")
        if manual_check:
            cmd.extend(["--manual-check", manual_check])
    return run_helper(cmd, workspace)


def print_session_result(
    tasks_attempted: int,
    tasks_completed: int,
    last_task: Optional[str],
    stop_reason: str,
) -> None:
    print("")
    print("=" * 60)
    print("RUN TASK SEQUENCE: SESSION RESULT")
    print("=" * 60)
    print(f"Tasks attempted: {tasks_attempted}")
    print(f"Tasks completed: {tasks_completed}")
    print(f"Last task touched: {last_task or '(none)'}")
    print(f"Stop reason: {stop_reason}")
    print("")


def main() -> int:
    args = parse_args()
    workspace = workspace_from_args(args.workspace)
    if not workspace.exists():
        print("RUN TASK SEQUENCE: FAIL")
        print(f"Reason: workspace does not exist: {workspace}")
        return 1

    passthrough = build_passthrough_args(args, workspace)
    tasks_attempted = 0
    tasks_completed = 0
    last_task: Optional[str] = None
    stop_reason = ""

    for _ in range(args.max_tasks):
        # 1. Select next ready task
        task_id, sel_code, sel_out = select_next_task(workspace)
        print(sel_out)
        if sel_code == 2:
            stop_reason = "no ready task"
            break
        if sel_code != 0 or not task_id:
            stop_reason = "selection failed"
            print_session_result(tasks_attempted, tasks_completed, last_task, stop_reason)
            return sel_code if sel_code != 0 else 1
        last_task = task_id
        tasks_attempted += 1

        print("")
        print(f"--- TASK {tasks_attempted}/{args.max_tasks}: {task_id} ---")
        print("")

        # 2. Phase 1: prep + optional launch for pinned task_id (stops at commit checkpoint)
        code, output = run_full_cycle(
            workspace=workspace,
            task_id=task_id,
            confirm_commit=False,
            manual_check=None,
            finalize=False,
            passthrough=passthrough,
        )
        print(output)
        if code not in (0, _EXIT_STOP_COMMIT, _EXIT_STOP_MANUAL):
            stop_reason = f"prep/launch failed for {task_id}"
            print_session_result(tasks_attempted, tasks_completed, last_task, stop_reason)
            return code

        if code == 0:
            tasks_completed += 1
            print(f"Task {task_id} completed in one run.")
            continue

        # 3. Checkpoint: commit (code == _EXIT_STOP_COMMIT)
        if code == _EXIT_STOP_COMMIT:
            try:
                reply = input(f"Continue with commit for {task_id}? (y/n): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                stop_reason = "operator aborted at commit checkpoint"
                print_session_result(tasks_attempted, tasks_completed, last_task, stop_reason)
                return 1
            if reply != "y":
                stop_reason = "operator declined commit"
                print_session_result(tasks_attempted, tasks_completed, last_task, stop_reason)
                return 0

            code, output = run_full_cycle(
                workspace=workspace,
                task_id=task_id,
                confirm_commit=True,
                manual_check=None,
                finalize=False,
                passthrough=passthrough,
            )
            print(output)
            if code not in (0, _EXIT_STOP_MANUAL):
                stop_reason = f"commit/build/smoke failed for {task_id}"
                print_session_result(tasks_attempted, tasks_completed, last_task, stop_reason)
                return code

            if code == 0:
                tasks_completed += 1
                print(f"Task {task_id} completed.")
                continue

        # 4. Checkpoint: manual verification (code == _EXIT_STOP_MANUAL)
        if code == _EXIT_STOP_MANUAL:
            try:
                note = input(
                    f"Manual verification note for {task_id} (or 'n' to abort): "
                ).strip()
            except (EOFError, KeyboardInterrupt):
                stop_reason = "operator aborted at manual checkpoint"
                print_session_result(tasks_attempted, tasks_completed, last_task, stop_reason)
                return 1
            if note.lower() == "n" or not note:
                stop_reason = "operator declined manual verification"
                print_session_result(tasks_attempted, tasks_completed, last_task, stop_reason)
                return 0

            code, output = run_full_cycle(
                workspace=workspace,
                task_id=task_id,
                confirm_commit=False,
                manual_check=note,
                finalize=True,
                passthrough=passthrough,
            )
            print(output)
            if code != 0:
                stop_reason = f"finalize/post failed for {task_id}"
                print_session_result(tasks_attempted, tasks_completed, last_task, stop_reason)
                return code

            tasks_completed += 1
            print(f"Task {task_id} completed (finalize).")
            continue

        stop_reason = f"unexpected exit code for {task_id}"
        print_session_result(tasks_attempted, tasks_completed, last_task, stop_reason)
        return 1

    stop_reason = stop_reason or f"reached max-tasks ({args.max_tasks})"
    print_session_result(tasks_attempted, tasks_completed, last_task, stop_reason)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

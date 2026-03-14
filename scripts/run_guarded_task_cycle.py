"""
Run a guarded WCS task cycle for a single task.
Orchestrates existing helpers; stops immediately on the first failure.
Does not execute worker code, run QA directly, or invent new task logic.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run a guarded WCS task cycle by orchestrating existing helpers. "
            "Stops immediately on first failure."
        )
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-019")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--mode",
        choices=["pre_worker", "post_worker", "full"],
        default="post_worker",
        help="Cycle mode: pre_worker, post_worker, or full (default: post_worker).",
    )
    parser.add_argument(
        "--draft-qa-result",
        action="store_true",
        help="Optional: run draft_qa_result_from_evidence.py with --write before QA validation (post_worker/full only).",
    )
    parser.add_argument(
        "--build-status",
        choices=["pass", "fail", "skip", "unknown"],
        help="QA evidence: build outcome (used only with --draft-qa-result).",
    )
    parser.add_argument(
        "--smoke-status",
        choices=["pass", "fail", "skip", "unknown"],
        help="QA evidence: smoke outcome (used only with --draft-qa-result).",
    )
    parser.add_argument(
        "--manual-status",
        choices=["pass", "fail", "skip", "unknown"],
        help="QA evidence: manual verification outcome (used only with --draft-qa-result).",
    )
    parser.add_argument(
        "--manual-check",
        action="append",
        default=[],
        metavar="TEXT",
        help="QA evidence: repeatable manual check description (used only with --draft-qa-result).",
    )
    parser.add_argument(
        "--artifact",
        action="append",
        default=[],
        metavar="PATH",
        help="QA evidence: repeatable artifact path (used only with --draft-qa-result).",
    )
    parser.add_argument(
        "--qa-note",
        action="append",
        default=[],
        metavar="TEXT",
        help="QA evidence: repeatable note line (used only with --draft-qa-result).",
    )
    return parser.parse_args()


def normalize_task_id(raw: str) -> str:
    t = raw.strip().upper()
    if not re.match(r"^WCS-\d+$", t):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return t


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def run_step(
    name: str,
    cmd: List[str],
    cwd: Path,
) -> Tuple[bool, str]:
    """Run a single orchestration step. Return (ok, output_text)."""
    proc = subprocess.run(
        cmd,
        cwd=str(cwd),
        capture_output=True,
        text=True,
    )
    combined = ""
    if proc.stdout:
        combined += proc.stdout
    if proc.stderr:
        if combined:
            combined += "\n"
        combined += proc.stderr
    ok = proc.returncode == 0
    return ok, combined.strip()


def task_paths(workspace: Path, task_id: str) -> Dict[str, Path]:
    return {
        "packet_json": workspace / "tasks" / f"{task_id}_task.json",
        "worker_result": workspace / "results" / f"{task_id}_worker_result.json",
        "qa_result": workspace / "qa" / f"{task_id}_qa_result.json",
    }


def ensure_workspace_and_packet(workspace: Path, task_id: str) -> Optional[str]:
    if not workspace.exists():
        return "Workspace path does not exist."
    paths = task_paths(workspace, task_id)
    if not paths["packet_json"].is_file():
        return f"Task packet not found: {paths['packet_json']}"
    try:
        data = read_json(paths["packet_json"])
    except Exception as e:  # noqa: BLE001
        return f"Could not read or parse task packet: {e}"
    if not isinstance(data, Dict):
        return "Task packet root must be an object."
    return None


def build_pre_worker_steps(
    workspace: Path,
    task_id: str,
) -> List[Tuple[str, List[str]]]:
    scripts_dir = workspace / "scripts"
    py = sys.executable
    steps: List[Tuple[str, List[str]]] = []

    steps.append(
        (
            "prepare_wcs_task_branch",
            [
                py,
                str(scripts_dir / "prepare_wcs_task_branch.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "build_cursor_handoff",
            [
                py,
                str(scripts_dir / "build_cursor_handoff.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "build_task_cycle_summary",
            [
                py,
                str(scripts_dir / "build_task_cycle_summary.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    return steps


def build_draft_qa_result_cmd(
    workspace: Path,
    task_id: str,
    args: argparse.Namespace,
) -> List[str]:
    """Build command line for draft_qa_result_from_evidence.py with --write and QA evidence passthrough."""
    scripts_dir = workspace / "scripts"
    py = sys.executable
    cmd: List[str] = [
        py,
        str(scripts_dir / "draft_qa_result_from_evidence.py"),
        "--task",
        task_id,
        "--workspace",
        str(workspace),
        "--write",
    ]
    if args.build_status is not None:
        cmd.extend(["--build-status", args.build_status])
    if args.smoke_status is not None:
        cmd.extend(["--smoke-status", args.smoke_status])
    if args.manual_status is not None:
        cmd.extend(["--manual-status", args.manual_status])
    for v in args.manual_check or []:
        cmd.extend(["--manual-check", v])
    for v in args.artifact or []:
        cmd.extend(["--artifact", v])
    for v in args.qa_note or []:
        cmd.extend(["--note", v])
    return cmd


def build_post_worker_steps(
    workspace: Path,
    task_id: str,
    draft_qa_result: bool = False,
    draft_qa_args: Optional[argparse.Namespace] = None,
) -> List[Tuple[str, List[str]]]:
    scripts_dir = workspace / "scripts"
    py = sys.executable
    paths = task_paths(workspace, task_id)

    worker_path = paths["worker_result"]
    qa_path = paths["qa_result"]

    steps: List[Tuple[str, List[str]]] = []

    steps.append(
        (
            "worker_change_check",
            [
                py,
                str(scripts_dir / "worker_change_check.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "commit_gate_check",
            [
                py,
                str(scripts_dir / "commit_gate_check.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "worker_result_validate_pre_stamp",
            [
                py,
                str(scripts_dir / "worker_result_validate.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
                "--mode",
                "pre-stamp",
            ],
        )
    )
    if draft_qa_result and draft_qa_args is not None:
        steps.append(
            (
                "draft_qa_result_from_evidence",
                build_draft_qa_result_cmd(workspace, task_id, draft_qa_args),
            )
        )
    steps.append(
        (
            "qa_result_validate_pre_stamp",
            [
                py,
                str(scripts_dir / "qa_result_validate.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
                "--mode",
                "pre-stamp",
            ],
        )
    )
    steps.append(
        (
            "stamp_guard_check",
            [
                py,
                str(scripts_dir / "stamp_guard_check.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )

    steps.append(
        (
            "stamp_worker_result",
            [
                py,
                str(scripts_dir / "stamp_result_timestamp.py"),
                str(worker_path),
            ],
        )
    )
    steps.append(
        (
            "stamp_qa_result",
            [
                py,
                str(scripts_dir / "stamp_result_timestamp.py"),
                str(qa_path),
            ],
        )
    )
    steps.append(
        (
            "pre_reconcile_check",
            [
                py,
                str(scripts_dir / "pre_reconcile_check.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "reconcile_task_outcome",
            [
                py,
                str(scripts_dir / "reconcile_task_outcome.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "post_reconcile_validate",
            [
                py,
                str(scripts_dir / "post_reconcile_validate.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "build_task_cycle_summary",
            [
                py,
                str(scripts_dir / "build_task_cycle_summary.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )

    return steps


def run_steps_sequence(
    workspace: Path,
    task_id: str,
    mode: str,
    steps: List[Tuple[str, List[str]]],
) -> int:
    print("RUN GUARDED TASK CYCLE: START")
    print(f"Task: {task_id}")
    print(f"Mode: {mode}")
    print(f"Workspace: {workspace}")
    print("")

    executed: List[str] = []

    for name, cmd in steps:
        print(f"Running step: {name}")
        print(f"Command: {' '.join(cmd)}")
        ok, output = run_step(name, cmd, cwd=workspace)
        executed.append(name)
        if output:
            print("--- step output begin ---")
            print(output)
            print("--- step output end ---")
        if not ok:
            print("")
            print("RUN GUARDED TASK CYCLE: FAIL")
            print(f"Task: {task_id}")
            print(f"Mode: {mode}")
            print(f"Workspace: {workspace}")
            print(f"Failed step: {name}")
            print(f"Failed command: {' '.join(cmd)}")
            return 1
        print(f"Step {name}: PASS")
        print("")

    print("RUN GUARDED TASK CYCLE: PASS")
    print(f"Task: {task_id}")
    print(f"Mode: {mode}")
    print(f"Workspace: {workspace}")
    if executed:
        print("Steps run (in order):")
        for name in executed:
            print(f"- {name} (PASS)")
    return 0


def main() -> int:
    args = parse_args()

    try:
        task_id = normalize_task_id(args.task)
    except ValueError as e:
        print("RUN GUARDED TASK CYCLE: FAIL")
        print(f"Task: {args.task!r}")
        print(f"Mode: {args.mode}")
        print(f"Workspace: {args.workspace or '(default)'}")
        print(f"Reason: {e}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        workspace = Path(__file__).resolve().parent.parent

    err = ensure_workspace_and_packet(workspace, task_id)
    if err:
        print("RUN GUARDED TASK CYCLE: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print(f"Workspace: {workspace}")
        print(f"Reason: {err}")
        return 1

    paths = task_paths(workspace, task_id)

    mode = args.mode
    steps: List[Tuple[str, List[str]]] = []
    draft_qa = getattr(args, "draft_qa_result", False)

    if mode == "pre_worker":
        steps = build_pre_worker_steps(workspace, task_id)
    elif mode == "post_worker":
        if not paths["worker_result"].is_file():
            print("RUN GUARDED TASK CYCLE: FAIL")
            print(f"Task: {task_id}")
            print(f"Mode: {mode}")
            print(f"Workspace: {workspace}")
            print("Reason: worker result JSON must exist for post_worker mode.")
            return 1
        if not paths["qa_result"].is_file() and not draft_qa:
            print("RUN GUARDED TASK CYCLE: FAIL")
            print(f"Task: {task_id}")
            print(f"Mode: {mode}")
            print(f"Workspace: {workspace}")
            print(
                "Reason: QA result JSON must exist for post_worker mode (or use --draft-qa-result to create it from evidence)."
            )
            return 1
        steps = build_post_worker_steps(
            workspace, task_id, draft_qa_result=draft_qa, draft_qa_args=args if draft_qa else None
        )
    elif mode == "full":
        pre = build_pre_worker_steps(workspace, task_id)
        steps.extend(pre)
        if not paths["worker_result"].is_file():
            print("RUN GUARDED TASK CYCLE: FAIL")
            print(f"Task: {task_id}")
            print(f"Mode: {mode}")
            print(f"Workspace: {workspace}")
            print("Reason: worker result JSON must exist for post-worker steps in full mode.")
            return 1
        if not paths["qa_result"].is_file() and not draft_qa:
            print("RUN GUARDED TASK CYCLE: FAIL")
            print(f"Task: {task_id}")
            print(f"Mode: {mode}")
            print(f"Workspace: {workspace}")
            print(
                "Reason: QA result JSON must exist for post-worker steps in full mode (or use --draft-qa-result to create it from evidence)."
            )
            return 1
        post = build_post_worker_steps(
            workspace, task_id, draft_qa_result=draft_qa, draft_qa_args=args if draft_qa else None
        )
        steps.extend(post)
    else:
        print("RUN GUARDED TASK CYCLE: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print(f"Workspace: {workspace}")
        print("Reason: unsupported mode.")
        return 1

    return run_steps_sequence(workspace, task_id, mode, steps)


if __name__ == "__main__":
    raise SystemExit(main())


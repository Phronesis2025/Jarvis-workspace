"""
Build a human-readable summary for a single WCS task cycle.
Reads task, worker, and QA artifacts; writes a markdown summary.
Does not execute the task, modify WCS code, or mutate backlog/state.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build a human-readable summary of a WCS task cycle from current evidence. "
            "Does not execute tasks or mutate state."
        )
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-019")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--output",
        help=(
            "Output file path. Default: "
            "scratch/task_cycle_summaries/<task>_task_cycle_summary.md"
        ),
    )
    return parser.parse_args()


def normalize_task_id(raw: str) -> str:
    t = raw.strip().upper()
    if not re.match(r"^WCS-\d+$", t):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return t


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {path}: {e}") from e


def get_repo_path(packet: Dict[str, Any], workspace: Path) -> Optional[Path]:
    repo = packet.get("repo_path")
    if repo:
        return Path(repo).resolve()
    state_file = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(state_file)
        return Path(data["repo_path"]).resolve()
    except Exception:
        return None


def get_current_branch(repo_path: Path) -> Optional[str]:
    try:
        r = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if r.returncode == 0 and r.stdout:
            return r.stdout.strip()
    except Exception:
        pass
    return None


def load_optional_json(path: Path, failures: List[str]) -> Optional[Dict[str, Any]]:
    if not path.is_file():
        return None
    try:
        data = read_json(path)
    except Exception as e:
        failures.append(f"Could not read or parse JSON file {path}: {e}")
        return None
    if not isinstance(data, dict):
        failures.append(f"JSON root must be an object in {path}.")
        return None
    return data


def build_cycle_assessment(
    has_worker: bool,
    has_qa: bool,
    worker_completed_at: Optional[str],
    qa_completed_at: Optional[str],
) -> str:
    if not has_worker and not has_qa:
        return "Task packet only: no worker or QA results present."
    if has_worker and not has_qa:
        if worker_completed_at:
            return (
                "Worker result present and completed; QA result not yet recorded."
            )
        return "Worker result present but appears pre-stamp (no completed_at); QA result missing."
    if has_worker and has_qa:
        if worker_completed_at and qa_completed_at:
            return (
                "Worker and QA results present with completed timestamps; "
                "task appears fully cycled based on current artifacts."
            )
        return (
            "Worker and QA results present, but at least one appears pre-stamp "
            "(missing completed_at)."
        )
    # Should not reach here, but keep a safe default.
    return "Cycle state could not be classified from current artifacts."


def infer_next_step(
    has_worker: bool,
    has_qa: bool,
    worker_completed_at: Optional[str],
    qa_completed_at: Optional[str],
) -> str:
    if not has_worker and not has_qa:
        return (
            "Next likely step: prepare a bounded worker handoff and run the worker task."
        )
    if has_worker and not has_qa:
        if worker_completed_at:
            return "Next likely step: perform QA for this task and record a QA result."
        return "Next likely step: finalize the worker implementation and then perform QA."
    if has_worker and has_qa:
        if worker_completed_at and qa_completed_at:
            return (
                "Next likely step: confirm backlog/reconcile state reflects this completed cycle."
            )
        return (
            "Next likely step: complete stamping or reconciliation steps for worker/QA results."
        )
    return "Next likely step: review artifacts manually to decide the safest next action."


def summarize_notes(text: str, max_len: int = 240) -> str:
    t = text.strip()
    if len(t) <= max_len:
        return t
    return t[: max_len - 3] + "..."


def build_summary_markdown(
    task_id: str,
    packet: Dict[str, Any],
    packet_md_present: bool,
    worker: Optional[Dict[str, Any]],
    qa: Optional[Dict[str, Any]],
    expected_branch: str,
    current_branch: Optional[str],
) -> Tuple[str, str]:
    """Return (content, evidence_summary_line)."""
    title = packet.get("title") or packet.get("task_id") or task_id
    goal = packet.get("goal") or packet.get("problem_summary") or packet.get("summary") or ""

    has_worker = worker is not None
    has_qa = qa is not None

    worker_status = worker.get("status") if worker else None
    worker_completed_at = worker.get("completed_at") if worker else None
    worker_summary = worker.get("summary") if worker else None

    qa_status = qa.get("status") if qa else None
    qa_completed_at = qa.get("completed_at") if qa else None
    qa_summary = qa.get("summary") if qa else None

    assessment = build_cycle_assessment(
        has_worker=has_worker,
        has_qa=has_qa,
        worker_completed_at=worker_completed_at,
        qa_completed_at=qa_completed_at,
    )
    next_step = infer_next_step(
        has_worker=has_worker,
        has_qa=has_qa,
        worker_completed_at=worker_completed_at,
        qa_completed_at=qa_completed_at,
    )

    current_branch_line = current_branch if current_branch else "(unable to resolve — check repo)"

    evidence_bits = []
    evidence_bits.append("task packet JSON")
    if packet_md_present:
        evidence_bits.append("task markdown")
    if has_worker:
        evidence_bits.append("worker result")
    if has_qa:
        evidence_bits.append("QA result")
    evidence_summary = ", ".join(evidence_bits)

    packet_present_text = "yes"
    worker_present_text = "yes" if has_worker else "no"
    qa_present_text = "yes" if has_qa else "no"
    packet_md_text = "yes" if packet_md_present else "no"

    content_lines = [
        f"# Task cycle summary: {task_id}",
        "",
        "## Task",
        f"- **ID:** {task_id}",
        f"- **Title:** {title}",
        f"- **Goal/summary:** {goal}" if goal else "- **Goal/summary:** (not specified)",
        "",
        "## Branch context",
        f"- **Expected branch:** {expected_branch}",
        f"- **Current branch:** {current_branch_line}",
        "",
        "## Evidence presence",
        f"- **Task packet JSON:** {packet_present_text}",
        f"- **Task packet markdown:** {packet_md_text}",
        f"- **Worker result JSON:** {worker_present_text}",
        f"- **QA result JSON:** {qa_present_text}",
        "",
        "## Worker result",
        f"- **Status:** {worker_status or '(not present)'}",
        f"- **Completed at:** {worker_completed_at or '-'}",
        "",
        "## QA result",
        f"- **Status:** {qa_status or '(not present)'}",
        f"- **Completed at:** {qa_completed_at or '-'}",
        "",
        "## Cycle assessment",
        assessment,
        "",
        "## Next likely step",
        next_step,
        "",
        "## Notes",
    ]

    if worker_summary:
        content_lines.append(
            f"- Worker summary: {summarize_notes(str(worker_summary))}"
        )
    if qa_summary:
        content_lines.append(
            f"- QA summary: {summarize_notes(str(qa_summary))}"
        )
    if not worker_summary and not qa_summary:
        content_lines.append(
            "- No worker/QA summaries available; review source artifacts if needed."
        )

    content = "\n".join(content_lines) + "\n"
    return content, evidence_summary


def main() -> int:
    args = parse_args()
    failures: List[str] = []

    try:
        task_id = normalize_task_id(args.task)
    except ValueError as e:
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print(f"- {e}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        workspace = Path(__file__).resolve().parent.parent

    if not workspace.exists():
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print("- Workspace path does not exist.")
        return 1

    tasks_dir = workspace / "tasks"
    results_dir = workspace / "results"
    qa_dir = workspace / "qa"

    packet_path = tasks_dir / f"{task_id}_task.json"
    if not packet_path.is_file():
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print(f"- Task packet not found: {packet_path}")
        return 1

    try:
        packet = read_json(packet_path)
    except Exception as e:
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print(f"- Could not read or parse task packet: {e}")
        return 1

    if not isinstance(packet, dict):
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print("- Task packet root must be an object.")
        return 1

    packet_md_path = tasks_dir / f"{task_id}_task.md"
    packet_md_present = packet_md_path.is_file()

    worker_path = results_dir / f"{task_id}_worker_result.json"
    qa_path = qa_dir / f"{task_id}_qa_result.json"

    worker = load_optional_json(worker_path, failures)
    qa = load_optional_json(qa_path, failures)

    expected_branch = f"jarvis-task-{task_id.lower()}"
    repo_path = get_repo_path(packet, workspace)
    current_branch = get_current_branch(repo_path) if repo_path and repo_path.exists() else None

    if args.output:
        out_path = Path(args.output).resolve()
    else:
        summaries_dir = workspace / "scratch" / "task_cycle_summaries"
        summaries_dir.mkdir(parents=True, exist_ok=True)
        out_path = summaries_dir / f"{task_id}_task_cycle_summary.md"

    if failures:
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        for f in failures:
            print(f"- {f}")
        return 1

    try:
        content, evidence_summary = build_summary_markdown(
            task_id=task_id,
            packet=packet,
            packet_md_present=packet_md_present,
            worker=worker,
            qa=qa,
            expected_branch=expected_branch,
            current_branch=current_branch,
        )
    except Exception as e:
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print(f"- Failed to build summary content: {e}")
        return 1

    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")
    except Exception as e:
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print(f"- Unable to write summary file: {e}")
        return 1

    print("TASK CYCLE SUMMARY BUILD: PASS")
    print(f"Task: {task_id}")
    print(f"Output: {out_path}")
    if current_branch:
        print(f"Current branch: {current_branch}")
    else:
        print("Current branch: (unable to resolve — check repo)")
    print(f"Summary: included {evidence_summary}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


"""
Select the next eligible ready task from the Jarvis/WCS backlog.
Read-only: does not modify backlog, daily plan, or any state.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Align with jarvis.py selection order
PRIORITY_ORDER = {"P1": 1, "P2": 2, "P3": 3, "P4": 4}
RISK_ORDER = {"low": 1, "medium": 2, "high": 3}
ELIGIBLE_BUCKETS_WCS = {"broken", "ugly"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Select the next eligible ready task from the backlog. "
            "Read-only; does not mutate state."
        )
    )
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--project",
        default="WCS",
        help="Project filter (default: WCS).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Max candidate tasks to show in ranked output (default: 10).",
    )
    return parser.parse_args()


def normalize(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def parse_task_number(task_id: str) -> int:
    t = normalize(task_id).upper()
    if not t.startswith("WCS-"):
        return 999999
    suffix = t.split("-", 1)[1]
    if not suffix.isdigit():
        return 999999
    return int(suffix)


def priority_rank(task: Dict[str, Any]) -> int:
    return PRIORITY_ORDER.get(normalize(task.get("priority")).upper(), 999)


def risk_rank(task: Dict[str, Any]) -> int:
    return RISK_ORDER.get(normalize(task.get("risk")).lower(), 999)


def sort_key(task: Dict[str, Any]) -> Tuple[int, int, int]:
    return (
        priority_rank(task),
        risk_rank(task),
        parse_task_number(normalize(task.get("task_id", ""))),
    )


def is_eligible(task: Any, project: str) -> bool:
    if not isinstance(task, dict):
        return False
    proj = normalize(task.get("project")).upper()
    if proj != project.upper():
        return False
    status = normalize(task.get("status")).lower()
    if status != "ready":
        return False
    bucket = normalize(task.get("bucket")).lower()
    if project.upper() == "WCS" and bucket not in ELIGIBLE_BUCKETS_WCS:
        return False
    tid = normalize(task.get("task_id")).upper()
    if not tid.startswith("WCS-"):
        return False
    return True


def load_backlog(workspace: Path) -> List[Dict[str, Any]]:
    path = workspace / "state" / "master_backlog.json"
    if not path.is_file():
        raise FileNotFoundError(f"Backlog not found: {path}")
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError(f"Backlog root must be a JSON array: {path}")
    return raw


def select_and_rank(
    backlog: List[Dict[str, Any]],
    project: str,
) -> Tuple[List[Dict[str, Any]], List[Tuple[Dict[str, Any], str]]]:
    """
    Return (eligible_sorted, skipped_with_reasons).
    eligible_sorted is sorted by priority, risk, task_id.
    skipped_with_reasons are ineligible tasks with a short reason (e.g. first N we considered).
    """
    eligible: List[Dict[str, Any]] = []
    skipped: List[Tuple[Dict[str, Any], str]] = []

    for task in backlog:
        if not isinstance(task, dict):
            continue
        proj = normalize(task.get("project")).upper()
        status = normalize(task.get("status")).lower()
        bucket = normalize(task.get("bucket")).lower()
        tid = normalize(task.get("task_id")).upper()

        if proj != project.upper():
            skipped.append((task, "wrong project"))
            continue
        if status != "ready":
            skipped.append((task, f"status not ready ({status})"))
            continue
        if project.upper() == "WCS" and bucket not in ELIGIBLE_BUCKETS_WCS:
            skipped.append((task, f"bucket not eligible ({bucket})"))
            continue
        if not tid.startswith("WCS-"):
            skipped.append((task, "invalid task id"))
            continue
        eligible.append(task)

    eligible.sort(key=sort_key)
    return eligible, skipped


def main() -> int:
    args = parse_args()
    workspace = Path(args.workspace).resolve() if args.workspace else Path(__file__).resolve().parent.parent
    project = normalize(args.project) or "WCS"
    limit = max(1, min(args.limit, 100))

    if not workspace.exists():
        print("SELECT NEXT READY TASK: FAIL")
        print("Failures:")
        print("- Workspace path does not exist.")
        return 1

    try:
        backlog = load_backlog(workspace)
    except FileNotFoundError as e:
        print("SELECT NEXT READY TASK: FAIL")
        print("Failures:")
        print(f"- {e}")
        return 1
    except json.JSONDecodeError as e:
        print("SELECT NEXT READY TASK: FAIL")
        print("Failures:")
        print(f"- Invalid JSON in backlog: {e}")
        return 1
    except ValueError as e:
        print("SELECT NEXT READY TASK: FAIL")
        print("Failures:")
        print(f"- {e}")
        return 1

    eligible, skipped = select_and_rank(backlog, project)

    if not eligible:
        print("SELECT NEXT READY TASK: NO MATCH")
        print(f"Workspace: {workspace}")
        print(f"Project: {project}")
        if skipped:
            status_reasons = {}
            for _, reason in skipped[:20]:
                status_reasons[reason] = status_reasons.get(reason, 0) + 1
            summary = "; ".join(f"{r}: {c}" for r, c in sorted(status_reasons.items()))
            print(f"Reason: no eligible ready task. Sample skip reasons: {summary}")
        else:
            print("Reason: no tasks in backlog for this project or backlog empty.")
        return 2

    selected = eligible[0]
    task_id = normalize(selected.get("task_id")).upper()
    title = normalize(selected.get("title")) or task_id
    priority = normalize(selected.get("priority"))
    bucket = normalize(selected.get("bucket"))
    risk = normalize(selected.get("risk"))
    status = normalize(selected.get("status"))

    print("SELECT NEXT READY TASK: PASS")
    print(f"Workspace: {workspace}")
    print(f"Project: {project}")
    print(f"Selected task id: {task_id}")
    print(f"Selected title: {title}")
    print(f"Priority: {priority}  Bucket: {bucket}  Risk: {risk}  Status: {status}")
    print(
        "Reason selected: first eligible ready task by deterministic order "
        "(priority, then risk, then task id)."
    )
    print(f"Reviewed candidate count: {len(eligible)}")
    print("")
    print("Ranked candidates (up to limit):")
    for i, t in enumerate(eligible[:limit], 1):
        tid = normalize(t.get("task_id")).upper()
        tit = normalize(t.get("title")) or tid
        pr = normalize(t.get("priority"))
        rk = normalize(t.get("risk"))
        print(f"  {i}. {tid}  {pr}  {rk}  {tit[:60]}{'...' if len(tit) > 60 else ''}")

    # Skipped section: show a few near-candidates or common skip reasons
    print("")
    print("Skipped (sample):")
    shown = 0
    for task, reason in skipped[:15]:
        if shown >= 8:
            break
        tid = normalize(task.get("task_id")).upper()
        st = normalize(task.get("status")).lower()
        print(f"  - {tid}: {reason}")
        shown += 1
    if not skipped:
        print("  (none; all non-ready tasks excluded from eligibility)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

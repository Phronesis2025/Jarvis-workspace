"""
Draft a truthful qa_result.json from CLI evidence (build/smoke/manual status).
Does not stamp, reconcile, or fabricate completion.
Operator should review the drafted result before guarded post-worker if appropriate.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, List


STATUS_CHOICES = ("pass", "fail", "skip", "unknown")


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Draft a truthful QA result JSON from CLI evidence (build/smoke/manual status). "
            "Does not stamp or fabricate completion."
        )
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-042")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write qa/WCS-XXX_qa_result.json; without this, dry-run only.",
    )
    parser.add_argument(
        "--build-status",
        choices=STATUS_CHOICES,
        help="Build (npm run build) outcome: pass, fail, skip, or unknown.",
    )
    parser.add_argument(
        "--smoke-status",
        choices=STATUS_CHOICES,
        help="Playwright smoke (npm run test:e2e:smoke) outcome: pass, fail, skip, or unknown.",
    )
    parser.add_argument(
        "--manual-status",
        choices=STATUS_CHOICES,
        help="Manual verification outcome: pass, fail, skip, or unknown.",
    )
    parser.add_argument(
        "--manual-check",
        action="append",
        default=[],
        metavar="TEXT",
        help="Repeatable: description of a manual check (e.g. 'Manual browser verification of /about').",
    )
    parser.add_argument(
        "--artifact",
        action="append",
        default=[],
        metavar="PATH",
        help="Repeatable: path to an artifact file; must exist or script fails.",
    )
    parser.add_argument(
        "--note",
        action="append",
        default=[],
        metavar="TEXT",
        help="Repeatable: note line to append to notes.",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    t = normalize_text(raw).upper()
    if not re.match(r"^WCS-\d+$", t):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return t


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_artifact_path(workspace: Path, raw: str) -> Path:
    p = Path(raw)
    if not p.is_absolute():
        p = workspace / raw
    return p.resolve()


def main() -> int:
    args = parse_args()

    try:
        task_id = validate_task_id(args.task)
    except ValueError as e:
        print("DRAFT QA RESULT: FAIL")
        print(f"Task: {normalize_text(args.task).upper() or '(missing)'}")
        print(f"Reason: {e}")
        return 1

    script_dir = Path(__file__).resolve().parent
    workspace = Path(args.workspace).resolve() if args.workspace else script_dir.parent
    if not workspace.exists():
        print("DRAFT QA RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print("Reason: Workspace path does not exist.")
        return 1

    task_packet_path = workspace / "tasks" / f"{task_id}_task.json"
    if not task_packet_path.is_file():
        print("DRAFT QA RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print("Reason: Task packet does not exist.")
        print(f"Expected: {task_packet_path}")
        return 1

    try:
        packet = read_json(task_packet_path)
    except Exception as e:
        print("DRAFT QA RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Reason: Could not read task packet: {e}")
        return 1

    if not isinstance(packet, dict):
        print("DRAFT QA RESULT: FAIL")
        print(f"Task: {task_id}")
        print("Reason: Task packet must be a JSON object.")
        return 1

    # Artifact paths must exist or we fail
    artifacts_resolved: List[str] = []
    for raw in args.artifact or []:
        p = resolve_artifact_path(workspace, raw)
        if not p.exists():
            print("DRAFT QA RESULT: FAIL")
            print(f"Task: {task_id}")
            print(f"Workspace: {workspace}")
            print(f"Reason: Artifact path does not exist: {p}")
            print(f"Supplied: {raw!r}")
            return 1
        artifacts_resolved.append(str(p))

    # Build checks from CLI evidence
    checks_run: List[str] = []
    checks_passed: List[str] = []
    checks_failed: List[str] = []

    if args.build_status in ("pass", "fail"):
        checks_run.append("npm run build")
        if args.build_status == "pass":
            checks_passed.append("npm run build")
        else:
            checks_failed.append("npm run build")

    if args.smoke_status in ("pass", "fail"):
        checks_run.append("npm run test:e2e:smoke")
        if args.smoke_status == "pass":
            checks_passed.append("npm run test:e2e:smoke")
        else:
            checks_failed.append("npm run test:e2e:smoke")

    manual_checks: List[str] = []
    if args.manual_status in ("pass", "fail"):
        manual_checks = [normalize_text(c) for c in (args.manual_check or []) if normalize_text(c)]
        if not manual_checks:
            manual_checks = ["Manual browser verification"]
        for c in manual_checks:
            checks_run.append(c)
            if args.manual_status == "pass":
                checks_passed.append(c)
            else:
                checks_failed.append(c)

    # Determine status: qa_fail if any failed; escalated if no usable checks; else qa_pass
    if checks_failed:
        status = "qa_fail"
    elif not checks_run:
        status = "escalated"
    else:
        status = "qa_pass"

    # qa_tool: truthful text only
    parts: List[str] = []
    if args.build_status in ("pass", "fail"):
        parts.append("Next build")
    if args.smoke_status in ("pass", "fail"):
        parts.append("Playwright smoke")
    if args.manual_status in ("pass", "fail"):
        parts.append("manual browser verification")
    qa_tool = "manual operator QA via " + " and ".join(parts) if parts else "manual operator QA (evidence incomplete; drafted as escalated)"

    # summary: evidence-based, formulaic
    if status == "qa_pass" and checks_run:
        bits = []
        if "npm run build" in checks_passed:
            bits.append("Build passed")
        if "npm run test:e2e:smoke" in checks_passed:
            bits.append("Playwright smoke passed")
        if any(c not in ("npm run build", "npm run test:e2e:smoke") for c in checks_passed):
            bits.append("manual verification passed")
        summary = ", ".join(bits) + " for the targeted change." if bits else "QA checks passed for the targeted change."
    elif status == "qa_fail" and checks_failed:
        bits = []
        if "npm run build" in checks_failed:
            bits.append("Build failed")
        if "npm run test:e2e:smoke" in checks_failed:
            bits.append("Playwright smoke failed")
        if any(c not in ("npm run build", "npm run test:e2e:smoke") for c in checks_failed):
            bits.append("manual verification failed")
        summary = ", ".join(bits) + " during QA for the targeted change." if bits else "QA failed for the targeted change."
    else:
        summary = "QA evidence was incomplete or inconclusive; result drafted as escalated for operator review."

    # notes
    notes_parts = [
        "Drafted by script from CLI evidence. Operator should review before guarded post-worker flow."
    ]
    if args.manual_status in ("skip", "unknown") and (args.build_status or args.smoke_status) in ("pass", "fail"):
        notes_parts.append("Manual verification was skipped or not evidenced.")
    if not checks_run and status == "escalated":
        notes_parts.append("No usable checks ran; evidence incomplete or only skip/unknown supplied.")
    for n in args.note or []:
        t = normalize_text(n)
        if t:
            notes_parts.append(t)
    notes = " ".join(notes_parts)

    draft = {
        "task_id": task_id,
        "status": status,
        "qa_tool": qa_tool,
        "summary": summary,
        "checks_run": checks_run,
        "checks_passed": checks_passed,
        "checks_failed": checks_failed,
        "artifacts": artifacts_resolved,
        "notes": notes,
        "completed_at": "",
    }

    out_path = workspace / "qa" / f"{task_id}_qa_result.json"
    written = False
    if args.write:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(draft, indent=2) + "\n", encoding="utf-8")
        written = True

    print("DRAFT QA RESULT: PASS")
    print(f"Task: {task_id}")
    print(f"Workspace: {workspace}")
    print(f"Output path: {out_path}")
    print(f"Written: {'yes' if written else 'no'}")
    print("")
    print(json.dumps(draft, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

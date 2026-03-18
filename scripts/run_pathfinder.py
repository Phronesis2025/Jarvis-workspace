"""
Pathfinder v1 — read-only discovery worker for WCS defects and change requests.

CLI entrypoint. Accepts minimal intake packet or full task packet.
Gathers bounded context, produces research brief with synthesis, optional draft backlog,
or escalation record. No production code edits. No scheduling. No unattended mode.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

WCS_PROJECT_STATUS = "state/project_status_wcs.json"
KNOWN_ISSUE_TYPES = {"defect", "change_request", "smoke_failure", "qa_failure", "unknown"}
CONFIDENCE_READY = "ready_for_implementation"
CONFIDENCE_NEEDS_MORE = "needs_more_context"
CONFIDENCE_BLOCKED = "blocked"

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

FULL_REQUIRED = {"task_id", "worker", "problem_summary", "scope", "goal"}


def _normalize(v: Any) -> str:
    if v is None:
        return ""
    return str(v).strip() if isinstance(v, str) else str(v).strip()


def _is_minimal_packet(data: dict) -> bool:
    """True if packet looks like minimal intake (has issue_summary, lacks full-task fields)."""
    has_issue = bool(_normalize(data.get("issue_summary")))
    has_full_markers = "worker" in data and data.get("worker") == "pathfinder" and "task_id" in data
    return has_issue and not (has_full_markers and "problem_summary" in data)


def _generate_run_id() -> str:
    """Unique run identifier for minimal intake (no packet task_id)."""
    return f"PF-run-{datetime.now().strftime('%Y%m%d-%H%M%S')}"


def validate_packet(data: Any) -> tuple[str, dict]:
    """
    Validate packet shape. Returns (packet_type, normalized_data) or raises ValueError.
    For minimal: no task_id in output; caller uses run_id for result.
    For full: task_id from packet.
    """
    if not isinstance(data, dict):
        raise ValueError("Packet must be a JSON object")

    if "issue_summary" in data and "worker" not in data and not _normalize(data.get("issue_summary")):
        raise ValueError("Minimal intake requires non-empty issue_summary")

    if _is_minimal_packet(data):
        issue = _normalize(data.get("issue_summary"))
        if not issue:
            raise ValueError("Minimal intake requires non-empty issue_summary")
        out = {
            "issue_summary": issue,
            "page_or_route": _normalize(data.get("page_or_route", "")),
            "evidence_paths": data.get("evidence_paths") if isinstance(data.get("evidence_paths"), list) else [],
            "suspected_files": data.get("suspected_files") if isinstance(data.get("suspected_files"), list) else [],
            "wcs_repo_path": _normalize(data.get("wcs_repo_path", "")),
            "severity": _normalize(data.get("severity", "")),
            "type": _normalize(data.get("type", "")),
        }
        # Minimal has no task_id; use run_id at output time
        return "minimal", out

    # Full task packet
    for key in FULL_REQUIRED:
        if key not in data or not _normalize(data.get(key)):
            raise ValueError(f"Full task packet requires non-empty '{key}'")
    if data.get("worker") != "pathfinder":
        raise ValueError("Full task packet must have worker='pathfinder'")

    evidence = data.get("known_artifacts") or data.get("evidence_paths")
    if not isinstance(evidence, list):
        evidence = []
    suspected = data.get("suspected_files")
    if not isinstance(suspected, list):
        suspected = []

    wcs_repo = _normalize(data.get("repo_path") or data.get("wcs_repo_path", ""))

    out = {
        "task_id": _normalize(data["task_id"]),
        "issue_summary": _normalize(data["problem_summary"]),
        "goal": _normalize(data["goal"]),
        "scope": _normalize(data["scope"]),
        "page_or_route": _normalize(data.get("repo_path") or data.get("page_or_route", "")),
        "evidence_paths": evidence,
        "suspected_files": suspected,
        "wcs_repo_path": wcs_repo,
    }
    return "full", out


# ---------------------------------------------------------------------------
# WCS path resolution
# ---------------------------------------------------------------------------

def _get_wcs_repo_path(workspace: Path, packet: dict) -> Path | None:
    """Resolve WCS repo path from packet or project status. Returns None if not available."""
    raw = _normalize(packet.get("wcs_repo_path", ""))
    if raw:
        p = Path(raw)
        if p.is_absolute() and p.exists():
            return p.resolve()
        candidate = workspace / raw
        if candidate.exists():
            return candidate.resolve()
    status_path = workspace / WCS_PROJECT_STATUS
    if status_path.exists():
        try:
            data = json.loads(status_path.read_text(encoding="utf-8"))
            repo = data.get("repo_path", "")
            if repo:
                p = Path(repo)
                if p.exists():
                    return p.resolve()
        except (json.JSONDecodeError, OSError):
            pass
    return None


def resolve_path(workspace: Path, raw: str, wcs_repo: Path | None, path_kind: str) -> Path | None:
    """
    Resolve path. path_kind: 'evidence' (workspace only) or 'suspected' (workspace then wcs_repo).
    Returns resolved Path if file exists, else None.
    """
    p = Path(raw)
    if p.is_absolute():
        return p.resolve() if p.exists() else None
    # Workspace-relative first
    candidate = workspace / raw
    if candidate.exists():
        return candidate.resolve()
    # For suspected files: try WCS repo when workspace resolution fails
    if path_kind == "suspected" and wcs_repo:
        candidate = wcs_repo / raw
        if candidate.exists():
            return candidate.resolve()
    return None


# ---------------------------------------------------------------------------
# Context gathering (rule-based, bounded)
# ---------------------------------------------------------------------------

def gather_context(workspace: Path, packet: dict) -> dict:
    """
    Rule-based gathering. Only reads paths from packet.
    evidence_paths: workspace-relative only.
    suspected_files: workspace-relative first, then WCS repo-relative when wcs_repo_path available.
    """
    artifacts_reviewed: list[str] = []
    files_reviewed: list[str] = []
    gathered: dict[str, str] = {}
    issues: list[str] = []

    wcs_repo = _get_wcs_repo_path(workspace, packet)
    evidence_paths = packet.get("evidence_paths") or []
    suspected_files = packet.get("suspected_files") or []

    for raw in evidence_paths:
        raw_str = _normalize(raw)
        if not raw_str:
            continue
        p = resolve_path(workspace, raw_str, None, "evidence")
        if p:
            try:
                content = p.read_text(encoding="utf-8", errors="replace")
                gathered[str(p)] = content[:8000]
                artifacts_reviewed.append(raw_str)
            except Exception as e:
                issues.append(f"Could not read evidence {raw_str}: {e}")
        else:
            issues.append(f"Evidence path not found: {raw_str}")

    for raw in suspected_files:
        raw_str = _normalize(raw)
        if not raw_str:
            continue
        p = resolve_path(workspace, raw_str, wcs_repo, "suspected")
        if p:
            try:
                content = p.read_text(encoding="utf-8", errors="replace")
                gathered[str(p)] = content[:8000]
                files_reviewed.append(raw_str)
            except Exception as e:
                issues.append(f"Could not read suspected file {raw_str}: {e}")
        else:
            issues.append(f"Suspected file not found: {raw_str}")

    return {
        "artifacts_reviewed": artifacts_reviewed,
        "files_reviewed": files_reviewed,
        "gathered_content": gathered,
        "issues": issues,
    }


# ---------------------------------------------------------------------------
# Rule-based synthesis
# ---------------------------------------------------------------------------

def _normalize_issue_type(packet: dict) -> str:
    """Infer or use explicit type. Returns known type or 'unknown'."""
    t = _normalize(packet.get("type", "")).lower()
    if t in KNOWN_ISSUE_TYPES:
        return t
    summary = (packet.get("issue_summary") or "").lower()
    if any(w in summary for w in ["smoke", "e2e", "playwright", "test fail"]):
        return "smoke_failure"
    if any(w in summary for w in ["qa fail", "qa_fail", "verification"]):
        return "qa_failure"
    if any(w in summary for w in ["improve", "change", "update", "add"]):
        return "change_request"
    if any(w in summary for w in ["fix", "broken", "bug", "defect"]):
        return "defect"
    return "unknown"


def _build_evidence_summary(context: dict) -> str:
    """One-line summary of what was gathered."""
    a = len(context["artifacts_reviewed"])
    f = len(context["files_reviewed"])
    miss = len(context["issues"])
    parts = []
    if a:
        parts.append(f"{a} artifact(s)")
    if f:
        parts.append(f"{f} file(s)")
    if parts:
        s = "Found " + ", ".join(parts)
        if miss:
            s += f"; {miss} path(s) not found"
        return s + "."
    return "No evidence or suspected files found." if not context["evidence_paths"] and not context["suspected_files"] else "Requested paths not found or not readable."


def _build_missing_context_summary(context: dict, packet: dict) -> str:
    """What was requested but not found."""
    if not context["issues"]:
        return "None."
    requested_evidence = len(packet.get("evidence_paths") or [])
    requested_suspected = len(packet.get("suspected_files") or [])
    found_evidence = len(context["artifacts_reviewed"])
    found_suspected = len(context["files_reviewed"])
    missing = []
    if requested_evidence > found_evidence:
        missing.append(f"{requested_evidence - found_evidence} evidence path(s)")
    if requested_suspected > found_suspected:
        missing.append(f"{requested_suspected - found_suspected} suspected file(s)")
    if missing:
        return "; ".join(context["issues"][:5])  # Bounded list
    return "None."


def _compute_confidence(context: dict, packet: dict) -> tuple[str, str]:
    """
    Returns (confidence, readiness_signal).
    confidence: ready_for_implementation | needs_more_context | blocked
    """
    found = context["artifacts_reviewed"] or context["files_reviewed"]
    requested = (packet.get("evidence_paths") or []) + (packet.get("suspected_files") or [])

    if not found and requested:
        return CONFIDENCE_BLOCKED, "Required paths not found; cannot proceed safely."
    if not found and not requested:
        return CONFIDENCE_NEEDS_MORE, "No evidence or suspected files provided; add paths for useful investigation."
    if found and not context["issues"]:
        return CONFIDENCE_READY, "Evidence gathered; ready for operator to open implementation task."
    if found and context["issues"]:
        return CONFIDENCE_NEEDS_MORE, "Partial evidence; some paths missing. Review and add if needed."
    return CONFIDENCE_NEEDS_MORE, "Review gathered context before next step."


def _likely_next_action(confidence: str, context: dict) -> str:
    """Rule-based next action."""
    if confidence == CONFIDENCE_READY:
        return "Review findings and open implementation task if scope is clear."
    if confidence == CONFIDENCE_NEEDS_MORE:
        if context["issues"]:
            return "Add missing evidence_paths or suspected_files, or confirm paths are correct."
        return "Add evidence_paths or suspected_files for richer context, or proceed with current findings."
    return "Provide valid evidence_paths or suspected_files before re-running Pathfinder."


# ---------------------------------------------------------------------------
# Result / escalation generation
# ---------------------------------------------------------------------------

def should_escalate(packet: dict, context: dict) -> tuple[bool, str]:
    """Decide if Pathfinder should escalate instead of producing a brief."""
    if not packet.get("issue_summary"):
        return True, "No issue or problem summary provided"
    evidence = packet.get("evidence_paths") or packet.get("known_artifacts") or []
    suspected = packet.get("suspected_files") or []
    if (evidence or suspected) and not context["artifacts_reviewed"] and not context["files_reviewed"]:
        return True, "Required artifacts or suspected files not found or not readable"
    return False, ""


def _build_draft_backlog_candidate(
    packet: dict, context: dict, run_id: str, confidence: str
) -> dict | None:
    """
    Build draft backlog candidate when confidence is sufficient.
    Omit when blocked. Include when ready or needs_more (has some evidence).
    Clearly marked as draft/operator-review-only.
    """
    if confidence == CONFIDENCE_BLOCKED:
        return None
    issue = packet.get("issue_summary", "")
    page = _normalize(packet.get("page_or_route", ""))
    suspected = context.get("files_reviewed") or context.get("suspected_files", [])
    primary_file = suspected[0] if suspected else ""
    title = issue[:80] + ("..." if len(issue) > 80 else "")
    return {
        "_draft": True,
        "_operator_review_required": True,
        "project": "WCS",
        "bucket": "ugly",
        "priority": "P3",
        "risk": "low",
        "title": title,
        "notes": primary_file or page or "Pathfinder intake",
        "source_run_id": run_id,
        "source": "pathfinder_v1",
    }


def build_result(
    packet: dict, context: dict, workspace: Path, run_id: str, ptype: str
) -> dict:
    """Build pathfinder_result JSON with synthesis and optional draft backlog."""
    issue = packet.get("issue_summary", "")
    task_id = run_id if ptype == "minimal" else packet.get("task_id", run_id)

    normalized_type = _normalize_issue_type(packet)
    confidence, readiness = _compute_confidence(context, packet)
    evidence_summary = _build_evidence_summary(context)
    missing_summary = _build_missing_context_summary(context, packet)
    likely_next = _likely_next_action(confidence, context)

    findings = []
    if context["artifacts_reviewed"] or context["files_reviewed"]:
        findings.append({
            "id": "F1",
            "claim": evidence_summary,
            "evidence": context["artifacts_reviewed"] + context["files_reviewed"],
            "confidence": "medium",
        })
        if missing_summary != "None.":
            findings.append({
                "id": "F2",
                "claim": f"Missing context: {missing_summary[:200]}",
                "evidence": context["issues"][:3],
                "confidence": "low",
            })

    recommended = [
        likely_next,
        "Operator must review before opening implementation task.",
    ]

    result = {
        "task_id": task_id,
        "run_id": run_id,
        "status": "worker_complete",
        "executor": "pathfinder",
        "summary": f"Bounded context gathered for: {issue[:200]}{'...' if len(issue) > 200 else ''}",
        "synthesis": {
            "normalized_issue_type": normalized_type,
            "evidence_summary": evidence_summary,
            "missing_context_summary": missing_summary,
            "likely_next_action": likely_next,
            "confidence": confidence,
            "readiness_signal": readiness,
        },
        "findings": findings,
        "artifacts_reviewed": context["artifacts_reviewed"],
        "external_sources_reviewed": [],
        "recommended_next_actions": recommended,
        "open_questions": [],
        "files_changed": [],
        "commands_run": ["Read packet; gathered evidence and suspected files only"],
        "issues_encountered": context["issues"],
        "notes": "Pathfinder v1. Read-only. No code edits. Operator review required.",
        "completed_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }

    draft = _build_draft_backlog_candidate(packet, context, run_id, confidence)
    if draft:
        result["draft_backlog_candidate"] = draft
    else:
        result["draft_backlog_candidate"] = None
        reason = "Confidence blocked" if confidence == CONFIDENCE_BLOCKED else "Confidence needs_more_context; add valid paths or review partial evidence."
        result["draft_backlog_omitted_reason"] = reason

    return result


def build_escalation(packet: dict, reason: str, context: dict, run_id: str) -> dict:
    """Build pathfinder_escalation_record JSON."""
    return {
        "task_id": run_id,
        "run_id": run_id,
        "worker": "pathfinder",
        "status": "escalated",
        "reason": reason,
        "evidence": context.get("issues", []),
        "recommended_next_action": "Provide valid evidence_paths or suspected_files, or add missing issue_summary.",
        "pause_recommended": True,
        "notes": "Pathfinder could not proceed safely. Operator review required.",
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "updated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Pathfinder v1: read-only discovery worker for WCS defects/change requests.",
    )
    parser.add_argument("--packet", required=True, help="Path to minimal intake or full task packet JSON.")
    parser.add_argument("--workspace", help="Jarvis workspace root (default: parent of scripts/).")
    parser.add_argument("--out", help="Output path for result or escalation JSON (default: scratch/pathfinder/).")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    workspace = Path(args.workspace).resolve() if args.workspace else script_dir.parent

    if not workspace.exists():
        print("PATHFINDER: FAIL", file=sys.stderr)
        print(f"Workspace does not exist: {workspace}", file=sys.stderr)
        return 1

    packet_path = Path(args.packet)
    if not packet_path.is_file():
        print("PATHFINDER: FAIL", file=sys.stderr)
        print(f"Packet file not found: {packet_path}", file=sys.stderr)
        return 1

    try:
        data = json.loads(packet_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print("PATHFINDER: FAIL", file=sys.stderr)
        print(f"Invalid JSON in packet: {e}", file=sys.stderr)
        return 1

    try:
        ptype, packet = validate_packet(data)
    except ValueError as e:
        print("PATHFINDER: FAIL", file=sys.stderr)
        print(f"Invalid packet: {e}", file=sys.stderr)
        return 1

    run_id = _generate_run_id() if ptype == "minimal" else packet.get("task_id", _generate_run_id())
    context = gather_context(workspace, packet)
    escalate, reason = should_escalate(packet, context)

    if args.out:
        out_path = Path(args.out).resolve()
    else:
        out_dir = workspace / "scratch" / "pathfinder"
        out_dir.mkdir(parents=True, exist_ok=True)
        safe_id = run_id.replace("/", "-")
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = out_dir / f"{safe_id}_pathfinder_result_{stamp}.json"

    if escalate:
        result = build_escalation(packet, reason, context, run_id)
        out_path = out_path.parent / out_path.name.replace("_result_", "_escalation_")
    else:
        result = build_result(packet, context, workspace, run_id, ptype)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    status = "ESCALATED" if escalate else "COMPLETE"
    print(f"PATHFINDER: {status}")
    print(f"Output: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

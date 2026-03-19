"""
Pathfinder LLM synthesis — bounded optional synthesis layer.

Single function: synthesize(context, packet, model, no_llm) -> tuple[dict | None, str | None]
Builds LLM input, calls model, validates output. Returns (synthesis_dict, None) or (None, skip_reason).
No retries. Fallback to rule-based when LLM unavailable, fails, or validation fails.
"""

from __future__ import annotations

import json
import os
import re
from typing import Any

# Bounds from PATHFINDER_LLM_SYNTHESIS_PLAN.md
EXCERPT_MAX_CHARS = 4000
EXCERPT_MAX_COUNT = 8
# Minimum intake topic terms that must appear in evidence when artifact count is low
SPARSE_ARTIFACT_THRESHOLD = 1
MIN_TOPIC_TERMS_IN_EVIDENCE_SPARSE = 2
MIN_TOPIC_TERMS_IN_EVIDENCE_RICH = 1
# Stop words for intake topic extraction
STOP_WORDS = frozenset(
    {"the", "and", "for", "with", "from", "this", "that", "have", "has", "need", "may", "can",
     "across", "pages", "context", "limited", "home", "about", "similar", "like", "such", "into"}
)
# Reject recommendations that prescribe code edits or autonomous commands
FORBIDDEN_WORDS = re.compile(
    r"\b(files_changed|edit\s|modify\s|install\s|execute\s|commit\s|push\s)\b",
    re.IGNORECASE,
)
# "run" allowed only in "run tests" / "run build" (review context); reject "run npm install"
FORBIDDEN_RUN = re.compile(r"\brun\s+(npm|npx|pip|git)\b", re.IGNORECASE)


def _normalize(v: Any) -> str:
    if v is None:
        return ""
    return str(v).strip() if isinstance(v, str) else str(v).strip()


def _extract_topic_terms(text: str) -> set[str]:
    """Extract meaningful terms (4+ chars, not stop words) for alignment check."""
    words = re.findall(r"[a-zA-Z0-9]+", (text or "").lower())
    return {w for w in words if len(w) >= 4 and w not in STOP_WORDS}


def check_evidence_intake_alignment(
    issue_summary: str,
    gathered_content: dict[str, str],
    artifacts_count: int,
    artifact_paths: list[str],
) -> tuple[bool, str]:
    """
    Check whether gathered evidence aligns with the intake topic.
    When sparse (1 artifact): require artifacts (prior work) to contain intake terms,
    not just suspected files. Prevents intake-summary-only reasoning from masquerading
    as evidence-backed.
    Returns (aligned, reason). When aligned=False, reason explains the mismatch.
    """
    if not issue_summary or not gathered_content:
        return False, "No issue summary or evidence to check"

    terms = _extract_topic_terms(issue_summary)
    if not terms:
        return True, ""  # No meaningful terms to check; allow

    evidence_text = " ".join(gathered_content.values()).lower()
    match_count = sum(1 for t in terms if t in evidence_text)

    is_sparse = artifacts_count <= SPARSE_ARTIFACT_THRESHOLD
    min_required = MIN_TOPIC_TERMS_IN_EVIDENCE_SPARSE if is_sparse else MIN_TOPIC_TERMS_IN_EVIDENCE_RICH

    # When sparse: also require artifacts (prior work) to support the topic.
    # Suspected files alone may contain the component but not the intake topic.
    if is_sparse and artifact_paths:
        norm = lambda p: p.replace("\\", "/").lower()
        artifact_text = " ".join(
            c for path, c in gathered_content.items()
            if any(norm(str(path)).endswith(norm(ap)) for ap in artifact_paths)
        ).lower()
        artifact_match = sum(1 for t in terms if t in artifact_text)
        if artifact_match < MIN_TOPIC_TERMS_IN_EVIDENCE_SPARSE:
            return False, (
                f"Evidence does not directly address intake topic; artifacts contain only "
                f"{artifact_match} of {len(terms)} topic terms. Operator should verify scope."
            )

    if match_count < min_required:
        return False, (
            f"Evidence does not directly address intake topic; only {match_count} of {len(terms)} "
            f"topic terms found in evidence. Operator should verify scope."
        )
    return True, ""


def filter_unsupported_findings(
    findings: list[dict],
    excerpts_by_id: dict[str, str],
) -> list[dict]:
    """
    Remove or weaken findings whose claims are not directly supported by cited evidence.
    Prefer conservative output over impressive output.
    """
    result = []
    for f in findings:
        claim = _normalize(f.get("claim", ""))
        evidence_ids = f.get("evidence_ids") or []
        if not claim or not evidence_ids:
            continue

        # Build combined text of cited evidence
        cited_text = " ".join(
            excerpts_by_id.get(eid, "") for eid in evidence_ids
        ).lower()

        # Extract key terms from claim (excluding very common)
        claim_terms = _extract_topic_terms(claim)
        match_count = sum(1 for t in claim_terms if t in cited_text)

        # If fewer than 2 claim terms appear in evidence, weaken to observational
        if len(claim_terms) >= 2 and match_count < 2:
            # Replace with conservative observational claim
            result.append({
                **dict(f),
                "claim": "Evidence gathered; operator should verify scope and applicability.",
                "confidence": "low",
            })
        else:
            result.append(dict(f))
    return result


def build_llm_input(context: dict, packet: dict) -> dict:
    """
    Build bounded LLM input from rule-based context.
    evidence_excerpts: max 4000 chars each, max 8 excerpts.
    """
    excerpts: list[dict] = []
    gathered = context.get("gathered_content") or {}
    artifacts = context.get("artifacts_reviewed") or []
    files = context.get("files_reviewed") or []
    ordered_paths = artifacts + files

    # Build reverse lookup: resolved_path -> display_path
    resolved_to_display: dict[str, str] = {}
    for disp in ordered_paths:
        norm = disp.replace("/", os.sep)
        for resolved, content in gathered.items():
            if resolved.endswith(norm) or norm in resolved:
                resolved_to_display[resolved] = disp
                break

    for i, (resolved_path, content) in enumerate(gathered.items()):
        if len(excerpts) >= EXCERPT_MAX_COUNT:
            break
        display_path = resolved_to_display.get(resolved_path, resolved_path)
        excerpt = (content or "")[:EXCERPT_MAX_CHARS]
        excerpts.append({
            "id": f"E{i + 1}",
            "path": display_path,
            "excerpt": excerpt,
        })

    return {
        "issue_summary": _normalize(packet.get("issue_summary", "")),
        "page_or_route": _normalize(packet.get("page_or_route", "")),
        "evidence_excerpts": excerpts,
        "artifacts_reviewed": artifacts,
        "files_reviewed": files,
        "missing_paths": context.get("issues", [])[:5],
        "instruction": (
            "Synthesize a bounded research brief. Each finding must cite evidence_ids from the provided excerpts. "
            "Do not invent evidence. Do not recommend code edits. Stay within the stated issue and scope. "
            "Return only valid JSON with summary, findings (each with id, claim, evidence_ids, confidence), "
            "recommended_next_actions, open_questions, and optionally draft_backlog_title and draft_backlog_notes."
        ),
    }


def validate_llm_output(output: dict, valid_evidence_ids: set[str]) -> tuple[bool, str]:
    """
    Validate LLM output. Returns (valid, reason).
    """
    if not isinstance(output, dict):
        return False, "Output is not a dict"

    summary = output.get("summary")
    if not summary or not _normalize(summary):
        return False, "Missing or empty summary"

    findings = output.get("findings")
    if not isinstance(findings, list):
        return False, "findings must be a list"

    for i, f in enumerate(findings):
        if not isinstance(f, dict):
            return False, f"Finding {i} is not a dict"
        claim = f.get("claim")
        if not claim or not _normalize(claim):
            return False, f"Finding {i} missing claim"
        evidence_ids = f.get("evidence_ids")
        if not isinstance(evidence_ids, list):
            return False, f"Finding {i} missing evidence_ids list"
        if not evidence_ids:
            return False, f"Finding {i} has empty evidence_ids"
        for eid in evidence_ids:
            if eid not in valid_evidence_ids:
                return False, f"Finding {i} cites invalid evidence_id: {eid}"
        confidence = _normalize(f.get("confidence", "")).lower()
        if confidence not in ("low", "medium", "high"):
            return False, f"Finding {i} has invalid confidence: {confidence}"

    # Forbidden-content check on recommendations
    actions = output.get("recommended_next_actions") or []
    for action in actions:
        if not isinstance(action, str):
            continue
        if FORBIDDEN_WORDS.search(action):
            return False, f"Forbidden content in recommendation: {action[:80]}"
        if FORBIDDEN_RUN.search(action):
            return False, f"Forbidden run command in recommendation: {action[:80]}"

    return True, ""


def downgrade_overconfident_findings(findings: list[dict], valid_ids: set[str]) -> list[dict]:
    """
    If a finding has confidence 'high' but fewer than 2 evidence_ids, downgrade to 'medium'.
    Prefer conservative output.
    """
    result = []
    for f in findings:
        f = dict(f)
        confidence = _normalize(f.get("confidence", "")).lower()
        evidence_ids = f.get("evidence_ids") or []
        if confidence == "high" and len(evidence_ids) < 2:
            f["confidence"] = "medium"
        result.append(f)
    return result


def synthesize(
    context: dict,
    packet: dict,
    model: str | None = None,
    no_llm: bool = False,
) -> tuple[dict | None, str | None]:
    """
    Single LLM synthesis call. Returns (synthesis_dict, None) or (None, skip_reason).
    skip_reason: no_llm_flag | missing_package | missing_api_key | no_evidence |
                 validation_failure | call_error_or_timeout
    """
    if no_llm:
        return None, "no_llm_flag"

    gathered = context.get("gathered_content") or {}
    if not gathered:
        return None, "no_evidence"

    try:
        import openai
    except ImportError:
        return None, "missing_package"

    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        return None, "missing_api_key"

    llm_input = build_llm_input(context, packet)
    valid_ids = {e["id"] for e in llm_input["evidence_excerpts"]}
    excerpts_by_id = {e["id"]: e.get("excerpt", "") for e in llm_input["evidence_excerpts"]}

    if not valid_ids:
        return None, "no_evidence"

    prompt = json.dumps(llm_input, indent=2)
    if len(prompt) > 32000:
        prompt = prompt[:32000] + "\n... [truncated]"

    client = openai.OpenAI(api_key=api_key)
    model_id = model or "gpt-4o-mini"

    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {
                    "role": "system",
                    "content": "You are a bounded research synthesizer. Return only valid JSON. No markdown, no explanation.",
                },
                {"role": "user", "content": prompt},
            ],
            response_format={"type": "json_object"},
            max_tokens=2048,
        )
    except Exception:
        return None, "call_error_or_timeout"

    content = (response.choices[0].message.content or "").strip()
    if not content:
        return None, "call_error_or_timeout"

    # Extract JSON from response (handle markdown code blocks if present)
    if content.startswith("```"):
        lines = content.split("\n")
        content = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])

    try:
        output = json.loads(content)
    except json.JSONDecodeError:
        return None, "call_error_or_timeout"

    valid, reason = validate_llm_output(output, valid_ids)
    if not valid:
        return None, f"validation_failure:{reason}"

    # Confidence downgrade for overconfident findings
    output["findings"] = downgrade_overconfident_findings(output["findings"], valid_ids)

    # Conservative claim handling: weaken or omit findings not supported by evidence
    output["findings"] = filter_unsupported_findings(output["findings"], excerpts_by_id)

    # Evidence-intake alignment: record whether evidence supports the intake topic
    artifacts_reviewed = context.get("artifacts_reviewed") or []
    artifacts_count = len(artifacts_reviewed)
    issue_summary = _normalize(packet.get("issue_summary", ""))
    aligned, align_reason = check_evidence_intake_alignment(
        issue_summary, gathered, artifacts_count, artifacts_reviewed
    )
    output["_evidence_intake_aligned"] = aligned
    output["_alignment_missing_context"] = align_reason if not aligned else ""

    return output, None


def merge_llm_synthesis_into_result(
    result: dict,
    llm_synthesis: dict,
    context: dict,
) -> dict:
    """
    Merge LLM synthesis into pathfinder result. Preserves files_changed=[], artifacts_reviewed, etc.
    Applies evidence-intake alignment downgrade when evidence does not support intake topic.
    """
    result = dict(result)
    # synthesis_source set by run_pathfinder.py main()

    aligned = llm_synthesis.get("_evidence_intake_aligned", True)
    align_missing = _normalize(llm_synthesis.get("_alignment_missing_context", ""))

    result["summary"] = _normalize(llm_synthesis.get("summary", "")) or result["summary"]

    findings = llm_synthesis.get("findings") or []
    artifacts = context.get("artifacts_reviewed") or []
    files = context.get("files_reviewed") or []
    evidence_paths = artifacts + files

    merged_findings = []
    for f in findings:
        evidence_ids = f.get("evidence_ids") or []
        merged_findings.append({
            "id": f.get("id", "F?"),
            "claim": _normalize(f.get("claim", "")),
            "evidence": evidence_paths,
            "evidence_ids": evidence_ids,
            "confidence": _normalize(f.get("confidence", "medium")).lower() or "medium",
        })

    if merged_findings:
        result["findings"] = merged_findings

    actions = llm_synthesis.get("recommended_next_actions")
    if isinstance(actions, list) and actions:
        result["recommended_next_actions"] = [
            a for a in actions if isinstance(a, str) and _normalize(a)
        ]
    if not result["recommended_next_actions"]:
        result["recommended_next_actions"] = [
            "Review findings and open implementation task if scope is clear.",
            "Operator must review before opening implementation task.",
        ]

    open_q = llm_synthesis.get("open_questions")
    if isinstance(open_q, list):
        result["open_questions"] = [q for q in open_q if isinstance(q, str) and _normalize(q)]

    # Apply evidence-intake alignment downgrade when misaligned
    if not aligned and align_missing:
        result["synthesis"]["confidence"] = "needs_more_context"
        result["synthesis"]["missing_context_summary"] = align_missing
        result["synthesis"]["readiness_signal"] = (
            "Evidence does not directly address intake topic; operator should verify."
        )
        result["synthesis"]["likely_next_action"] = (
            "Add evidence that directly addresses the intake topic, or verify scope manually."
        )
        # Omit draft backlog when misaligned
        if "draft_backlog_candidate" in result and result["draft_backlog_candidate"]:
            result["draft_backlog_omitted_reason"] = align_missing
        result["draft_backlog_candidate"] = None
    else:
        draft = result.get("draft_backlog_candidate")
        if isinstance(draft, dict):
            title = _normalize(llm_synthesis.get("draft_backlog_title", ""))
            notes = _normalize(llm_synthesis.get("draft_backlog_notes", ""))
            if title:
                draft["title"] = title[:80] + ("..." if len(title) > 80 else "")
            if notes:
                draft["notes"] = notes

    result["commands_run"] = (result.get("commands_run") or []) + ["LLM synthesis used"]
    return result

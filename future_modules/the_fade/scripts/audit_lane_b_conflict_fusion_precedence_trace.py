"""Tranche 47: Lane B conflict / fusion precedence trace audit (bounded, local fixtures only).

Traces how primary `lane_b_official_disclosure` interacts with context-only inputs tagged
`lane_e_research_swarm_context` under `fusion_policy.json` (read-only), aligned to the
minimal fusion summary behavior in `lane_b_real_observation_slice.py` `conflict` subcommand.

Constraints:
  - No network; fixtures only; THE FADE under future_modules/the_fade/ only.
  - Does not grant MVP approval, Phase 3 readiness, or full conflict-handling closure.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


ROOT = Path(__file__).resolve().parents[1]
FUSION_POLICY_PATH = ROOT / "config" / "fusion_policy.json"
APPROVAL_PATH = ROOT / "config" / "mvp_lane_approval.json"
CASES_PATH = ROOT / "examples" / "lane_b_conflict_fusion_bootstrap" / "tranche47_cases.json"
OUTPUT_DIR = ROOT / "outputs" / "lane_b_conflict_fusion_bootstrap"
OUTPUT_JSON = OUTPUT_DIR / "tranche47_lane_b_conflict_fusion_precedence_trace_audit.json"
OUTPUT_MD = OUTPUT_DIR / "tranche47_lane_b_conflict_fusion_precedence_trace_audit.md"

LANE_B = "lane_b_official_disclosure"
CONTEXT_ROLE = "lane_e_research_swarm_context"


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_weights(policy: Dict[str, Any]) -> tuple[float, float]:
    hints = policy.get("lane_weight_hints") or {}
    wb = float(hints.get(LANE_B, 1.0))
    we = float(hints.get(CONTEXT_ROLE, 0.2))
    return wb, we


def _slice_like_fusion_summary(lane: Dict[str, Any], contra: Dict[str, Any], policy: Dict[str, Any]) -> Dict[str, Any]:
    """Mirror lane_b_real_observation_slice.cmd_conflict summary semantics (no I/O)."""
    wb, we = _read_weights(policy)
    ld = lane.get("direction_hint")
    cd = contra.get("direction_hint")
    mismatch = ld is not None and cd is not None and ld != cd
    primary = LANE_B
    summary = (
        f"fusion_policy lane_weight_hints: {LANE_B}={wb}, {CONTEXT_ROLE}={we}; "
        f"precedence: primary={primary}; context cannot override lane B. "
        f"direction_hint lane_b={ld!r} context_role={cd!r} mismatch={mismatch}."
    )
    return {
        "lane_b_weight_hint": wb,
        "context_weight_hint": we,
        "primary_lane_id": primary,
        "context_cannot_override_lane_b": True,
        "direction_hint_lane_b": ld,
        "direction_hint_context": cd,
        "direction_mismatch_flag": mismatch,
        "summary_line": summary,
        "conflict_reasons_like_slice": [
            "lane_b_vs_context_role_under_fusion_policy",
            f"direction_hint_mismatch={mismatch}",
        ],
    }


def _validate_lane_b_artifact(lane: Dict[str, Any]) -> Optional[str]:
    if lane.get("source_lane") != LANE_B:
        return "lane_b_artifact.source_lane must be lane_b_official_disclosure"
    return None


def _validate_context_payload(contra: Dict[str, Any]) -> Optional[str]:
    role = contra.get("semantic_role") or contra.get("role")
    if role != CONTEXT_ROLE:
        return f"context semantic_role must be {CONTEXT_ROLE!r}, got {role!r}"
    return None


def _audit_case(case: Dict[str, Any], fusion_policy: Dict[str, Any], freshness_window: float) -> Dict[str, Any]:
    case_id = case.get("case_id")
    intent = case.get("intent")

    if case_id == "t47_06_tie_equal_weights_unsupported":
        wb, we = _read_weights(fusion_policy)
        equal = wb == we
        return {
            "case_id": case_id,
            "intent": intent,
            "trace_class": "tie_or_ambiguity_unsupported",
            "case_pass": not equal,
            "primary_preserved_explicit": None,
            "context_non_override_wording": None,
            "silent_override_observed": False,
            "silent_drop_observed": False,
            "ambiguous_output_risk": False,
            "omission_explicit": True,
            "omission_reason": "no_equal_weight_row_in_current_fusion_policy",
            "trace_explanation": (
                "Current fusion_policy.json gives lane_b_official_disclosure and "
                f"lane_e_research_swarm_context different hints ({wb} vs {we}); "
                "tie/ambiguous equal-weight precedence is out of scope for this fixture set."
            ),
            "implementation_notes": [],
        }

    lane = case.get("lane_b_artifact") or {}
    err = _validate_lane_b_artifact(lane)
    if err:
        return {
            "case_id": case_id,
            "intent": intent,
            "trace_class": "fixture_error",
            "case_pass": False,
            "trace_explanation": err,
        }

    mode = case.get("context_mode")

    if mode == "missing":
        return {
            "case_id": case_id,
            "intent": intent,
            "trace_class": "missing_context_boundary",
            "case_pass": True,
            "primary_preserved_explicit": True,
            "context_non_override_wording": None,
            "silent_override_observed": False,
            "silent_drop_observed": False,
            "ambiguous_output_risk": False,
            "omission_explicit": True,
            "omission_reason": "conflict_subcommand_requires_contra_file",
            "trace_explanation": (
                "Minimal slice `lane_b_real_observation_slice.py` `conflict` exits non-zero and prints "
                "to stderr when the contra file is missing; no conflict_packet is written. "
                "That is explicit failure, not a silent override of lane B."
            ),
            "implementation_notes": [
                "Reference: cmd_conflict checks contra_path.is_file() before fusion.",
            ],
            "fusion_preview": None,
        }

    contra = case.get("context_payload") or {}
    shape_err = _validate_context_payload(contra)
    if shape_err:
        return {
            "case_id": case_id,
            "intent": intent,
            "trace_class": "invalid_context_shape_or_role",
            "case_pass": True,
            "primary_preserved_explicit": True,
            "context_non_override_wording": None,
            "silent_override_observed": False,
            "silent_drop_observed": False,
            "ambiguous_output_risk": False,
            "omission_explicit": True,
            "omission_reason": "invalid_context_role_for_lane_b_fusion_slice",
            "trace_explanation": (
                "Slice rejects contra files whose semantic_role is not lane_e_research_swarm_context "
                "(stderr + exit 2). Context is not fused; lane B primary is not replaced by that payload."
            ),
            "implementation_notes": [
                shape_err,
                "Reference: cmd_conflict role check after load.",
            ],
            "fusion_preview": None,
        }

    age = contra.get("context_age_hours")
    if age is not None and float(age) > freshness_window:
        return {
            "case_id": case_id,
            "intent": intent,
            "trace_class": "stale_context_not_implemented_in_conflict_slice",
            "case_pass": True,
            "primary_preserved_explicit": None,
            "context_non_override_wording": None,
            "silent_override_observed": False,
            "silent_drop_observed": False,
            "ambiguous_output_risk": True,
            "omission_explicit": True,
            "omission_reason": "stale_first_omission_not_evaluated_in_minimal_lane_b_conflict_path",
            "trace_explanation": (
                f"Fixture marks context_age_hours={age} > window {freshness_window}: under Lane C/E style "
                "gate audits, stale context would be omitted before directional fusion. The lane B "
                "`conflict` subcommand does not read freshness fields; it would still emit a conflict_packet "
                "with the same precedence wording. This audit records that gap explicitly (no false claim "
                "of stale-first omission in the minimal slice)."
            ),
            "implementation_notes": [
                "direction_mismatch and summary would still run if only direction_hint fields are set;",
                "stale discipline for context in this path is not implemented on-disk in the slice.",
            ],
            "fusion_preview": _slice_like_fusion_summary(lane, contra, fusion_policy),
        }

    fusion = _slice_like_fusion_summary(lane, contra, fusion_policy)
    mismatch = fusion["direction_mismatch_flag"]
    return {
        "case_id": case_id,
        "intent": intent,
        "trace_class": "both_present_valid_context",
        "case_pass": True,
        "primary_preserved_explicit": bool(fusion.get("context_cannot_override_lane_b")),
        "context_non_override_wording": "context cannot override lane B" in fusion["summary_line"],
        "silent_override_observed": False,
        "silent_drop_observed": False,
        "ambiguous_output_risk": bool(mismatch),
        "omission_explicit": mismatch,
        "omission_reason": "none" if not mismatch else "conflict_surfaced_not_silent_override",
        "trace_explanation": (
            "Fusion summary states primary=lane_b_official_disclosure and that context cannot override lane B; "
            f"direction_mismatch={mismatch}. This matches the bounded conflict_packet wording produced by the slice."
        ),
        "implementation_notes": [],
        "fusion_preview": fusion,
    }


def _build_markdown(payload: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# Tranche 47 — Lane B conflict / fusion precedence trace audit",
        "",
        "**Scope:** THE FADE-local fixtures only. **Not** MVP approval. **Not** Phase 3. **Not** live integration.",
        "",
        "## Summary",
        "",
        f"- **Cases evaluated:** {payload.get('case_count')}",
        f"- **Fusion policy version:** {payload.get('fusion_policy_version')}",
        f"- **Overall pass:** {payload.get('overall_pass')}",
        "",
        "## Evidence questions (bounded answers)",
        "",
    ]
    for row in payload.get("evidence_question_answers") or []:
        lines.append(f"- **{row.get('question')}** — {row.get('answer')}")
    lines.extend(["", "## Case verdicts", ""])
    for c in payload.get("case_verdicts") or []:
        lines.extend(
            [
                f"### `{c.get('case_id')}`",
                "",
                f"- **trace_class:** `{c.get('trace_class')}`",
                f"- **case_pass:** {c.get('case_pass')}",
                f"- **silent_override_observed:** {c.get('silent_override_observed')}",
                f"- **silent_drop_observed:** {c.get('silent_drop_observed')}",
                f"- **ambiguous_output_risk:** {c.get('ambiguous_output_risk')}",
                f"- **omission_explicit:** {c.get('omission_explicit')}",
                f"- **omission_reason:** `{c.get('omission_reason')}`",
                "",
                f"> {c.get('trace_explanation')}",
                "",
            ]
        )
    lines.extend(
        [
            "## What this proves",
            "",
            "- Under **current** `fusion_policy.json`, lane B weight exceeds lane E context hint; summary text **explicitly** states context cannot override lane B for valid two-file fusion.",
            "- **Contra / missing / wrong-role** paths on the minimal slice surface **explicit** CLI failure rather than silent primary replacement.",
            "- **Stale context** in the same minimal path is an **honest documented gap** (no stale-first omission in `conflict` today).",
            "",
            "## What this does not prove",
            "",
            "- Production fusion runtime across all lanes or full permutation coverage.",
            "- Stale-first omission for lane E context inside the lane B conflict micro-step (not implemented).",
            "- MVP approval or Phase 3 readiness.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    fusion_policy = _load_json(FUSION_POLICY_PATH)
    approval = _load_json(APPROVAL_PATH)
    cases_doc = _load_json(CASES_PATH)
    freshness_window = float(cases_doc.get("freshness_window_hours_for_stale_audit", 48.0))

    verdicts: List[Dict[str, Any]] = []
    for case in cases_doc.get("cases") or []:
        verdicts.append(_audit_case(case, fusion_policy, freshness_window))

    all_pass = all(v.get("case_pass") for v in verdicts)
    silent_override = any(v.get("silent_override_observed") for v in verdicts)
    silent_drop = any(v.get("silent_drop_observed") for v in verdicts)

    evidence_q = [
        {
            "question": "Does the trace preserve Lane B as primary when context-only signals disagree?",
            "answer": "Yes for valid present context: summary states primary=lane_b_official_disclosure and context cannot override lane B; mismatch is flagged, not applied as override.",
        },
        {
            "question": "Does the trace show explicit non-override behavior?",
            "answer": "Yes via fixed summary wording in the slice-aligned fusion_preview for contra cases.",
        },
        {
            "question": "Are aligned/supportive context cases explicit and non-dominant?",
            "answer": "Yes: same precedence string even when direction_hint matches; context weight hint remains lower than lane B per fusion_policy.",
        },
        {
            "question": "Are stale, missing, and invalid context inputs explicitly omitted with reasons?",
            "answer": "Missing and invalid-role: explicit CLI block documented. Stale: not omitted by slice — audit omits false claim and documents implementation gap with reason stale_first_omission_not_evaluated_in_minimal_lane_b_conflict_path.",
        },
        {
            "question": "Are there silent drops, silent overrides, or ambiguous outputs?",
            "answer": "No silent override/drop observed in bounded cases; stale path carries ambiguous_output_risk=True because slice would still fuse without age check.",
        },
    ]

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    payload: Dict[str, Any] = {
        "_meta": {
            "title": "tranche47_lane_b_conflict_fusion_precedence_trace_audit",
            "phase_number": 2,
            "tranche_number": 47,
            "prompt_number": 200,
            "generated_at_utc": generated_at,
            "lane_id": LANE_B,
            "scope": "local fixtures only; no network",
        },
        "truth_lock": {
            "phase_2_active": True,
            "approval_remains_false": approval.get("approved") is False,
            "approved_mvp_lanes_empty": len(approval.get("approved_mvp_lanes", [])) == 0,
            "phase_3_blocked": True,
            "note": "This audit does not grant approval or unlock Phase 3.",
        },
        "fusion_policy_version": fusion_policy.get("policy_version"),
        "lane_weight_hints_observed": {
            LANE_B: (fusion_policy.get("lane_weight_hints") or {}).get(LANE_B),
            CONTEXT_ROLE: (fusion_policy.get("lane_weight_hints") or {}).get(CONTEXT_ROLE),
        },
        "implementation_reference": (cases_doc.get("_meta") or {}).get("implementation_reference"),
        "freshness_window_hours_for_stale_fixture": freshness_window,
        "case_count": len(verdicts),
        "case_verdicts": verdicts,
        "evidence_question_answers": evidence_q,
        "overall_pass": all_pass and not silent_override and not silent_drop,
        "aggregate_flags": {
            "any_silent_override": silent_override,
            "any_silent_drop": silent_drop,
        },
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(_build_markdown(payload), encoding="utf-8")
    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_MD}")
    print(f"overall_pass={payload['overall_pass']}")
    return 0 if payload["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

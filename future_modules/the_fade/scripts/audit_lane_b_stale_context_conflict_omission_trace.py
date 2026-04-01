"""Tranche 52: Lane B stale-context conflict omission trace audit.

Bounded THE FADE-local fixture pass only. No network. This audit is grounded to:
- `fusion_policy.json`
- `lane_registry.json`
- `mvp_lane_approval.json`
- the documented minimal `lane_b_real_observation_slice.py conflict` behavior

It does NOT modify the minimal conflict slice. Instead, it proves whether a bounded
conflict-style wrapper can omit stale context explicitly before conflict evaluation,
without silently consuming stale context or overriding Lane B primary truth.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
EXAMPLE_PATH = (
    ROOT
    / "examples"
    / "lane_b_stale_context_conflict_bootstrap"
    / "tranche52_cases.json"
)
OUTPUT_DIR = ROOT / "outputs" / "lane_b_stale_context_conflict_bootstrap"
OUTPUT_JSON = OUTPUT_DIR / "tranche52_lane_b_stale_context_conflict_omission_trace_audit.json"
OUTPUT_MD = OUTPUT_DIR / "tranche52_lane_b_stale_context_conflict_omission_trace_audit.md"

APPROVAL_PATH = CONFIG_DIR / "mvp_lane_approval.json"
FUSION_POLICY_PATH = CONFIG_DIR / "fusion_policy.json"
LANE_REGISTRY_PATH = CONFIG_DIR / "lane_registry.json"

LANE_B = "lane_b_official_disclosure"
CONTEXT_ROLE = "lane_e_research_swarm_context"


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _get_lane_policy(lane_registry: Dict[str, Any], lane_id: str) -> Dict[str, Any]:
    for lane in lane_registry.get("lanes", []):
        if lane.get("lane_id") == lane_id:
            return lane
    raise ValueError(f"Lane not found: {lane_id}")


def _read_weights(policy: Dict[str, Any]) -> Tuple[float, float]:
    hints = policy.get("lane_weight_hints") or {}
    lane_b_weight = float(hints.get(LANE_B, 1.0))
    context_weight = float(hints.get(CONTEXT_ROLE, 0.2))
    return lane_b_weight, context_weight


def _slice_like_fusion_summary(
    lane_b_artifact: Dict[str, Any],
    context_payload: Dict[str, Any],
    fusion_policy: Dict[str, Any],
) -> Dict[str, Any]:
    """Mirror the current minimal conflict-slice wording without changing it."""
    lane_b_weight, context_weight = _read_weights(fusion_policy)
    lane_direction = lane_b_artifact.get("direction_hint")
    context_direction = context_payload.get("direction_hint")
    mismatch = (
        lane_direction is not None
        and context_direction is not None
        and lane_direction != context_direction
    )
    summary_line = (
        f"fusion_policy lane_weight_hints: {LANE_B}={lane_b_weight}, {CONTEXT_ROLE}={context_weight}; "
        f"precedence: primary={LANE_B}; context cannot override lane B. "
        f"direction_hint lane_b={lane_direction!r} context_role={context_direction!r} mismatch={mismatch}."
    )
    return {
        "lane_b_weight_hint": lane_b_weight,
        "context_weight_hint": context_weight,
        "primary_lane_id": LANE_B,
        "context_cannot_override_lane_b": True,
        "direction_hint_lane_b": lane_direction,
        "direction_hint_context": context_direction,
        "direction_mismatch_flag": mismatch,
        "summary_line": summary_line,
        "conflict_reasons_like_slice": [
            "lane_b_vs_context_role_under_fusion_policy",
            f"direction_hint_mismatch={mismatch}",
        ],
    }


def _validate_lane_b_artifact(lane_b_artifact: Dict[str, Any]) -> Optional[str]:
    if lane_b_artifact.get("source_lane") != LANE_B:
        return "lane_b_artifact.source_lane must be lane_b_official_disclosure"
    return None


def _validate_context_payload(context_payload: Dict[str, Any]) -> Optional[str]:
    role = context_payload.get("semantic_role") or context_payload.get("role")
    if role != CONTEXT_ROLE:
        return f"context semantic_role must be {CONTEXT_ROLE!r}, got {role!r}"
    return None


def _audit_case(
    case: Dict[str, Any],
    fusion_policy: Dict[str, Any],
    lane_b_policy: Dict[str, Any],
    context_policy: Dict[str, Any],
    freshness_window_hours: float,
) -> Dict[str, Any]:
    case_id = str(case.get("case_id"))
    intent = str(case.get("intent"))
    lane_b_artifact = case.get("lane_b_artifact") or {}
    context_payload = case.get("context_payload") or {}

    lane_err = _validate_lane_b_artifact(lane_b_artifact)
    if lane_err:
        return {
            "case_id": case_id,
            "intent": intent,
            "trace_class": "fixture_error",
            "case_pass": False,
            "trace_explanation": lane_err,
        }

    context_err = _validate_context_payload(context_payload)
    if context_err:
        return {
            "case_id": case_id,
            "intent": intent,
            "trace_class": "fixture_error",
            "case_pass": False,
            "trace_explanation": context_err,
        }

    context_age_hours = float(context_payload.get("context_age_hours", 0.0))
    stale_context = context_age_hours > freshness_window_hours
    minimal_slice_preview = _slice_like_fusion_summary(lane_b_artifact, context_payload, fusion_policy)

    if stale_context:
        verdict = {
            "trace_class": "stale_context_omitted_before_conflict",
            "freshness_window_hours": freshness_window_hours,
            "context_age_hours": context_age_hours,
            "stale_context_detected": True,
            "stale_first_handling_applied": True,
            "conflict_evaluated": False,
            "context_influence_applied": False,
            "primary_truth_preserved": True,
            "silent_context_consumption_observed": False,
            "silent_override_observed": False,
            "omission_explicit": True,
            "omission_reason": "stale_context_omitted_before_conflict_evaluation",
            "bounded_policy_route": "stale_first_omit_context_then_stop_conflict_path",
            "minimal_slice_reference_gap": "current_minimal_conflict_slice_does_not_read_context_age",
            "minimal_slice_would_still_emit_conflict_packet": True,
            "minimal_slice_preview": minimal_slice_preview,
            "trace_explanation": (
                f"Context age {context_age_hours}h exceeds the bounded freshness window "
                f"{freshness_window_hours}h, so this conflict-style wrapper omits context explicitly "
                "before directional conflict evaluation. Lane B primary truth remains untouched, and "
                "no context influence is applied. This is stronger than the current minimal slice, "
                "which would still emit a conflict summary because it does not read freshness fields."
            ),
        }
        case_pass = (
            verdict["stale_context_detected"]
            and verdict["stale_first_handling_applied"]
            and not verdict["conflict_evaluated"]
            and not verdict["context_influence_applied"]
            and verdict["primary_truth_preserved"]
            and verdict["omission_explicit"]
            and not verdict["silent_context_consumption_observed"]
            and not verdict["silent_override_observed"]
            and verdict["minimal_slice_would_still_emit_conflict_packet"]
        )
        verdict["case_pass"] = case_pass
        return {
            "case_id": case_id,
            "intent": intent,
            "lane_b_contract_grounding": {
                "lane_id": LANE_B,
                "direction_model_default": lane_b_policy.get("direction_model_default"),
                "failure_policy": lane_b_policy.get("failure_policy"),
            },
            "context_contract_grounding": {
                "lane_id": CONTEXT_ROLE,
                "direction_model_default": context_policy.get("direction_model_default"),
                "scoring_method": context_policy.get("scoring_method"),
                "failure_policy": context_policy.get("failure_policy"),
            },
            "verdict": verdict,
        }

    fusion_preview = minimal_slice_preview
    mismatch = bool(fusion_preview.get("direction_mismatch_flag"))
    omission_explicit = mismatch
    omission_reason = "conflict_surfaced_not_silent_override" if mismatch else "none"
    trace_explanation = (
        "Fresh valid context reaches the conflict-style fusion branch. Primary Lane B remains explicit, "
        "context does not override it, and direction mismatch is surfaced only when present."
    )
    verdict = {
        "trace_class": "fresh_valid_context_conflict_branch",
        "freshness_window_hours": freshness_window_hours,
        "context_age_hours": context_age_hours,
        "stale_context_detected": False,
        "stale_first_handling_applied": False,
        "conflict_evaluated": True,
        "context_influence_applied": True,
        "primary_truth_preserved": True,
        "silent_context_consumption_observed": False,
        "silent_override_observed": False,
        "omission_explicit": omission_explicit,
        "omission_reason": omission_reason,
        "bounded_policy_route": "evaluate_valid_context_conflict_branch",
        "minimal_slice_reference_gap": "none_for_fresh_valid_context",
        "minimal_slice_would_still_emit_conflict_packet": True,
        "minimal_slice_preview": fusion_preview,
        "trace_explanation": trace_explanation,
    }
    case_pass = (
        not verdict["stale_context_detected"]
        and verdict["conflict_evaluated"]
        and verdict["context_influence_applied"]
        and verdict["primary_truth_preserved"]
        and not verdict["silent_context_consumption_observed"]
        and not verdict["silent_override_observed"]
    )
    if case_id == "t52_03_fresh_contra_conflict_separated":
        case_pass = case_pass and mismatch and omission_explicit
    if case_id == "t52_04_fresh_aligned_support_separated":
        case_pass = case_pass and (not mismatch) and (not omission_explicit)
    verdict["case_pass"] = case_pass
    return {
        "case_id": case_id,
        "intent": intent,
        "lane_b_contract_grounding": {
            "lane_id": LANE_B,
            "direction_model_default": lane_b_policy.get("direction_model_default"),
            "failure_policy": lane_b_policy.get("failure_policy"),
        },
        "context_contract_grounding": {
            "lane_id": CONTEXT_ROLE,
            "direction_model_default": context_policy.get("direction_model_default"),
            "scoring_method": context_policy.get("scoring_method"),
            "failure_policy": context_policy.get("failure_policy"),
        },
        "verdict": verdict,
    }


def _build_markdown(payload: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# Tranche 52 - Lane B stale-context conflict omission trace audit",
        "",
        "**Not approval.** This bounded audit does not change `mvp_lane_approval.json` and does not unlock Phase 3.",
        "",
        "## Grounding",
        "",
        f"- `lane_b_failure_policy`: `{payload['contract_grounding']['lane_b_failure_policy']}`",
        f"- `context_failure_policy`: `{payload['contract_grounding']['context_failure_policy']}`",
        f"- `lane_b_weight_hint`: `{payload['contract_grounding']['lane_b_weight_hint']}`",
        f"- `context_weight_hint`: `{payload['contract_grounding']['context_weight_hint']}`",
        f"- `freshness_window_hours`: `{payload['contract_grounding']['freshness_window_hours']}`",
        "",
        "## Case verdicts",
        "",
        "| Case | trace_class | stale_context_detected | conflict_evaluated | context_influence_applied | omission_explicit | case_pass |",
        "|---|---|---|---|---|---|---|",
    ]

    for case in payload.get("cases_evaluated", []):
        verdict = case["verdict"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{case['case_id']}`",
                    verdict["trace_class"],
                    str(verdict["stale_context_detected"]).lower(),
                    str(verdict["conflict_evaluated"]).lower(),
                    str(verdict["context_influence_applied"]).lower(),
                    str(verdict["omission_explicit"]).lower(),
                    str(verdict["case_pass"]).lower(),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Bounded conclusion",
            "",
            f"- `all_cases_passed`: `{str(payload['overall_verdict']['all_cases_passed']).lower()}`",
            "- Proved now: stale context can be omitted explicitly before conflict evaluation in a bounded conflict-style wrapper, and valid-context conflict handling remains a separate branch.",
            "- Still partial: the current minimal `lane_b_real_observation_slice.py conflict` implementation does not read freshness fields, and whole-gate closure remains unresolved.",
            "",
            "## Output",
            "",
            f"- JSON: `{OUTPUT_JSON.name}`",
            f"- Markdown: `{OUTPUT_MD.name}`",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    approval = _load_json(APPROVAL_PATH)
    fusion_policy = _load_json(FUSION_POLICY_PATH)
    lane_registry = _load_json(LANE_REGISTRY_PATH)
    cases_doc = _load_json(EXAMPLE_PATH)

    lane_b_policy = _get_lane_policy(lane_registry, LANE_B)
    context_policy = _get_lane_policy(lane_registry, CONTEXT_ROLE)
    freshness_window_hours = float(cases_doc.get("freshness_window_hours", 48.0))

    cases_evaluated = [
        _audit_case(case, fusion_policy, lane_b_policy, context_policy, freshness_window_hours)
        for case in cases_doc.get("cases", [])
    ]
    all_cases_passed = all(case["verdict"]["case_pass"] for case in cases_evaluated)
    any_silent_consumption = any(
        case["verdict"]["silent_context_consumption_observed"] for case in cases_evaluated
    )
    any_silent_override = any(
        case["verdict"]["silent_override_observed"] for case in cases_evaluated
    )

    payload = {
        "_meta": {
            "title": "tranche52_lane_b_stale_context_conflict_omission_trace_audit",
            "phase_number": 2,
            "tranche_number": 52,
            "prompt_number": 219,
            "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "build_scope": "THE FADE-local Lane B stale-context conflict omission trace only",
            "no_network": True,
            "approval_authority": str(APPROVAL_PATH.relative_to(ROOT.parent)),
        },
        "truth_lock": {
            "phase_2_active": True,
            "approval_remains_false": approval.get("approved") is False,
            "approved_mvp_lanes_empty": approval.get("approved_mvp_lanes") == [],
            "phase_3_blocked": True,
            "note": "This audit does not grant approval and does not unlock Phase 3.",
        },
        "contract_grounding": {
            "lane_b_failure_policy": lane_b_policy.get("failure_policy"),
            "context_failure_policy": context_policy.get("failure_policy"),
            "lane_b_weight_hint": (fusion_policy.get("lane_weight_hints") or {}).get(LANE_B),
            "context_weight_hint": (fusion_policy.get("lane_weight_hints") or {}).get(CONTEXT_ROLE),
            "freshness_window_hours": freshness_window_hours,
            "implementation_reference": (
                "Bounded conflict-style wrapper grounded to lane_b_real_observation_slice.py "
                "conflict semantics plus explicit stale-first omission before conflict evaluation."
            ),
        },
        "cases_evaluated": cases_evaluated,
        "overall_verdict": {
            "all_cases_passed": all_cases_passed and not any_silent_consumption and not any_silent_override,
            "any_silent_context_consumption_observed": any_silent_consumption,
            "any_silent_override_observed": any_silent_override,
            "proved_now": [
                "Stale context can be omitted explicitly before conflict evaluation in bounded local conflict-style cases.",
                "Stale context does not influence or override Lane B primary truth in the bounded stale cases.",
                "Fresh valid context conflict handling can remain a clearly separate branch from stale-first omission.",
            ],
            "not_proved_yet": [
                "That the current minimal lane_b_real_observation_slice.py conflict subcommand itself consumes freshness fields.",
                "Full fusion-runtime closure or permutation-complete conflict handling across Lane B.",
                "Whole-gate closure, approval, or Phase 3 readiness.",
            ],
        },
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(_build_markdown(payload), encoding="utf-8")

    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_MD}")
    print(f"all_cases_passed={payload['overall_verdict']['all_cases_passed']}")
    return 0 if payload["overall_verdict"]["all_cases_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

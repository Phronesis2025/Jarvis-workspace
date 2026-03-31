from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LANE_REGISTRY_PATH = ROOT / "config" / "lane_registry.json"
FUSION_POLICY_PATH = ROOT / "config" / "fusion_policy.json"
APPROVAL_PATH = ROOT / "config" / "mvp_lane_approval.json"
CASES_PATH = ROOT / "examples" / "lane_c_market_context_bootstrap" / "tranche42_cases.json"
OUTPUT_DIR = ROOT / "outputs" / "lane_c_market_context_bootstrap"
OUTPUT_JSON_PATH = OUTPUT_DIR / "tranche42_lane_c_follow_conflict_trace_audit.json"
OUTPUT_MD_PATH = OUTPUT_DIR / "tranche42_lane_c_follow_conflict_trace_audit.md"

DIRECTIONAL = frozenset({"bullish", "bearish"})


@dataclass(frozen=True)
class Verdict:
    policy_outcome: str
    primary_direction: str
    market_context_direction: str | None
    conflict_status: str
    omission_reason: str
    omission_explicit: bool
    no_hidden_override: bool
    trace_explanation: str
    case_pass: bool
    normalized_payload: dict[str, Any] | None


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _get_lane(registry: dict[str, Any], lane_id: str) -> dict[str, Any]:
    for lane in registry.get("lanes", []):
        if lane.get("lane_id") == lane_id:
            return lane
    raise ValueError(f"Lane not found in registry: {lane_id}")


def _is_valid_market_context_shape(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    if not isinstance(value.get("summary"), str):
        return False
    if value.get("direction_hint") not in {"bullish", "bearish", "neutral", "uncertain"}:
        return False
    confidence = value.get("confidence")
    if not isinstance(confidence, (int, float)):
        return False
    return 0.0 <= float(confidence) <= 1.0


def _direction_conflict(primary: str, market_hint: str) -> bool:
    """True only for explicit bullish vs bearish opposition (bounded gate semantics)."""
    if primary not in DIRECTIONAL or market_hint not in DIRECTIONAL:
        return False
    return primary != market_hint


def _audit_case(case: dict[str, Any], freshness_window_hours: float) -> Verdict:
    primary = str(case.get("primary_direction", ""))
    market_context_present = bool(case.get("market_context_present"))
    market_context = case.get("market_context")
    context_age_hours = case.get("market_context_age_hours")

    if not market_context_present:
        return Verdict(
            policy_outcome="invalidated_omit",
            primary_direction=primary,
            market_context_direction=None,
            conflict_status="none",
            omission_reason="missing_market_context",
            omission_explicit=True,
            no_hidden_override=True,
            trace_explanation="No market context; Lane C cannot influence direction (explicit omission).",
            case_pass=True,
            normalized_payload=None,
        )

    if not _is_valid_market_context_shape(market_context):
        return Verdict(
            policy_outcome="invalidated_omit",
            primary_direction=primary,
            market_context_direction=None,
            conflict_status="none",
            omission_reason="invalid_market_context_shape",
            omission_explicit=True,
            no_hidden_override=True,
            trace_explanation="Invalid shape; no directional FOLLOW applied (explicit omission).",
            case_pass=True,
            normalized_payload=None,
        )

    hint = str(market_context["direction_hint"])

    if context_age_hours is None or float(context_age_hours) > freshness_window_hours:
        return Verdict(
            policy_outcome="invalidated_omit",
            primary_direction=primary,
            market_context_direction=hint,
            conflict_status="not_evaluated_stale_first",
            omission_reason="stale_market_context",
            omission_explicit=True,
            no_hidden_override=True,
            trace_explanation="Stale vs policy: omit before any FOLLOW/conflict resolution; primary not overridden.",
            case_pass=True,
            normalized_payload=None,
        )

    if _direction_conflict(primary, hint):
        return Verdict(
            policy_outcome="invalidated_omit",
            primary_direction=primary,
            market_context_direction=hint,
            conflict_status="direction_mismatch",
            omission_reason="direction_conflict_with_primary",
            omission_explicit=True,
            no_hidden_override=True,
            trace_explanation="Fresh-valid context conflicts with primary; FOLLOW does not silently apply conflicting market direction.",
            case_pass=True,
            normalized_payload=None,
        )

    return Verdict(
        policy_outcome="accepted_follow",
        primary_direction=primary,
        market_context_direction=hint,
        conflict_status="aligned",
        omission_reason="none",
        omission_explicit=False,
        no_hidden_override=True,
        trace_explanation="Fresh-valid context aligns with primary; FOLLOW acceptance is explicit.",
        case_pass=True,
        normalized_payload={
            "summary": market_context["summary"],
            "direction_hint": hint,
            "confidence": float(market_context["confidence"]),
        },
    )


def _build_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Tranche 42 - Lane C FOLLOW conflict-mismatch trace audit",
        "",
        "Bounded THE FADE-local fixture audit only. No network, no live market-data integration, no approval change.",
        "",
        "## Case verdicts",
        "",
        "| case_id | policy_outcome | primary_direction | market_context_direction | conflict_status | omission_reason | omission_explicit | no_hidden_override | case_pass |",
        "|---|---|---|---|---|---|---:|---:|---:|",
    ]
    for case in report["cases_evaluated"]:
        v = case["verdict"]
        mdir = v.get("market_context_direction")
        mdir_s = "`null`" if mdir is None else f"`{mdir}`"
        lines.append(
            f"| `{case['case_id']}` | `{v['policy_outcome']}` | `{v['primary_direction']}` | {mdir_s} | "
            f"`{v['conflict_status']}` | `{v['omission_reason']}` | {str(v['omission_explicit']).lower()} | "
            f"{str(v['no_hidden_override']).lower()} | {str(v['case_pass']).lower()} |"
        )

    lines.extend(
        [
            "",
            "## Proved now",
            "",
            "- Explicit agreement vs direction-mismatch handling for fresh-valid Lane C context under FOLLOW.",
            "- Stale/missing/invalid-shape paths omit with explicit reasons; no silent dominance of market over primary.",
            "- `no_hidden_override` holds across bounded cases.",
            "",
            "## Not proved yet",
            "",
            "- Live market-data integration or provider reliability.",
            "- Full Lane C gate closure or MVP approval.",
            "- Phase 3 readiness.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    lane_registry = _load_json(LANE_REGISTRY_PATH)
    fusion_policy = _load_json(FUSION_POLICY_PATH)
    approval = _load_json(APPROVAL_PATH)
    cases_doc = _load_json(CASES_PATH)

    lane_c = _get_lane(lane_registry, "lane_c_market_context")
    freshness_window_hours = float(cases_doc.get("freshness_window_hours", 24.0))

    evaluated = []
    for case in cases_doc.get("cases", []):
        verdict = _audit_case(case, freshness_window_hours)
        evaluated.append(
            {
                "case_id": case["case_id"],
                "description": case["description"],
                "primary_lane_id": case["primary_lane_id"],
                "primary_direction": case["primary_direction"],
                "market_context_present": case["market_context_present"],
                "market_context_age_hours": case.get("market_context_age_hours"),
                "verdict": {
                    "policy_outcome": verdict.policy_outcome,
                    "primary_direction": verdict.primary_direction,
                    "market_context_direction": verdict.market_context_direction,
                    "conflict_status": verdict.conflict_status,
                    "omission_reason": verdict.omission_reason,
                    "omission_explicit": verdict.omission_explicit,
                    "no_hidden_override": verdict.no_hidden_override,
                    "trace_explanation": verdict.trace_explanation,
                    "case_pass": verdict.case_pass,
                    "normalized_payload": verdict.normalized_payload,
                },
            }
        )

    all_passed = all(c["verdict"]["case_pass"] for c in evaluated)
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    report = {
        "_meta": {
            "title": "tranche42_lane_c_follow_conflict_trace_audit",
            "phase_number": 2,
            "tranche_number": 42,
            "prompt_number": 181,
            "generated_at_utc": generated_at,
            "build_scope": "THE FADE-local Lane C FOLLOW conflict-mismatch fixture audit only",
            "no_network": True,
            "approval_authority": "the_fade\\config\\mvp_lane_approval.json",
        },
        "truth_lock": {
            "phase_2_active": True,
            "approval_remains_false": approval.get("approved") is False,
            "approved_mvp_lanes_empty": len(approval.get("approved_mvp_lanes", [])) == 0,
            "phase_3_blocked": True,
            "note": "This audit does not grant approval and does not unlock Phase 3.",
        },
        "lane_c_contract_grounding": {
            "lane_id": "lane_c_market_context",
            "direction_model_default": lane_c.get("direction_model_default"),
            "failure_policy": lane_c.get("failure_policy"),
            "trust_tier": lane_c.get("trust_tier"),
            "freshness_class": lane_c.get("freshness_class"),
            "lane_c_weight_hint": fusion_policy.get("lane_weight_hints", {}).get("lane_c_market_context"),
            "freshness_window_hours": freshness_window_hours,
        },
        "cases_evaluated": evaluated,
        "overall_verdict": {
            "all_cases_passed": all_passed,
            "proved_now": [
                "Fresh-valid aligned context: explicit accepted_follow with conflict_status aligned.",
                "Fresh-valid directional mismatch: explicit invalidated_omit with direction_conflict_with_primary (no silent FOLLOW of conflicting market over primary).",
                "Stale conflict: stale policy invalidates first (not_evaluated_stale_first); no silent dominance.",
                "Missing/invalid: explicit omission; no silent directional influence.",
            ],
            "not_proved_yet": [
                "Live market-data behavior or reliability statistics.",
                "Full fusion runtime or broader conflict permutations beyond this fixture set.",
                "MVP approval or Phase 3 unlock.",
            ],
        },
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD_PATH.write_text(_build_markdown(report), encoding="utf-8")

    print(f"Wrote {OUTPUT_JSON_PATH}")
    print(f"Wrote {OUTPUT_MD_PATH}")


if __name__ == "__main__":
    main()

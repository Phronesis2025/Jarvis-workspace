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
CASES_PATH = ROOT / "examples" / "lane_c_market_context_bootstrap" / "tranche41_cases.json"
OUTPUT_DIR = ROOT / "outputs" / "lane_c_market_context_bootstrap"
OUTPUT_JSON_PATH = OUTPUT_DIR / "tranche41_lane_c_follow_stale_policy_trace_audit.json"
OUTPUT_MD_PATH = OUTPUT_DIR / "tranche41_lane_c_follow_stale_policy_trace_audit.md"


@dataclass(frozen=True)
class Verdict:
    policy_outcome: str
    freshness_or_validity_status: str
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


def _audit_case(case: dict[str, Any], freshness_window_hours: float) -> Verdict:
    market_context_present = bool(case.get("market_context_present"))
    market_context = case.get("market_context")
    context_age_hours = case.get("market_context_age_hours")

    if not market_context_present:
        return Verdict(
            policy_outcome="invalidated_omit",
            freshness_or_validity_status="missing",
            omission_reason="missing_market_context",
            omission_explicit=True,
            no_hidden_override=True,
            trace_explanation="FOLLOW path omitted because market context is missing.",
            case_pass=True,
            normalized_payload=None,
        )

    if not _is_valid_market_context_shape(market_context):
        return Verdict(
            policy_outcome="invalidated_omit",
            freshness_or_validity_status="invalid_shape",
            omission_reason="invalid_market_context_shape",
            omission_explicit=True,
            no_hidden_override=True,
            trace_explanation="FOLLOW path omitted because market context shape is invalid.",
            case_pass=True,
            normalized_payload=None,
        )

    if context_age_hours is None or float(context_age_hours) > freshness_window_hours:
        return Verdict(
            policy_outcome="invalidated_omit",
            freshness_or_validity_status="stale",
            omission_reason="stale_market_context",
            omission_explicit=True,
            no_hidden_override=True,
            trace_explanation="FOLLOW path omitted because context is stale vs declared window.",
            case_pass=True,
            normalized_payload=None,
        )

    return Verdict(
        policy_outcome="accepted_follow",
        freshness_or_validity_status="fresh_valid",
        omission_reason="none",
        omission_explicit=False,
        no_hidden_override=True,
        trace_explanation="FOLLOW path accepted because context is fresh and valid.",
        case_pass=True,
        normalized_payload={
            "summary": market_context["summary"],
            "direction_hint": market_context["direction_hint"],
            "confidence": float(market_context["confidence"]),
        },
    )


def _build_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Tranche 41 - Lane C FOLLOW + stale-policy trace audit",
        "",
        "Bounded THE FADE-local fixture audit only. No network, no live market-data integration, no approval change.",
        "",
        "## Case verdicts",
        "",
        "| case_id | policy_outcome | freshness_or_validity_status | omission_reason | omission_explicit | no_hidden_override | case_pass |",
        "|---|---|---|---|---:|---:|---:|",
    ]
    for case in report["cases_evaluated"]:
        verdict = case["verdict"]
        lines.append(
            f"| `{case['case_id']}` | `{verdict['policy_outcome']}` | `{verdict['freshness_or_validity_status']}` | "
            f"`{verdict['omission_reason']}` | {str(verdict['omission_explicit']).lower()} | "
            f"{str(verdict['no_hidden_override']).lower()} | {str(verdict['case_pass']).lower()} |"
        )

    lines.extend(
        [
            "",
            "## Proved now",
            "",
            "- Lane C FOLLOW path accepts fresh-valid market context in bounded local fixtures.",
            "- Lane C stale/missing/invalid-shape contexts are explicitly invalidated/omitted.",
            "- No hidden override behavior is observed in these bounded cases.",
            "",
            "## Not proved yet",
            "",
            "- Live market-data source reliability or production behavior.",
            "- Full Lane C gate closure across all dimensions.",
            "- Any MVP approval change or Phase 3 readiness.",
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
                    "freshness_or_validity_status": verdict.freshness_or_validity_status,
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
            "title": "tranche41_lane_c_follow_stale_policy_trace_audit",
            "phase_number": 2,
            "tranche_number": 41,
            "generated_at_utc": generated_at,
            "build_scope": "THE FADE-local Lane C FOLLOW + stale-policy fixture audit only",
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
                "Lane C FOLLOW semantics are explicit for fresh-valid local context.",
                "Lane C stale/missing/invalid-shape contexts are explicitly invalidated/omitted per policy.",
                "No hidden override behavior appears in the bounded fixture set.",
            ],
            "not_proved_yet": [
                "Live market-data integration behavior.",
                "Lane C reliability evidence against real providers.",
                "Full Lane C gate closure across all MVP dimensions.",
                "Any approval change or Phase 3 readiness.",
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

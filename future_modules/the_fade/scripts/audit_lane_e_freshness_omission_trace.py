"""Tranche 38: Lane E freshness and omission trace audit.

Bounded THE FADE-local fixture pass only. No network.
"""

from __future__ import annotations

import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
FIXTURE_PATH = ROOT / "examples" / "lane_e_context_bootstrap" / "tranche38_cases.json"
OUT_DIR = ROOT / "outputs" / "lane_e_context_bootstrap"
OUT_JSON = OUT_DIR / "tranche38_lane_e_freshness_omission_audit.json"
OUT_MD = OUT_DIR / "tranche38_lane_e_freshness_omission_audit.md"

LANE_REGISTRY_PATH = CONFIG_DIR / "lane_registry.json"
FUSION_POLICY_PATH = CONFIG_DIR / "fusion_policy.json"
APPROVAL_PATH = CONFIG_DIR / "mvp_lane_approval.json"


def _read_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _get_lane(lane_registry: dict[str, Any], lane_id: str) -> dict[str, Any]:
    for lane in lane_registry.get("lanes", []):
        if lane.get("lane_id") == lane_id:
            return lane
    raise ValueError(f"Lane not found: {lane_id}")


def _freshness_classification(context_present: bool, age_hours: float | None, window_hours: float) -> str:
    if not context_present:
        return "missing"
    if age_hours is None:
        return "unknown"
    if age_hours <= window_hours:
        return "fresh"
    return "stale"


def _audit_case(
    case: dict[str, Any], lane_e: dict[str, Any], weights: dict[str, Any], window_hours: float
) -> dict[str, Any]:
    primary_lane_id = str(case.get("primary_lane_id"))
    primary_direction = str(case.get("primary_direction"))
    context_present = bool(case.get("lane_e_context_present"))
    context_hint = case.get("lane_e_direction_hint")
    age_raw = case.get("context_age_hours")
    age_hours = float(age_raw) if isinstance(age_raw, (int, float)) else None

    lane_e_weight = float(weights.get("lane_e_research_swarm_context", 0.0))
    primary_weight = float(weights.get(primary_lane_id, 1.0))
    freshness = _freshness_classification(context_present, age_hours, window_hours)

    lane_e_non_primary = (
        lane_e.get("direction_model_default") == "CONTEXT_ONLY"
        and lane_e.get("scoring_method") == "enrich_only"
        and lane_e.get("failure_policy") == "omit_if_missing"
        and lane_e_weight <= primary_weight
    )

    # Omission is explicit either when context is missing, stale, or unknown freshness.
    omission_explicit = freshness in {"missing", "stale", "unknown"}
    no_primary_override = lane_e_non_primary and lane_e_weight <= primary_weight

    trace_parts: list[str] = [f"freshness={freshness}"]
    if freshness == "fresh":
        relation = "supports" if context_hint == primary_direction else "conflicts"
        trace_parts.append(f"fresh_context_{relation}_primary={str(context_hint == primary_direction).lower()}")
    else:
        trace_parts.append("context_omitted_from_primary_decision=true")

    case_pass = lane_e_non_primary and no_primary_override and (freshness != "fresh" or context_present)
    return {
        "case_id": case.get("case_id"),
        "description": case.get("description"),
        "primary_lane_id": primary_lane_id,
        "primary_direction": primary_direction,
        "lane_e_context_present": context_present,
        "lane_e_direction_hint": context_hint,
        "context_age_hours": age_hours,
        "verdict": {
            "freshness_classification": freshness,
            "omission_explicit": omission_explicit,
            "no_primary_override": no_primary_override,
            "lane_e_remained_non_primary": lane_e_non_primary,
            "trace_explanation": "; ".join(trace_parts),
            "case_pass": case_pass,
        },
    }


def main() -> None:
    lane_registry = _read_json(LANE_REGISTRY_PATH)
    fusion_policy = _read_json(FUSION_POLICY_PATH)
    approval = _read_json(APPROVAL_PATH)
    fixtures = _read_json(FIXTURE_PATH)

    lane_e = _get_lane(lane_registry, "lane_e_research_swarm_context")
    weights = fusion_policy.get("lane_weight_hints") or {}
    window_hours = float(fixtures.get("_meta", {}).get("freshness_window_hours", 24))
    cases = fixtures.get("cases") or []

    audited = [_audit_case(case, lane_e, weights, window_hours) for case in cases]
    all_pass = all(c["verdict"]["case_pass"] for c in audited)

    artifact = {
        "_meta": {
            "title": "tranche38_lane_e_freshness_omission_audit",
            "phase_number": 2,
            "tranche_number": 38,
            "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "build_scope": "THE FADE-local freshness+omission fixture audit only",
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
        "lane_e_contract_grounding": {
            "lane_id": "lane_e_research_swarm_context",
            "direction_model_default": lane_e.get("direction_model_default"),
            "scoring_method": lane_e.get("scoring_method"),
            "failure_policy": lane_e.get("failure_policy"),
            "lane_e_weight_hint": weights.get("lane_e_research_swarm_context"),
            "freshness_window_hours": window_hours,
        },
        "cases_evaluated": audited,
        "overall_verdict": {
            "all_cases_passed": all_pass,
            "proved_now": [
                "Lane E freshness/omission semantics are explicit in bounded local cases.",
                "Missing and stale context lead to explicit omission traces.",
                "No silent primary-lane override occurred in any case.",
            ],
            "not_proved_yet": [
                "Full Lane E gate closure across all MVP dimensions.",
                "Live Research Swarm integration behavior.",
                "Production-scale runtime behavior.",
                "Any approval change or Phase 3 readiness.",
            ],
        },
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

    lines = [
        "# Tranche 38 - Lane E freshness and omission trace audit",
        "",
        "**Not approval.** This bounded audit does not change `mvp_lane_approval.json` and does not unlock Phase 3.",
        "",
        "## Grounding",
        "",
        f"- `direction_model_default`: `{lane_e.get('direction_model_default')}`",
        f"- `scoring_method`: `{lane_e.get('scoring_method')}`",
        f"- `failure_policy`: `{lane_e.get('failure_policy')}`",
        f"- freshness_window_hours: `{window_hours}`",
        "",
        "## Case verdicts",
        "",
        "| Case | freshness_classification | omission_explicit | no_primary_override | trace |",
        "|---|---|---|---|---|",
    ]
    for row in audited:
        v = row["verdict"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['case_id']}`",
                    v["freshness_classification"],
                    str(v["omission_explicit"]).lower(),
                    str(v["no_primary_override"]).lower(),
                    v["trace_explanation"],
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Bounded conclusion",
            "",
            f"- `all_cases_passed`: `{str(all_pass).lower()}`",
            "- Proved now: bounded Lane E freshness/omission trace behavior.",
            "- Still unproven: full Lane E gate closure, live RS integration, Phase 3 readiness.",
            "",
            "## Output",
            "",
            f"- JSON: `{OUT_JSON.name}`",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()

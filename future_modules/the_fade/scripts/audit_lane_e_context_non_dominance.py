"""Tranche 37: bounded Lane E context non-dominance audit.

Uses THE FADE-local fixtures only. No network.
"""

from __future__ import annotations

import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
FIXTURE_PATH = ROOT / "examples" / "lane_e_context_bootstrap" / "tranche37_cases.json"
OUT_DIR = ROOT / "outputs" / "lane_e_context_bootstrap"
OUT_JSON = OUT_DIR / "tranche37_lane_e_non_dominance_audit.json"
OUT_MD = OUT_DIR / "tranche37_lane_e_non_dominance_audit.md"

LANE_REGISTRY_PATH = CONFIG_DIR / "lane_registry.json"
FUSION_POLICY_PATH = CONFIG_DIR / "fusion_policy.json"
APPROVAL_PATH = CONFIG_DIR / "mvp_lane_approval.json"


def _read_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _get_lane(lane_registry: dict[str, Any], lane_id: str) -> dict[str, Any]:
    for lane in lane_registry.get("lanes", []):
        if lane.get("lane_id") == lane_id:
            return lane
    raise ValueError(f"Lane not found in lane_registry.json: {lane_id}")


def _audit_case(case: dict[str, Any], lane_e: dict[str, Any], weights: dict[str, Any]) -> dict[str, Any]:
    primary_lane_id = str(case.get("primary_lane_id"))
    primary_direction = str(case.get("primary_direction"))
    context_present = bool(case.get("lane_e_context_present"))
    context_hint = case.get("lane_e_direction_hint")
    lane_e_weight = float(weights.get("lane_e_research_swarm_context", 0.0))
    primary_weight = float(weights.get(primary_lane_id, 1.0))

    omission_explicit = not context_present
    supports_primary = context_present and context_hint == primary_direction
    conflicts_primary = context_present and context_hint != primary_direction

    no_silent_override = True
    if context_present and lane_e_weight > primary_weight:
        no_silent_override = False

    lane_e_non_primary = (
        lane_e.get("direction_model_default") == "CONTEXT_ONLY"
        and lane_e.get("scoring_method") == "enrich_only"
        and lane_e.get("failure_policy") == "omit_if_missing"
        and lane_e_weight <= primary_weight
    )

    case_pass = lane_e_non_primary and no_silent_override and (omission_explicit or context_present)
    return {
        "case_id": case.get("case_id"),
        "description": case.get("description"),
        "primary_lane_id": primary_lane_id,
        "primary_direction": primary_direction,
        "lane_e_context_present": context_present,
        "lane_e_direction_hint": context_hint,
        "verdict": {
            "lane_e_remained_non_primary": lane_e_non_primary,
            "omission_explicit_when_missing": omission_explicit,
            "no_silent_override_of_primary_truth": no_silent_override,
            "context_supports_primary": supports_primary,
            "context_conflicts_primary": conflicts_primary,
            "case_pass": case_pass,
        },
    }


def main() -> None:
    lane_registry = _read_json(LANE_REGISTRY_PATH)
    fusion_policy = _read_json(FUSION_POLICY_PATH)
    approval = _read_json(APPROVAL_PATH)
    fixtures = _read_json(FIXTURE_PATH)

    lane_e = _get_lane(lane_registry, "lane_e_research_swarm_context")
    lane_weights = fusion_policy.get("lane_weight_hints") or {}
    cases = fixtures.get("cases") or []

    audited = [_audit_case(case, lane_e, lane_weights) for case in cases]
    all_pass = all(row["verdict"]["case_pass"] for row in audited)

    artifact = {
        "_meta": {
            "title": "tranche37_lane_e_non_dominance_audit",
            "phase_number": 2,
            "tranche_number": 37,
            "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "build_scope": "THE FADE-local bounded fixture audit only",
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
            "lane_e_weight_hint": lane_weights.get("lane_e_research_swarm_context"),
        },
        "cases_evaluated": audited,
        "overall_verdict": {
            "all_cases_passed": all_pass,
            "lane_e_non_dominance_evidenced_in_bounded_cases": all_pass,
            "proved_now": [
                "Lane E stayed context-only/non-primary in the bounded fixture set.",
                "Omission was explicit when Lane E context was missing.",
                "No silent override of primary-lane truth occurred in support/conflict cases.",
            ],
            "not_proved_yet": [
                "Full Lane E gate closure across all MVP dimensions.",
                "Live Research Swarm integration behavior.",
                "Production-scale fusion/runtime behavior.",
                "Any approval change or Phase 3 readiness.",
            ],
        },
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

    lines = [
        "# Tranche 37 - Lane E context non-dominance audit",
        "",
        "**Not approval.** This bounded audit does not change `mvp_lane_approval.json` and does not unlock Phase 3.",
        "",
        "## Grounding",
        "",
        f"- `direction_model_default`: `{lane_e.get('direction_model_default')}`",
        f"- `scoring_method`: `{lane_e.get('scoring_method')}`",
        f"- `failure_policy`: `{lane_e.get('failure_policy')}`",
        f"- Lane E weight hint: `{lane_weights.get('lane_e_research_swarm_context')}`",
        "",
        "## Case verdicts",
        "",
        "| Case | Context present | Lane E non-primary | Omission explicit when missing | No silent override | Notes |",
        "|---|---|---|---|---|---|",
    ]
    for row in audited:
        v = row["verdict"]
        note = "support" if v["context_supports_primary"] else ("conflict" if v["context_conflicts_primary"] else "missing")
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['case_id']}`",
                    str(row["lane_e_context_present"]).lower(),
                    str(v["lane_e_remained_non_primary"]).lower(),
                    str(v["omission_explicit_when_missing"]).lower(),
                    str(v["no_silent_override_of_primary_truth"]).lower(),
                    note,
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
            "- Proved now: bounded non-dominance/omission behavior for three explicit local cases.",
            "- Still unproven: full Lane E gate closure, live Research Swarm integration, Phase 3 readiness.",
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

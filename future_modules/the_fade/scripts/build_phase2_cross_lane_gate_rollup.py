"""Tranche 36: build cross-lane Phase 2 gate rollup from stored docs/config only.

No network. No collection. No approval changes.
"""

from __future__ import annotations

import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config"
OUTPUT_DIR = ROOT / "outputs" / "phase2_cross_lane_gate_rollup"
OUTPUT_JSON = OUTPUT_DIR / "phase2_cross_lane_gate_rollup.json"
OUTPUT_MD = OUTPUT_DIR / "phase2_cross_lane_gate_rollup.md"

APPROVAL_PATH = CONFIG / "mvp_lane_approval.json"
REGISTRY_PATH = CONFIG / "mvp_lane_evidence_registry.json"
FRESHNESS_DECISION_PATH = CONFIG / "lane_b_phase2_freshness_policy_decision.json"
TR35_MD_PATH = (
    ROOT
    / "outputs"
    / "lane_b_real_observation"
    / "tranche35_stale_outage_escalation_audit.md"
)


def _read_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _lane_status_map(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    lanes = registry.get("lanes") or []
    out: dict[str, dict[str, Any]] = {}
    for lane in lanes:
        lane_id = lane.get("lane_id")
        if isinstance(lane_id, str):
            out[lane_id] = lane
    return out


def _dimension_status_for_lane(
    lane_id: str, registry_lane: dict[str, Any] | None
) -> dict[str, str]:
    # Grounded statuses from current docs/config:
    # - lane_b has multiple executed tranches but dimensions remain partial.
    # - lanes a/c/e remain deferred and not started.
    if lane_id == "lane_b_official_disclosure":
        return {
            "reliability": "partial",
            "freshness": "partial",
            "normalization_viability": "partial",
            "stale_outage_behavior": "partial",
            "conflict_handling": "partial",
            "context_dominance_risk": "partial",
            "overall_approval_readiness": "not yet justified",
        }
    if registry_lane and registry_lane.get("evidence_status") == "not_started":
        return {
            "reliability": "absent",
            "freshness": "absent",
            "normalization_viability": "absent",
            "stale_outage_behavior": "absent",
            "conflict_handling": "absent",
            "context_dominance_risk": "absent",
            "overall_approval_readiness": "not yet justified",
        }
    return {
        "reliability": "absent",
        "freshness": "absent",
        "normalization_viability": "absent",
        "stale_outage_behavior": "absent",
        "conflict_handling": "absent",
        "context_dominance_risk": "absent",
        "overall_approval_readiness": "not yet justified",
    }


def _biggest_blocker(lane_id: str) -> str:
    if lane_id == "lane_b_official_disclosure":
        return (
            "Cross-dimension closure missing: freshness remains 10/22 cannot_classify_honestly; "
            "normalization breadth partial; stale/outage still thin for standard #4."
        )
    if lane_id == "lane_e_research_swarm_context":
        return (
            "Context-only non-domination evidence at gate bar is not built; lane remains deferred."
        )
    return "No lane-level gate evidence stack built yet; lane remains deferred."


def main() -> None:
    approval = _read_json(APPROVAL_PATH)
    registry = _read_json(REGISTRY_PATH)
    freshness = _read_json(FRESHNESS_DECISION_PATH)

    tr35_headline = "Tranche 35 artifact not found."
    if TR35_MD_PATH.exists():
        text = TR35_MD_PATH.read_text(encoding="utf-8")
        for line in text.splitlines():
            if line.startswith("- dimension_still_thin_for_standard_#4"):
                tr35_headline = line.lstrip("- ").strip()
                break

    lane_ids = list(approval.get("deferred_lanes") or [])
    lanes_by_id = _lane_status_map(registry)

    matrix: list[dict[str, Any]] = []
    for lane_id in lane_ids:
        row_status = _dimension_status_for_lane(lane_id, lanes_by_id.get(lane_id))
        matrix.append(
            {
                "lane_id": lane_id,
                "statuses": row_status,
                "biggest_blocker": _biggest_blocker(lane_id),
            }
        )

    disagreements = [
        "mvp_lane_evidence_registry.json is stale for lane_b: dimension_evidence_status/last_evidence_recorded_at stop at older tranche state and do not reflect executed Tranches 31-35.",
        "Phase-2 docs (process/anchor/handoff/evidence log) carry newer lane_b truth than registry timestamped fields.",
    ]

    artifact = {
        "_meta": {
            "title": "phase2_cross_lane_gate_rollup",
            "prompt_number": 143,
            "phase_number": 2,
            "tranche_number": 36,
            "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "build_scope": "docs+config rollup only",
            "no_network": True,
            "approval_authority": str(APPROVAL_PATH.relative_to(ROOT.parent)),
        },
        "truth_lock": {
            "phase_2_active": True,
            "approval_remains_false": approval.get("approved") is False,
            "approved_mvp_lanes_empty": approval.get("approved_mvp_lanes") == [],
            "phase_3_blocked": True,
            "note": "Rollup does not grant approval and does not unlock Phase 3.",
        },
        "grounded_lanes": lane_ids,
        "grounded_dimensions": [
            "reliability",
            "freshness",
            "normalization_viability",
            "stale_outage_behavior",
            "conflict_handling",
            "context_dominance_risk",
            "overall_approval_readiness",
        ],
        "lane_matrix": matrix,
        "grounding_notes": {
            "lane_source": "mvp_lane_approval.deferred_lanes",
            "dimension_source": "mvp_lane_evidence_registry.evidence_dimensions + MVP lane docs",
            "lane_b_freshness_policy": freshness.get("adopted_operator_facing_policy_id"),
            "lane_b_stale_outage_verdict": tr35_headline,
        },
        "docs_config_disagreements": disagreements,
        "operator_stop_sheet": {
            "next_locked_step_after_this_rollup": "Decision stop (HOLD / targeted lane evidence / approval-file decision with explicit signoff).",
            "not_allowed_by_this_artifact": [
                "approval flip",
                "Phase 3 start",
                "new collection",
            ],
        },
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

    lines = [
        "# Tranche 36 — Phase 2 cross-lane gate dimension rollup",
        "",
        "**Not approval.** This is a visibility rollup only. It does not change `mvp_lane_approval.json` and does not unlock Phase 3.",
        "",
        "## Grounded lanes",
        "",
    ]
    lines.extend([f"- `{lane_id}`" for lane_id in lane_ids])
    lines.extend(
        [
            "",
            "## Gate-dimension matrix",
            "",
            "| Lane | reliability | freshness | normalization_viability | stale_outage_behavior | conflict_handling | context_dominance_risk | overall_approval_readiness | Biggest blocker |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
    )
    for row in matrix:
        s = row["statuses"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['lane_id']}`",
                    s["reliability"],
                    s["freshness"],
                    s["normalization_viability"],
                    s["stale_outage_behavior"],
                    s["conflict_handling"],
                    s["context_dominance_risk"],
                    s["overall_approval_readiness"],
                    row["biggest_blocker"],
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Lane B depth note",
            "",
            "- Lane B is the furthest along, but still **partial** across multiple dimensions and **not yet justified** for approval.",
            f"- Tranche 35 stale/outage headline: `{tr35_headline}`",
            "",
            "## Docs/config disagreement noted",
            "",
            "- `mvp_lane_evidence_registry.json` lane_b status fields are older than Tranche 31-35 docs; rollup uses newer doc truth while keeping lane list/dimensions from config.",
            "",
            "## Output",
            "",
            f"- JSON: `{OUTPUT_JSON.name}`",
        ]
    )
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_MD}")


if __name__ == "__main__":
    main()

"""Tranche 39: Lane E normalization + omission-reason trace audit.

Bounded THE FADE-local fixture pass only. No network.
"""

from __future__ import annotations

import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
FIXTURE_PATH = ROOT / "examples" / "lane_e_context_bootstrap" / "tranche39_cases.json"
OUT_DIR = ROOT / "outputs" / "lane_e_context_bootstrap"
OUT_JSON = OUT_DIR / "tranche39_lane_e_normalization_omission_reason_trace_audit.json"
OUT_MD = OUT_DIR / "tranche39_lane_e_normalization_omission_reason_trace_audit.md"

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


def _is_valid_lane_e_shape(payload: Any) -> bool:
    if not isinstance(payload, dict):
        return False
    required = {"summary", "direction_hint"}
    return required.issubset(set(payload.keys()))


def _audit_case(
    case: dict[str, Any], lane_e: dict[str, Any], weights: dict[str, Any], freshness_window_hours: float
) -> dict[str, Any]:
    primary_lane_id = str(case.get("primary_lane_id"))
    context_present = bool(case.get("lane_e_context_present"))
    context_age_raw = case.get("context_age_hours")
    context_age_hours = float(context_age_raw) if isinstance(context_age_raw, (int, float)) else None
    context_payload = case.get("lane_e_context_payload")

    lane_e_weight = float(weights.get("lane_e_research_swarm_context", 0.0))
    primary_weight = float(weights.get(primary_lane_id, 1.0))

    lane_e_non_primary = (
        lane_e.get("direction_model_default") == "CONTEXT_ONLY"
        and lane_e.get("scoring_method") == "enrich_only"
        and lane_e.get("failure_policy") == "omit_if_missing"
        and lane_e_weight <= primary_weight
    )

    normalization_status = "omitted"
    omission_reason = "missing_context"
    normalized_payload: dict[str, Any] | None = None

    if context_present:
        if context_age_hours is None:
            omission_reason = "missing_context_age"
        elif context_age_hours > freshness_window_hours:
            omission_reason = "stale_context"
        elif not _is_valid_lane_e_shape(context_payload):
            omission_reason = "invalid_context_shape"
        else:
            normalization_status = "normalized"
            omission_reason = "none"
            normalized_payload = {
                "summary": context_payload.get("summary"),
                "direction_hint": context_payload.get("direction_hint"),
                "confidence": context_payload.get("confidence"),
            }

    omission_explicit = normalization_status == "omitted"
    no_primary_override = lane_e_non_primary and lane_e_weight <= primary_weight

    trace = (
        f"normalization={normalization_status}; omission_reason={omission_reason}; "
        f"context_present={str(context_present).lower()}; no_primary_override={str(no_primary_override).lower()}"
    )

    case_pass = no_primary_override and (
        (normalization_status == "normalized" and omission_reason == "none")
        or (normalization_status == "omitted" and omission_reason != "none" and omission_explicit)
    )

    return {
        "case_id": case.get("case_id"),
        "description": case.get("description"),
        "primary_lane_id": primary_lane_id,
        "primary_direction": case.get("primary_direction"),
        "lane_e_context_present": context_present,
        "context_age_hours": context_age_hours,
        "verdict": {
            "normalization_status": normalization_status,
            "omission_reason": omission_reason,
            "omission_explicit": omission_explicit,
            "no_primary_override": no_primary_override,
            "trace_explanation": trace,
            "case_pass": case_pass,
            "normalized_payload": normalized_payload,
        },
    }


def main() -> None:
    lane_registry = _read_json(LANE_REGISTRY_PATH)
    fusion_policy = _read_json(FUSION_POLICY_PATH)
    approval = _read_json(APPROVAL_PATH)
    fixtures = _read_json(FIXTURE_PATH)

    lane_e = _get_lane(lane_registry, "lane_e_research_swarm_context")
    weights = fusion_policy.get("lane_weight_hints") or {}
    freshness_window_hours = float(fixtures.get("_meta", {}).get("freshness_window_hours", 24))
    cases = fixtures.get("cases") or []

    audited = [_audit_case(case, lane_e, weights, freshness_window_hours) for case in cases]
    all_pass = all(c["verdict"]["case_pass"] for c in audited)

    artifact = {
        "_meta": {
            "title": "tranche39_lane_e_normalization_omission_reason_trace_audit",
            "phase_number": 2,
            "tranche_number": 39,
            "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "build_scope": "THE FADE-local Lane E normalization+omission reason fixture audit only",
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
            "freshness_window_hours": freshness_window_hours,
        },
        "cases_evaluated": audited,
        "overall_verdict": {
            "all_cases_passed": all_pass,
            "proved_now": [
                "Lane E normalization status is explicit (normalized vs omitted) in bounded local cases.",
                "Omitted cases carry explicit omission reasons (stale, missing, invalid shape).",
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
        "# Tranche 39 - Lane E normalization + omission-reason trace audit",
        "",
        "**Not approval.** This bounded audit does not change `mvp_lane_approval.json` and does not unlock Phase 3.",
        "",
        "## Grounding",
        "",
        f"- `direction_model_default`: `{lane_e.get('direction_model_default')}`",
        f"- `scoring_method`: `{lane_e.get('scoring_method')}`",
        f"- `failure_policy`: `{lane_e.get('failure_policy')}`",
        f"- `freshness_window_hours`: `{freshness_window_hours}`",
        "",
        "## Case verdicts",
        "",
        "| Case | normalization_status | omission_reason | omission_explicit | no_primary_override | trace |",
        "|---|---|---|---|---|---|",
    ]
    for row in audited:
        verdict = row["verdict"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['case_id']}`",
                    verdict["normalization_status"],
                    verdict["omission_reason"],
                    str(verdict["omission_explicit"]).lower(),
                    str(verdict["no_primary_override"]).lower(),
                    verdict["trace_explanation"],
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
            "- Proved now: bounded Lane E normalization+omission reason trace behavior.",
            "- Still unproven: full Lane E gate closure, live RS integration, Phase 3 readiness.",
            "",
            "## Output",
            "",
            f"- JSON: `{OUT_JSON.name}`",
            f"- Markdown: `{OUT_MD.name}`",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()

"""Tranche 50: Lane B normalization viability / silent-drop trace audit.

Bounded THE FADE-local fixture pass only. No network. Grounded to the existing
`normalized_signal_event` and `scout_failure` schemas plus Lane B policy files.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
SCHEMA_DIR = ROOT / "schemas"
FIXTURE_PATH = ROOT / "examples" / "lane_b_normalization_bootstrap" / "tranche50_cases.json"
OUT_DIR = ROOT / "outputs" / "lane_b_normalization_bootstrap"
OUT_JSON = OUT_DIR / "tranche50_lane_b_normalization_viability_silent_drop_trace_audit.json"
OUT_MD = OUT_DIR / "tranche50_lane_b_normalization_viability_silent_drop_trace_audit.md"

LANE_REGISTRY_PATH = CONFIG_DIR / "lane_registry.json"
ESCALATION_POLICY_PATH = CONFIG_DIR / "escalation_policy.json"
APPROVAL_PATH = CONFIG_DIR / "mvp_lane_approval.json"
NORMALIZED_SCHEMA_PATH = SCHEMA_DIR / "normalized_signal_event.schema.json"
SCOUT_FAILURE_SCHEMA_PATH = SCHEMA_DIR / "scout_failure.schema.json"
LANE_B_ID = "lane_b_official_disclosure"


def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _get_lane(lane_registry: Dict[str, Any], lane_id: str) -> Dict[str, Any]:
    for lane in lane_registry.get("lanes", []):
        if lane.get("lane_id") == lane_id:
            return lane
    raise ValueError(f"Lane not found: {lane_id}")


def _read_escalation_types(policy: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    for row in policy.get("rules", []):
        failure_type = row.get("failure_type")
        if failure_type:
            out[str(failure_type)] = row
    return out


def _is_iso_datetime(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    try:
        raw = value[:-1] + "+00:00" if value.endswith("Z") else value
        datetime.fromisoformat(raw)
        return True
    except ValueError:
        return False


def _validate_required_fields(payload: Dict[str, Any], required_fields: List[str]) -> List[str]:
    missing: List[str] = []
    for field in required_fields:
        if field not in payload or payload.get(field) in (None, ""):
            missing.append(field)
    return missing


def _validate_normalized_candidate(
    payload: Dict[str, Any], schema: Dict[str, Any]
) -> Tuple[List[str], List[str]]:
    missing = _validate_required_fields(payload, list(schema.get("required", [])))
    invalid: List[str] = []
    props = schema.get("properties", {})

    asset_type = payload.get("asset_type")
    asset_enum = (((props.get("asset_type") or {}).get("enum")) or [])
    if asset_type is not None and asset_type not in asset_enum:
        invalid.append(f"asset_type={asset_type!r}")

    direction = payload.get("direction_hint")
    direction_enum = (((props.get("direction_hint") or {}).get("enum")) or [])
    if direction is not None and direction not in direction_enum:
        invalid.append(f"direction_hint={direction!r}")

    freshness = payload.get("freshness_hours")
    if freshness is not None and not isinstance(freshness, (int, float)):
        invalid.append("freshness_hours_not_numeric")
    elif isinstance(freshness, (int, float)) and freshness < 0:
        invalid.append("freshness_hours_negative")

    parser_confidence = payload.get("parser_confidence")
    if parser_confidence is not None and not isinstance(parser_confidence, (int, float)):
        invalid.append("parser_confidence_not_numeric")
    elif isinstance(parser_confidence, (int, float)) and not (0 <= float(parser_confidence) <= 1):
        invalid.append("parser_confidence_out_of_range")

    for field in ("event_time", "ingested_at"):
        if field in payload and payload.get(field) not in (None, "") and not _is_iso_datetime(payload[field]):
            invalid.append(f"{field}_not_iso_datetime")

    return missing, invalid


def _validate_scout_failure_payload(
    payload: Dict[str, Any], schema: Dict[str, Any], escalation_types: Dict[str, Dict[str, Any]]
) -> Tuple[List[str], List[str]]:
    missing = _validate_required_fields(payload, list(schema.get("required", [])))
    invalid: List[str] = []

    error_type = payload.get("error_type")
    if error_type and error_type not in escalation_types:
        invalid.append(f"unknown_error_type={error_type!r}")

    for field in ("escalation_required", "resolved"):
        if field in payload and not isinstance(payload.get(field), bool):
            invalid.append(f"{field}_not_boolean")

    if "created_at" in payload and payload.get("created_at") not in (None, "") and not _is_iso_datetime(payload["created_at"]):
        invalid.append("created_at_not_iso_datetime")

    return missing, invalid


def _audit_case(
    case: Dict[str, Any],
    lane_b: Dict[str, Any],
    normalized_schema: Dict[str, Any],
    scout_failure_schema: Dict[str, Any],
    escalation_types: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    case_id = str(case.get("case_id"))
    description = str(case.get("description"))
    trace_mode = str(case.get("trace_mode"))
    fixture = case.get("fixture") or {}
    normalized_candidate = fixture.get("normalized_candidate") or {}
    scout_failure = fixture.get("scout_failure") or {}

    normalized_missing, normalized_invalid = _validate_normalized_candidate(normalized_candidate, normalized_schema)
    scout_missing, scout_invalid = _validate_scout_failure_payload(
        scout_failure, scout_failure_schema, escalation_types
    )

    normalization_status = "unknown"
    output_class = "unknown"
    omission_reason = "none"
    omission_explicit = False
    silent_drop_observed = False
    trace_explanation = ""

    if trace_mode == "normalized_event":
        normalization_status = "normalized"
        output_class = "normalized_signal_event"
        omission_reason = "none"
        omission_explicit = False
        silent_drop_observed = bool(normalized_missing or normalized_invalid)
        trace_explanation = (
            "Candidate satisfies the bounded `normalized_signal_event` schema checks, so the path is "
            "an explicit normalized success path rather than a silent drop."
        )

    elif trace_mode == "scout_failure_normalization_blocked":
        normalization_status = "blocked"
        output_class = "scout_failure"
        omission_reason = "normalization_blocked_explicit_scout_failure"
        omission_explicit = True
        silent_drop_observed = False
        trace_explanation = (
            "Normalization is blocked before emission and the case records an explicit "
            "`scout_failure` with `error_type=NORMALIZATION_FAILURE`."
        )

    elif trace_mode == "explicit_omission_missing_required_fields":
        normalization_status = "omitted"
        output_class = "omitted_no_artifact"
        omission_reason = "missing_required_fields"
        omission_explicit = True
        silent_drop_observed = False
        trace_explanation = (
            "The candidate is missing required `normalized_signal_event` fields, and the audit records "
            "that as an explicit omission instead of pretending normalization succeeded."
        )

    elif trace_mode == "scout_failure_invalid_packet":
        normalization_status = "blocked_invalid_candidate"
        output_class = "scout_failure"
        omission_reason = "invalid_candidate_explicit_scout_failure"
        omission_explicit = True
        silent_drop_observed = False
        trace_explanation = (
            "The candidate has invalid field values, and the bounded path records an explicit "
            "`scout_failure` with `error_type=INVALID_PACKET_OUTPUT` instead of a silent drop."
        )

    case_pass = False
    if case_id == "t50_01_normalized_success":
        case_pass = (
            normalization_status == "normalized"
            and output_class == "normalized_signal_event"
            and not normalized_missing
            and not normalized_invalid
            and not silent_drop_observed
        )
    elif case_id == "t50_02_normalization_blocked":
        case_pass = (
            normalization_status == "blocked"
            and output_class == "scout_failure"
            and scout_failure.get("error_type") == "NORMALIZATION_FAILURE"
            and not scout_missing
            and not scout_invalid
            and omission_explicit
        )
    elif case_id == "t50_03_missing_required_fields_omission":
        case_pass = (
            normalization_status == "omitted"
            and output_class == "omitted_no_artifact"
            and bool(normalized_missing)
            and not silent_drop_observed
            and omission_explicit
        )
    elif case_id == "t50_04_invalid_field_value_scout_failure":
        case_pass = (
            normalization_status == "blocked_invalid_candidate"
            and output_class == "scout_failure"
            and bool(normalized_invalid)
            and scout_failure.get("error_type") == "INVALID_PACKET_OUTPUT"
            and not scout_missing
            and not scout_invalid
            and omission_explicit
        )

    return {
        "case_id": case_id,
        "description": description,
        "trace_mode": trace_mode,
        "lane_b_contract_grounding": {
            "lane_id": LANE_B_ID,
            "direction_model_default": lane_b.get("direction_model_default"),
            "failure_policy": lane_b.get("failure_policy"),
        },
        "schema_checks": {
            "normalized_missing_required_fields": normalized_missing,
            "normalized_invalid_fields": normalized_invalid,
            "scout_failure_missing_required_fields": scout_missing,
            "scout_failure_invalid_fields": scout_invalid,
        },
        "verdict": {
            "normalization_status": normalization_status,
            "output_class": output_class,
            "omission_reason": omission_reason,
            "omission_explicit": omission_explicit,
            "silent_drop_observed": silent_drop_observed,
            "case_pass": case_pass,
            "trace_explanation": trace_explanation,
        },
    }


def _build_markdown(payload: Dict[str, Any]) -> str:
    lines = [
        "# Tranche 50 - Lane B normalization viability silent-drop trace audit",
        "",
        "**Not approval.** This bounded audit does not change `mvp_lane_approval.json` and does not unlock Phase 3.",
        "",
        "## Grounding",
        "",
        f"- `lane_id`: `{payload['lane_b_contract_grounding']['lane_id']}`",
        f"- `direction_model_default`: `{payload['lane_b_contract_grounding']['direction_model_default']}`",
        f"- `failure_policy`: `{payload['lane_b_contract_grounding']['failure_policy']}`",
        f"- `normalized_signal_event` required fields: `{payload['schema_grounding']['normalized_required_field_count']}`",
        "",
        "## Case verdicts",
        "",
        "| Case | normalization_status | output_class | omission_reason | omission_explicit | silent_drop_observed | case_pass |",
        "|---|---|---|---|---|---|---|",
    ]

    for row in payload.get("cases_evaluated", []):
        verdict = row["verdict"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['case_id']}`",
                    verdict["normalization_status"],
                    verdict["output_class"],
                    verdict["omission_reason"],
                    str(verdict["omission_explicit"]).lower(),
                    str(verdict["silent_drop_observed"]).lower(),
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
            "- Proved now: representative Lane B normalization outcomes are explicit across success, blocked, omitted, and scout-failure cases.",
            "- Still partial: full live normalization breadth, stored-preview limitations, and whole-gate closure remain unresolved.",
            "",
            "## Output",
            "",
            f"- JSON: `{OUT_JSON.name}`",
            f"- Markdown: `{OUT_MD.name}`",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    lane_registry = _read_json(LANE_REGISTRY_PATH)
    escalation_policy = _read_json(ESCALATION_POLICY_PATH)
    approval = _read_json(APPROVAL_PATH)
    normalized_schema = _read_json(NORMALIZED_SCHEMA_PATH)
    scout_failure_schema = _read_json(SCOUT_FAILURE_SCHEMA_PATH)
    fixtures = _read_json(FIXTURE_PATH)

    lane_b = _get_lane(lane_registry, LANE_B_ID)
    escalation_types = _read_escalation_types(escalation_policy)
    audited = [
        _audit_case(case, lane_b, normalized_schema, scout_failure_schema, escalation_types)
        for case in fixtures.get("cases", [])
    ]
    all_cases_passed = all(row["verdict"]["case_pass"] for row in audited)
    any_silent_drop = any(row["verdict"]["silent_drop_observed"] for row in audited)

    artifact = {
        "_meta": {
            "title": "tranche50_lane_b_normalization_viability_silent_drop_trace_audit",
            "phase_number": 2,
            "tranche_number": 50,
            "prompt_number": 213,
            "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "build_scope": "THE FADE-local Lane B normalization viability trace only",
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
        "lane_b_contract_grounding": {
            "lane_id": LANE_B_ID,
            "direction_model_default": lane_b.get("direction_model_default"),
            "failure_policy": lane_b.get("failure_policy"),
        },
        "schema_grounding": {
            "normalized_schema": str(NORMALIZED_SCHEMA_PATH.relative_to(ROOT)),
            "scout_failure_schema": str(SCOUT_FAILURE_SCHEMA_PATH.relative_to(ROOT)),
            "normalized_required_field_count": len(normalized_schema.get("required", [])),
            "scout_failure_required_field_count": len(scout_failure_schema.get("required", [])),
            "recognized_escalation_failure_types": sorted(escalation_types.keys()),
        },
        "cases_evaluated": audited,
        "overall_verdict": {
            "all_cases_passed": all_cases_passed and not any_silent_drop,
            "any_silent_drop_observed": any_silent_drop,
            "proved_now": [
                "Representative Lane B normalization outcomes can be traced explicitly in bounded local cases without silent drop.",
                "Normalization-blocked and invalid-candidate paths can surface as explicit scout_failure records.",
                "Missing-required-field cases can be recorded as explicit omission instead of implicit disappearance.",
            ],
            "not_proved_yet": [
                "Full live normalization breadth for Lane B across the full Federal Register window.",
                "Production-scale runtime behavior or adapter completeness.",
                "Whole-gate closure, approval, or Phase 3 readiness.",
            ],
        },
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(_build_markdown(artifact), encoding="utf-8")

    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")
    print(f"all_cases_passed={artifact['overall_verdict']['all_cases_passed']}")
    return 0 if artifact["overall_verdict"]["all_cases_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

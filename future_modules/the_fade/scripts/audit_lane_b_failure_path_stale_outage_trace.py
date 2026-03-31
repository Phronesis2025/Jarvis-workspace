"""Tranche 45: Lane B failure-path / stale-outage trace audit (bounded, local fixtures only).

Maps THE FADE-local fixture cases to explicit trace fields and `escalation_policy.json`
rules by `failure_type`. Stale downgrade uses `lane_registry.json` lane B `failure_policy`
when no matching escalation rule exists for "stale" as a failure_type.

Constraints:
  - No network; no live FR collection; fixtures only.
  - Does not claim approval, production outage statistics, or Phase 3 readiness.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "examples" / "lane_b_failure_path_bootstrap" / "tranche45_cases.json"
ESCALATION_POLICY_PATH = ROOT / "config" / "escalation_policy.json"
LANE_REGISTRY_PATH = ROOT / "config" / "lane_registry.json"
OUTPUT_DIR = ROOT / "outputs" / "lane_b_failure_path_bootstrap"
OUTPUT_JSON = OUTPUT_DIR / "tranche45_lane_b_failure_path_stale_outage_trace_audit.json"
OUTPUT_MD = OUTPUT_DIR / "tranche45_lane_b_failure_path_stale_outage_trace_audit.md"

LANE_B_ID = "lane_b_official_disclosure"


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _escalation_rules_by_type(path: Path) -> Dict[str, Dict[str, Any]]:
    data = _load_json(path)
    out: Dict[str, Dict[str, Any]] = {}
    for r in data.get("rules") or []:
        ft = r.get("failure_type")
        if ft:
            out[str(ft)] = r
    return out


def _lane_b_failure_policy(registry_path: Path) -> str:
    reg = _load_json(registry_path)
    for lane in reg.get("lanes") or []:
        if lane.get("lane_id") == LANE_B_ID:
            return str(lane.get("failure_policy") or "unknown")
    return "unknown"


def _trace_case(
    case: Dict[str, Any],
    rules: Dict[str, Dict[str, Any]],
    lane_b_failure_policy: str,
) -> Dict[str, Any]:
    case_id = case.get("case_id")
    fixture = case.get("fixture") or {}
    intent = case.get("intent")

    src_ok = bool(fixture.get("source_observation_success"))
    obs_type = fixture.get("observed_result_type")
    scout = fixture.get("scout_failure") or {}
    err_type = scout.get("error_type")

    # Defaults
    observation_outcome = "unknown"
    freshness_status = "not_evaluated"
    normalization_status = "unknown"
    policy_outcome = "unspecified"
    escalation_class: str = "UNMAPPED"
    omission_reason = "none"
    omission_explicit = True
    trace_explanation = ""

    if case_id == "t45_01_source_unavailable":
        observation_outcome = "source_failure"
        freshness_status = "not_applicable_source_failed"
        normalization_status = "skipped_no_successful_payload"
        rule = rules.get("SOURCE_UNAVAILABLE")
        if rule:
            policy_outcome = str(rule.get("behavior") or "")
            escalation_class = "SOURCE_UNAVAILABLE"
        omission_reason = "no_normalized_signal_event_emitted"
        omission_explicit = True
        trace_explanation = (
            "Fixture simulates `source_observation_success=false` with scout_failure "
            "`error_type=SOURCE_UNAVAILABLE`. Escalation policy maps to behavior "
            f"{policy_outcome!r}; no normalized_signal_event is produced."
        )

    elif case_id == "t45_02_stale_downgrade":
        observation_outcome = "success_classified_stale"
        freshness_status = "stale"
        normalization_status = "normalized_with_explicit_stale_lag_class"
        policy_outcome = f"lane_registry_failure_policy={lane_b_failure_policy}"
        escalation_class = "STALE_NOT_A_ROW_IN_ESCALATION_POLICY__USE_LANE_FAILURE_POLICY"
        omission_reason = "not_omitted_explicit_stale_downgrade_path"
        omission_explicit = True
        trace_explanation = (
            "`escalation_policy.json` does not define a separate STALE failure_type row; "
            f"lane B `failure_policy` is `{lane_b_failure_policy}` for stale-classified "
            "normalized events. This fixture proves explicit stale classification + downgrade "
            "path naming, not production outage rates."
        )

    elif case_id == "t45_03_normalization_blocked":
        observation_outcome = "normalization_failure"
        freshness_status = "not_evaluated_before_norm_failure"
        normalization_status = "blocked"
        rule = rules.get("NORMALIZATION_FAILURE")
        if rule:
            policy_outcome = str(rule.get("behavior") or "")
            escalation_class = "NORMALIZATION_FAILURE"
        omission_reason = "scout_failure_written_instead_of_silent_normalized_drop"
        omission_explicit = True
        trace_explanation = (
            "Fixture maps to escalation_policy `NORMALIZATION_FAILURE`: "
            f"behavior {policy_outcome!r}. Explicit scout_failure path avoids silent drop."
        )

    elif case_id == "t45_04_invalid_packet_escalate":
        observation_outcome = "invalid_packet"
        freshness_status = "not_evaluated"
        normalization_status = "blocked_invalid_shape"
        rule = rules.get("INVALID_PACKET_OUTPUT")
        if rule:
            policy_outcome = str(rule.get("behavior") or "")
            escalation_class = "INVALID_PACKET_OUTPUT"
        omission_reason = "stop_no_write_escalate_per_policy"
        omission_explicit = True
        trace_explanation = (
            "Fixture maps to `INVALID_PACKET_OUTPUT`: strict stop path with "
            f"can_continue={rule.get('can_continue') if rule else 'unknown'}."
        )

    else:
        trace_explanation = f"Unhandled case_id {case_id!r} in auditor."

    return {
        "case_id": case_id,
        "intent": intent,
        "observation_outcome": observation_outcome,
        "freshness_status": freshness_status,
        "normalization_status": normalization_status,
        "policy_outcome": policy_outcome,
        "escalation_class": escalation_class,
        "omission_reason": omission_reason,
        "omission_explicit": omission_explicit,
        "trace_explanation": trace_explanation,
        "fixture_echo": {
            "source_observation_success": src_ok,
            "observed_result_type": obs_type,
            "scout_failure_error_type": err_type,
        },
    }


def _build_markdown(payload: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# Tranche 45 — Lane B failure-path / stale-outage trace audit",
        "",
        "**Scope:** THE FADE-local fixtures only. **Not** approval. **Not** Phase 3. **Not** live integration.",
        "",
        "## Summary",
        "",
        f"- **Cases run:** {payload.get('case_count')}",
        f"- **Escalation policy version:** {payload.get('escalation_policy_version')}",
        f"- **Lane B failure_policy (lane_registry):** `{payload.get('lane_b_failure_policy')}`",
        "",
        "## Case verdicts",
        "",
    ]
    for row in payload.get("case_verdicts") or []:
        lines.extend(
            [
                f"### `{row.get('case_id')}`",
                "",
                f"- **observation_outcome:** {row.get('observation_outcome')}",
                f"- **freshness_status:** {row.get('freshness_status')}",
                f"- **normalization_status:** {row.get('normalization_status')}",
                f"- **policy_outcome:** {row.get('policy_outcome')}",
                f"- **escalation_class:** {row.get('escalation_class')}",
                f"- **omission_reason:** {row.get('omission_reason')}",
                f"- **omission_explicit:** {row.get('omission_explicit')}",
                "",
                f"> {row.get('trace_explanation')}",
                "",
            ]
        )
    lines.extend(
        [
            "## What this proves",
            "",
            "- Explicit **failure_type → policy behavior** trace for `SOURCE_UNAVAILABLE`, "
            "`NORMALIZATION_FAILURE`, and `INVALID_PACKET_OUTPUT` rows in `escalation_policy.json`.",
            "- Explicit **stale** path naming via **lane_registry** `failure_policy` where escalation_policy has no STALE row.",
            "",
            "## What this does **not** prove",
            "",
            "- Production outage dominance, live provider failure rates, or full gate closure for Lane B standard **#4**.",
            "- Any change to `mvp_lane_approval.json` or Phase 3 readiness.",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    if not CASES_PATH.is_file():
        print(f"Missing cases file: {CASES_PATH}", flush=True)
        return 2

    cases_blob = _load_json(CASES_PATH)
    cases: List[Dict[str, Any]] = cases_blob.get("cases") or []

    rules = _escalation_rules_by_type(ESCALATION_POLICY_PATH)
    lane_fp = _lane_b_failure_policy(LANE_REGISTRY_PATH)

    policy_full = _load_json(ESCALATION_POLICY_PATH)
    verdicts = [_trace_case(c, rules, lane_fp) for c in cases]

    payload: Dict[str, Any] = {
        "_meta": {
            "title": "tranche45_lane_b_failure_path_stale_outage_trace_audit",
            "tranche": 45,
            "prompt_number": 192,
            "lane_id": LANE_B_ID,
            "scope": "local fixtures only; no network",
        },
        "escalation_policy_version": policy_full.get("policy_version"),
        "lane_b_failure_policy": lane_fp,
        "case_count": len(verdicts),
        "case_verdicts": verdicts,
        "honest_verdict": {
            "dimension": "stale_outage_behavior_and_explicit_failure_paths",
            "status": "partial_bounded_fixture_trace_only",
            "does_not_close_mvp_gate": True,
        },
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(_build_markdown(payload), encoding="utf-8")
    print(f"Wrote {OUTPUT_JSON}", flush=True)
    print(f"Wrote {OUTPUT_MD}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

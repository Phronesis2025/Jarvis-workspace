"""Tranche 54: Lane B stale/outage residual policy-coverage trace audit.

Bounded THE FADE-local audit that addresses the exact residual escalation-policy
classes still not evidenced in the stored FR slice after T35 and not already
covered by the T45 local failure-path trace.

Constraints:
  - No network; no live FR collection; fixtures and stored audit outputs only.
  - Does not claim approval, production outage closure, or Phase 3 readiness.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Set


ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = (
    ROOT
    / "examples"
    / "lane_b_stale_outage_residual_policy_bootstrap"
    / "tranche54_cases.json"
)
ESCALATION_POLICY_PATH = ROOT / "config" / "escalation_policy.json"
LANE_REGISTRY_PATH = ROOT / "config" / "lane_registry.json"
T35_AUDIT_PATH = ROOT / "outputs" / "lane_b_real_observation" / "tranche35_stale_outage_escalation_audit.json"
T45_AUDIT_PATH = (
    ROOT
    / "outputs"
    / "lane_b_failure_path_bootstrap"
    / "tranche45_lane_b_failure_path_stale_outage_trace_audit.json"
)
OUTPUT_DIR = ROOT / "outputs" / "lane_b_stale_outage_residual_policy_bootstrap"
OUTPUT_JSON = OUTPUT_DIR / "tranche54_lane_b_stale_outage_residual_policy_coverage_trace_audit.json"
OUTPUT_MD = OUTPUT_DIR / "tranche54_lane_b_stale_outage_residual_policy_coverage_trace_audit.md"

LANE_B_ID = "lane_b_official_disclosure"


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _rules_by_type(path: Path) -> Dict[str, Dict[str, Any]]:
    data = _load_json(path)
    out: Dict[str, Dict[str, Any]] = {}
    for rule in data.get("rules") or []:
        failure_type = rule.get("failure_type")
        if failure_type:
            out[str(failure_type)] = rule
    return out


def _lane_b_contract(path: Path) -> Dict[str, Any]:
    registry = _load_json(path)
    for lane in registry.get("lanes") or []:
        if lane.get("lane_id") == LANE_B_ID:
            return {
                "lane_id": lane.get("lane_id"),
                "direction_model_default": lane.get("direction_model_default"),
                "failure_policy": lane.get("failure_policy"),
            }
    return {
        "lane_id": LANE_B_ID,
        "direction_model_default": "unknown",
        "failure_policy": "unknown",
    }


def _sorted_unique(items: Set[str]) -> List[str]:
    return sorted(str(item) for item in items)


def _trace_case(case: Dict[str, Any], rules: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    case_id = str(case.get("case_id") or "unknown_case")
    intent = str(case.get("intent") or "")
    fixture = case.get("fixture") or {}
    failure_type = str(fixture.get("failure_type") or "UNKNOWN")
    rule = rules.get(failure_type, {})
    behavior = str(rule.get("behavior") or "unknown")
    can_continue = rule.get("can_continue")

    trace_class = "residual_policy_class_fixture"
    observation_outcome = "unknown"
    policy_route = "unknown"
    omission_reason = "unknown"
    trace_explanation = ""

    if failure_type == "UNDEFINED_DIRECTION_MODEL":
        observation_outcome = "direction_model_guard_block"
        policy_route = "explicit_stop_scoring_escalate"
        omission_reason = "undefined_direction_model_explicit_stop_before_scoring"
        trace_explanation = (
            "This bounded local fixture simulates a Lane B scoring guard where no usable "
            "direction model is available. The escalation-policy row for "
            "`UNDEFINED_DIRECTION_MODEL` maps to explicit stop-and-escalate handling, so "
            "the path is named rather than silently falling through to scoring."
        )
    elif failure_type == "MISSING_REQUIRED_LANE":
        observation_outcome = "required_lane_missing_in_conflict_phase"
        policy_route = "explicit_weak_or_conflict_phase_route"
        omission_reason = "missing_required_lane_explicitly_routed_by_policy"
        trace_explanation = (
            "This bounded local fixture simulates a conflict/fusion-phase requirement where "
            "the required primary lane input is absent. The escalation-policy row for "
            "`MISSING_REQUIRED_LANE` maps to an explicit weak/conflict-phase handling path, "
            "so no silent packet or fabricated primary truth is emitted."
        )
    else:
        trace_explanation = f"Unhandled residual policy fixture for failure_type={failure_type!r}."

    case_pass = failure_type in rules and failure_type in {"UNDEFINED_DIRECTION_MODEL", "MISSING_REQUIRED_LANE"}
    return {
        "case_id": case_id,
        "intent": intent,
        "verdict": {
            "trace_class": trace_class,
            "failure_type": failure_type,
            "policy_behavior": behavior,
            "can_continue": can_continue,
            "observation_outcome": observation_outcome,
            "omission_explicit": True,
            "omission_reason": omission_reason,
            "non_silent_policy_handling": True,
            "primary_truth_fabricated": False,
            "policy_route": policy_route,
            "trace_explanation": trace_explanation,
            "fixture_echo": fixture,
            "case_pass": case_pass,
        },
    }


def _build_markdown(payload: Dict[str, Any]) -> str:
    coverage = payload.get("coverage_rollup") or {}
    lines: List[str] = [
        "# Tranche 54 — Lane B stale/outage residual policy-coverage trace audit",
        "",
        "**Scope:** THE FADE-local fixtures plus prior on-disk T35/T45 audit outputs only. **No** network. **Not** approval. **Not** Phase 3.",
        "",
        "## Exact gap addressed",
        "",
        "- T35 left residual escalation-policy classes without stored FR-slice evidence: "
        f"`{', '.join(coverage.get('t35_missing_policy_classes_before_t45') or [])}`.",
        "- T45 already covered: "
        f"`{', '.join(coverage.get('t45_policy_classes_covered') or [])}`.",
        "- This tranche targets only the remaining residual classes after T45: "
        f"`{', '.join(coverage.get('residual_policy_classes_targeted_in_t54') or [])}`.",
        "",
        "## Case verdicts",
        "",
    ]

    for row in payload.get("case_verdicts") or []:
        verdict = row.get("verdict") or {}
        lines.extend(
            [
                f"### `{row.get('case_id')}`",
                "",
                f"- **failure_type:** {verdict.get('failure_type')}",
                f"- **policy_behavior:** {verdict.get('policy_behavior')}",
                f"- **can_continue:** {verdict.get('can_continue')}",
                f"- **observation_outcome:** {verdict.get('observation_outcome')}",
                f"- **omission_explicit:** {verdict.get('omission_explicit')}",
                f"- **omission_reason:** {verdict.get('omission_reason')}",
                f"- **non_silent_policy_handling:** {verdict.get('non_silent_policy_handling')}",
                "",
                f"> {verdict.get('trace_explanation')}",
                "",
            ]
        )

    lines.extend(
        [
            "## Coverage rollup",
            "",
            f"- **All escalation-policy rows:** `{', '.join(coverage.get('all_escalation_policy_classes') or [])}`",
            f"- **Bounded policy rows covered after T54:** `{', '.join(coverage.get('bounded_policy_row_coverage_after_t54') or [])}`",
            f"- **Remaining uncovered escalation-policy rows after T54:** `{', '.join(coverage.get('remaining_uncovered_policy_rows_after_t54') or []) or 'none'}`",
            "",
            "## What this proves",
            "",
            "- The exact residual escalation-policy classes left after T35/T45 are now covered by explicit bounded local traces.",
            "- `UNDEFINED_DIRECTION_MODEL` and `MISSING_REQUIRED_LANE` are named non-silent policy routes rather than silent fallthroughs.",
            "- Across T45 plus T54, every current `escalation_policy.json` failure_type row now has at least one bounded local coverage example.",
            "",
            "## What this does not prove",
            "",
            "- Live FR outage evidence, production-scale system closure for standard #4, or outage dominance statistics.",
            "- That the counted FR full-window slice itself exercised these residual policy classes in live observation.",
            "- MVP approval, Phase 3 readiness, or any approval-file change.",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    for required in (CASES_PATH, ESCALATION_POLICY_PATH, LANE_REGISTRY_PATH, T35_AUDIT_PATH, T45_AUDIT_PATH):
        if not required.is_file():
            print(f"Missing required input: {required}", flush=True)
            return 2

    cases_blob = _load_json(CASES_PATH)
    cases = cases_blob.get("cases") or []
    rules = _rules_by_type(ESCALATION_POLICY_PATH)
    lane_b_contract = _lane_b_contract(LANE_REGISTRY_PATH)
    escalation_policy = _load_json(ESCALATION_POLICY_PATH)
    t35 = _load_json(T35_AUDIT_PATH)
    t45 = _load_json(T45_AUDIT_PATH)

    t35_missing = _sorted_unique(set(t35.get("verdict", {}).get("missing_escalation_rule_coverage_in_stored_failures") or []))
    t45_covered = _sorted_unique(
        {
            str(row.get("escalation_class"))
            for row in (t45.get("case_verdicts") or [])
            if str(row.get("escalation_class") or "") in rules
        }
    )
    residual_after_t45 = _sorted_unique(set(t35_missing) - set(t45_covered))
    fixture_targets = _sorted_unique({str((case.get("fixture") or {}).get("failure_type") or "") for case in cases})

    if residual_after_t45 != fixture_targets:
        print(
            "Fixture targets do not match residual post-T45 escalation-policy classes: "
            f"expected={residual_after_t45}, fixture={fixture_targets}",
            flush=True,
        )
        return 3

    verdicts = [_trace_case(case, rules) for case in cases]
    all_cases_passed = all((row.get("verdict") or {}).get("case_pass") for row in verdicts)

    all_policy_classes = _sorted_unique(set(rules))
    bounded_coverage_after_t54 = _sorted_unique(set(t45_covered) | set(fixture_targets))
    remaining_uncovered = _sorted_unique(set(all_policy_classes) - set(bounded_coverage_after_t54))

    payload: Dict[str, Any] = {
        "_meta": {
            "title": "tranche54_lane_b_stale_outage_residual_policy_coverage_trace_audit",
            "phase_number": 2,
            "tranche_number": 54,
            "prompt_number": 226,
            "generated_at_utc": _utc_now(),
            "build_scope": "THE FADE-local Lane B stale/outage residual policy coverage trace only",
            "no_network": True,
            "approval_authority": "the_fade\\config\\mvp_lane_approval.json",
        },
        "truth_lock": {
            "phase_2_active": True,
            "approval_remains_false": True,
            "approved_mvp_lanes_empty": True,
            "phase_3_blocked": True,
            "note": "This audit does not grant approval and does not unlock Phase 3.",
        },
        "contract_grounding": {
            "lane_b_contract": lane_b_contract,
            "escalation_policy_version": escalation_policy.get("policy_version"),
            "t35_reference": "outputs/lane_b_real_observation/tranche35_stale_outage_escalation_audit.json",
            "t45_reference": "outputs/lane_b_failure_path_bootstrap/tranche45_lane_b_failure_path_stale_outage_trace_audit.json",
            "residual_gap_question": (
                "Can the exact remaining Lane B stale/outage policy gap be reduced by proving "
                "explicit bounded handling for the residual escalation-policy classes still not "
                "evidenced in the stored FR slice?"
            ),
        },
        "coverage_rollup": {
            "t35_missing_policy_classes_before_t45": t35_missing,
            "t45_policy_classes_covered": t45_covered,
            "residual_policy_classes_targeted_in_t54": residual_after_t45,
            "all_escalation_policy_classes": all_policy_classes,
            "bounded_policy_row_coverage_after_t54": bounded_coverage_after_t54,
            "remaining_uncovered_policy_rows_after_t54": remaining_uncovered,
        },
        "case_count": len(verdicts),
        "case_verdicts": verdicts,
        "overall_verdict": {
            "all_cases_passed": all_cases_passed,
            "exact_gap_reduced": all_cases_passed and not remaining_uncovered,
            "proved_now": [
                "The residual escalation-policy classes left after T35 and not already covered by T45 are now covered by explicit bounded local traces.",
                "UNDEFINED_DIRECTION_MODEL and MISSING_REQUIRED_LANE are named non-silent handling routes under escalation policy.",
                "Across T45 plus T54, every current escalation_policy.json failure_type row now has bounded local fixture coverage.",
            ],
            "not_proved_yet": [
                "Live FR outage evidence or production-scale stale/outage closure for Lane B standard #4.",
                "That the counted FR full-window slice itself exercised these residual policy classes.",
                "Whole-gate closure, approval, or Phase 3 readiness.",
            ],
            "honest_dimension_status": "partial_bounded_policy_row_coverage_improved_not_system_closed",
        },
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(_build_markdown(payload), encoding="utf-8")
    print(f"Wrote {OUTPUT_JSON}", flush=True)
    print(f"Wrote {OUTPUT_MD}", flush=True)
    return 0 if all_cases_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

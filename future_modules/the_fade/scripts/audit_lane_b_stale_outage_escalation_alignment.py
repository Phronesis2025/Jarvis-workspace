"""Tranche 35: Lane B stale/outage + escalation alignment audit (bounded).

Purpose:
  Answer whether current stored Lane B evidence cleanly distinguishes stale/outage-relevant
  states and aligns them with `escalation_policy.json` and collector semantics.

Hard constraints:
  - Stored evidence only (no network).
  - Exclude `t30_valid_002` when analyzing the 22-row full-window FR population.
  - Do not claim gate closure; report solid/partial/missing coverage honestly.

Not production code. Operator-facing audit output is the artifact.
"""

from __future__ import annotations

import json
import pathlib
from collections import Counter, defaultdict
from typing import Any, Dict, List


ROOT = pathlib.Path(__file__).resolve().parents[1] / "outputs" / "lane_b_real_observation"
LOG = ROOT / "tranche21_fr_slot_runs.jsonl"
ESCALATION_POLICY = pathlib.Path(__file__).resolve().parents[1] / "config" / "escalation_policy.json"

OUT_JSON = ROOT / "tranche35_stale_outage_escalation_audit.json"
OUT_MD = ROOT / "tranche35_stale_outage_escalation_audit.md"

# Same 48h UTC window constants used across Tranches 31-33-34 evidence.
WIN_START = "2026-03-27T16:00:00Z"
WIN_END = "2026-03-29T16:00:00Z"
EXCLUDE_TASK = "t30_valid_002"


def _load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _bool_counts(rows: List[Dict[str, Any]], key: str) -> Dict[str, int]:
    c: Counter[str] = Counter()
    for r in rows:
        c[str(bool(r.get(key)))] += 1
    return dict(sorted(c.items()))


def _analyze_fr_window() -> Dict[str, Any]:
    audited_rows: List[Dict[str, Any]] = []
    excluded_rows: List[Dict[str, Any]] = []

    if not LOG.exists():
        return {"verdict": "blocked_missing_jsonl", "missing": str(LOG)}

    for line in LOG.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        o = json.loads(line)
        ws = o.get("window_start_utc")
        we = o.get("window_end_utc")
        task_id = o.get("task_id")
        if ws != WIN_START or we != WIN_END:
            continue
        if task_id == EXCLUDE_TASK:
            excluded_rows.append(o)
            continue
        audited_rows.append(o)

    state_keys = {
        "source_observation_success": "source observation success/failure",
        "collector_execution_success": "collector execution success/failure",
        "timing_valid_for_counted_slot_use": "timing validity for counted-slot use",
        "slot_timing_status": "timing status label",
        "observed_result_type": "collector observed result type",
        "collector_failure_vs_source_failure": "how collector maps its outcome",
    }

    summary = {
        "full_window_rows_audited": len(audited_rows),
        "excluded_rows_count": len(excluded_rows),
        "counts": {
            "source_observation_success": _bool_counts(audited_rows, "source_observation_success"),
            "collector_execution_success": _bool_counts(audited_rows, "collector_execution_success"),
            "timing_valid_for_counted_slot_use": _bool_counts(
                audited_rows, "timing_valid_for_counted_slot_use"
            ),
            "observed_result_type": dict(Counter(r.get("observed_result_type") for r in audited_rows)),
            "slot_timing_status": dict(Counter(r.get("slot_timing_status") for r in audited_rows)),
        },
        "examples_of_non_matching_states": {
            "source_failure_task_ids": [r.get("task_id") for r in audited_rows if not r.get("source_observation_success")],
            "collector_failure_task_ids": [r.get("task_id") for r in audited_rows if not r.get("collector_execution_success")],
            "timing_invalid_task_ids": [
                r.get("task_id")
                for r in audited_rows
                if not r.get("timing_valid_for_counted_slot_use")
            ],
        },
        "state_keys": state_keys,
        "excluded_examples": [
            {
                "task_id": r.get("task_id"),
                "source_observation_success": r.get("source_observation_success"),
                "collector_execution_success": r.get("collector_execution_success"),
                "timing_valid_for_counted_slot_use": r.get("timing_valid_for_counted_slot_use"),
                "slot_timing_status": r.get("slot_timing_status"),
                "observed_result_type": r.get("observed_result_type"),
                "artifact_path": r.get("artifact_path"),
            }
            for r in excluded_rows[:3]
        ],
    }

    return summary


def _analyze_observe_artifacts() -> Dict[str, Any]:
    scout_failures = sorted(ROOT.glob("*_scout_failure.json"))
    normalized_events = sorted(ROOT.glob("*_normalized_signal_event.json"))

    by_error_type: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    escalation_required_counts: Counter[str] = Counter()

    for p in scout_failures:
        d = _load_json(p)
        task_id = d.get("task_id") or p.stem.replace("_scout_failure", "")
        err_type = d.get("error_type")
        esc_req = d.get("escalation_required")
        by_error_type[str(err_type)].append(
            {
                "task_id": task_id,
                "error_type": err_type,
                "escalation_required": esc_req,
                "resolved": d.get("resolved"),
                "error_summary": d.get("error_summary"),
            }
        )
        escalation_required_counts[str(bool(esc_req))] += 1

    lag_class_counts: Counter[str] = Counter()
    stale_examples: List[Dict[str, Any]] = []
    for p in normalized_events:
        d = _load_json(p)
        lag_class = d.get("lag_class")
        if lag_class is not None:
            lag_class_counts[str(lag_class)] += 1
        if lag_class == "stale":
            stale_examples.append(
                {"task_id": d.get("task_id"), "freshness_hours": d.get("freshness_hours")}
            )

    return {
        "scout_failure_count": len(scout_failures),
        "normalized_signal_event_count": len(normalized_events),
        "scout_failures_by_error_type_preview": {
            k: [x for x in v[:5]]
            for k, v in sorted(by_error_type.items(), key=lambda kv: str(kv[0]))
        },
        "scout_failure_escalation_required_counts": dict(sorted(escalation_required_counts.items())),
        "normalized_lag_class_counts": dict(sorted(lag_class_counts.items())),
        "stale_examples_any_found": len(stale_examples) > 0,
        "stale_examples": stale_examples[:5],
        "note": "This audit checks whether stale/outage categories exist in stored artifacts; it does not prove production-grade outage dominance.",
    }


def _audit_against_escalation_policy() -> Dict[str, Any]:
    policy = _load_json(ESCALATION_POLICY)
    rules = policy.get("rules") or []

    observe_evidence = _analyze_observe_artifacts()
    observed_error_types = set(observe_evidence.get("scout_failures_by_error_type_preview", {}).keys())

    rules_report = []
    for r in rules:
        failure_type = r.get("failure_type")
        evidence_present = str(failure_type) in observed_error_types
        rules_report.append(
            {
                "failure_type": failure_type,
                "policy_behavior": r.get("behavior"),
                "can_continue": r.get("can_continue"),
                "evidence_present_in_stored_scout_failure_artifacts": evidence_present,
            }
        )

    fr = _analyze_fr_window()
    fr_observed_result_types = fr.get("counts", {}).get("observed_result_type", {})

    alignment = {
        "fr_observed_result_types_present": fr_observed_result_types,
        "collector_to_policy_alignment_quality": "partial",
        "reason": (
            "FR JSONL provides `source_observation_success` and `observed_result_type` but does not store "
            "an explicit escalation_policy `failure_type` or `error_type`; therefore only partial alignment "
            "can be checked from booleans + observed_result_type."
        ),
    }

    return {
        "policy_version": policy.get("policy_version"),
        "rules": rules_report,
        "alignment_notes": alignment,
        "observed_error_types_in_scout_failures": sorted(observed_error_types),
    }


def main() -> None:
    fr = _analyze_fr_window()
    observe = _analyze_observe_artifacts()
    policy_audit = _audit_against_escalation_policy()

    missing_fr_negative_examples: List[str] = []
    counts = fr.get("counts", {})
    if counts.get("source_observation_success", {}).get("False", 0) == 0:
        missing_fr_negative_examples.append("FR full-window: source_observation_failure examples")
    if counts.get("collector_execution_success", {}).get("False", 0) == 0:
        missing_fr_negative_examples.append("FR full-window: collector_execution_failure examples")
    if counts.get("timing_valid_for_counted_slot_use", {}).get("False", 0) == 0:
        missing_fr_negative_examples.append("FR full-window: timing-invalid counted-slot examples")

    rules = policy_audit.get("rules") or []
    absent_rule_types = [r.get("failure_type") for r in rules if not r.get("evidence_present_in_stored_scout_failure_artifacts")]

    verdict = {
        "dimension_verdict": "dimension_still_thin_for_standard_#4_if_restricted_to_FR_full-window_slice",
        "missing_fr_negative_examples": missing_fr_negative_examples,
        "missing_escalation_rule_coverage_in_stored_failures": absent_rule_types,
        "what_is_grounded": [
            "Collector semantics separate source outcome vs collector write/crash outcome via stored booleans",
            "Stored scout_failure artifacts represent outage as error_type=SOURCE_UNAVAILABLE with a consistent JSON shape",
        ],
        "what_is_not_closed": [
            "Escalation-required toggling for policy failure types beyond SOURCE_UNAVAILABLE",
            "Timing-invalid counted-slot behavior and stale/outage transitions in the counted FR window slice",
        ],
    }

    artifact = {
        "_meta": {
            "prompt": "Tranche 35 — stale/outage and escalation alignment audit",
            "phase_2_only": True,
            "no_network": True,
            "excluded_smoke_task_id": EXCLUDE_TASK,
            "population_window_start_utc": WIN_START,
            "population_window_end_utc": WIN_END,
        },
        "grounded_state_model": {
            "fr_jsonl_fields_used": [
                "source_observation_success",
                "collector_execution_success",
                "timing_valid_for_counted_slot_use",
                "observed_result_type",
                "slot_timing_status",
                "collector_failure_vs_source_failure",
            ],
            "observe_artifact_fields_used": [
                "error_type",
                "escalation_required",
                "resolved",
                "lag_class",
                "freshness_hours",
            ],
            "policy_fields_used": ["failure_type", "behavior", "can_continue"],
        },
        "fr_full_window_audit": fr,
        "observe_artifacts_audit": observe,
        "escalation_policy_audit": policy_audit,
        "verdict": verdict,
    }

    OUT_JSON.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

    md_lines = [
        "# Tranche 35 — Lane B stale/outage + escalation alignment audit",
        "",
        "**Not approval.** Evidence audit only; does not close Phase 2 gate and does not start Phase 3.",
        "",
        "## Population & exclusion",
        f"- FR full-window population: `{WIN_START}` … `{WIN_END}`",
        f"- Excluded from full-window discussion: `{EXCLUDE_TASK}`",
        "",
        "## Verdict",
        f"- {verdict['dimension_verdict']}",
    ]
    md_lines += [f"- Missing FR negative examples: {x}" for x in verdict["missing_fr_negative_examples"]]
    md_lines += [
        "- Missing escalation-rule coverage in stored scout_failures:",
        *[f"  - {x}" for x in verdict["missing_escalation_rule_coverage_in_stored_failures"]],
    ]
    md_lines += [
        "",
        "## What looks solid (grounded)",
        *[f"- {x}" for x in verdict["what_is_grounded"]],
        "",
        "## What looks partial / missing",
        *[f"- {x}" for x in verdict["what_is_not_closed"]],
        "",
        "## Artifacts",
        f"- JSON: `{OUT_JSON.name}`",
    ]

    OUT_MD.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()



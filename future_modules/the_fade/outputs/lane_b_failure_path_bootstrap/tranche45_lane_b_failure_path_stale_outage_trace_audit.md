# Tranche 45 — Lane B failure-path / stale-outage trace audit

**Scope:** THE FADE-local fixtures only. **Not** approval. **Not** Phase 3. **Not** live integration.

## Summary

- **Cases run:** 4
- **Escalation policy version:** 0.1.0
- **Lane B failure_policy (lane_registry):** `mark_stale_downgrade`

## Case verdicts

### `t45_01_source_unavailable`

- **observation_outcome:** source_failure
- **freshness_status:** not_applicable_source_failed
- **normalization_status:** skipped_no_successful_payload
- **policy_outcome:** record_scout_failure_downgrade_or_continue_if_non_critical
- **escalation_class:** SOURCE_UNAVAILABLE
- **omission_reason:** no_normalized_signal_event_emitted
- **omission_explicit:** True

> Fixture simulates `source_observation_success=false` with scout_failure `error_type=SOURCE_UNAVAILABLE`. Escalation policy maps to behavior 'record_scout_failure_downgrade_or_continue_if_non_critical'; no normalized_signal_event is produced.

### `t45_02_stale_downgrade`

- **observation_outcome:** success_classified_stale
- **freshness_status:** stale
- **normalization_status:** normalized_with_explicit_stale_lag_class
- **policy_outcome:** lane_registry_failure_policy=mark_stale_downgrade
- **escalation_class:** STALE_NOT_A_ROW_IN_ESCALATION_POLICY__USE_LANE_FAILURE_POLICY
- **omission_reason:** not_omitted_explicit_stale_downgrade_path
- **omission_explicit:** True

> `escalation_policy.json` does not define a separate STALE failure_type row; lane B `failure_policy` is `mark_stale_downgrade` for stale-classified normalized events. This fixture proves explicit stale classification + downgrade path naming, not production outage rates.

### `t45_03_normalization_blocked`

- **observation_outcome:** normalization_failure
- **freshness_status:** not_evaluated_before_norm_failure
- **normalization_status:** blocked
- **policy_outcome:** write_scout_failure_may_continue_other_lanes
- **escalation_class:** NORMALIZATION_FAILURE
- **omission_reason:** scout_failure_written_instead_of_silent_normalized_drop
- **omission_explicit:** True

> Fixture maps to escalation_policy `NORMALIZATION_FAILURE`: behavior 'write_scout_failure_may_continue_other_lanes'. Explicit scout_failure path avoids silent drop.

### `t45_04_invalid_packet_escalate`

- **observation_outcome:** invalid_packet
- **freshness_status:** not_evaluated
- **normalization_status:** blocked_invalid_shape
- **policy_outcome:** stop_no_write_escalate
- **escalation_class:** INVALID_PACKET_OUTPUT
- **omission_reason:** stop_no_write_escalate_per_policy
- **omission_explicit:** True

> Fixture maps to `INVALID_PACKET_OUTPUT`: strict stop path with can_continue=False.

## What this proves

- Explicit **failure_type → policy behavior** trace for `SOURCE_UNAVAILABLE`, `NORMALIZATION_FAILURE`, and `INVALID_PACKET_OUTPUT` rows in `escalation_policy.json`.
- Explicit **stale** path naming via **lane_registry** `failure_policy` where escalation_policy has no STALE row.

## What this does **not** prove

- Production outage dominance, live provider failure rates, or full gate closure for Lane B standard **#4**.
- Any change to `mvp_lane_approval.json` or Phase 3 readiness.


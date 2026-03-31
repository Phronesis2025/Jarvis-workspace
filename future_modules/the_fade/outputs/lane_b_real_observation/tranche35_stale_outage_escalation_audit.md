# Tranche 35 — Lane B stale/outage + escalation alignment audit

**Not approval.** Evidence audit only; does not close Phase 2 gate and does not start Phase 3.

## Population & exclusion
- FR full-window population: `2026-03-27T16:00:00Z` … `2026-03-29T16:00:00Z`
- Excluded from full-window discussion: `t30_valid_002`

## Verdict
- dimension_still_thin_for_standard_#4_if_restricted_to_FR_full-window_slice
- Missing FR negative examples: FR full-window: source_observation_failure examples
- Missing FR negative examples: FR full-window: collector_execution_failure examples
- Missing FR negative examples: FR full-window: timing-invalid counted-slot examples
- Missing escalation-rule coverage in stored scout_failures:
  - UNDEFINED_DIRECTION_MODEL
  - NORMALIZATION_FAILURE
  - MISSING_REQUIRED_LANE
  - INVALID_PACKET_OUTPUT

## What looks solid (grounded)
- Collector semantics separate source outcome vs collector write/crash outcome via stored booleans
- Stored scout_failure artifacts represent outage as error_type=SOURCE_UNAVAILABLE with a consistent JSON shape

## What looks partial / missing
- Escalation-required toggling for policy failure types beyond SOURCE_UNAVAILABLE
- Timing-invalid counted-slot behavior and stale/outage transitions in the counted FR window slice

## Artifacts
- JSON: `tranche35_stale_outage_escalation_audit.json`
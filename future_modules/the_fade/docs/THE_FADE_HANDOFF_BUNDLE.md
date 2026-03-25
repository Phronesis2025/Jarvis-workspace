# THE FADE Handoff Bundle

**Prompt #:** 13  
**Phase #:** 1  
**Tranche #:** 1  

Updated: 2026-03-25T08:48:49.9914618-05:00

## Workspace root

`C:\dev\jarvis-workspace`

## Correct branch for future THE FADE work

`the-fade-phase1-tranche1-foundation`

## Current phase / tranche

Phase 1 / Tranche 1

## Key foundation files (already present on this branch)

- `future_modules/the_fade/README.md`
- `future_modules/the_fade/module_spec.md`
- `future_modules/the_fade/docs/CANON_INDEX.md`
- `future_modules/the_fade/docs/THE_FADE_PHASE0_FINAL_LOCK.md`
- `future_modules/the_fade/docs/THE_FADE_PHASE0_FINAL_LOCK_ATTESTATION.md`
- Phase 1 schemas:
  - `future_modules/the_fade/schemas/fade_task_packet.schema.json`
  - `future_modules/the_fade/schemas/scanner_candidate_set.schema.json`
  - `future_modules/the_fade/schemas/normalized_signal_event.schema.json`
  - `future_modules/the_fade/schemas/lane_scorecard.schema.json`
  - `future_modules/the_fade/schemas/contra_signal_result.schema.json`
  - `future_modules/the_fade/schemas/signal_packet.schema.json`
  - `future_modules/the_fade/schemas/conflict_packet.schema.json`
  - `future_modules/the_fade/schemas/scout_failure.schema.json`

## Lock authority truth (do not override)

Use `future_modules/the_fade/docs/THE_FADE_PHASE0_FINAL_LOCK.md` as the execution-control lock for this module, plus:
- the eight `JARVIS_THE_FADE_*.md` canon files
- build order in `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`

## What must not be touched yet

- Phase 2 gate-prep artifacts exist but approval is not granted yet:
  - `future_modules/the_fade/config/mvp_lane_approval.json` exists with `approved: false`
  - `future_modules/the_fade/config/mvp_lane_approval.json` has no MVP lanes approved yet (`approved_mvp_lanes` is empty)
  - `future_modules/the_fade/docs/MVP_SOURCE_RELIABILITY_AUDIT.md` exists as the operator pre-audit
- Operator decision recorded in `mvp_lane_approval.json`: defer approval; gather lane-level evidence before any approval change.
- Do not start any runtime/scanner/dashboard-contract work in this pass.
- No dashboard implementation and no `dashboard_contract/`.
- No heartbeat schema/code for Tranches 1–3.

## Exact next step (current)

Start MASTER Phase 2 / Tranche 2:
1. Gather/record lane-level reliability/freshness/normalization and stale/outage evidence against `future_modules/the_fade/docs/MVP_SOURCE_RELIABILITY_AUDIT.md` (keep `approved:false` during evidence collection).
2. When evidence meets the gate standard, update `future_modules/the_fade/config/mvp_lane_approval.json` from `approved: false` to `approved: true` (populate `approved_by` + `approved_at` and the chosen MVP lanes).
3. After gate approval, update `future_modules/the_fade/config/lane_registry.json` + `future_modules/the_fade/config/escalation_policy.json` to match the approved MVP lane set.


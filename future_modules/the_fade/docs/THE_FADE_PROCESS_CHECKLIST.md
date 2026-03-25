# THE FADE Process Checklist

**Prompt #:** 13  
**Phase #:** 1  
**Tranche #:** 1  

Updated: 2026-03-25T09:02:37.6307666-05:00

## Current state

- Phase 1 / Tranche 1: **DONE**
  - Scout-layer foundation contracts created (schemas, config registries, examples)
  - Phase 0 final lock + attestation are present and govern execution for this module
  - No Phase 2+ implementation is started
- Phase 2 / Tranche 2 gate prep exists; operator recorded a deferred decision (`approved:false`), so no MVP lanes are approved yet.
- Phase 2 / Tranche 3 evidence pack exists for operator evidence collection; approval is still not granted.

## Bounded phase ladder (from here)

## MASTER Phase 2 — Scout MVP data stack and pre-audit
- Tranche 2: **NEXT**
- Must complete before any Tranche 3 runner work:
  - operator must decide the MVP lane gate in `future_modules/the_fade/config/mvp_lane_approval.json` and set `approved: true` (fill `approved_by` + `approved_at`)
  - only after the gate is approved, update `future_modules/the_fade/config/lane_registry.json` and `future_modules/the_fade/config/escalation_policy.json` to reflect the approved MVP lanes

## MASTER Phase 3 — Universe scanner
- Tranche 3: **NOT STARTED**
- Scanner implementation comes only after Phase 2 approval and audit are done.

## MASTER Phase 4+ — Out of scope for this handoff
- Not started; no action in this pass.

## Exact current next step (recorded)

Start MASTER Phase 2 / Tranche 2:
1. Gather/record lane-level reliability/freshness/normalization and stale/outage evidence against `future_modules/the_fade/docs/MVP_SOURCE_RELIABILITY_AUDIT.md`.
2. Use `future_modules/the_fade/config/mvp_lane_evidence_registry.json` and `future_modules/the_fade/docs/MVP_LANE_EVIDENCE_LOG.md` as the evidence-tracking authorities while keeping `approved:false`.
3. When evidence meets the gate standard, update `future_modules/the_fade/config/mvp_lane_approval.json` from `approved: false` to `approved: true` (populate `approved_by` + `approved_at` and the chosen MVP lanes).
4. After gate approval, update `future_modules/the_fade/config/lane_registry.json` + `future_modules/the_fade/config/escalation_policy.json` to match the approved MVP lane set.


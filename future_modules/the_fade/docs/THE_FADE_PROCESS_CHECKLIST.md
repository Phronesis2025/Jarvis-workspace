# THE FADE Process Checklist

**Prompt #:** 30  
**Phase #:** 2  
**Tranche #:** 8  

Updated: 2026-03-25T11:03:06.8869312-05:00

## Current state

- Phase 1 / Tranche 1: **DONE**
  - Scout-layer foundation contracts created (schemas, config registries, examples)
  - Phase 0 final lock + attestation are present and govern execution for this module
  - No Phase 2+ implementation is started
- Phase 2 / Tranche 2 gate prep exists; operator recorded a deferred decision (`approved:false`), so no MVP lanes are approved yet.
- Phase 2 / Tranche 3 evidence pack exists for operator evidence collection; approval is still not granted.
- Phase 2 / Tranche 4: lane B evidence is in-progress (partial). Stale/outage behavior and context-dominance risk are now recorded as partial, but approval is still not granted.

## Bounded phase ladder (from here)

## MASTER Phase 2 — Scout MVP data stack and pre-audit
- Tranche 8: **NEXT**
- Must complete before any Tranche 3 runner work:
  - operator must decide the MVP lane gate in `future_modules/the_fade/config/mvp_lane_approval.json` and set `approved: true` (fill `approved_by` + `approved_at`)
  - only after the gate is approved, update `future_modules/the_fade/config/lane_registry.json` and `future_modules/the_fade/config/escalation_policy.json` to reflect the approved MVP lanes

## MASTER Phase 3 — Universe scanner
- Tranche 3: **NOT STARTED**
- Scanner implementation comes only after Phase 2 approval and audit are done.

## MASTER Phase 4+ — Out of scope for this handoff
- Not started; no action in this pass.

## Exact current next step (recorded)

Continue MASTER Phase 2 / evidence collection (Tranche 8):
1. Record, for `lane_b_official_disclosure` only:
   - `stale_outage_behavior`: an explicit controlled stale/unavailable incident replay with timestamps and observed downgrade/escalation/omit behavior outcomes
   - `context_dominance_risk`: adversarial/conflict-case evidence proving context-only enrichment never gains precedence over `lane_b_official_disclosure` primary truth under gate conditions
   - protocol reference: `docs/MVP_LANE_EVIDENCE_LOG.md` → “Lane B controlled evidence protocol (operator checklist)”
2. Keep `future_modules/the_fade/config/mvp_lane_approval.json` unchanged (`approved:false`) until the operator determines the evidence meets the gate standard.


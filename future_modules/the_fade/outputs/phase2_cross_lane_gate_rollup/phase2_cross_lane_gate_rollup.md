# Tranche 36 — Phase 2 cross-lane gate dimension rollup

**Not approval.** This is a visibility rollup only. It does not change `mvp_lane_approval.json` and does not unlock Phase 3.

## Grounded lanes

- `lane_a_public_signal`
- `lane_b_official_disclosure`
- `lane_c_market_context`
- `lane_e_research_swarm_context`

## Gate-dimension matrix

| Lane | reliability | freshness | normalization_viability | stale_outage_behavior | conflict_handling | context_dominance_risk | overall_approval_readiness | Biggest blocker |
|---|---|---|---|---|---|---|---|---|
| `lane_a_public_signal` | absent | absent | absent | absent | absent | absent | not yet justified | No lane-level gate evidence stack built yet; lane remains deferred. |
| `lane_b_official_disclosure` | partial | partial | partial | partial | partial | partial | not yet justified | Cross-dimension closure missing: freshness remains 10/22 cannot_classify_honestly; normalization breadth partial; stale/outage still thin for standard #4. |
| `lane_c_market_context` | absent | absent | absent | absent | absent | absent | not yet justified | No lane-level gate evidence stack built yet; lane remains deferred. |
| `lane_e_research_swarm_context` | absent | absent | absent | absent | absent | absent | not yet justified | Context-only non-domination evidence at gate bar is not built; lane remains deferred. |

## Lane B depth note

- Lane B is the furthest along, but still **partial** across multiple dimensions and **not yet justified** for approval.
- Tranche 35 stale/outage headline: `dimension_still_thin_for_standard_#4_if_restricted_to_FR_full-window_slice`

## Docs/config disagreement noted

- `mvp_lane_evidence_registry.json` lane_b status fields are older than Tranche 31-35 docs; rollup uses newer doc truth while keeping lane list/dimensions from config.

## Output

- JSON: `phase2_cross_lane_gate_rollup.json`
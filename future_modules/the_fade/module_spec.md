# THE FADE — module specification (scout)

**Prompt #:** 5  
**Phase #:** 1  
**Tranche #:** 1  
Updated: 2026-03-25T08:27:13.5370442-05:00

## Purpose

Define machine-readable **scout** artifacts: task packets, scanner output, normalized events, lane scorecards, contra results, signal packets, conflict packets, failures; plus registries and policy JSON consumed by later phases. Align with `JARVIS_THE_FADE_SIGNAL_ENGINE_SPEC.md` and `JARVIS_THE_FADE_ARCHITECTURE_AND_STORAGE_SPEC.md` (paths: `docs/CANON_INDEX.md`).

## Boundaries (in)

- Schemas under `schemas/` for scout-layer packets and failures  
- Config under `config/` for lanes, direction models (v2 posture), fusion thresholds/weights (**initial defaults**), scanner policy shell, escalation mapping, safety governor **manual-only** baseline  
- Examples under `examples/` proving schema validity  

## Boundaries (out)

- Research brief, risk gate, paper trades, portfolio, daily summaries, learning reports  
- Live or paper execution, broker adapters  
- Dashboard UI and `dashboard_contract/` (gated by Phase 0 lock §3.3)  
- Heartbeat schema and heartbeat metrics code in Tranches 1–3 (see below)  
- MVP vendor/provider lock — **Phase 2** after `mvp_lane_approval.json` is approved (`approved: true`)  

## Inputs (conceptual)

- **fade_task_packet** — one unit of scout work (future: from scanner or operator)  
- Raw lane evidence (future adapters)  
- Policy/registries in `config/`  

## Outputs (conceptual)

- **scanner_candidate_set** (Phase 3 runner)  
- **normalized_signal_event** sets (Phase 4+)  
- **lane_scorecard**, **contra_signal_result** (Phases 5–6)  
- **signal_packet**, **conflict_packet** (Phase 7)  
- **scout_failure** when a stage records structured failure  

## Non-goals

- No “helpful” extra lanes or sources beyond canon MVP posture until Phase 2 approval  
- No pretending downstream artifacts are scout outputs  

## Heartbeat monitor (deferred)

Alpha/Beta heartbeat, failover, and heartbeat production metrics are **out of scope** until **MASTER Phase 13** (hardening), per `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md` and normative intent in `JARVIS_THE_FADE_SIGNAL_ENGINE_SPEC.md` §20 (path: `docs/CANON_INDEX.md`).

**Tranches 1–3:** There is **no** `schemas/scout_heartbeat.schema.json`, **no** heartbeat-specific config files, and **no** heartbeat metrics code in this module. Satisfying MASTER Phase 1 “placeholder” wording is **documentation-only** (this subsection).

## Config alias

`config/fusion_policy.json` is the **threshold/weight policy registry** (single file; no duplicate registry filename).

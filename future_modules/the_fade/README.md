# THE FADE (scout module)

**Prompt #:** 5  
**Phase #:** 1  
**Tranche #:** 1  

## What this is

**THE FADE** is the **scout-layer** worker for multi-source signal intelligence in Jarvis: candidates in, normalized evidence, lane scoring, contra checks, fusion, **signal_packet** / **conflict_packet** out. It is **not** the full product stack (research brief, risk gate, paper trading, daily summary, learning, autonomy, live execution live elsewhere in canon).

## Active execution control

- **Lock:** `docs/THE_FADE_PHASE0_FINAL_LOCK.md`  
- **Design canon:** eight `JARVIS_THE_FADE_*.md` files — paths in `docs/CANON_INDEX.md`  
- **Build order:** `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md` (path per CANON_INDEX)

## Current phase / tranche

**MASTER Phase 1 — Scout contracts and policy foundations (Tranche 1).**  
This folder contains schemas, baseline config, examples, and docs only. **No runners,** no scanner script, no adapters, no dashboard UI.

## Explicitly deferred (not in this tranche)

- Phase 2: `mvp_lane_approval.json`, `deferred_sources.json`, `MVP_SOURCE_RELIABILITY_AUDIT.md`, named MVP vendors in registry/audit  
- Phase 3: `scripts/run_universe_scan.py`, `outputs/scanner/`  
- `dashboard_contract/`, any `dashboard/` routes for FADE  
- `schemas/scout_heartbeat.schema.json`, heartbeat metrics code (through Tranche 3)  
- `tasks/`, `state/`, `outputs/failures/`, `logs/` until a committed consumer exists  
- Downstream analyst pipeline, paper trading, daily summaries — per canon, not scout identity

## Manual-first

Scripts and automation come in later phases. This tranche is **contracts + policy shells + examples** only.

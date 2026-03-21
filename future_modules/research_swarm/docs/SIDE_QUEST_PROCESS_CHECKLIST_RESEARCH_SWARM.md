# Research Swarm — Side Quest Process Checklist

**Last updated:** 2026-03-21  
**Current phase:** Phase A — Unattended bounded collector

---

## Current Status

| Item | Status |
|------|--------|
| Phase A collector | Implemented, smoke-proven |
| URL list input | Supported |
| Bounded discovery input | Supported |
| Skip/log restricted | Implemented |
| Skip/log unsupported | Implemented |
| Cumulative ledger | Implemented |
| Hourly ops path | Implemented (no-overlap) |
| Dashboard review page | Implemented — `/research-swarm` (R55) |
| Evaluator / Archivist | Manual |

---

## Current Phase

**Phase A — Unattended bounded collector**

- Runs on operator URL list + optional bounded discovery
- Merges, dedups, classifies (GitHub, article, unsupported video/other)
- Skips restricted/paywalled articles; logs
- Skips unsupported sources; logs
- Continues after per-item failures
- Writes run summary JSON + MD; appends to ledger
- Hourly scheduling supported via ops scripts (lock-based no-overlap)

---

## Completed Items

- [x] Phase A collector entrypoint (`run_phase_a_collector.py`)
- [x] Bounded discovery query file support
- [x] Skip/log restricted articles
- [x] Skip/log unsupported sources
- [x] Durable run summary + ledger
- [x] Ops scripts (run once, register hourly)
- [x] Smoke test passed
- [x] Extractor API v1 (QUALIFIED PASS)
- [x] Discovery (GitHub + article)
- [x] Acquisition (GitHub + article)
- [x] Broader corpus eval (real list)
- [x] Dashboard Research Swarm page (R55)

---

## Deferred Items

- Video/transcript acquisition
- Evaluator API automation
- Archivist API automation
- Jarvis export/orchestration (dashboard has read-only Research Swarm page)
- Broad production trust

---

## What Is Now Allowed

- Phase A unattended collection (bounded)
- Operator URL list + optional discovery
- Hourly scheduled runs (no-overlap)
- Human review of collected output mandatory

---

## What Is Still NOT Allowed

- Evaluator automation
- Archivist automation
- Video/X/Twitter/Reddit support
- Jarvis integration claims
- Broad autonomous research judgment

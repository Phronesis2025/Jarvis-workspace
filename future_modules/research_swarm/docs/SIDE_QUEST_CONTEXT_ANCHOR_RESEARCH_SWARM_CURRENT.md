# Research Swarm — Side Quest Context Anchor

**Last updated:** 2026-03-21  
**Purpose:** New-chat handoff anchor for Research Swarm continuation work.  
**R55:** Dashboard Research Swarm review page added at `/research-swarm`.

---

## What This Side Quest Is

- **Research Swarm** — planned Jarvis input-learning engine
- Transforms raw research sources (GitHub, article/webpage) into structured knowledge for evaluation and archiving
- **Phase A:** Unattended bounded collector — runs on operator URL list + optional bounded discovery; writes run summary + cumulative ledger
- **Extractor API v1** — scaffold hardened, QUALIFIED PASS (bounded assistive drafting)
- **Discovery / Intake** — implemented for GitHub + generic article/webpage
- **Content Acquisition** — implemented for GitHub + generic article/webpage
- **Single-run automation** — `run_pipeline.py` (operator-triggered)
- **Batch runner** — `run_batch.py` (up to 10 runs)
- **Broader corpus eval** — `run_broader_corpus_eval.py` (uses operator URL list)
- Human review still mandatory after collection
- Evaluator and archivist remain manual

---

## What This Side Quest Is Not

- Not an active Jarvis runtime module
- Not integrated with Jarvis Dashboard, export, or orchestration
- Not evaluator or archivist API automation
- Not video/X/Twitter/Reddit source support
- Not broad production trust (collector is bounded, for learning)

---

## Current Maturity / Status

| Label | Status |
|-------|--------|
| **Phase A collector** | Implemented — unattended bounded collection |
| **Extractor API v1** | QUALIFIED PASS — bounded assistive drafting |
| **Discovery** | Implemented — GitHub + article/webpage |
| **Acquisition** | Implemented — GitHub + article/webpage |
| **Supported sources** | GitHub + article/webpage only |
| **Dashboard review page** | Yes — `/research-swarm` reads summary + ledger |
| **Integrated with Jarvis export** | No |
| **Human review** | Mandatory |
| **Evaluator / Archivist** | Manual |
| **Scheduling** | Hourly possible via ops scripts (no-overlap) |

---

## Exact Workspace Paths

| Role | Path |
|------|------|
| Module root | `future_modules/research_swarm/` |
| Scripts | `future_modules/research_swarm/scripts/` |
| Outputs | `future_modules/research_swarm/outputs/` |
| Examples | `future_modules/research_swarm/examples/` |
| Ops | `future_modules/research_swarm/ops/` |
| Docs | `future_modules/research_swarm/docs/` |

---

## Phase A Collector

| File | Purpose |
|------|---------|
| `scripts/run_phase_a_collector.py` | Main entrypoint: URL list + optional discovery → collect → ledger |
| `examples/phase_a_discovery_queries.json` | Bounded discovery query file |
| `examples/phase_a_smoke_urls.txt` | Smoke-test URL subset |
| `ops/run_phase_a_collector_once.ps1` | Run once (no-overlap lock) |
| `ops/register_phase_a_hourly_task.ps1` | Register hourly scheduled task |
| `outputs/phase_a_collection_ledger.jsonl` | Cumulative per-item ledger |
| `outputs/phase_a_run_summary_*.json` | Per-run summary |

---

## Current Direction

- **Phase A focus:** Unattended bounded collector for durable collection data
- Runs on operator URL list + optional bounded discovery
- Scheduling goal: hourly, no overlap
- **Collection review:** Files (summary JSON/MD, ledger) + dashboard page `/research-swarm`
- Primary bottleneck: **extraction schema** (LLM enum drift) and restricted/paywalled skips
- Purpose: gather durable collection data for later human review and learning

---

## Known Weakness Profile

- **Acquisition reliability:** Restricted/paywalled articles (e.g. Medium HTTP 403) — skip/log
- **Extraction schema:** LLM sometimes outputs category values outside enum (strategy, agent vs method/tool/pattern)
- **Video/X/Twitter/Reddit:** Not supported; classified and skipped
- **Evaluator/archivist:** Manual; no automation

---

## Locked Constraints

- Manual review gate remains mandatory
- No evaluator/archivist automation in scope
- No video/X/Twitter/Reddit support
- Schema contracts preserved
- Collector is bounded; no broad autonomous research judgment

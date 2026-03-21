# Research Swarm — Side Quest Handoff Bundle

**Last updated:** 2026-03-21  
**Purpose:** New-chat handoff for continuing Research Swarm work. Attach to new chat for context continuity.  
**R55:** Dashboard Research Swarm page at `/research-swarm`; reads `phase_a_run_summary_*.json` + `phase_a_collection_ledger.jsonl`.

---

## Current Live Truth Summary

- **Research Swarm** — prototype input-learning engine in `future_modules/research_swarm/`
- **Phase A:** Unattended bounded collector — runs on operator URL list + optional discovery; writes run summary + ledger
- **Supported sources:** GitHub + article/webpage only
- **Current bottleneck:** Extraction schema (LLM enum drift) and restricted/paywalled skips
- **Evaluator and archivist remain manual**
- **Dashboard:** Research Swarm review page at `/research-swarm` (reads summary + ledger)
- **Not integrated with Jarvis export/orchestration**
- **Human review mandatory** after collection
- **Scheduling:** Hourly possible via ops scripts (no-overlap)

---

## Critical File List

| File | Path | Why It Matters |
|------|------|----------------|
| Context anchor | `future_modules/research_swarm/docs/SIDE_QUEST_CONTEXT_ANCHOR_RESEARCH_SWARM_CURRENT.md` | What this quest is, Phase A focus |
| Process checklist | `future_modules/research_swarm/docs/SIDE_QUEST_PROCESS_CHECKLIST_RESEARCH_SWARM.md` | Done/active/deferred |
| Phase A collector | `future_modules/research_swarm/scripts/run_phase_a_collector.py` | Main collector entrypoint |
| Ops run once | `future_modules/research_swarm/ops/run_phase_a_collector_once.ps1` | Run collector with no-overlap |
| Ops register hourly | `future_modules/research_swarm/ops/register_phase_a_hourly_task.ps1` | Register hourly task |
| Example URLs | `future_modules/research_swarm/docs/Example URLs.txt` | Operator real URL list |
| Discovery queries | `future_modules/research_swarm/examples/phase_a_discovery_queries.json` | Bounded discovery input |
| Ledger | `future_modules/research_swarm/outputs/phase_a_collection_ledger.jsonl` | Cumulative collection ledger |
| Dashboard page | `dashboard/src/app/research-swarm/page.tsx` | Research Swarm review (R55) |
| Extractor API | `future_modules/research_swarm/scripts/run_extractor_api.py` | Extraction CLI |

---

## Run Commands

### Phase A collector (once)

```
cd future_modules/research_swarm/scripts
python run_phase_a_collector.py --urls-file ../docs/Example URLs.txt
```

With discovery:

```
python run_phase_a_collector.py --urls-file ../docs/Example URLs.txt --queries-file ../examples/phase_a_discovery_queries.json
```

### Ops (Windows PowerShell)

```
cd future_modules/research_swarm/ops
.\run_phase_a_collector_once.ps1
```

Register hourly (run as Administrator):

```
.\register_phase_a_hourly_task.ps1
```

---

## Module Integration Status

| Label | Status |
|-------|--------|
| Phase A collector | Yes — bounded unattended |
| Dashboard review page | Yes — `/research-swarm` |
| Integrated with Jarvis export | No |
| Human review mandatory | Yes |
| Video/X/Twitter/Reddit | Not supported |

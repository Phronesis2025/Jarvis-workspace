# Research Swarm — Side Quest Handoff Bundle

**Last updated:** 2026-03-20  
**Purpose:** New-chat handoff for continuing Research Swarm work. Attach to new chat for context continuity.

---

## Bundle Purpose

This bundle provides the minimum context for a new chat to continue Research Swarm work without re-discovering the module. It does not replace the full canon docs (JARVIS_LIVE_HANDOFF_BUNDLE, etc.) but supplements them for this side quest.

---

## Current Live Truth Summary

- **Research Swarm** is a prototype input-learning engine in `future_modules/research_swarm/`
- **Manual flow proven:** source packet → extract → evaluate → archive (2 full runs)
- **Extractor API v1** — QUALIFIED PASS; bounded assistive drafting; human must supplement
- **Discovery first build** — implemented, GitHub-only, freshness-aware ranking
- **Acquisition first build** — implemented, GitHub-only
- **End-to-end GitHub pipeline proof passed** — discovery → acquisition → extraction
- **Current allowed use:** full GitHub pipeline; local/operator-reviewed; human review mandatory
- **Current limitations:** GitHub-only source support; thin-source sensitivity; evaluator/archivist manual
- **Not integrated with Jarvis** — no dashboard, no export, no orchestration

---

## Critical File List

| File | Path | Why It Matters |
|------|------|----------------|
| Context anchor | `SIDE_QUEST_CONTEXT_ANCHOR_RESEARCH_SWARM_CURRENT.md` | What this quest is, current direction (workspace root) |
| Process checklist | `SIDE_QUEST_PROCESS_CHECKLIST_RESEARCH_SWARM.md` | Completed items, active position (workspace root) |
| Pipeline proof note | `future_modules/research_swarm/outputs/github_pipeline_proof_note.md` | End-to-end proof summary |
| Discovery queue (proof) | `future_modules/research_swarm/outputs/discovery_queue_20260321-040543.json` | Proof run — discovery output |
| Source packet (proof) | `future_modules/research_swarm/outputs/source_packet_20260321-040550.json` | Proof run — acquisition output |
| Extraction report (proof) | `future_modules/research_swarm/outputs/extraction_report_20260321-040550_api.json` | Proof run — extraction output |
| Stage decision | `future_modules/research_swarm/outputs/extractor_api_stage_decision.md` | QUALIFIED PASS; allowed vs not |
| Discovery runner | `future_modules/research_swarm/scripts/run_discovery.py` | Discovery CLI |
| Acquisition runner | `future_modules/research_swarm/scripts/run_acquisition.py` | Acquisition CLI |
| Extractor runner | `future_modules/research_swarm/scripts/run_extractor_api.py` | Extractor CLI |
| Module spec | `future_modules/research_swarm/module_spec.md` | Purpose, scope, non-goals |

---

## Important Files — Tight Summary

### Full GitHub Pipeline

```
# 1. Discovery
python future_modules/research_swarm/scripts/run_discovery.py --query "your query"

# 2. Acquisition (pick URL from discovery queue)
python future_modules/research_swarm/scripts/run_acquisition.py --url <github_url>

# 3. Extraction
python future_modules/research_swarm/scripts/run_extractor_api.py --packet <packet_path>
```

- **Status:** Proven end-to-end for GitHub
- **Scope:** Bounded assistive drafting; human review mandatory
- **Source support:** GitHub only

### Review Gate Outcomes

- **PASS** → proceed to evaluator (manual)
- **REVISE** → retry API or minor edit
- **REJECT** → fall back to manual extraction

---

## Files Intentionally Excluded

- Full JARVIS canon — reference as needed
- Pathfinder, WCS, n8n, dashboard — out of scope
- Duplicate copies under `future_modules/research_swarm/docs/` — not canonical side-quest artifacts

---

## Suggested First Files to Inspect

1. `SIDE_QUEST_CONTEXT_ANCHOR_RESEARCH_SWARM_CURRENT.md` (workspace root)
2. `future_modules/research_swarm/outputs/github_pipeline_proof_note.md`
3. `future_modules/research_swarm/outputs/discovery_queue_20260321-040543.json`
4. `future_modules/research_swarm/outputs/source_packet_20260321-040550.json`
5. `future_modules/research_swarm/outputs/extraction_report_20260321-040550_api.json`
6. `future_modules/research_swarm/scripts/run_discovery.py`
7. `future_modules/research_swarm/scripts/run_acquisition.py`

---

## Module Integration Status

| Label | Status |
|-------|--------|
| Concept only | No — designed and proven |
| Design-only | No — manual flow + pipeline proven |
| Implementation started | Yes — discovery, acquisition, extractor |
| Partially proven | Yes — manual flow + API assistive drafting |
| Bounded GitHub pipeline | Yes — discovery → acquisition → extraction proven |
| Locally operational | Yes — for bounded GitHub pipeline |
| Human review mandatory | Yes |
| Not integrated with Jarvis | Yes |
| Integrated with Jarvis | No |
| Safe for unattended use | No |

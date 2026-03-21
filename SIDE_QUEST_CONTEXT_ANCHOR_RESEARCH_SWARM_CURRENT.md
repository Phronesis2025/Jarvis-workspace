# Research Swarm — Side Quest Context Anchor

**Last updated:** 2026-03-20  
**Purpose:** New-chat handoff anchor for Research Swarm continuation work.

---

## What This Side Quest Is

- **Research Swarm** — planned Jarvis input-learning engine
- Transforms raw research sources (YouTube, Reddit, GitHub) into structured, evaluated knowledge
- Manual flow: source packet → extract → evaluate → archive
- **Extractor API v1** — scaffold hardened, QUALIFIED PASS (bounded assistive drafting)
- **Discovery / Intake** — first build implemented, GitHub-only, freshness-aware
- **Content Acquisition** — first build implemented, GitHub-only
- **First bounded end-to-end GitHub pipeline proof passed** (discovery → acquisition → extraction)
- Evaluator and archivist remain manual

---

## What This Side Quest Is Not

- Not an active Jarvis runtime module
- Not integrated with Jarvis Dashboard, export, or orchestration
- Not evaluator or archivist API automation
- Not a one-line command wrapper
- Not safe for unattended use
- Not broad source-class support yet (GitHub-only for discovery + acquisition)

---

## Current Maturity / Status

| Label | Status |
|-------|--------|
| **Manual flow proven** | Yes — two end-to-end runs with archive entries |
| **Extractor API v1** | QUALIFIED PASS — bounded assistive drafting |
| **Discovery first build** | Implemented — GitHub-only, freshness-aware |
| **Acquisition first build** | Implemented — GitHub-only |
| **End-to-end GitHub pipeline** | Proven — discovery → acquisition → extraction |
| **Integrated with Jarvis** | No |
| **Human review** | Mandatory |
| **Source support** | GitHub only (discovery + acquisition) |

---

## Exact Workspace Paths

| Role | Path |
|------|------|
| Module root | `C:\dev\jarvis-workspace\future_modules\research_swarm\` |
| Schemas | `future_modules/research_swarm/schemas/` |
| Prompts | `future_modules/research_swarm/prompts/` |
| Scripts | `future_modules/research_swarm/scripts/` |
| Outputs | `future_modules/research_swarm/outputs/` |
| Docs | `future_modules/research_swarm/docs/` |

---

## Related Module Files

| File | Purpose |
|------|---------|
| `future_modules/research_swarm/module_spec.md` | Module purpose, scope, non-goals |
| `future_modules/research_swarm/README.md` | Current v1 role set, operating stance |
| `future_modules/research_swarm/scripts/run_discovery.py` | Discovery CLI — GitHub search |
| `future_modules/research_swarm/scripts/run_acquisition.py` | Acquisition CLI — GitHub packet generation |
| `future_modules/research_swarm/scripts/run_extractor_api.py` | Extractor API CLI entry point |
| `future_modules/research_swarm/outputs/github_pipeline_proof_note.md` | End-to-end GitHub pipeline proof summary |
| `future_modules/research_swarm/outputs/extractor_api_stage_decision.md` | Side-by-side stage decision (QUALIFIED PASS) |

---

## Current Direction

- **Post-pipeline-proof / bounded quality-tightening or broadening decision**
- Extractor API v1 remains qualified-pass assistive
- GitHub-only upstream pipeline proven
- Human review remains mandatory
- Evaluator and archivist remain manual
- Not integrated with Jarvis

---

## Known Weakness Profile

- **Source support:** GitHub-only for discovery and acquisition
- **Thin-source sensitivity:** Extraction quality depends on source richness
- **Extractor API:** Generic methods/patterns, thinner key claims, abstract open questions
- **Not unattended:** Human review mandatory
- **No broader source-class support yet** (YouTube, Reddit, article deferred)

---

## Locked Constraints

- Manual review gate remains mandatory
- Manual extraction is fallback at all times
- No evaluator/archivist automation in scope
- No unattended use; no broad production trust
- Schema contracts preserved; no drift

---

## What the Next Chat Should Do First

1. Read `SIDE_QUEST_HANDOFF_BUNDLE_RESEARCH_SWARM_LATEST.md` (workspace root)
2. Inspect `future_modules/research_swarm/outputs/github_pipeline_proof_note.md`
3. Inspect proof artifacts: discovery queue, acquired packet, extraction report from proof run
4. Decide next bounded move:
   - **Option A:** Tighten GitHub pipeline quality (completeness labeling, thin-content handling, candidate filtering)
   - **Option B:** Explicitly decide whether to broaden source support after tightening

Do not assume broader activation. The next step is the smallest bounded move.

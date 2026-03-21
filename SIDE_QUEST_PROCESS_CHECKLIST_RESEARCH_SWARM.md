# Research Swarm — Side Quest Process Checklist

**Last updated:** 2026-03-20  
**Current phase:** Post-pipeline-proof / bounded quality-tightening or broadening decision

---

## Current Status

| Item | Status |
|------|--------|
| Manual flow | Proven (2 runs) |
| Extractor API v1 | Implemented, hardened, QUALIFIED PASS |
| API vs manual comparison | Completed — first_run and second_run SOFT PASS |
| Stage decision | Completed — QUALIFIED PASS |
| Discovery first build | Completed — GitHub-only, freshness-aware |
| Acquisition first build | Completed — GitHub-only |
| GitHub-only contract correction | Completed — article deferred |
| End-to-end GitHub pipeline proof | Completed — PASS |

---

## Current Phase

**Post-pipeline-proof — bounded quality-tightening or broadening decision**

- Bounded upstream GitHub pipeline (discovery → acquisition → extraction) proven
- Human review mandatory
- Next: tighten quality rules, or decide whether to broaden source support

---

## Exact Process Position

- Extraction layer: **complete** (runner, client, validator, smoke test, comparison, stage decision)
- Discovery layer: **complete** — first build, GitHub-only
- Acquisition layer: **complete** — first build, GitHub-only
- End-to-end GitHub pipeline: **proven**
- **Active position:** Post-pipeline-proof; decide quality tightening vs broadening

---

## Completed Items

- [x] Schemas defined (source_intake, extraction_report, evaluation_report, knowledge_archive_entry)
- [x] Prompts defined (extractor, evaluator, archivist)
- [x] Decision rules documented (KNOWLEDGE_ARCHIVE_DECISION_RULES.md)
- [x] First manual run (narrative/operator-style source)
- [x] Second manual run (technical/API-style source)
- [x] Extractor API v1 implementation and stage decision (QUALIFIED PASS)
- [x] Discovery first build (GitHub-only, freshness-aware)
- [x] Acquisition first build (GitHub-only)
- [x] GitHub-only contract correction (article deferred)
- [x] End-to-end GitHub pipeline proof

---

## Current Active Items

- [ ] Operator decision: quality-tightening pass vs broaden source support

---

## Deferred Items

- Evaluator API integration
- Archivist API integration
- Broader source-class discovery (YouTube, Reddit, article)
- Broader source-class acquisition (article when schema supports)
- Jarvis integration (dashboard, export, orchestration)
- Scheduling or background runs
- Unattended use
- Broad production trust

---

## What Is Now Allowed

- API-assisted extraction drafting in local/operator-reviewed use
- Full GitHub pipeline: discovery → acquisition → extraction
- Use API output as starting draft; human adds missing signal
- Manual review before evaluator step
- GitHub-only upstream pipeline for bounded research

---

## What Is Still NOT Allowed

- Unattended or unsupervised use
- Evaluator automation
- Archivist automation
- Removal of human review
- Jarvis integration claims
- Broad production trust
- Broader source-class discovery/acquisition without explicit decision

---

## Proof Labels

| Artifact | Proof |
|----------|-------|
| Manual run 1 | Proven — archive entry created |
| Manual run 2 | Proven — archive entry created |
| Extractor API v1 | QUALIFIED PASS; bounded assistive drafting |
| Discovery first build | Implemented; GitHub-only; freshness-aware |
| Acquisition first build | Implemented; GitHub-only |
| End-to-end GitHub pipeline | Proven — discovery → acquisition → extraction |

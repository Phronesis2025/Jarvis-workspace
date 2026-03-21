# Research Swarm — Side Quest Process Checklist

**Last updated:** 2026-03-20  
**Current phase:** Post-validation / bounded-quality-improvement-or-hold

---

## Current Status

| Item | Status |
|------|--------|
| Manual flow | Proven (2 runs) |
| Extractor API v1 scaffolding | Implemented, hardened |
| Extractor API smoke test | Completed — passed on second_run |
| API vs manual baseline comparison | Completed — second_run SOFT PASS |
| Rollout stage decision | Completed — QUALIFIED PASS |
| Second-source validation | Completed — first_run SOFT PASS |

---

## Current Phase

**Post-validation — bounded quality improvement or hold**

- API v1 is locally operational for assistive drafting
- Human review mandatory
- Known weaknesses documented
- Next: prompt-tuning for patterns/claims, or operator decision to hold

---

## Exact Process Position

- Build sequence steps 1–11: **complete** (runner, client, validator, smoke test, comparison, stage decision, second-source validation)
- **Active position:** Post-validation; decide whether to tune prompts or hold at qualified-pass status

---

## Completed Items

- [x] Schemas defined (source_intake, extraction_report, evaluation_report, knowledge_archive_entry)
- [x] Prompts defined (extractor, evaluator, archivist)
- [x] Decision rules documented (KNOWLEDGE_ARCHIVE_DECISION_RULES.md)
- [x] First manual run (narrative/operator-style source)
- [x] Second manual run (technical/API-style source)
- [x] Extractor API spec, review gate, failure modes documented
- [x] Extractor API v1 implementation plan
- [x] Extractor API v1 build packet
- [x] `run_extractor_api.py` entry point
- [x] `extractor_api_client.py` OpenAI client
- [x] `extractor_api_validate.py` schema validator
- [x] Extractor API scaffold hardening
- [x] Production source packets repaired (valid JSON)
- [x] First real smoke path (second_run)
- [x] API vs manual comparison (second_run)
- [x] Stage decision (QUALIFIED PASS)
- [x] Second-source validation (first_run)

---

## Current Active Items

- [ ] Operator decision: prompt-tuning pass vs leave at qualified-pass status

---

## Deferred Items

- Transcript acquisition automation
- Evaluator API integration
- Archivist API integration
- One-line command wrapper
- Jarvis integration (dashboard, export, orchestration)
- Scheduling or background runs
- Unattended use
- Broad production trust

---

## What Is Now Allowed

- API-assisted extraction drafting in local/operator-reviewed use
- Run against repaired production packets
- Use API output as starting draft; human adds missing signal
- Manual review before evaluator step

---

## What Is Still NOT Allowed

- Unattended or unsupervised use
- Evaluator automation
- Archivist automation
- Removal of human review
- Jarvis integration claims
- Broad production trust

---

## Before v1 (Extractor API Default)

- Repeated schema-valid outputs
- Acceptable similarity to manual baseline
- No repeated fabrication issues
- Operator trust threshold met
- Clear fallback working
- Quality improvement on known weakness profile

---

## Before Integration with Jarvis

- Extractor API v1 proven as default with review gate
- Transcript acquisition at least partially automated
- Clear handoff contract for archive entries to other modules

---

## Before "Live with Jarvis"

- Module invoked by Jarvis orchestration
- Outputs consumed by dashboard or other modules
- Not the current state

---

## Proof Labels

| Artifact | Proof |
|----------|-------|
| Manual run 1 | Proven — archive entry created |
| Manual run 2 | Proven — archive entry created |
| Extractor API v1 | Smoke-proven locally; QUALIFIED PASS |
| API output quality | Proven as bounded assistive drafting; thinner than manual baseline |

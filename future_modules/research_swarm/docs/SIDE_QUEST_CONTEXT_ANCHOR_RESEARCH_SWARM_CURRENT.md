# Research Swarm — Side Quest Context Anchor

**Last updated:** 2026-03-20  
**Purpose:** New-chat handoff anchor for Research Swarm continuation work.

---

## What This Side Quest Is

- **Research Swarm** — planned Jarvis input-learning engine
- Transforms raw research sources (YouTube, Reddit, GitHub) into structured, evaluated knowledge
- Manual flow: source packet → extract → evaluate → archive
- Extractor API v1 scaffold exists, hardened, and locally smoke-proven
- Side-by-side stage decision: **QUALIFIED PASS** (bounded assistive drafting only)
- Evaluator and archivist remain manual

---

## What This Side Quest Is Not

- Not an active Jarvis runtime module
- Not integrated with Jarvis Dashboard, export, or orchestration
- Not transcript acquisition automation
- Not evaluator or archivist API automation
- Not a one-line command wrapper
- Not safe for unattended use

---

## Current Maturity / Status

| Label | Status |
|-------|--------|
| **Manual flow proven** | Yes — two end-to-end runs with archive entries |
| **Extractor API v1** | Smoke-proven locally; side-by-side QUALIFIED PASS |
| **Second-source validation** | Completed — first_run and second_run both SOFT PASS |
| **Proven** | Manual flow + API assistive drafting (bounded, operator-reviewed) |
| **Integrated with Jarvis** | No |
| **Human review** | Mandatory |

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
| `module_spec.md` | Module purpose, scope, non-goals |
| `README.md` | Current v1 role set, operating stance |
| `docs/MANUAL_RUN_CHECKLIST.md` | Operator checklist for manual runs |
| `docs/EXTRACTOR_API_V1_BUILD_PACKET.md` | Execution build checklist |
| `docs/EXTRACTOR_API_REVIEW_GATE.md` | Manual acceptance gate for API output |
| `scripts/run_extractor_api.py` | Extractor API CLI entry point |
| `scripts/extractor_api_client.py` | OpenAI API client for extraction |
| `scripts/extractor_api_validate.py` | Schema validator for extraction output |
| `outputs/extractor_api_stage_decision.md` | Side-by-side stage decision (QUALIFIED PASS) |

---

## Current Direction

- **Post-validation / bounded-quality-improvement-or-hold**
- API v1 is locally operational for assistive drafting
- Human review remains mandatory
- Known weakness profile (generic methods/patterns, thinner key claims, abstract open questions)
- Evaluator and archivist remain manual
- Not integrated with Jarvis

---

## Known API Weakness Profile

- Generic methods/pattern labels vs concrete implementation patterns
- Thinner key claims than manual baseline
- Weaker technical nuance (e.g., sign-then-post, yes/no tokens, phased validation)
- Abstract open questions vs implementation-specific
- Acceptable as first draft; operator must supplement

---

## Locked Constraints

- Manual review gate remains mandatory
- Manual extraction is fallback at all times
- No evaluator/archivist automation in scope
- No transcript acquisition in Extractor API v1 scope
- No unattended use; no broad production trust
- Schema contracts preserved; no drift

---

## What the Next Chat Should Do First

1. Read `SIDE_QUEST_HANDOFF_BUNDLE_RESEARCH_SWARM_LATEST.md`
2. Inspect `outputs/extractor_api_stage_decision.md` and comparison notes (`extractor_api_comparison_second_run.md`, `extractor_api_comparison_first_run.md`)
3. Decide next bounded move:
   - **Option A:** Prompt-tuning pass targeting concrete implementation patterns and technical claims
   - **Option B:** Operator decision to leave API v1 at qualified-pass assistive status for now

Do not assume broader activation. The next step is the smallest bounded move.

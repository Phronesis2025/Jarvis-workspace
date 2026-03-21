# Extractor API v1 Build Packet

Execution-ready build checklist for Extractor API v1. Use to guide implementation work.

---

## 1. Objective

- This build packet covers **only Extractor API v1**.
- Evaluator and archivist remain **manual**; no automation in scope.
- Transcript acquisition remains **separate work**; not part of this build.
- Implementation must preserve current schema contracts (`extraction_report.schema.json`) and the manual review gate (`EXTRACTOR_API_REVIEW_GATE.md`).

---

## 2. Scope

### In Scope

- API-backed extractor invocation (source packet in, extraction report out)
- Extractor prompt handoff (instructions + schema expectations)
- Schema validation of extractor output before review
- Writing extraction output to expected location (e.g. `outputs/`)
- Operator review handoff (no auto-proceed to evaluator)
- Logging/traceability for extractor run
- Fallback path to manual extraction

### Out of Scope

- Evaluator automation
- Archivist automation
- Transcript acquisition automation
- One-line command wrapper
- Scheduling
- Dashboard integration
- Supabase storage
- Chunking or summarization for long transcripts

---

## 3. Planned Files to Add Later

Do **not** create these now. Define for future build execution.

| File | Responsibility | Why It Exists |
|------|----------------|---------------|
| `future_modules/research_swarm/scripts/run_extractor_api.py` | Entry point; accepts source packet path; invokes extractor; writes output | Operator invokes extraction from CLI |
| `future_modules/research_swarm/scripts/extractor_api_client.py` | Bounded LLM API client; sends prompt + source; returns raw JSON | Isolates API calls; testable surface |
| `future_modules/research_swarm/scripts/extractor_api_validate.py` | Loads extraction JSON; validates against schema; returns pass/fail | Enforces schema before review |

Keep minimal. One runner + one client + one validator. No overbuild.

---

## 4. Build Sequence

| Step | Objective | Expected Output | Failure Condition |
|------|-----------|-----------------|-------------------|
| **1** | Create API runner entry point | `run_extractor_api.py` accepts `--packet <path>`; prints usage | No runnable entry point |
| **2** | Create bounded API client surface | `extractor_api_client.py` accepts source packet dict; returns raw API response | Client does not accept packet or returns unusable response |
| **3** | Connect extractor prompt + source packet input | Prompt loaded; packet fields (raw_content, source_type, etc.) passed to API | Prompt or input not wired correctly |
| **4** | Enforce structured JSON output | API instructed to emit extraction_report shape; response parsed as JSON | Malformed JSON; wrong shape |
| **5** | Add schema validation | `extractor_api_validate.py` validates output against `schemas/extraction_report.schema.json` | Validation not run or not blocking |
| **6** | Write extraction output artifact | Valid extraction JSON written to `outputs/` with sensible naming | Output not written; wrong path |
| **7** | Add run logging | packet_id, source_url, timestamp, model, success/failure, retries logged | No traceability for runs |
| **8** | Add operator review handoff behavior | Runner prints review gate reference; does not auto-proceed | Implies auto-proceed to evaluator |
| **9** | Run first smoke test against existing manual source packet | API runs on `source_packet_first_run.json` or `source_packet_second_run.json`; output produced | Smoke test fails |
| **10** | Compare API extraction to manual baseline | Side-by-side: API output vs `extraction_report_first_run.json` or `extraction_report_second_run.json` | No comparison performed |
| **11** | Document findings; decide pass-fail for rollout stage | Notes on quality drift; decision: proceed to API default or stay side-by-side | No documented decision |

---

## 5. Validation / Smoke Checks

Before Extractor API v1 is considered working:

- [ ] Valid extraction JSON created (parsable, no syntax error)
- [ ] Schema validation passes (`extraction_report.schema.json`)
- [ ] All required arrays present (methods_tools_patterns, key_claims, hype_signals, open_questions)
- [ ] All required scalars present (report_id, packet_id, source_url, created_at, summary)
- [ ] Evidence fields populated for methods_tools_patterns and key_claims
- [ ] No fabricated content in smoke sample (spot-check evidence vs source)
- [ ] Output written to expected outputs location
- [ ] Review gate can be applied manually (checklist from `EXTRACTOR_API_REVIEW_GATE.md` usable)
- [ ] Logging produces traceable run record

---

## 6. Rollout Decision Gate

Before moving from **side-by-side comparison** to **API default with review gate**, all must be true:

- **Repeated schema-valid outputs** — multiple runs; no schema failures
- **Acceptable similarity to manual baseline** — patterns, claims, hype_signals comparable to first/second run quality
- **No repeated fabrication issues** — evidence traceable to source
- **Operator trust threshold met** — operator willing to use API as default with review
- **Clear fallback working** — manual extraction path documented and executable

If any criterion fails, stay in side-by-side mode. Do not proceed to API default.

---

## 7. Failure / Rollback Rules

If Extractor API v1 is unstable:

- **Repeated schema failures** → Stop using API for extraction; fall back to manual
- **Repeated invented evidence** → Stop; do not let fabricated output into evaluation
- **Repeated weak pattern extraction** → Revise prompt or fall back to manual
- **Repeated hype misclassification** → Revise prompt or fall back to manual

**Fallback is manual extraction.** Do not let unstable API output become the default. Do not proceed to evaluator with unreviewed or failed extraction.

---

## 8. Operator Notes

- This build packet is for **implementation planning**. Tasks are defined; execution happens later.
- Not all named files need to be created until build execution starts. Follow the sequence.
- Stay on task. Do not expand into transcript automation, evaluator work, or archivist work.
- Manual extraction remains the fallback at all times.

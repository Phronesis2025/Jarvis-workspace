# OpenAI Extractor Integration Plan

Plan for API-assisted extraction in Research Swarm. Extractor is the first automated step; evaluator and archivist remain manual.

---

## Objective

- Extractor becomes the first API-assisted step.
- Evaluator and archivist stay manual for now.
- Goal: reduce manual load without losing evidence discipline.
- Manual baseline (two runs) remains the quality reference.

---

## Why Extractor First

- **Bounded schema** — extraction_report has fixed structure; fewer degrees of freedom.
- **Easiest to compare** — manual extractions exist; side-by-side comparison is straightforward.
- **High repetition** — same prompt logic, same schema, same evidence rules across sources.
- **Lower risk** — evaluator and archivist involve judgment calls; extractor is more mechanical.

---

## Inputs

Extractor consumes:

- **Source packet JSON** — per `schemas/source_intake.schema.json`
- **Transcript / raw content** — from packet `raw_content`
- **Existing extraction schema** — `schemas/extraction_report.schema.json`
- **Existing extractor prompt logic** — from `prompts/extractor_prompt.md`

---

## Outputs

Extractor must produce:

- **extraction_report JSON only**
- **Schema-valid output** — passes `extraction_report.schema.json`
- **No freeform essay** — structured fields only: summary, methods_tools_patterns, key_claims, hype_signals, open_questions

---

## Model Strategy

- Start with one OpenAI small model (e.g. gpt-4o-mini or equivalent).
- Use structured JSON output (response_format / JSON mode).
- Keep prompts bounded; avoid long system context.
- Retain manual review after generation — operator inspects before evaluation step.

---

## Validation Rules

Before accepting API output:

1. **Schema validation** — output conforms to extraction_report schema.
2. **Evidence presence** — every methods_tools_patterns and key_claims item has non-empty evidence.
3. **No fabricated claims** — evidence traces to source; no invented quotes.
4. **Manual comparison** — compare against manual extraction quality bar (e.g. first and second run) for calibration.

---

## Rollout Stages

| Stage | Description |
|-------|-------------|
| **1** | Manual + API side-by-side: run both; compare outputs; tune prompt if needed |
| **2** | API default with manual review: API generates; operator reviews before evaluation |
| **3** | Wrapper integration later: script or module that invokes API; still requires review gate |

---

## Out of Scope

- Evaluator API integration
- Archivist API integration
- Autonomous research loops
- Dashboard integration
- Live scheduling

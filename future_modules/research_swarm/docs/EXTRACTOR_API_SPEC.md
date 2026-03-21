# Extractor API Spec

Concrete implementation-ready specification for API-assisted extraction. Extractor step only.

---

## Objective

- This spec covers **only the extractor step**.
- Extractor consumes a source packet and produces an extraction report.
- Extractor output must match `extraction_report.schema.json` exactly.
- Extractor output is **reviewed manually** before the evaluator step.
- No evaluator or archivist automation.

---

## Inputs

### Canonical Input

- **Source packet JSON** — per `schemas/source_intake.schema.json`
- Source packet is the single handoff object into extractor.
- Extractor does not depend on evaluator state, archive state, or any downstream artifact.

### Packet Fields Used by Extractor

| Field | Required | Usage |
|-------|----------|-------|
| `packet_id` | yes | Passed through to `packet_id` in output; `report_id` generated for extraction |
| `source_url` | yes | Passed through; identifies source |
| `source_type` | yes | youtube \| reddit \| github; affects extraction framing |
| `raw_content` | yes | Primary extraction input; transcript, post body, README |
| `metadata` | no | title, channel, author, subreddit, repo_name; context only |
| `content_completeness` | no | full \| partial \| summary_only; constrains interpretation |
| `raw_content_format` | no | transcript \| markdown \| plain_text \| code \| mixed; hints for parsing |

### Other Inputs

- **Extractor prompt logic** — from `prompts/extractor_prompt.md`
- **Extraction schema** — `schemas/extraction_report.schema.json`

---

## Output Contract

Extractor produces **one** extraction_report JSON object.

### Requirements

- **Schema-valid** — passes `extraction_report.schema.json` validation.
- **Required arrays always present** — methods_tools_patterns, key_claims, hype_signals, open_questions (may be empty arrays but must exist).
- **Required scalars present** — report_id, packet_id, source_url, created_at, summary.
- **No freeform prose** outside schema fields.
- **No invented quotes** — evidence must trace to source.
- **No invented methods, claims, or hype signals** — all must be grounded in raw_content.

### Prohibited

- Fabricated evidence.
- Claims not supported by transcript/source.
- Hype signals not present in source language.
- Methods or patterns not evidenced in source.

---

## Model Interaction Shape

Implementation-neutral API interaction pattern. No SDK names, no code.

### Request Shape

1. **System / instruction block**
   - Bounded instructions
   - Schema expectations (required fields, structure)
   - Evidence rules
   - Prohibition on fabrication

2. **User / content block**
   - Source packet fields relevant to extraction
   - raw_content as primary payload
   - source_type for framing

3. **Output format**
   - Require structured JSON
   - Explicit schema or schema-like structure
   - Single response; no multi-turn for extraction

### Constraints

- **Bounded instructions** — prompt length controlled; avoid context bloat.
- **Schema expectations** — model instructed to emit valid extraction_report shape.
- **Evidence-only** — extractor constrained to transcript/source; no external knowledge injection.
- **No autonomous reasoning loop** — one request, one response; no iterative refinement by model.

---

## Evidence Rules

### methods_tools_patterns

- Every item **must** include `evidence`.
- Evidence = quote or paraphrase from source.
- `name` and `description` must be supported by evidence.
- `category` (method | tool | pattern) must fit the described item.

### key_claims

- Every item **must** include `evidence` and `confidence`.
- Evidence = quote or paraphrase from source.
- Confidence = stated | inferred | speculative; must reflect source support.
- Claim scope must match evidence; no overreach.

### hype_signals

- Must be grounded in **exact source language** or clear paraphrase.
- Do not invent hype; only flag what is present.
- Prefer quoted or near-quoted phrases.

### open_questions

- Reflect **real missing details** — e.g. URLs not given, types not specified.
- Not speculation or “what if” questions.
- Grounded in gaps visible in source.

---

## Source-Type Handling

Same output contract across all supported source types. Extraction logic adapts to content structure, not schema.

| Source Type | Content Shape | Extractor Behavior |
|-------------|---------------|--------------------|
| **YouTube** | Transcript; spoken language; may have repetition, filler | Parse for methods, claims; flag promotional language; handle speech-to-text artifacts |
| **Reddit** | Post + optional comments; markdown; conversational | Parse post body; optional comment context; flag community norms vs claims |
| **GitHub** | README, docs; markdown; code blocks | Parse for patterns, usage, architecture; handle code vs prose |

Output schema is identical. No source-type-specific output fields.

---

## Review Requirement

- Extractor output is **never** auto-accepted on first run.
- **Manual review remains mandatory** before evaluation step.
- Evaluator cannot proceed until extractor output passes review.
- See `EXTRACTOR_API_REVIEW_GATE.md` for checklist.

---

## Versioning / Comparison

### Baseline Sources

- **First run** — narrative/operator-style source (source_packet_first_run, extraction_report_first_run).
- **Second run** — technical/API-style source (source_packet_second_run, extraction_report_second_run).

### Comparison Protocol

- **Side-by-side** — run API extractor on same source; compare output to manual extraction.
- **Spot checks** — periodically compare API output to manual baseline for same or similar sources.
- **Calibration** — if API output drifts from quality bar, adjust prompt or fall back to manual.

### Versioning

- No schema version drift during extractor API integration.
- If schema changes, re-establish baseline before trusting API output.

---

## Out of Scope

- Evaluator automation
- Archivist automation
- Transcript acquisition
- One-line run command
- Scheduling
- Dashboarding

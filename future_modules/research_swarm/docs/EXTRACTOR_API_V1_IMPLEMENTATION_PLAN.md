# Extractor API v1 Implementation Plan

Implementation plan for integrating API-assisted extraction into Research Swarm. Extractor step only.

---

## 1. Objective

- Extractor API v1 **replaces manual extraction drafting only** — the operator no longer composes the extraction report by hand from the prompt.
- Evaluator and archivist remain **manual**.
- Manual extraction remains the **fallback** when API output fails review or is unavailable.
- API output must pass the **review gate** before the evaluator step.
- Extractor API v1 is **assistive**, not autonomous. The human stays in the loop.

---

## 2. Current Manual Flow (Baseline)

1. Source packet created (with transcript/raw content).
2. Operator runs extractor prompt manually (e.g. via chat or copy-paste).
3. Extraction report produced.
4. Operator reviews extraction.
5. Evaluator step begins.

**Manual runs 1 and 2 are the quality baseline.** First run = narrative/operator style. Second run = technical/API style. API output will be compared against these.

---

## 3. Target Extractor API v1 Flow

1. Source packet exists.
2. Operator runs extractor API tool (script or module).
3. API generates extraction_report JSON.
4. Operator performs review gate check per `EXTRACTOR_API_REVIEW_GATE.md`.
5. **If accepted** → proceed to evaluator step.
6. **If rejected** → retry API or fall back to manual extraction.

Extractor API v1 **does not remove the human review gate**. The operator must explicitly accept before evaluator proceeds.

---

## 4. Repository Integration Points

### Planned Locations

| Location | Purpose |
|----------|---------|
| `future_modules/research_swarm/` | Module root; schemas, prompts, outputs |
| `future_modules/research_swarm/scripts/` | Invocation entry point (e.g. run_extractor.py) |
| `future_modules/research_swarm/prompts/` | Extractor prompt (existing); API-specific prompt if needed |

### Conceptual Components

| Component | Responsibility |
|-----------|----------------|
| **extractor_api_runner** | Accepts source packet; calls LLM API; returns raw response. Lives in scripts or a small module. |
| **extractor_api_prompt** | Bounded instructions + schema expectations + evidence rules. May extend or wrap `prompts/extractor_prompt.md`. |
| **schema validator** | Validates output against `schemas/extraction_report.schema.json`. Rejects invalid JSON before review. |
| **review handoff** | Writes extraction_report to disk; operator reviews; no auto-proceed to evaluator. |

Do not create files in this planning step — only describe placement and responsibilities.

---

## 5. Input Surface

Extractor API receives:

### Source Packet Fields

- `packet_id`
- `source_url`
- `source_type`
- `raw_content`
- `metadata` (title, channel, author, subreddit, repo_name)
- `content_completeness`
- `raw_content_format`

### Other Inputs

- Extractor prompt instructions (from `prompts/extractor_prompt.md` or API variant)
- Extraction schema expectations (from `schemas/extraction_report.schema.json`)

**Source packet remains the canonical input object.** Extractor does not accept evaluator output, archive state, or any downstream artifact.

---

## 6. Output Surface

Extractor API produces:

### extraction_report JSON

- `report_id`
- `packet_id`
- `source_url`
- `created_at`
- `summary`
- `methods_tools_patterns`
- `key_claims`
- `hype_signals`
- `open_questions`

Output must pass `schemas/extraction_report.schema.json` validation.

**No partial objects allowed.** All required arrays present (may be empty). All required scalars present.

---

## 7. Manual Review Gate Integration

Review gate is performed by the operator after API returns output.

### Checklist Source

`docs/EXTRACTOR_API_REVIEW_GATE.md`

### Outcomes

| Outcome | Action |
|---------|--------|
| **PASS** | Proceed to evaluator step |
| **REVISE** | Retry API with adjusted prompt, or make minor edits to output |
| **REJECT** | Fall back to manual extraction per existing checklist |

Extractor API v1 does not auto-proceed. Operator must explicitly pass before evaluator runs.

---

## 8. Failure Handling

Extractor API v1 is **not trusted without validation**.

| Failure | Response |
|---------|----------|
| **Schema failure** | Reject output; retry or fall back to manual |
| **Invented evidence** | Reject; do not proceed; retry with stricter prompt or manual |
| **Weak pattern extraction** | Revise prompt to demand specificity; retry or manual extraction |
| **Long transcript degradation** | Manual fallback; or chunking strategy if proven later |

See `docs/EXTRACTOR_API_FAILURE_MODES.md` for full failure mode catalog and detection signals.

---

## 9. Logging / Traceability

Log during extraction:

- `packet_id`
- `source_url`
- `timestamp` (start, end)
- `model` used
- `extraction success/failure`
- `retry attempts` (if any)

Logging enables:

- Later comparison of manual vs API extraction quality
- Calibration against first-run and second-run baselines
- Debugging of systematic failures

Log format and storage (file, stdout, etc.) TBD at implementation time.

---

## 10. Rollout Plan

| Stage | Description |
|-------|-------------|
| **Stage 1** | Manual + API side-by-side — run both on same source; compare outputs; tune prompt |
| **Stage 2** | API default with review gate — API generates; operator reviews; manual remains fallback |
| **Stage 3** | Wrapper integration later — script or module chains extractor; evaluator/archivist still manual |

Manual extraction remains available throughout all stages.

---

## 11. Explicit Non-Goals

Extractor API v1 does **NOT** include:

- Evaluator automation
- Archivist automation
- Transcript acquisition automation
- One-line command wrapper
- Background research loops
- Scheduling
- Dashboard integration

These will be addressed in future work.

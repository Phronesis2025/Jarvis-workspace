# First Run Operator Guide

Walk-through for executing the first Research Swarm manual run.

---

## Overview

This run validates:

**source → extraction → evaluation → archive entry**

One source in, one knowledge archive entry out (if archive or archive_with_warning).

---

## Step 1 — Select Video

Operator chooses a YouTube video relevant to:

- AI agents
- automation
- research workflows
- AI tooling

Confirm transcript is available (video captions or external tool).

---

## Step 2 — Capture Transcript

Copy transcript manually from the video.

---

## Step 3 — Build Source Packet

Use:

`run_packets/FIRST_RUN_PACKET_TEMPLATE.md`

Create JSON matching `schemas/source_intake.schema.json`.

---

## Step 4 — Run Extractor Prompt

Use:

`prompts/extractor_prompt.md`

- Input: source packet
- Output: extraction report JSON

---

## Step 5 — Validate Extraction

Check:

- evidence quotes exist for methods_tools_patterns and key_claims
- schema validation passes (`schemas/extraction_report.schema.json`)
- no hallucinated claims; all evidence traces to source

---

## Step 6 — Run Evaluator Prompt

Use:

`prompts/evaluator_prompt.md`

- Input: extraction report
- Output: evaluation report JSON

**Validate evaluation report:**

- Validate against `schemas/evaluation_report.schema.json`
- Confirm archive_recommendation is justified by extraction evidence
- Confirm hype/credibility judgments are evidence-backed

---

## Step 7 — Apply Archive Decision

Use:

`docs/KNOWLEDGE_ARCHIVE_DECISION_RULES.md`

Possible decisions:

- archive
- archive_with_warning
- skip_archive

If skip_archive:

- stop the run
- v1 does not persist skip records

---

## Step 8 — Create Archive Entry

**Only if decision = `archive` or `archive_with_warning`.** Skip this step if decision = skip_archive.

Use:

`prompts/archivist_prompt.md`

- Input: source packet + extraction report + evaluation report
- Output: knowledge archive entry JSON
- `archive_decision` in the entry must exactly match the decision from Step 7

Validate against:

`schemas/knowledge_archive_entry.schema.json`

---

## Step 9 — Store Outputs

Write JSON artifacts to:

`outputs/`

Use naming convention from `outputs/README.md`.

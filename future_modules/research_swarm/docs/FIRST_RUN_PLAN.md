# Research Swarm v1 First Run Plan

Exact flow for the first manual execution. No automation, no scripts.

---

## Objective

This run validates the full pipeline:

**source → extraction → evaluation → archive entry**

Success means: one source in, one knowledge archive entry out, with all intermediate artifacts validated against existing schemas.

---

## Source Type for v1

**YouTube transcript** is the first supported source type.

Why:

- Transcripts are structured; predictable format
- Easier to capture raw content (manual copy or tool)
- Easier to test extraction and evidence citation
- No API integration required for v1

Reddit and GitHub will follow in later runs.

---

## Inputs

Operator must provide:

| Field | Required | Description |
|-------|----------|-------------|
| source_url | Y | Canonical YouTube video URL |
| source_type | Y | `youtube` |
| raw_content | Y | Full or partial transcript |
| metadata | N | title, author, channel, published_at |

Schema: `schemas/source_intake.schema.json`

Packet must include: `packet_id`, `created_at`, plus the fields above.

---

## Pipeline Stages

| Stage | Input | Output | Reference |
|-------|-------|--------|-----------|
| 1. Source Intake | URL, transcript, metadata | Source intake packet | `schemas/source_intake.schema.json` |
| 2. Extraction | Source packet | Extraction report | `prompts/extractor_prompt.md`, `schemas/extraction_report.schema.json` |
| 3. Evaluation | Extraction report | Evaluation report | `prompts/evaluator_prompt.md`, `schemas/evaluation_report.schema.json` |
| 4. Archive Decision | Extraction + evaluation | archive / archive_with_warning / skip_archive | `docs/KNOWLEDGE_ARCHIVE_DECISION_RULES.md` |
| 5. Archive Entry Creation | Extraction + evaluation + decision | Knowledge archive entry (only if archive or archive_with_warning) | `prompts/archivist_prompt.md`, `schemas/knowledge_archive_entry.schema.json` |

**skip_archive handling:** If decision is skip_archive, stop the normal archive-entry path. v1 manual runs do NOT persist skip-archive disposition records. Skip records may be supported later as a separate audit/disposition step.

---

## Human Review Points

| Point | After | Operator Checks |
|-------|-------|-----------------|
| **Review 1** | Extraction | Evidence quotes exist; no invented content; methods_tools_patterns and key_claims cite source |
| **Review 2** | Evaluation | Credibility/hype scores align with extraction; archive_recommendation is justified |
| **Review 3** | Before archive creation | Archive decision matches `KNOWLEDGE_ARCHIVE_DECISION_RULES.md`; if skip_archive, stop—no archive entry; v1 does not persist skip records |

---

## Success Criteria

The run succeeds if:

- `extraction_report` JSON validates against `schemas/extraction_report.schema.json`
- Evaluation report is internally consistent with extraction (scores cite extraction content)
- Archive decision follows `docs/KNOWLEDGE_ARCHIVE_DECISION_RULES.md`
- Archive entry validates against `schemas/knowledge_archive_entry.schema.json`
- All required arrays exist (even if empty)

---

## Failure Conditions

Stop and fix if:

- Extraction contains invented evidence (not in source)
- Any JSON fails schema validation
- Archive decision conflicts with decision rules
- Output missing required fields
- Hype warnings lack evidence, why_flagged, or severity (each warning must include signal, evidence, why_flagged, severity; evidence quotes/paraphrases source language)

---

## Scope Boundaries

- **Single source only** — One YouTube video per run
- **Manual execution** — Operator runs each stage by hand
- **No automation** — No scripts, no scheduled runs
- **No external integrations** — No YouTube API, no auto-fetch

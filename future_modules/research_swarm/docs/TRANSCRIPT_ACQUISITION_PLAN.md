# Transcript Acquisition Plan

Plan for automated transcript capture. Manual copying is acceptable for early proof, but not for long-term operation.

---

## Objective

Operator should not have to manually extract every transcript long-term. The system should attempt to retrieve transcript and metadata from a given URL, then populate the source packet.

---

## Desired Behavior

Given a YouTube URL (or other supported source URL), the system should attempt to produce:

- **transcript text** — full or partial caption/transcript
- **title** — video or post title
- **channel / author** — source attribution
- **captured_at** — ISO 8601 timestamp
- **content_completeness** — full | partial | summary_only
- **raw_content_format** — transcript | markdown | plain_text | code | mixed

These map directly to source packet fields per `schemas/source_intake.schema.json`.

---

## Acquisition Strategy

Use a tiered approach:

| Tier | Method | Description |
|------|--------|-------------|
| **1. Primary** | Transcript fetcher | Dedicated transcript/caption retrieval for the source type |
| **2. Secondary** | Page extraction fallback | If primary fails: scrape or parse page for available text |
| **3. Manual** | Operator fallback | If automated retrieval fails: operator pastes content; packet marked manual |

Do not assume a specific library. Design for:
- Pluggable transcript fetcher
- Pluggable page extraction fallback
- Clear handoff to manual when both fail

---

## Failure Handling

If transcript cannot be obtained:

- Mark source **unavailable** or **partial** as appropriate.
- Do **not** fabricate transcript.
- Allow manual fallback: operator can paste content and proceed.
- Do not block the run; operator decides whether to skip or retry.

---

## Output Contract

Transcript acquisition step should ultimately:

1. Populate `raw_content` with retrieved text.
2. Populate `metadata` (title, channel/author) when available.
3. Set `captured_at`, `content_completeness`, `raw_content_format`.
4. Produce a source packet compatible with `source_intake.schema.json` for downstream extractor.

---

## Out of Scope

- Summarization
- Extraction
- Evaluation
- Archive creation

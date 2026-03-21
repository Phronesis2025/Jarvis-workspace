# Content Acquisition Layer — Implementation Plan

**Purpose:** Implementation-ready plan for the Content Acquisition Layer. Converts chosen source references into normalized source packets for Research Swarm extraction.

**Aligned with:** CONTENT_ACQUISITION_LAYER_PLAN.md

**Position:** Upstream of extraction; downstream of discovery. Acquisition only — no discovery, no extraction, no evaluation.

---

## 1. Objective

This implementation plan covers the bounded layer that:

- **Accepts** a chosen source reference (URL or stable identifier)
- **Acquires** usable content and metadata from that source
- **Normalizes** content into a valid source packet
- **Hands** that packet downstream to Research Swarm extraction

Clarifications:

- This is **upstream of extraction**. Extraction consumes packets; acquisition produces them.
- This is **not** source discovery. Discovery selects; acquisition pulls.
- This is **not** evaluator or archivist work. Those steps happen later.
- This is **not** unattended operation. Operator provides source and reviews output.

---

## 2. Position in the larger flow

The ladder:

1. **Topic/ticker/question defined** — operator or discovery
2. **Discovery/intake selects candidate** — SOURCE_DISCOVERY_INTAKE_PLANNER (out of scope for this implementation)
3. **Content acquisition** — *this implementation* — pulls/normalizes content
4. **Source packet emitted** — valid JSON to `outputs/`
5. **Extraction runs** — existing `run_extractor_api.py` flow
6. **Evaluator/archivist** — later (manual, out of scope)

This implementation step covers: acquisition runner, source-type handlers, packet builder, validation. It does not cover: discovery, extraction changes, evaluator, archivist, Jarvis integration.

---

## 3. Repository integration points

Use the existing Research Swarm future-module structure under `future_modules/research_swarm/`.

| Placement | Responsibility |
|-----------|----------------|
| `scripts/run_acquisition.py` | Entrypoint. Accepts source URL/reference, dispatches by type, writes packet to outputs. |
| `scripts/acquisition/` (or `acquisition/` module under scripts) | Source-type handlers. One handler per type (youtube, twitter, reddit, github, article). |
| `scripts/acquisition/packet_builder.py` (or shared util) | Assembles normalized fields into packet dict; generates packet_id; assigns completeness. |
| `scripts/acquisition/source_classifier.py` | Infers source_type from URL if not provided. |
| `scripts/acquisition/metadata_normalizer.py` | Normalizes source-type-specific metadata into common structure. |
| `schemas/` | Reuse or align with existing `source_intake` expectations. No schema redesign. |
| `outputs/` | Acquisition writes packets here. Filename convention: `source_packet_{run_id}.json` or similar. |
| `docs/` | Acquisition usage, completeness labels, failure conditions. |

No new top-level packages. Keep acquisition within the Research Swarm module boundary.

---

## 4. Planned implementation components

| Component | Responsibility |
|-----------|-----------------|
| **Acquisition entrypoint** | CLI or script. Accepts URL, optional source_type, optional output path. Dispatches to handler. |
| **Source classifier** | From URL, infer source_type (youtube, twitter, reddit, github, article). Fallback: ask operator or fail. |
| **Source-type fetch/parse handlers** | One per type. Fetch content, extract text, extract metadata. Return raw_content + metadata + completeness hint. |
| **Metadata normalizer** | Convert handler output into common metadata shape (title, author, date, IDs, etc.). |
| **Packet serializer** | Build final packet dict with packet_id, source_url, source_type, raw_content, metadata, content_completeness, raw_content_format. Write JSON. |
| **Completeness label helper** | Logic to assign content_completeness from handler hint + content inspection. |
| **Acquisition result summary** | Concise output: success/fail, packet path, completeness label, any warnings. |

---

## 5. Input surface

Operator input into this layer:

| Input | Required | Purpose |
|-------|----------|---------|
| **source_url** | Yes | Canonical URL or stable reference (e.g. YouTube video URL). |
| **source_type** | No (inferrable) | Override inferred type. One of: youtube, twitter, reddit, github, article. |
| **output_path** | No | Where to write packet. Default: `outputs/source_packet_{run_id}.json`. |
| **topic_hint** | No | Optional context for operator record; may go into metadata. |
| **handling_notes** | No | Hints from discovery handoff (e.g. "focus on comments"). Pass-through to handler if useful. |

Keep it simple. No giant config system. CLI flags or minimal config file sufficient.

---

## 6. Output surface

This layer produces:

| Output | Description |
|--------|-------------|
| **Normalized source packet JSON** | Valid packet aligned with existing contract. Fields: packet_id, source_url, source_type, raw_content, metadata, content_completeness, raw_content_format. Additional fields (created_at, captured_at, purpose) allowed if consistent with existing packets. |
| **Acquisition result summary** | Operator-facing: success/fail, packet path, completeness label. On failure: reason, escalation suggestion. |

This layer does **not** produce:

- Extraction report
- Archive record
- Evaluation output

---

## 7. Source-type implementation boundaries

### YouTube

| Aspect | Implementation boundary |
|--------|-------------------------|
| **Preferred path** | Fetch transcript via API or library (e.g. youtube-transcript-api). Include description if useful. |
| **Fallback path** | Description + title only. Or: operator supplies manual transcript path. |
| **Completeness issues** | Auto-captions wrong/absent; non-English; long videos truncated. |
| **Good enough** | Transcript or description + title with sufficient substance. raw_content has meaningful text. |
| **Stop/escalate** | No transcript, no description, no manual input → fail. Do not emit metadata_only and pretend usable. |

### X/Twitter

| Aspect | Implementation boundary |
|--------|-------------------------|
| **Preferred path** | Fetch post + thread via API or scraping. Include quoted context. |
| **Fallback path** | Single post only if thread unavailable. |
| **Completeness issues** | Truncation; deleted posts; rate limits; thread depth. |
| **Good enough** | Post text captured. Thread preferred but single post acceptable. |
| **Stop/escalate** | Inaccessible; no content recovered; API auth required and not available → fail. |

### Reddit

| Aspect | Implementation boundary |
|--------|-------------------------|
| **Preferred path** | Fetch post body + high-signal comments (score/depth heuristic or config). |
| **Fallback path** | Post body only. |
| **Completeness issues** | Large threads; removed comments; which comments to include. |
| **Good enough** | Post body + some comments. Configurable comment cap. |
| **Stop/escalate** | Post removed; 404; subreddit private → fail. |

### GitHub

| Aspect | Implementation boundary |
|--------|-------------------------|
| **Preferred path** | Repo: README. Issue: issue body + top comments. Optionally key file content. |
| **Fallback path** | README only for repo. Issue body only for issue. |
| **Completeness issues** | Large repos; large files; context boundaries. |
| **Good enough** | README or issue body with meaningful content. Truncate with clear boundary if needed. |
| **Stop/escalate** | Repo/issue private; 404; empty README and no issue → fail. |

### Generic article/webpage

| Aspect | Implementation boundary |
|--------|-------------------------|
| **Preferred path** | Extract main article text; strip nav/ads/sidebars. Preserve headings/paragraphs. |
| **Fallback path** | Full page text if article extraction fails. |
| **Completeness issues** | Paywall; dynamic content; layout noise; ads. |
| **Good enough** | Substantive main text. Minimum length threshold. |
| **Stop/escalate** | Paywall; blocked; only boilerplate recovered → fail. |

---

## 8. Completeness labeling implementation

Implementation assigns `content_completeness` based on what was captured:

| Label | When to use | When to refuse packet |
|-------|-------------|------------------------|
| **full_transcript** | Full transcript captured (YouTube, podcast). | — |
| **partial_transcript** | Part of transcript; gaps or truncation. | — |
| **page_text_only** | Article/page text; no transcript. | — |
| **summary_only** | Only description, abstract, or summary. | If raw_content too thin (< N chars). |
| **metadata_only** | Only metadata; no substantive content. | **Refuse.** Do not create packet. Escalate. |

**Refuse packet when:**

- Only metadata recovered
- raw_content below minimum viable length (e.g. < 200 chars; configurable)
- Content is obviously placeholder or error message
- Source inaccessible and no usable fallback

**Rule:** Never emit a packet that pretends useful content when there is none.

---

## 9. Operator usage shape

Intended first operator workflow:

1. **Operator provides chosen source** — URL (and optionally source_type) from discovery or manual selection.
2. **Acquisition command runs** — e.g. `python scripts/run_acquisition.py --url <URL> [--type youtube]`.
3. **Packet written to outputs** — `outputs/source_packet_{run_id}.json`.
4. **Acquisition prints summary** — success, packet path, content_completeness.
5. **Operator reviews packet quality** — opens JSON or quick validation step.
6. **Extraction runs manually** — operator invokes `run_extractor_api.py --packet <path>` when satisfied.

CLI shape is illustrative. Final syntax may differ, but the flow should be: URL → packet → review → extraction.

---

## 10. Proof / rollout path

| Stage | Description |
|-------|-------------|
| **Stage 1** | Manual-assisted acquisition for 1–2 source types (e.g. YouTube + article). Operator may paste content; scripts help structure packet. Validate alignment with existing packet contract. |
| **Stage 2** | Helper-driven packet generation. Script fetches for supported types. Explicit operator review before extraction. |
| **Stage 3** | Broader source-type support. Twitter, Reddit, GitHub handlers. Same review discipline. |
| **Stage 4** | Later integration with discovery output. Discovery produces candidate list; acquisition consumes URLs. |
| **Stage 5** | Much later: automation, batch runs, scheduling. Out of scope for this plan. |

First proof should be narrow (one source type) and honest. No premature generalization.

---

## 11. Failure / stop conditions

Implementation must fail or escalate instead of writing a misleading packet when:

| Condition | Action |
|-----------|--------|
| Inaccessible source | Fail. Report: "Source inaccessible (404/timeout/blocked)." |
| Transcript unavailable, no fallback | Fail. Do not emit. Escalate for manual transcript. |
| Only metadata recovered | Fail. Do not create packet. |
| Content too thin | Fail if below threshold. Report: "Content too thin for extraction." |
| Ambiguous source identity | Fail. "Could not resolve source. Provide unambiguous URL." |
| Parse/fetch failure | Fail. Report error. Do not fabricate content. |
| Unsupported source type | Fail. "Source type X not yet supported." |

**Core rule:** Bad acquisition must not be disguised as valid packet generation. When in doubt, fail and report.

---

## 12. Explicit non-goals

This implementation plan does **not** include:

- Source discovery implementation
- Extraction implementation changes (beyond consuming new packets)
- Evaluator automation
- Archivist automation
- Stock signal scoring
- Jarvis integration
- Unattended scheduling
- Broad production hardening (rate limiting, retries, caching)
- Full vendor API integration (YouTube Data API, Twitter API, etc.) — start with simplest viable path

This plan is acquisition-layer implementation only.

# Content Acquisition Layer Plan

**Purpose:** Bounded planning spec for the pre-extraction intake layer that converts chosen sources into normalized source packets for Research Swarm.

**Position:** Upstream of extraction; downstream of (future) source discovery.

**Not in scope:** Source discovery, evaluation, archiving, stock scoring, Jarvis integration.

---

## 1. Objective

This layer converts a **chosen source** into a **normalized source packet** ready for Research Swarm extraction.

- **Input:** Source URL or reference (already chosen by operator or future discovery layer)
- **Output:** Valid source packet JSON in the format expected by the extractor
- **Does not do:** Evaluation, archiving, deciding which sources are worth choosing
- **Does not do:** Stock signal scoring, Jarvis orchestration, unattended runs

This is a **pre-extraction intake layer**. It normalizes and assembles; it does not evaluate or archive.

---

## 2. Position in the larger stock-agent flow

The clean ladder:

1. **Source chosen** — operator or future discovery picks the source (out of scope for this layer)
2. **Acquisition layer** — pulls content, normalizes it, builds packet
3. **Source packet created** — valid JSON ready for extraction
4. **Research Swarm extraction** — extractor runs on packet (existing flow)
5. **Evaluator and archivist** — happen later (manual, out of scope)

Clarifications:

- This layer is **not** source discovery. Discovery picks what to acquire; acquisition pulls what was picked.
- This layer is **not** stock scoring. Scoring happens downstream or elsewhere.
- This layer is **not** unattended operation. Operator remains in the loop.

---

## 3. Accepted source types

Initial source types this layer should support conceptually:

| Source type | Raw content ideally captured | Metadata that matters | Completeness issues |
|-------------|-----------------------------|------------------------|----------------------|
| **YouTube video** | Transcript (auto or manual), description | Video ID, title, channel, publish date, duration | Auto-captions may be wrong or absent; manual transcript may be required |
| **X/Twitter post or thread** | Post text, reply text in thread | Author, post ID, timestamp | Thread depth limits; truncated threads; deleted/missing posts |
| **Reddit post or thread** | Post body, high-signal comments | Subreddit, author, post ID, score, timestamp | Comment volume; which comments matter; deleted/removed |
| **GitHub repo/readme/issue** | README, issue body, key file snippets | Repo URL, issue number, author | Large repos; partial capture; context boundaries |
| **Article/webpage** | Cleaned article text | URL, title, author, publish date | Paywalls; ads; layout noise; dynamic content |

---

## 4. Normalized packet contract

Target source packet fields this layer must produce. Aligned with existing packet expectations; no schema redesign.

| Field | Purpose |
|-------|---------|
| `packet_id` | Unique identifier for this acquisition run (e.g. UUID or timestamp-based) |
| `source_url` | Canonical URL of the source (or stable reference if no URL) |
| `source_type` | One of: `youtube`, `twitter`, `reddit`, `github`, `article` |
| `raw_content` | Normalized text content in a single string — the extractor’s primary input |
| `metadata` | Structured metadata (title, author, date, IDs, etc.) for downstream context |
| `content_completeness` | Label indicating what was captured (see §6) |
| `raw_content_format` | How raw_content is structured (e.g. `transcript`, `thread`, `article`). Helps extractor interpret layout. |

Operator language:

- **packet_id** — “Which packet is this?” Uniqueness for runs and comparisons.
- **source_url** — “Where did this come from?” Traceability and re-acquisition.
- **source_type** — “What kind of source?” Drives acquisition path and extractor expectations.
- **raw_content** — “What text do we have?” The main payload for extraction.
- **metadata** — “What do we know about the source?” Context for key claims and dates.
- **content_completeness** — “How complete is the capture?” Signals extraction quality risk.
- **raw_content_format** — “How is the content laid out?” Transcript vs thread vs article structure.

---

## 5. Source-type acquisition paths

High-level preferred path for each source type. Conceptual only; no API implementation.

**YouTube video**

- Fetch transcript if available (auto-captions or manual)
- Fallback: description + title + manual notes/transcript
- If transcript absent and not manually supplied → mark incomplete and escalate

**X/Twitter post or thread**

- Fetch post text and thread replies
- Include quoted context when available
- Truncation or missing posts → mark partial and note what’s missing

**Reddit post or thread**

- Fetch post body
- Include high-signal comments (operator-defined or heuristic: score, depth, direct replies)
- Large threads → cap or sample; document inclusion rules in metadata

**GitHub repo/readme/issue**

- Repo: README + optionally key file snippets
- Issue: issue body + relevant comments
- Large files → truncate with clear boundaries; document scope

**Article/webpage**

- Extract main article text; strip ads/nav/sidebars
- Preserve structure if useful (headings, paragraphs)
- Paywall or blocked → mark inaccessible and escalate

---

## 6. Completeness labeling

This layer must mark `content_completeness` so downstream extraction knows what to expect.

| Label | Meaning |
|-------|---------|
| `full_transcript` | Full transcript captured (YouTube, podcast, etc.) |
| `partial_transcript` | Only part of transcript available |
| `page_text_only` | Page/article text only; no transcript |
| `summary_only` | Only summary, description, or abstract |
| `metadata_only` | No substantive content; metadata only |

Why it matters:

- Extraction quality depends on content richness. Thin content yields thin extractions.
- Completeness labels allow the operator to decide: proceed, supplement, or skip.
- Bad acquisition should not be disguised as good packet input.

---

## 7. Failure / stop conditions

When acquisition should stop or escalate instead of producing a packet:

| Condition | Action |
|-----------|--------|
| Transcript unavailable and no fallback | Stop; do not produce packet. Escalate for manual transcript or skip. |
| Page blocked / inaccessible | Stop. Document reason. Do not fabricate content. |
| Content too incomplete | Stop or mark `metadata_only`; do not pretend full content. |
| Source type unsupported | Stop. Document. Extend layer if needed. |
| Raw content too thin to justify extraction | Stop. Do not create packet. Operator decides next step. |
| Ambiguous source identity | Stop. Resolve URL/reference before acquisition. |

Core rule: **Bad acquisition should not be disguised as good packet input.** When in doubt, escalate.

---

## 8. Manual vs future automation boundary

**Manual or semi-manual for now:**

- Source selection — operator chooses what to acquire
- Fallback transcript retrieval — when auto-transcript fails
- Judgment calls on comment inclusion (Reddit, GitHub)
- Escalation on thin content — operator decides proceed/skip
- Packet file generation — may start as copy-paste or local scripts

**Future automation candidates:**

- Transcript fetch (YouTube, podcasts)
- Page content pull (articles, webpages)
- Metadata collection (all source types)
- Packet file generation (scripted from URL)
- Batch acquisition for chosen URL lists

Keep it honest: today’s boundary is manual-heavy. Automation is a later step, not a requirement for this plan.

---

## 9. Minimal rollout path

Boring, bounded rollout:

| Stage | Description |
|-------|-------------|
| **Stage 1** | Manual packet assembly using clear intake rules. Operator pulls content, pastes into template, saves as packet JSON. Validates alignment with existing packet contract. |
| **Stage 2** | Helper scripts for supported source types. Scripts pull content and emit packet JSON. Operator still selects sources and runs scripts. |
| **Stage 3** | Semi-automated acquisition before extraction. One command: URL → packet. Operator reviews packet before extraction. |
| **Stage 4** | Later discovery integration. Discovery layer chooses sources; acquisition runs; handoff to Research Swarm. Out of scope for this plan. |

---

## 10. Explicit non-goals

This layer does **not** do:

- Source discovery
- Evaluator work
- Archivist work
- Stock signal scoring
- Autonomous run scheduling
- Jarvis integration
- Unattended operation

This layer is acquisition and normalization only.

# Source Discovery / Intake Planner

**Purpose:** Bounded planning spec for the discovery and triage layer that finds candidate sources for a research target and hands selected candidates to the Content Acquisition Layer.

**Position:** Upstream of acquisition; upstream of extraction. First step in the research intake chain.

**Not in scope:** Content acquisition, extraction, evaluation, archiving, stock scoring, Jarvis integration.

---

## 1. Objective

This layer **finds and triages candidate sources** for a given research target (ticker, topic, question).

- **Input:** Research topic, ticker, theme, company, tool, or question
- **Output:** Selected candidate sources handed off for acquisition
- **Does not do:** Normalize or fetch full content (acquisition’s job)
- **Does not do:** Score trades or produce portfolio actions
- **Does not do:** Extraction, evaluation, or archiving

This is a **discovery and triage layer only**. It identifies what to acquire; it does not acquire, extract, or score.

---

## 2. Position in the larger flow

The ladder:

1. **Topic / ticker / question defined** — operator frames the research target
2. **Discovery/intake** — finds candidate sources, filters, triages, selects
3. **Selected sources handed to acquisition** — planner passes URLs/references forward
4. **Acquisition layer** — creates source packets (see CONTENT_ACQUISITION_LAYER_PLAN)
5. **Research Swarm extraction** — runs on packets
6. **Evaluator / archivist** — later (manual)

Clarifications:

- This layer is **not** acquisition. Discovery selects; acquisition pulls.
- This layer is **not** extraction. Extraction consumes packets that acquisition built.
- This layer is **not** stock scoring. Scoring is downstream or elsewhere.
- This layer is **not** unattended operation. Operator frames topics and reviews selection.

---

## 3. Accepted discovery inputs

Kinds of starting inputs this planner should accept:

| Input type | Behavior change |
|------------|-----------------|
| **Ticker** | Focus on company, product, competitors; earnings, announcements, analyst coverage |
| **Company name** | Broader than ticker; include non-ticker entities (privates, subsidiaries) |
| **Product / tool name** | Focus on reviews, integrations, technical discussion, adoption signals |
| **Sector / theme** | Broader search; cross-company, thematic trends, industry-level signal |
| **Research question** | Open-ended; frame search around question phrasing and key terms |
| **Catalyst / event topic** | Time-bound; earnings, launches, regulatory, macro events |

Each input narrows or broadens the search space and shifts which source classes matter most.

---

## 4. Candidate source classes

Initial classes the planner should consider:

| Source class | Why useful | Typical signal | Noise/credibility risks |
|--------------|------------|----------------|-------------------------|
| **YouTube videos** | Deep dives, interviews, technical walkthroughs | Expert opinions, product demos, conference talks | Varying quality; hype; outdated content |
| **X/Twitter posts/threads** | Real-time, founder/developer voice | Early signals, reactions, debates | Echo chambers; short context; noise |
| **Reddit posts/threads** | Community sentiment, technical Q&A | Practical experience, niche discussions | Meme noise; brigading; low SNR |
| **GitHub repos/issues/readmes** | Implementation detail, adoption, issues | Technical depth, usage patterns | Fragmented; context spread across files |
| **Articles / webpages / blogs** | Structured analysis, news, op-eds | Curated arguments, citations | Paywalls; SEO fluff; outdated |
| **Earnings materials / docs** | Official company data, filings | Primary source facts | Dense; needs extraction focus |

---

## 5. Intake filtering rules

**First-pass filters — exclude:**

- Obviously irrelevant to topic/ticker
- Duplicate or reposted content (same source, same claim)
- Too little substance (single-line, meme-only)
- Pure hype with no usable claims (price targets without reasoning)
- Source identity too ambiguous (anonymous, no attribution)
- Inaccessible / dead link
- Low-value aggregations (listicles with no original analysis)

**Remain eligible even if imperfect:**

- Strong signal but partial context — worth acquiring to assess
- Controversial claims worth investigation — don’t filter on disagreement alone
- Niche technical content with low polish but high substance — GitHub, Reddit, obscure docs

**Rule:** Filter obvious junk; keep borderline candidates for human triage when signal potential exists.

---

## 6. Triage / prioritization logic

How the planner should rank or order candidates. Operator-facing, bounded.

| Dimension | Effect on priority |
|-----------|---------------------|
| **Relevance to topic** | Closer match → higher |
| **Novelty** | New angle or recent → higher |
| **Technical depth** | More implementable detail → higher |
| **Likely signal density** | More extractable claims → higher |
| **Credibility** | Primary source / known expert → higher |
| **Timeliness** | Fresher for time-sensitive topics → higher |
| **Extraction usefulness** | Structure and completeness matter for downstream |

No complex scoring system required. A simple ordered list (high / medium / low) or ranked queue suffices. Operator can override.

---

## 7. Handoff contract to acquisition

What the planner passes forward for each selected candidate. **Not** the full source packet — that is acquisition’s output. This is the **selection handoff**.

| Field | Purpose |
|-------|---------|
| **source_url** | Canonical URL or stable reference |
| **source_class** | One of: youtube, twitter, reddit, github, article, earnings |
| **selection_reason** | Brief note: why this was selected |
| **priority** | high / medium / low (or ordinal) |
| **completeness_notes** | Expected completeness risk (e.g. “thread may be truncated”) |
| **special_handling** | Optional: “focus on comments,” “README only,” etc. |

Acquisition uses this to know what to pull and how to treat it.

---

## 8. Manual vs future automation boundary

**Manual for now:**

- Topic framing — operator defines research target
- Candidate judgment — operator reviews filtered list
- Noise filtering — operator overrides or refines
- Final selection for acquisition — operator chooses what gets handed off

**Possible later automation:**

- Search aggregation (multi-platform queries)
- Duplicate clustering (same content, multiple URLs)
- Simple relevance ranking
- Freshness filtering (date thresholds)
- Candidate queue generation (structured list for operator review)

Keep it honest: today’s boundary is manual-heavy. Automation is a later step.

---

## 9. Failure / stop conditions

When discovery/intake should stop or escalate:

| Condition | Action |
|-----------|--------|
| No credible candidates found | Stop. Report. Operator may broaden topic or try different phrasing. |
| Only hype/noise found | Stop. Do not pass junk to acquisition. Escalate. |
| Topic too vague | Stop. Ask operator to narrow or add context. |
| Source set too broad | Stop or cap. Handoff overload helps no one. Prioritize and trim. |
| Discovery results stale or low-signal | Stop. Do not feed old/noise downstream. Operator decides retry. |
| Candidate overload without clear ranking | Stop. Do not hand off unordered dump. Require triage first. |

Core rule: **Bad discovery should not feed junk downstream.** When in doubt, escalate.

---

## 10. Minimal rollout path

Bounded rollout:

| Stage | Description |
|-------|-------------|
| **Stage 1** | Manual discovery checklist. Operator searches each source class, keeps notes, manually compiles URL list for acquisition. |
| **Stage 2** | Helper search templates by source class. Saved queries or templates for ticker/topic. Operator still runs searches and selects. |
| **Stage 3** | Semi-structured candidate queue. Tool or list format: candidates with URL, class, priority. Operator reviews and approves handoff. |
| **Stage 4** | Later automation feeding acquisition. Discovery runs, produces queue, operator approves. Acquisition pulls. Out of scope for this plan. |

---

## 11. Explicit non-goals

This layer does **not** do:

- Transcript or content acquisition
- Extraction drafting
- Evaluator work
- Archivist work
- Stock signal scoring
- Trade decisioning
- Jarvis integration
- Unattended scheduled runs

This layer is discovery and triage only.

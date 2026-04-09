# JARVIS THE FOUNDRY — Context Anchor
**Last Updated:** 2026-04-11  
**Status:** Phases 1–5 built (dashboard + local JSON). Phase 6 optional — not started.  
**Purpose:** New-chat starting point for the research-intake, master-idea-registry, dashboard review, and implementation queue module.

---

## 1. What This Module Is

**JARVIS THE FOUNDRY** is the Jarvis research-ingestion and idea-forging module.

It exists to take raw external research inputs and convert them into ranked, reviewable, implementation-ready ideas for the stock module and related future modules.

It will unify three intake lanes:

1. **X article reviews**
2. **Daily / hourly X post research outputs**
3. **GitHub repo review outputs**

The module will normalize those sources into one **Master Idea Registry**, score the extracted ideas, surface the best ones on the dashboard, and feed a human-reviewed implementation queue.

---

## 2. Why This Exists Now

The current research work is valuable but fragmented.

Right now the operator has:
- many X article reviews
- recurring X post brief outputs
- GitHub repo review outputs
- useful knowledge files spread across multiple formats and locations

The problem is not lack of ideas.  
The problem is lack of a **durable scoring, promotion, and review system**.

The goal of JARVIS THE FOUNDRY is to stop losing good research in a pile of markdown and instead turn it into:

- reusable knowledge
- ranked ideas
- implementation candidates
- a visible next-best queue

---

## 3. Intentional Build Override

The operator is intentionally overriding the earlier **dashboard-first deferral** for this module.

This is a bounded exception, not a general architecture reversal.

### Why the override is allowed
The dashboard will materially speed up:
- entering new article text
- entering GitHub links
- entering raw X posts / brief text
- reviewing extracted results
- seeing the current top ideas
- deciding what to implement next

### What remains true despite the override
The module still follows Jarvis core discipline:
- bounded scope
- explicit schemas
- visible state
- scoreable outputs
- no fake autonomy
- human review before promotion to implementation

---

## 4. Core Module Outcome

By the end of the first build lane, the operator should be able to:

1. paste article text into a dashboard page and get a structured review output
2. paste a GitHub link into a dashboard page and get a structured review output
3. ingest X post research outputs into the same system
4. automatically extract candidate ideas from each source
5. score and deduplicate those ideas
6. review the promoted ideas in one dashboard page
7. see the next best implementation candidates clearly

---

## 5. Name and Positioning

### Official module name
**JARVIS THE FOUNDRY**

### Short description
A research-to-implementation intake and registry system that forges raw findings into ranked build decisions.

### Why this name fits
The module is not just collecting ideas.  
It is **refining, hammering, ranking, and shaping** them into something buildable.

Raw ore in.  
Usable metal out.

---

## 6. What This Module Is Not

This module is **not**:
- a fully autonomous research brain
- an auto-builder that directly ships ideas into production
- a replacement for human judgment
- a “just install everything” repo collector
- a screenshot-chasing winner-copy engine

If it cannot separate signal from garbage, it fails.

---

## 7. Core Build Principles

1. **Registry first, dashboard second, automation third**
2. **Canonical idea objects beat loose notes**
3. **Score before promote**
4. **Human review remains mandatory before implementation**
5. **One clean pipeline beats multiple one-off scripts**
6. **Dashboard is an operator surface, not the thinking substitute**
7. **Local/exportable truth remains important even if Supabase is used operationally**

---

## 8. Primary Objects

The module will use four core objects:

### A. Source Record
A single ingested item and its processed review output.

Examples:
- one pasted X article
- one GitHub repo URL
- one X post brief file or text block

### B. Candidate Idea
A single extracted idea from one source record.

### C. Registry Idea
A deduplicated canonical idea that has survived scoring and promotion.

### D. Implementation Queue Item
A registry idea that is approved for design/build work.

---

## 9. Tranche 1 Lock (Approved — Complete)

Tranche 1 / Phase 1 is locked and implemented as documentation and contracts:

1. schema/contracts for the four canonical objects
2. scoring rubric mechanics (dimensions, formula, hard gates, bands, anti-hype cap)
3. dashboard page list and page build order
4. storage stance (JSON canonical machine truth)
5. tranche order, promotion states, and thresholds

No additional entities were authorized in Tranche 1.

---

## 10. Locked Dashboard Pages (Built Routes)

Canonical pages and current dashboard routes:

| Page | Route |
|------|--------|
| Master Idea Registry Review | `/foundry-registry-review` |
| Article Intake | `/foundry-article-intake` |
| GitHub Intake | `/foundry-github-intake` |
| X Post Intake | `/foundry-x-post-intake` |
| Implementation Queue | `/foundry-implementation-queue` |

Locked page build order (historical):
1. **Master Idea Registry Review**
2. **Article Intake**
3. **GitHub Intake**
4. **X Post Intake**
5. **Implementation Queue**

---

## 11. Locked Storage Stance

### Canonical stance
- **Local exportable JSON remains canonical machine truth** for this module’s structured state.
- Markdown may exist as human-readable companion state/summaries.
- Dashboard is the operator UI surface (no Supabase or DB-first move in Phases 1–5).
- Supabase is **Phase 6 optional** only, as an operational read/write/read-model layer — not started.

### Local state layout (under `future_modules/the_foundry/state/`)

| Path | Role |
|------|------|
| `source_records/` | Ingested source records (structured JSON). |
| `candidate_ideas/` | Extracted candidate ideas. |
| `registry_ideas/` | Canonical registry ideas (review/scoring surface). |
| `queue_recommendations/` | **Engine output:** batch JSON (`run_id`, `items[]`); historical/engine-generated queue recommendations. |
| `implementation_queue_items/` | **Operator-owned overlay:** per-`queue_id` JSON files; bounded dashboard edits persist here and override batch fields for that id when present. |
| `indexes/` | Engine inputs / index packets (e.g. example runner input). |

### Queue data rule (honest)
- Batch files under `queue_recommendations/` are engine output, not the operator edit log.
- Operator approval, notes, status, blockers, and `next_action` updates from the Implementation Queue page write **only** to `implementation_queue_items/<queue_id>.json`, full contract-valid item.

### Important rule
No promotion logic may depend on vague prose alone.

Scoring and registry promotion must use structured fields.

Phases 1–5 do not use database-only truth or SQLite-first state.

### Intake scoring reality (dashboard path, as built)
- **Bounded, deterministic, heuristic:** the eight rubric integers on candidates produced via dashboard intake are **derived from observable input characteristics** (e.g. length, lane, light structure, keyword signals)—**not** LLM semantic judgment of idea quality.
- **Locked formula still authoritative in engine:** the Python registry engine continues to apply the **locked weighted score**, hard gates, bands, and anti-hype cap when that pipeline runs on structured candidates.
- **Not full semantic ranking:** present intake scoring is **input-varying** mechanical scoring, not deep natural-language ranking of claims.

---

## 12. Locked Tranche Order

1. **Tranche 1:** official docs, schemas, scoring rubric, page list, storage decision, promotion states/thresholds
2. **Tranche 2:** local/core registry engine
3. **Tranche 3:** registry review dashboard page
4. **Tranche 4:** three intake pages
5. **Tranche 5:** implementation queue page
6. **Tranche 6:** optional expansion/read-model refinement/automation helpers

---

## 13. Current Operator Decision

Tranches 1–5 are implemented. The next sane step is **commit/push** of the repo state and any local JSON the operator chooses to version — not new feature work unless explicitly scoped.

A fresh chat for Phase 6 or follow-on fixes should begin from:
- this context anchor
- the module spec
- the master build checklist
- the handoff bundle

**Phase 6** (optional expansion: Supabase, automation helpers, bulk tools, etc.) is **not started** and is not implied by the current build.

---

## 14. One-Sentence Mission

**Build JARVIS THE FOUNDRY as a clean research intake, scoring, registry, and review system that helps the stock module absorb only the highest-value ideas.**

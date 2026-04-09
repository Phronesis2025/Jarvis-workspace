# JARVIS THE FOUNDRY — Handoff Bundle
**Last Updated:** 2026-04-11  
**Status:** Tranches 1–5 built; documentation aligned. Next step: commit/push (not new scope). Phase 6 optional — not started.

---

## 1. What We Are Building

We are building **JARVIS THE FOUNDRY**, a Jarvis module that ingests research sources and forges them into a ranked implementation system for the stock module.

This module combines:
- X article review outputs
- X post / research briefing outputs
- GitHub repo review outputs

The module will:
- ingest source inputs
- produce structured review outputs
- extract candidate ideas
- score and dedupe them
- promote surviving ideas into a master registry
- surface the best ideas in the dashboard
- maintain an implementation queue (engine batch output + operator overlay persistence)

**As built (Phases 1–5):** all five dashboard pages exist; local JSON under `future_modules/the_foundry/state/` remains canonical structured truth. There is **no** Phase 6 Supabase/automation expansion in progress.

---

## 2. Why This Matters

The operator has already done substantial research work.

The value is currently limited by fragmentation.

The missing layer is not more scanning.  
The missing layer is a **master registry and promotion system** that turns scattered findings into ranked, reviewable build decisions.

---

## 3. Official Module Name

**JARVIS THE FOUNDRY**

### Short pitch
A research-forging engine that turns raw findings into ranked implementation intelligence.

---

## 4. Approved Exception

The operator is intentionally approving a bounded exception to prior dashboard-first deferral for this module.

Reason:
The dashboard will materially speed up research intake and review.

This does **not** cancel the wider Jarvis discipline around:
- schemas
- bounded scope
- visible state
- human review
- explainable promotion logic

---

## 5. Non-Negotiable Design Stance

### The module must be:
- structured
- score-driven
- dedupe-aware
- human-reviewable
- dashboard-usable
- exportable

### The module must not be:
- a research junk drawer
- a hype feed
- a self-promoting AI commander
- an auto-builder from weak ideas

---

## 6. Core Build Decision

### Tranche order (locked)
1. Tranche 1: official docs, schemas, scoring rubric, page list, storage decision, promotion states/thresholds — **done**
2. Tranche 2: local/core registry engine — **done**
3. Tranche 3: registry review dashboard page — **done**
4. Tranche 4: three intake pages — **done**
5. Tranche 5: implementation queue page — **done**
6. Tranche 6: optional expansion/read-model refinement/automation helpers — **not started**

### First build truth
The dashboard is an operator surface.  
The registry logic is the core.

Do not build pretty chaos.

### Phase / tranche ladder (current)

| Phase | Scope | Status |
|-------|--------|--------|
| 1 | Docs, schemas, rubric, page list, storage lock | Complete |
| 2 | Local/core registry engine | Complete |
| 3 | Registry review dashboard | Complete |
| 4 | Three intake pages | Complete |
| 5 | Implementation queue page + operator overlay JSON | Complete |
| 6 | Optional expansion (e.g. Supabase, automation helpers) | **Not started** |

---

## 7. Required Dashboard Pages (Locked)

Implemented routes (Jarvis dashboard app):

| Page | Route |
|------|--------|
| Master Idea Registry Review | `/foundry-registry-review` |
| Article Intake | `/foundry-article-intake` |
| GitHub Intake | `/foundry-github-intake` |
| X Post Intake | `/foundry-x-post-intake` |
| Implementation Queue | `/foundry-implementation-queue` |

Locked build order:
1. **Master Idea Registry Review**
2. **Article Intake**
3. **GitHub Intake**
4. **X Post Intake**
5. **Implementation Queue**

**Supporting APIs (bounded, local-first):** `POST /api/foundry/intake`, `PATCH /api/foundry/queue-item` — not a workflow engine; validate and write exportable JSON only.

---

## 8. Canonical Data Objects (Locked)

The build must define and use:

- **Source Record**
- **Candidate Idea**
- **Registry Idea**
- **Implementation Queue Item**

No additional canonical entities are allowed in Tranche 1.

---

## 9. Required Scoring Dimensions and Mechanics (Locked)

Every candidate idea must be evaluated using all eight dimensions:

- evidence strength
- transferability
- expected upside
- risk reduction value
- implementation cost
- novelty
- dependency burden
- confidence

Scale: integer `0-5` per dimension.

Formula:

```text
(
  evidence_strength * 0.22 +
  transferability * 0.18 +
  expected_upside * 0.16 +
  risk_reduction_value * 0.14 +
  (5 - implementation_cost) * 0.10 +
  novelty * 0.08 +
  (5 - dependency_burden) * 0.07 +
  confidence * 0.05
) / 5 * 100
```

Hard gates:
- cannot rank above `watchlist` if `evidence_strength < 2`
- cannot rank above `watchlist` if `transferability < 2`
- cannot rank above `watchlist` if implementation implication is vague/missing
- cannot rank above `watchlist` if dedupe incomplete
- registry promotion requires human review

Recommendation bands:
- `discard`: `<35` or severe gate failure
- `watchlist`: `35-49`
- `research_next`: `50-64`
- `implement_soon`: `65-79`
- `queue_candidate`: `80+` and all hard gates passed

Anti-hype rule:
- cap at `watchlist` for hype-heavy items, bare tool mentions, unclear method, unresolved duplicates, or weak source-quality noise

### Intake scoring (dashboard) — current truth
- **Deterministic heuristics** on **observable** pasted text / URL characteristics populate the eight rubric fields—**input-varying**, **bounded**, **not** LLM semantic ranking.
- The **Python engine** still owns the **locked weighted formula** and gate/band logic when that code path runs.
- Treat “ranked” in UI copy as **mechanical score order** from that pipeline, not deep semantic ordering of ideas.

---

## 10. Immediate Questions the Build Chat Must Answer

1. What exact schema will each object use?
2. Where is the first durable source of truth?
3. What gets stored for each intake lane?
4. How is dedupe handled?
5. How are scores computed?
6. What requires human approval?
7. What dashboard data model is needed?
8. What is Tranche 1 versus later expansion?

For a post–Phase 5 chat, treat these as **largely settled** in `contracts/`, `state/`, and the dashboard sources; open **new** questions only for Phase 6 scope or bugfixes.

---

## 11. Recommended Storage Stance (Locked)

Use structured **local exportable JSON** as **canonical machine truth** for Foundry structured state.

Markdown may exist as human-readable companion state/summaries.
Dashboard is the operator UI surface.
Supabase is **Phase 6 optional** as an operational read/write/read-model layer only — **not in use for Phases 1–5**.

### Local state layout (`future_modules/the_foundry/state/`)

- `source_records/` — source records
- `candidate_ideas/` — candidates
- `registry_ideas/` — registry ideas
- `queue_recommendations/` — **engine batch output** (history; `run_id` + `items`)
- `implementation_queue_items/` — **operator-owned overlay** (`<queue_id>.json`); Implementation Queue page writes here; merges over batch items for the same `queue_id`
- `indexes/` — engine/index inputs

Rules:
- promotion/scoring/queue recommendation must read structured JSON, not prose
- Phases 1–5: no database-only truth, no SQLite-first state
- do not treat `queue_recommendations/` as the operator edit log — edits live in `implementation_queue_items/`

---

## 12. What a Good First Deliverable Looks Like

A good first deliverable from the new build conversation would define:

- module scope
- canonical entities
- required fields
- scoring rubric
- promotion flow
- dashboard page inventory
- storage stance
- first tranche plan

If the first deliverable tries to jump straight into flashy automation, it is drifting.

---

## 13. One-Line Build Goal

**Build JARVIS THE FOUNDRY into a clean, score-driven intake and registry system that makes the next best stock-module idea obvious.**

---

## 14. Post–Phase 5 Handoff Note

- **Phases 1–5** are implemented per the master checklist and module spec.
- **Phase 6** is explicitly optional and **not started**; do not assume Supabase or automation is approved or in progress.
- **Next step after doc lock:** commit and push (and version any local JSON the operator wants in git), **not** open-ended new feature work unless re-scoped.

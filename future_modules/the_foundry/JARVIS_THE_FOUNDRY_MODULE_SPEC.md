# JARVIS THE FOUNDRY — Module Specification
**Last Updated:** 2026-04-11  
**Status:** Contracts locked; Phases 1–5 built. Phase 6 optional — not started.  
**Type:** Official module definition

---

## 1. Module Purpose

JARVIS THE FOUNDRY converts research inputs into ranked implementation intelligence.

It ingests:
- X article review inputs
- GitHub repo review inputs
- X post / briefing inputs

It outputs:
- structured review records
- extracted candidate ideas
- scored and deduplicated registry ideas
- a human-reviewed implementation queue

---

## 2. Product Problem

The research system has useful inputs but weak consolidation.

### Current pain
- article reviews are isolated
- GitHub review findings are isolated
- X brief outputs are isolated
- good ideas do not automatically accumulate into one ranked master system
- the operator lacks one obvious view of “what should we implement next?”

### Module answer
Create one repeatable pipeline:  
**intake -> review -> idea extraction -> scoring -> dedupe -> promotion -> review -> implementation queue**

---

## 3. In Scope

### Intake lanes
1. Article text
2. GitHub link
3. X post / briefing text

### Core processing
1. source record creation
2. structured review generation
3. candidate idea extraction
4. scoring
5. deduplication
6. promotion recommendation
7. registry update
8. queue recommendation

### Dashboard surfaces
1. source intake pages
2. source-lane top-10 tables
3. master idea registry review page
4. implementation queue page

---

## 4. Out of Scope for Initial Build

- auto-building code directly from new ideas
- autonomous implementation approval
- broad multi-agent orchestration
- full generalized research crawler expansion
- production-grade portfolio/risk engine
- replacing existing stock-module research flows immediately

---

## 5. Canonical Entities (Locked)

### 5.1 Source Record
Represents one ingested source and its processed review.

Required fields:
- source_id
- source_type
- source_lane
- input_mode
- title
- raw_input_ref
- processed_output_ref
- source_url_or_locator
- source_hash
- ingestion_method
- source_timestamp
- created_at
- reviewer_model
- review_version
- extraction_version
- review_status
- extraction_status
- review_summary
- key_claims
- quality_flags
- processing_notes
- candidate_ids

Locked enums:
- source_type: `article_text | github_repo | x_post_brief`
- source_lane: `article | github | x_post`
- review_status: `pending | complete | failed | escalated`
- extraction_status: `not_started | complete | failed | escalated`

### 5.2 Candidate Idea
Represents one idea extracted from one source record.

Required fields:
- candidate_id
- source_id
- source_lane
- title
- summary
- category
- claim
- implementation_implication
- problem_solved
- proposed_pattern
- idea_kind
- confidence
- evidence_strength
- transferability
- expected_upside
- risk_reduction_value
- implementation_cost
- novelty
- dependency_burden
- needs_validation
- verification_gaps
- duplicate_group_key
- dedupe_confidence
- registry_match_id
- recommendation_state
- recommendation_reason
- extraction_method
- created_at

Locked enums:
- idea_kind: `pattern | workflow | component | control | architecture | research_method | data_method | tooling`
- recommendation_state: `discard | watchlist | research_next | implement_soon | queue_candidate`

### 5.3 Registry Idea
Represents a promoted canonical idea.

Required fields:
- idea_id
- title
- summary
- category
- canonical_problem
- canonical_pattern
- dedupe_key
- source_refs
- supporting_source_count
- contradicting_source_count
- confidence
- evidence_strength
- transferability
- expected_upside
- risk_reduction_value
- implementation_cost
- novelty
- dependency_burden
- score_breakdown
- weighted_score
- status
- review_state
- promotion_reason
- review_notes
- implementation_notes
- dependencies
- related_ideas
- queue_eligibility
- queue_reason
- first_seen_at
- created_at
- last_updated

Locked enums:
- status: `active | watchlist | research_next | implement_soon | queued | archived | rejected`
- review_state: `pending_review | approved_registry | rejected_registry | needs_more_research`

### 5.4 Implementation Queue Item
Represents an idea selected for design/build work.

Required fields:
- queue_id
- idea_id
- queue_rank
- priority_band
- why_now
- required_resources
- expected_build_output
- owner
- operator_approval_state
- approval_notes
- target_module
- effort_estimate
- dependency_status
- source_confidence_snapshot
- success_criteria
- next_action
- status
- blockers
- created_at
- last_updated

Locked enums:
- status: `proposed | ready | in_design | in_build | blocked | done | dropped`
- operator_approval_state: `pending | approved | rejected`

---

## 6. Scoring Rubric (Locked)

Each candidate idea should be scored on:

1. **Evidence Strength**
2. **Transferability**
3. **Expected Upside**
4. **Risk Reduction Value**
5. **Implementation Cost**
6. **Novelty**
7. **Dependency Burden**
8. **Confidence**

Scale: integer `0-5` per dimension.

Weighted score formula:

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
- cannot rank above `watchlist` if `implementation_implication` is vague/missing
- cannot rank above `watchlist` if dedupe is incomplete
- registry promotion still requires human review

Recommendation bands:
- `discard`: `<35` or severe gate failure
- `watchlist`: `35-49`
- `research_next`: `50-64`
- `implement_soon`: `65-79`
- `queue_candidate`: `80+` and all hard gates passed

Anti-hype cap:
- cap at `watchlist` if mostly hype, bare tool mention, unclear method, unresolved duplicate, or weak source-quality noise

### 6.1 Intake path vs engine (as implemented)
- **Dashboard intake:** fills the eight dimension fields with **deterministic heuristics** from **observable** pasted text or URL traits. Scores **vary with input**; they are **not** semantic/LLM judgments of the idea.
- **Registry engine (Python):** still computes **weighted_score** from those fields using the **locked formula** above, plus gates and recommendation bands—when the engine path runs on stored structured candidates.
- This is **not** full semantic ranking across idea meaning; it is **bounded mechanical** scoring plus the **locked** downstream formula.

---

## 7. Promotion Rules (Locked)

### Promotion should require:
- complete structured fields
- acceptable evidence minimum
- dedupe check complete
- scoring complete
- human review complete

Locked promotion states and thresholds:
- recommendation path: `discard -> watchlist -> research_next -> implement_soon -> queue_candidate`
- registry state gate: `review_state` must be `approved_registry` before implementation queue progression

### Promotion should not happen if:
- evidence is too thin
- idea is already captured well enough in registry
- implementation implication is vague
- source quality is too weak
- the “idea” is really just hype, a tool mention, or a screenshot result with no method

---

## 8. Dashboard Surface Design (Locked List + Order)

Locked pages (exactly five) and **implemented routes**:

| Page | Route |
|------|--------|
| Master Idea Registry Review | `/foundry-registry-review` |
| Article Intake | `/foundry-article-intake` |
| GitHub Intake | `/foundry-github-intake` |
| X Post Intake | `/foundry-x-post-intake` |
| Implementation Queue | `/foundry-implementation-queue` |

Locked build order:
1. Master Idea Registry Review
2. Article Intake
3. GitHub Intake
4. X Post Intake
5. Implementation Queue

### 8.1 Article Intake Page
Operator pastes article text and receives:
- structured review
- candidate ideas
- top 10 extracted ideas for article lane
- storage confirmation

### 8.2 GitHub Intake Page
Operator pastes GitHub link and receives:
- repo review output
- candidate ideas
- top 10 extracted ideas for GitHub lane
- storage confirmation

### 8.3 X Post Intake Page
Operator pastes post text or briefing block and receives:
- structured review
- candidate ideas
- top 10 extracted ideas for X-post lane
- storage confirmation

### 8.4 Master Idea Registry Review Page
Should show:
- top ranked ideas
- filters by status/category/source lane
- supporting source count
- score breakdown
- promotion reason
- implementation notes
- related ideas

### 8.5 Implementation Queue Page
Should show:
- next ideas to build (by `queue_rank`; no extra automation beyond deterministic ordering)
- queue rank
- required resources and expected build output (contract fields)
- blockers and status
- operator approval state, approval notes, and `next_action`

**As built:** the queue page reads `state/queue_recommendations/*.json` and overlays `state/implementation_queue_items/<queue_id>.json` when present; bounded operator edits persist only to the overlay files (full Implementation Queue Item v1).

---

## 9. Storage Model

### Initial recommended model
- **Local exportable JSON is canonical machine truth** for structured Foundry state.
- Dashboard is the operator UI surface.
- Markdown can exist as companion human-readable state/summaries.
- Promotion/scoring/queue recommendation must read structured JSON, not prose.

### Local state directories (implemented)

Under `future_modules/the_foundry/state/`:

- `source_records/` — ingested sources and processed review pointers/metadata as JSON.
- `candidate_ideas/` — extracted candidates.
- `registry_ideas/` — canonical registry ideas for review.
- `queue_recommendations/` — **engine batch output** (history/run artifacts); not the operator edit log.
- `implementation_queue_items/` — **operator-owned persistence** for queue items keyed by `queue_id`; overrides batch fields for that id when file exists.
- `indexes/` — engine/index inputs (e.g. example packets).

### Supabase stance
Supabase is **Phase 6 optional** as an operational read/write/read-model layer only — **not started**.

Phases 1–5 do not:
- switch to database-only truth
- introduce SQLite-first state

---

## 10. Worker/Process Requirement

This module may include a promotion/registry process, but it must still obey Jarvis worker discipline.

Any active registry worker/process must define:
- purpose
- scope
- input packet
- output contract
- QA path
- escalation rules

No undefined “AI commander” nonsense.

---

## 11. Success Criteria

The first successful version of JARVIS THE FOUNDRY is achieved when:

1. three source lanes can ingest cleanly
2. source reviews are stored consistently
3. candidate ideas are extracted in structured form
4. ideas are scored and deduped
5. registry ideas are reviewable in one place
6. implementation queue candidates are obvious
7. operator time-to-ingest and time-to-decide are materially lower than current workflow

---

## 12. Failure Modes to Avoid

- vague schemas
- duplicate idea explosion
- score inflation
- dashboard pages with no reliable backend
- over-automation before promotion rules are trusted
- building pretty UI over weak logic
- letting the module become a giant research junk drawer

---

## 13. Tranche Order (Locked)

1. Tranche 1: official docs, schemas, scoring rubric, page list, storage decision, promotion states/thresholds — **complete**
2. Tranche 2: local/core registry engine — **complete**
3. Tranche 3: registry review dashboard page — **complete**
4. Tranche 4: three intake pages — **complete**
5. Tranche 5: implementation queue page — **complete**
6. Tranche 6: optional expansion/read-model refinement/automation helpers — **not started**

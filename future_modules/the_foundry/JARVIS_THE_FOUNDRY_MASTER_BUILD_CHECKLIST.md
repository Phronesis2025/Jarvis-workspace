# JARVIS THE FOUNDRY — Master Build Checklist
**Last Updated:** 2026-04-13  
**Status:** Phases 1–5 complete; intake A/B scoring modes + `scoring_evaluations/` sidecar; **minimal Vercel persistence** (fs/Blob adapter + Node engine on hosted). Phase 6 not started.

---

## Phase Ladder

- [x] Research intake concept defined
- [x] Need for unified idea registry identified
- [x] Dashboard-first exception approved for this module
- [x] **Phase 1 — Docs/Schemas/Rubric/Page-List/Storage Lock**
- [x] Phase 2 — Core registry engine
- [x] Phase 3 — Dashboard review surfaces
- [x] Phase 4 — Dashboard intake surfaces
- [x] Phase 5 — Queue and promotion refinement
- [ ] Phase 6 — Optional automation/read-model expansion  ← **not started; optional only**

---

## Phase 1 — Registry Foundation

- [x] Lock official module name
- [x] Lock module purpose and scope
- [x] Lock source lanes
- [x] Lock canonical entity set (exactly 4): Source Record, Candidate Idea, Registry Idea, Implementation Queue Item
- [x] Lock required fields per entity
- [x] Lock scoring rubric dimensions and weighted formula
- [x] Lock hard gates and anti-hype cap rules
- [x] Lock promotion states/review states
- [x] Lock discard/watchlist/research_next/implement_soon/queue_candidate thresholds
- [x] Lock first storage stance
- [x] Lock first dashboard page list (exactly 5 pages)
- [x] Lock page build order

### Exit condition
A new build conversation can start implementation planning without arguing about definitions.

---

## Phase 2 — Core Registry Engine

- [x] Implement Source Record schema contract in local/core engine
- [x] Implement Candidate Idea schema contract in local/core engine
- [x] Implement Registry Idea schema contract in local/core engine
- [x] Implement Implementation Queue Item schema contract in local/core engine
- [x] Define dedupe rules
- [x] Define score computation rules
- [x] Define promotion recommendation rules
- [x] Define export formats
- [x] Define failure / escalation outputs

### Exit condition
A structured source input can become a scored candidate idea set and a reviewable registry update.

### Implemented paths
- Engine library: `future_modules/the_foundry/engine/foundry_registry_engine.py`
- Runner: `future_modules/the_foundry/scripts/run_foundry_registry_engine.py`
- Script usage: `future_modules/the_foundry/scripts/README.md`
- Contracts: `future_modules/the_foundry/contracts/`
- Local canonical state root: `future_modules/the_foundry/state/`
- Example input: `future_modules/the_foundry/state/indexes/example_engine_input.json`
- **Dashboard parity engine (hosted / Node):** `dashboard/src/lib/foundry-registry-engine-node.ts` — same locked formula and gates as Python; used when `VERCEL=1`, `FOUNDRY_STORAGE_DRIVER=blob`, or `FOUNDRY_ENGINE_RUNTIME=node`.

### Hosting / persistence (dashboard — doc lock)
- **Storage adapter:** `dashboard/src/lib/foundry-storage.ts` — `getJson` / `putJson` / `listJsonKeys` / `listJsonMeta` / `exists`; backends **fs** (default) and **Vercel Blob** (`@vercel/blob`).
- **Hosted env (durable runtime):** `FOUNDRY_STORAGE_DRIVER=blob` + `BLOB_READ_WRITE_TOKEN`. Optional aliases for driver: `vercel_blob`, `vercel-blob`.
- **Local dev:** omit driver or `FOUNDRY_STORAGE_DRIVER=fs`; intake may use **Python** engine (`py -3`) when Node path is not selected.
- **Vercel:** Root Directory **`dashboard/`**; ensure repo layout exposes `../future_modules/the_foundry/` at runtime (include files outside root if required).
- **Merge reads:** `dashboard/src/lib/foundry-read-merge.ts` (+ queue/registry loaders) — repo `state/` seed + Blob runtime for hosted dashboards.

---

## Phase 3 — Dashboard Review Surfaces

- [x] Build Master Idea Registry Review page
- [x] Build filters for category / status / source lane
- [x] Build score display
- [x] Build supporting-source display
- [x] Build promotion notes display
- [x] Build related-idea view
- [x] Build top-idea summary cards

### Exit condition
The operator can clearly see the best ideas and why they rank high.

### Implemented route and read model
- Dashboard route: `dashboard/src/app/foundry-registry-review/page.tsx`
- Client view: `dashboard/src/components/FoundryRegistryReviewClient.tsx`
- Read-only data loader: `dashboard/src/lib/data.ts#getFoundryRegistryReviewData` (storage adapter + seed/Blob merge when Blob driver)
- Inputs: `foundry/registry_ideas/*` and `foundry/source_records/*` via adapter; local fs maps to `future_modules/the_foundry/state/…`

---

## Phase 4 — Dashboard Intake Surfaces

- [x] Build Article Intake page
- [x] Build GitHub Intake page
- [x] Build X Post Intake page
- [x] Build source-lane top-10 tables
- [x] Build intake status feedback
- [x] Build storage confirmation
- [x] Ensure all three lanes flow into same registry logic

### Exit condition
New inputs can be added quickly without leaving the dashboard.

### Implemented routes and intake API
- `dashboard/src/app/foundry-article-intake/page.tsx`
- `dashboard/src/app/foundry-github-intake/page.tsx`
- `dashboard/src/app/foundry-x-post-intake/page.tsx`
- `dashboard/src/app/api/foundry/intake/route.ts`
- `dashboard/src/components/FoundryLaneIntakeClient.tsx`
- `dashboard/src/lib/foundry-intake.ts` (Python engine locally when selected; Node engine on Vercel / Blob)
- `dashboard/src/lib/foundry-scoring.ts` (client-safe scoring helpers; weighted preview matches Python engine)
- `dashboard/src/lib/foundry-rubric-anchors.ts` (explicit 0–5 anchor strings + version id)
- `dashboard/src/lib/foundry-rubric-proposal.ts` (Option A bounded anchor → proposal)
- `dashboard/src/lib/foundry-scoring-persistence.ts` (server-only sidecar writes via storage adapter)
- `dashboard/src/lib/foundry-storage.ts`, `dashboard/src/lib/foundry-read-merge.ts`, `dashboard/src/lib/foundry-registry-engine-node.ts`
- `dashboard/src/app/api/foundry/score-preview/route.ts` (Option B manual rubric weighted preview; no disk writes)
- `dashboard/src/app/api/foundry/option-a-preview/route.ts` (Option A proposal preview; no engine / no sidecar)

### Intake scoring truth (doc lock)
- **Option A (`option_a_rubric_assisted`):** **Explicit-anchor rubric proposal** (see `docs/OPTION_A_RUBRIC_ANCHOR_MATRIX.md`) → proposed integers + reasons + source-tied evidence. **Heuristic prefill** (legacy buckets) is stored as `heuristic_prefill_scores` only—not final rubric truth. Operator **locks** final integers (`option_a_locked_rubric_scores`); engine uses **finals** only. Not LLM semantic ranking.
- **Option B (`option_b_manual_matrix`):** operator supplies all eight integers 0–5; engine applies **locked formula** only.
- **Persisted audit:** each intake run writes `scoring_evaluations/eval_<candidate_id>.json` at logical path `foundry/scoring_evaluations/…` (fs → `state/scoring_evaluations/`; Blob → same key under Blob). Fields: `scoring_mode_selected`, `evaluation_method`, `heuristic_prefill_scores`, `proposed_scores`, `final_scores`, `score_reasons`, `evidence_support`, `weighted_score`, and when applicable `rubric_anchor_version`. Flipping the UI toggle does not rewrite past files.
- **Engine:** **Python** `foundry_registry_engine.py` locally when selected; **Node** `foundry-registry-engine-node.ts` on hosted — **locked weighted formula and gates unchanged**; operates on the eight **final** integers.

---

## Phase 5 — Queue and Promotion Refinement

- [x] Build Implementation Queue page
- [x] Add bounded operator review actions (local JSON persistence)
- [x] Surface next-best ordering via `queue_rank` (deterministic; no extra automation)
- [x] Display “why now” and “required resources” from locked queue contract
- [x] Add blocker tracking (contract field + operator edits)
- [x] Add implementation status tracking (`status` enum)

### Exit condition
The module provides a clean next-best implementation queue, not just idea storage.

### Implemented route, read model, and writes
- Dashboard route: `dashboard/src/app/foundry-implementation-queue/page.tsx` → **`/foundry-implementation-queue`**
- Client: `dashboard/src/components/FoundryImplementationQueueClient.tsx`
- Queue loader + validation: `dashboard/src/lib/foundry-queue.ts` (adapter + seed/Blob merge)
- Operator PATCH API: `dashboard/src/app/api/foundry/queue-item/route.ts`
- Reads: `foundry/queue_recommendations/*.json` (engine batches) and registry context from `foundry/registry_ideas/*` (enrichment)
- Writes: `foundry/implementation_queue_items/<queue_id>.json` (operator overlay; full v1 item, contract-valid)

### Local state tree (reference)

`future_modules/the_foundry/state/`

- `source_records/`
- `candidate_ideas/`
- `registry_ideas/`
- `queue_recommendations/` — engine batch JSON
- `implementation_queue_items/` — operator-owned queue overlay
- `indexes/`
- `scoring_evaluations/` (intake sidecars)

---

## Phase 6 — Optional Expansion

- [ ] Add Supabase read/write refinement if needed
- [ ] Add automation helpers
- [ ] Add bulk import helpers
- [ ] Add historical scoring review tools
- [ ] Add stale-idea audit checks
- [ ] Add contradiction / overlap checks

### Exit condition
Expansion improves operator speed without destabilizing the core logic.

**Status:** Not started. No Phase 6 work is implied by Phases 1–5.

---

## Hard Rules

- [ ] No vague entity definitions
- [ ] No auto-promotion without review in first build
- [ ] No dashboard page without a clear backend contract
- [ ] No queue item without a reason, resource note, and status
- [ ] No implementation hype before registry logic works
- [ ] No scope creep into “general AI research platform”

---

## First Tranche Recommendation

### Tranche 1
- official docs
- schemas
- scoring rubric
- page list
- storage decision
- promotion states/thresholds

### Tranche 2
- local/core registry engine

### Tranche 3
- registry review dashboard page

### Tranche 4
- three intake pages

### Tranche 5
- implementation queue page

### Tranche 6
- optional expansion/read-model refinement/automation helpers

That is the sane order.

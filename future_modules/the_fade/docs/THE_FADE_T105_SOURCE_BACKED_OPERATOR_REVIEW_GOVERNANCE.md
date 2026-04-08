# THE FADE — T105 source-backed operator review (governance lock)

**Prompt #:** 396  
**Phase #:** 3 — **local pipeline governance** (T105 docs only; no source-backed review code in this tranche)  
**Tranche #:** 105  
**Label:** `THE_FADE_PHASE3_T105_GOVERNANCE_LOCK_SOURCE_BACKED_OPERATOR_REVIEW`  

**Updated:** 2026-04-08T17:28:17+00:00  

---

## Purpose

T102 produces **`operator_review.md`** from run-folder packets. T104 produces **`source_snapshot.json`** from the same bounded inputs. The next smallest operator-meaningful improvement is **one** merged, factual review that presents **both** what the run produced **and** what Federal Register source context was captured on disk — without new plumbing, new fetches, or scanner semantics.

T105 governs exactly one future implementation tranche for one **source-backed operator review** script. It must read only existing run-folder artifacts and write one concise markdown review. No AI, no inference-heavy analysis, no scanner claims.

T105 does not implement the review surface.

**Companion:** `THE_FADE_T105_SOURCE_BACKED_OPERATOR_REVIEW_ACCEPTANCE_CRITERIA.md`  
**Machine-readable note:** `phase2_mvp_approval_scope_decision.json` -> `post_t105_source_backed_operator_review_governance`

---

## 1) Exact governed slice

One future implementation tranche may add one local source-backed operator review script only that:

- reads exactly one existing completed run folder under  
  `future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`
- reads **only** these files in that folder (each must exist for a successful PASS of that invocation):
  - `run_summary.json`
  - exactly one copied request JSON matching `fr_universe_scanner_request_*.json`
  - exactly one copied result JSON matching `bridge_universe_scanner_result_*.json`
  - `operator_review.md` (T102 output)
  - `source_snapshot.json` (T104 output)
- writes **exactly one** operator-readable markdown review artifact in that same run folder (section 3)
- local-only, factual-only, bounded extraction and **simple transparent derived counts** only (for example counts already computable from result JSON — same class as T102)
- **no** cross-folder reads, **no** history scans, **no** network I/O

---

## 2) Exact future artifact allowance

Allowed in the future implementation tranche:

1. One script only at fixed path (section 3).
2. Optional small README only in the same directory as that script.
3. Optional one tiny helper `.py` only in the same directory if strictly necessary and explicitly named in the README.
4. One review artifact only at fixed name (section 3), per processed run folder.

Forbidden:

- second entrypoint,
- framework buildout,
- extra reporting surfaces outside this slice.

---

## 3) Fixed implementation path and artifact name

Implementation path is fixed to:

`future_modules/the_fade/review/local_run/build_source_backed_operator_review_from_run_folder.py`

Review artifact filename is fixed to:

`source_backed_operator_review.md`

---

## 4) What the review surface may do

The future script may:

- open one run folder supplied by path/basename (same resolution convention as existing `review/local_run` scripts),
- load the five governed files only,
- extract **factual** fields already present in JSON/markdown on disk,
- compute **simple transparent counts** from the copied result JSON (for example length of `candidate_outputs`, count of `row_status == deferred`) — **no** new interpretation beyond mechanical counting,
- **merge** into one markdown outline:
  - **Run / pipeline facts** (from `run_summary.json`, request/result JSON, and non-duplicative pointers to paths already listed),
  - **Source context facts** (from `source_snapshot.json` — for example `source_name`, `universe_source_ref`, `candidate_source_packet_ref`, `scan_policy_version`, verbatim `operator_notes` **only if** reproduced from JSON already in snapshot or request without rewriting),
- optionally reference that `operator_review.md` exists and its role (factual pointer only — **no** re-summarization beyond quoting bounded lines if needed for linkage, prefer avoiding large paste),
- print local PASS/FAIL and output path.

**Merge rule:** Do **not** paraphrase Federal Register or invent document lists. Prefer citing **exact strings** from `source_snapshot.json` / request JSON fields already on disk.

---

## 5) Allowed review artifact content (bounded)

Allowed content is factual and bounded, including:

- run id / folder name  
- run status from `run_summary.json`  
- request path and result path (as recorded on disk — copied paths and/or `source_*` paths from `run_summary.json` when present)  
- request id, contract version  
- source name (must match factual `source_name` from `source_snapshot.json` when present, or literal `Federal Register` only if consistent with `universe_source_ref` on disk)  
- `universe_source_ref`, `candidate_source_packet_ref`, `scan_policy_version` (from snapshot and/or request — **same values on disk**, no reconciliation “logic” beyond listing once)  
- `scanner_status` from result JSON  
- count of `candidate_outputs`, count of `deferred` (mechanical)  
- warnings already on disk (from result JSON)  
- timestamps already on disk (`as_of_utc`, `produced_at_utc`, run start/finish, etc.)  
- **`results_count` only if** already present as a numeric field in `source_snapshot.json` (do not re-parse ingress text unless identical mechanical rule to T104 is explicitly duplicated — prefer reading the snapshot field only)  
- explicit statement: this is **not** a scanner decision artifact and **not** a decision engine  

**Not allowed:**

- recommendations, prioritization, trade ideas, buyer-fit, ranking, scoring, “should buy/sell” language  
- claims that the run “validated” markets or “selected” outcomes  
- LLM-generated narrative or paraphrase of source documents  

---

## 6) Explicitly forbidden in the future implementation tranche

- AI/LLM summarization  
- recommendations or trade ideas  
- ranking/scoring/selection logic  
- new data fetches / network calls  
- provider adapters/clients  
- dashboard/UI  
- runtime orchestration  
- scheduling/jobs/workers  
- lane reopen  
- evidence collection  
- registry/approval edits  
- multi-slice bundling  
- hidden intelligence creep  
- broad reporting framework buildup  
- pretending the review is a scanner or automated decision system  

---

## 7) Anti-drift rules

1. One implementation slice only.  
2. One script only at fixed path.  
3. One review artifact only at fixed name.  
4. One run folder at a time.  
5. No “while we’re here” extras.  
6. No widening into intelligence, dashboards, provider expansion, or orchestration.

---

## 8) Non-claims

- T105 does not implement the script.  
- T105 does not authorize scanner/runtime/provider/dashboard expansion.  
- T105 does not authorize production orchestration or approval/lane changes.  
- T105 does not require re-running T89 ingress; it consumes **already materialized** run-folder artifacts only.

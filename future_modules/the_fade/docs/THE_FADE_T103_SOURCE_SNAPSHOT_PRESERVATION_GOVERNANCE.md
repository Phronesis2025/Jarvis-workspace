# THE FADE — T103 source snapshot preservation (governance lock)

**Prompt #:** 393  
**Phase #:** 3 — **local pipeline governance** (T103 docs only; no source-snapshot code in this tranche)  
**Tranche #:** 103  
**Label:** `THE_FADE_PHASE3_T103_GOVERNANCE_LOCK_SOURCE_SNAPSHOT_PRESERVATION`  

**Updated:** 2026-04-08T16:36:15+00:00  

---

## Purpose

T100–T102 give operators a clean per-run folder, summary, and factual `operator_review.md`. The next smallest operator-meaningful improvement is one bounded **source snapshot** in that same run folder so operators can see **what Federal Register context the run was tied to**, using **only data already on disk** for that run — not new fetches and not scanner semantics.

T103 governs exactly one future implementation tranche for one local **source snapshot preservation** script. It must preserve a **factual, bounded** snapshot artifact inside the run folder. No AI, no speculative analysis, no scanner claims.

T103 does not implement the snapshot surface.

**Companion:** `THE_FADE_T103_SOURCE_SNAPSHOT_PRESERVATION_ACCEPTANCE_CRITERIA.md`  
**Machine-readable note:** `phase2_mvp_approval_scope_decision.json` -> `post_t103_source_snapshot_preservation_governance`

---

## 1) Exact governed slice

One future implementation tranche may add one local source-snapshot script only that:

- reads exactly one existing completed run folder under  
  `future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`
- preserves **one** bounded factual source snapshot for that run **in that same run folder**
- uses **only** already-fetched or already-governed ingress-related facts available from the **read boundary** below (no new network I/O in the snapshot tranche)
- local-only, factual-only, bounded extraction and transparent mechanical counts only

---

## 2) Exact future artifact allowance

Allowed in the future implementation tranche:

1. One script only at fixed path (section 7).
2. Optional small README only in the same directory as that script.
3. Optional one tiny helper `.py` only in the same directory if strictly necessary and explicitly named in the README.
4. One snapshot artifact only at fixed name (section 7), per processed run folder.

Forbidden:

- second entrypoint,
- framework buildout,
- extra reporting surfaces outside this slice.

---

## 3) Read boundary (strict)

The future script may read **only** the following, for **one** run folder per invocation:

**Required (when present):**

- `run_summary.json` in that run folder
- exactly one copied request JSON in that run folder matching `fr_universe_scanner_request_*.json`
- exactly one copied result JSON in that run folder matching `bridge_universe_scanner_result_*.json`

**Optional:**

- `operator_review.md` in that run folder — **optional**; do not require it for PASS

**Explicit dependency on Federal Register “raw” API body:**

- As of **T89** ingress on disk, the Federal Register documents API **JSON body is not** written as a separate companion file; the **UniverseScannerRequest** packet holds bounded refs and **`operator_notes`** text that includes a factual **`results_count=`** summary line per T89’s fixed wording.
- Therefore this slice **does not** authorize reading arbitrary other directories, history scans, or “find any FR response on disk.”
- If a **later** governed ingress tranche introduces a **single** bounded companion artifact (for example one JSON file colocated with the request under `inputs/phase3_universe_scanner_requests/` with a **fixed naming rule** documented in that tranche’s governance), **extending** the read boundary requires a **new governance tranche** — **not** implied by T103.

---

## 4) Write boundary

- Writes **exactly one** factual source snapshot file in the **same** run folder.
- Fixed artifact name (singular): **`source_snapshot.json`**
- No other new files in the run folder from this script.

---

## 5) Allowed snapshot content (bounded)

Content must be **factual** and derived only from the read boundary. Examples of **allowed** fields / sections:

- **Source identity:** literal source name **`Federal Register`** (fixed string), plus `universe_source_ref` from the copied request JSON when present
- **Query / reference:** `candidate_source_packet_ref` from the copied request (includes the bounded query URL already stored on disk)
- **Ingress policy label:** `scan_policy_version` from the copied request
- **Request envelope:** `request_id`, `contract_version`, `as_of_utc` from the copied request
- **Verbatim ingress summary:** full verbatim string value of `operator_notes` from the copied request (no rewriting)
- **Transparent mechanical count (optional):** integer `results_count` **only** if extracted by a **fixed, documented** substring match against `operator_notes` consistent with T89’s format (`results_count=<integer>`); if not parseable, omit or record `null` with no inference
- **Run linkage (factual):** `run_id`, `started_at_utc`, `finished_at_utc`, `status` from `run_summary.json` when present
- **Result envelope (context only, not scanner output):** `produced_at_utc`, `scanner_status` from copied result JSON — **must not** be presented as scan completion or intelligence
- **Explicit statement** (required string field or prominent JSON property): this artifact is a **factual source snapshot**, **not** a scanner decision artifact and **not** a ranking or recommendation

**Not allowed in the artifact:**

- recommendations, prioritization, buyer-fit, scoring, ranking, “best” language
- document lists, titles, or identifiers **not** literally present in the read-boundary JSON/text fields
- paraphrased or LLM-generated summaries of source content

---

## 6) Explicitly forbidden in the future implementation tranche

- AI/LLM summarization  
- recommendations or trade ideas  
- ranking/scoring/selection logic  
- **new** live fetches or multi-source ingestion (no `urllib`, HTTP clients, or subprocess calls to ingress tools)  
- provider adapters/clients beyond what is already on disk  
- dashboard/UI  
- runtime orchestration  
- scheduling/jobs/workers  
- lane reopen  
- evidence collection  
- registry/approval edits  
- multi-slice bundling  
- hidden intelligence creep  
- broad reporting framework buildup  
- pretending a source snapshot is scanner output  

---

## 7) Fixed implementation path and artifact name

Implementation path is fixed to:

`future_modules/the_fade/review/local_run/build_source_snapshot_from_run_folder.py`

Snapshot artifact filename is fixed to:

`source_snapshot.json`

---

## 8) Anti-drift rules

1. One implementation slice only.  
2. One script only at fixed path.  
3. One run folder at a time.  
4. One snapshot artifact only at fixed name.  
5. No “while we’re here” extras.  
6. No widening into intelligence, dashboards, provider expansion, or orchestration.

---

## 9) Non-claims

- T103 does not implement the snapshot script.  
- T103 does not authorize scanner/runtime/provider/dashboard expansion.  
- T103 does not authorize production orchestration or approval/lane changes.  
- T103 does not assert that full Federal Register document payloads exist on disk today.

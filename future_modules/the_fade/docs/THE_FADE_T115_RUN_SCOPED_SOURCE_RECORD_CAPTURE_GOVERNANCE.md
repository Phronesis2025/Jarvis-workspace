# THE FADE — T115 Run-Scoped Source-Record Capture (Governance Lock)

**Label:** `THE_FADE_PHASE3_T115_GOVERNANCE_LOCK_RUN_SCOPED_SOURCE_RECORD_CAPTURE`  
**Prompt #:** 413  
**Tranche #:** 115  
**Phase:** 3 — local pipeline (scanner-enabling slice; **not** a scanner)  
**Updated:** 2026-04-09T18:30:00+00:00

**Authority:** This file is **governance and boundary only**. It **does not** implement executable code. **T115** locks **exactly one** future implementation tranche: a **single** local script that, for **one** completed happy-path run folder, performs **one** bounded read-only Federal Register API fetch aligned with that run’s already-stored query reference, and writes **one** factual **`source_records_snapshot.json`** beside the run’s other artifacts. This slice **preserves** bounded Federal Register **source records** for **one** run — it is **not** scanner execution, **not** ranking or scoring, **not** selection, **not** AI/LLM output, and **not** a trading or investment recommendation.

**Companion:** `THE_FADE_T115_RUN_SCOPED_SOURCE_RECORD_CAPTURE_ACCEPTANCE_CRITERIA.md`  
**Machine-readable pointer:** `future_modules/the_fade/config/phase3_t115_run_scoped_source_record_capture.json`

---

## 1. Slice identity (exactly one implementation tranche later)

| Property | Value |
|----------|--------|
| Slice name | Run-scoped Federal Register source-record capture |
| Future build tranche | **One** tranche only — implement **only** this doc + the acceptance criteria doc |
| Scope | **Local-only**; **one** run folder in → **one** `source_records_snapshot.json` out per invocation; **no** batch over multiple runs in one process unless each run is a **separate** explicit invocation with **separate** single fetch (default: **one** run folder argument per process) |

The implementation **must** target **exactly one** existing completed run directory per invocation, resolved to a **direct child** of:

`future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`

**Forbidden:** Implicit scanning of all `run_*` folders without an explicit single-folder argument; reading sibling run folders; reading outside the resolved run folder (except the script lives under `review/local_run/` and standard library imports).

---

## 2. Allowed future implementation outputs (hard cap)

The **only** authorized new artifacts from the future build tranche are:

| Kind | Path / name | Notes |
|------|----------------|-------|
| **Single entrypoint script** | `future_modules/the_fade/review/local_run/build_source_records_snapshot_from_run_folder.py` | **No** second CLI entrypoint |
| **Optional README** | `future_modules/the_fade/review/local_run/README_source_records_snapshot.md` | Short usage only |
| **Optional tiny helper** | **At most one** additional `*.py` in **the same directory** as the entrypoint, **only** if strictly necessary; name **must** be fixed in the implementation tranche and in acceptance criteria |
| **Per-run output artifact** | `source_records_snapshot.json` | **Exactly** this basename, **inside** the chosen `run_<YYYYMMDDTHHMMSSZ>/` folder only |

**Forbidden:** Framework packages, generic “client libraries,” schedulers, workers, dashboards, HTTP servers, second snapshot filename, writing the snapshot outside the run folder, multi-slice bundling in one tranche.

---

## 3. Fixed implementation path and artifact name (pinned)

| Property | Value |
|----------|--------|
| **Script path** | `future_modules/the_fade/review/local_run/build_source_records_snapshot_from_run_folder.py` |
| **Snapshot artifact** | `source_records_snapshot.json` (co-located in the same run folder) |

---

## 4. Allowed read surface (one run folder only)

Inside **only** the resolved run folder, the implementation **may** read **only**:

1. **`source_snapshot.json`** — required for a normal path: confirms on-disk Federal Register context already summarized for this run (run linkage, request identifiers, explicit non-scanner statements as already recorded).
2. **Exactly one** **`fr_universe_scanner_request_*.json`** — required: source of **`candidate_source_packet_ref`** (and related envelope fields) used to reconstruct the **bounded** Federal Register `documents.json` GET. If more than one file matches the glob, **FAIL** (deterministic ambiguity).
3. **`run_summary.json`** — **optional**, **only** if the implementation tranche documents a **strictly necessary** reason in acceptance criteria (e.g. copying `run_id` / timestamps already required in the snapshot); **no** other keys may drive fetch shape beyond what the request JSON already supplies.

**Forbidden:** Parsing or interpreting **`operator_review.md`**, **`source_backed_operator_review.md`**, or any other Markdown; reading **`bridge_universe_scanner_result_*.json`** for this slice (not authorized — keep fetch bounded to request reference only); reading **`operator_review_gate.json`**, **`operator_attention_signal.json`**, queue JSON, or any path **outside** the single run folder; cross-folder history scans; globbing “latest” run without an explicit argument.

---

## 5. Network boundary (exactly one bounded fetch)

The later implementation **may** perform **exactly one** HTTP **GET** per successful invocation:

- **Target:** Federal Register **documents** API — URL **must** be derived **only** from the on-disk **`candidate_source_packet_ref`** string inside the run’s **`fr_universe_scanner_request_*.json`**.
- **Derivation rule:** If the field uses the prefix `federal_register_query:`, strip that prefix; the remainder **must** be a single absolute HTTPS URL. Otherwise the field **must** already be a single absolute HTTPS URL. The URL **must** use host **`www.federalregister.gov`** and path **`/api/v1/documents.json`** (query string is **only** what appears in that stored string — **no** added parameters, **no** widened date windows, **no** new filters).
- **Response handling:** Parse **one** JSON response body from that **single** GET. Extract **only** the **`results`** array (or empty array) from the top-level API response. **No** follow-up GETs: **no** pagination loop, **no** `next_page_url` traversal, **no** retry storms beyond minimal transparent handling documented in acceptance (e.g. single failure = non-zero exit).
- **Preservation:** Persist **only** factual fields from that one response into **`source_records_snapshot.json`** per §6. **No** multi-source fetches, **no** iterative crawling, **no** unrelated history pulls, **no** calling T89 ingress or other tools as subprocess (this slice owns **one** GET only).

---

## 6. Allowed snapshot artifact content (factual, bounded)

**`source_records_snapshot.json`** **must** be JSON with **at least**:

- **`artifact_kind`**: fixed literal identifying this as a factual source-record snapshot (exact string in acceptance criteria).
- **`source_name`**: `"Federal Register"` (or equivalent fixed literal in acceptance).
- **`run_folder_name`**: basename of the run directory.
- **`run_id`**: from **`run_summary.json`** when present and justified, else **`null`** with documented rule.
- **`request_id`**: from the request JSON.
- **`candidate_source_packet_ref`**: verbatim from the request JSON (the same string used to derive the GET).
- **`fetch_url_used`**: the exact URL string used for the GET (after governed derivation).
- **`fetch_timestamp_utc`**: ISO-8601 UTC from local clock at **successful** response receipt (before write).
- **`api_response_metadata`**: bounded object — e.g. **`count`**, **`total_pages`** (if present in API JSON), **`page`** (if present) — **no** full raw response dump unless acceptance caps total serialized size (prefer **omit** large opaque blobs).
- **`source_records`**: **bounded** array of objects; **each** object **only** factual fields **if** present in the corresponding API result item, such as: **`document_number`**, **`publication_date`**, **`title`**, **`type`** / **`document_type`**, **`html_url`**, **`pdf_url`**, **`abstract`** (only if returned by API and truncated/capped per acceptance), **agency names** (only if returned, as strings or small arrays — no enrichment).
- **`explicit_non_scanner_statement`**: required fixed literal stating this artifact is a **factual source-record snapshot**, **not** a scanner decision, **not** ranking/scoring/selection, **not** a recommendation.

**Forbidden in the artifact:** LLM-generated text, “insights,” priorities, ranks, trade ideas, invented fields, full HTML bodies, unbounded attachment of raw API JSON beyond the capped **`source_records`** list.

---

## 7. Remains forbidden (even in the later implementation tranche)

- AI/LLM summarization or generation  
- Recommendations, trade ideas, investment advice  
- Scanner logic, universe scan claims, request-to-result bridge behavior  
- Ranking, scoring, selection semantics  
- Multi-source fetching or provider adapters beyond the **one** governed Federal Register GET  
- Dashboard / UI / API servers  
- Runtime orchestration, scheduling, jobs, workers  
- Lane reopen, evidence collection expansion outside this run-scoped slice  
- Edits to **`mvp_lane_approval.json`** or **`mvp_lane_evidence_registry.json`**  
- Multi-slice bundling (“while we’re here” extras)  
- Pretending **`source_records_snapshot.json`** is scanner output or an operator gate decision  

---

## 8. Anti-drift rules

- **One** governance slice (**T115**) authorizes **one** implementation slice — not a standing program.  
- **One** script entrypoint (plus optional one tiny helper **only** if necessary).  
- **One** run folder per invocation.  
- **One** snapshot file per successful invocation.  
- **One** HTTP GET per successful invocation.  
- **No** widening into intelligence products, dashboards, or orchestration platforms.

---

## 9. Non-claims

**T115** does **not** implement source-record capture, does **not** authorize a universe scanner, does **not** authorize production pipelines, and does **not** substitute for honest PASS/FAIL execution against acceptance criteria in a future build tranche.

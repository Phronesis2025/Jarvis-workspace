# THE FADE — T115 Run-Scoped Source-Record Capture (Acceptance Criteria)

**Label:** `THE_FADE_PHASE3_T115_GOVERNANCE_LOCK_RUN_SCOPED_SOURCE_RECORD_CAPTURE`  
**Prompt #:** 413  
**Tranche #:** 115  
**Updated:** 2026-04-09T18:30:00+00:00

**Authority:** Executable work is **not** in **T115**. A **future** single build tranche **PASS**es only if **all** criteria below are met. **FAIL** if any mandatory criterion is unmet. **Scope violation** if forbidden behavior appears anywhere in that tranche’s diff.

**Governance:** `THE_FADE_T115_RUN_SCOPED_SOURCE_RECORD_CAPTURE_GOVERNANCE.md`  
**Pointer:** `future_modules/the_fade/config/phase3_t115_run_scoped_source_record_capture.json`

---

## A. Mandatory scope (implementation tranche)

1. **Exactly one** new primary script: `future_modules/the_fade/review/local_run/build_source_records_snapshot_from_run_folder.py`.
2. **At most one** optional README: `future_modules/the_fade/review/local_run/README_source_records_snapshot.md`.
3. **At most one** optional helper `*.py` in the **same** directory, **only** if strictly necessary; helper name **must** be listed in the implementation PR/commit message body or a one-line comment at top of the entrypoint (operator-visible).
4. **No** other new Python entrypoints under `future_modules/the_fade/` for this slice.
5. Per successful run: **exactly one** output file **`source_records_snapshot.json`** inside the **single** specified `run_<YYYYMMDDTHHMMSSZ>/` folder.

---

## B. Input / read rules

1. **CLI (or equivalent):** Caller **must** pass exactly **one** run folder identifier resolving to a **direct child** of `outputs/local_happy_path_runs/` whose name starts with `run_`.
2. **Required reads:** `source_snapshot.json` and exactly one `fr_universe_scanner_request_*.json` in that folder.
3. **Optional read:** `run_summary.json` **only** if the implementation documents in this file (amended in the **same** implementation tranche) the **single** justified use (recommended: copy `run_id` / `started_at_utc` / `finished_at_utc` into snapshot). If not used, **do not** open the file.
4. **Forbidden reads:** Any `*.md`, `bridge_universe_scanner_result_*.json`, `operator_review_gate.json`, queue files, paths outside the run folder, other `run_*` folders.

---

## C. Network rules (one GET)

1. **Exactly one** HTTP **GET** per successful invocation to the URL derived **only** from `candidate_source_packet_ref` in the request JSON, per governance §5.
2. URL **must** satisfy: scheme `https`, host `www.federalregister.gov`, path `/api/v1/documents.json`.
3. **No** pagination: **do not** issue a second GET for `next_page_url` or any continuation.
4. **No** subprocess invocation of `ingress/federal_register/build_universe_scanner_request_from_federal_register.py` or other tools to obtain URL or body.
5. **No** mutating Federal Register state (GET only).

---

## D. Output JSON (minimum fields)

The written **`source_records_snapshot.json`** **must** include:

| Field | Rule |
|--------|------|
| `artifact_kind` | Literal: `the_fade_t115_source_records_snapshot_v1` |
| `source_name` | Literal: `Federal Register` |
| `run_folder_name` | Basename of run dir |
| `run_id` | From `run_summary.json` if that file was read per §B.3; else `null` |
| `request_id` | From request JSON |
| `candidate_source_packet_ref` | Verbatim string from request JSON |
| `fetch_url_used` | Exact URL used for GET |
| `fetch_timestamp_utc` | ISO-8601 UTC |
| `api_response_metadata` | Object; **must** include `results_length` (integer, length of `results` array used). Other keys **only** if copied from top-level API JSON and **small** (e.g. `count`, `total_pages`). |
| `source_records` | Array; **max** **50** elements (if API returns more, truncate to first **50** deterministically and set `source_records_truncated: true`; if ≤50, omit `source_records_truncated` or set `false`) |
| Per-record fields | **Only** keys present in API `results[]` items, drawn from: `document_number`, `publication_date`, `title`, `document_type` **or** `type`, `html_url`, `pdf_url`, `abstract`, agency-related fields as returned. **No** invented keys. |
| `abstract` | If present, **max** 4000 characters per record; truncate with `"truncated": true` on that record. |
| `explicit_non_scanner_statement` | Literal: `This is a factual Federal Register source-record snapshot for one local run folder. It is not scanner output, not ranking or scoring, not selection, and not a recommendation.` |

---

## E. Success (PASS)

- Script runs locally with **one** valid completed run folder (e.g. `run_20260408T125708Z` on disk).
- **One** GET succeeds; **`source_records_snapshot.json`** is written with all mandatory fields and valid JSON.
- Snapshot states factual API-derived records only; includes required **non-scanner** literal.
- No forbidden reads, no second GET, no Markdown parsing, no edits to `mvp_lane_approval.json` / `mvp_lane_evidence_registry.json`.

---

## F. Failure (FAIL)

- Missing `source_snapshot.json` or missing / ambiguous request JSON in the run folder.
- URL derivation fails validation (host/path not Federal Register documents API).
- Network error, non-200 response, or non-JSON body — script **must** exit non-zero **without** claiming success; **no** partial snapshot pretending completeness unless acceptance explicitly allows a documented “empty error object” (default: **no** — fail closed).
- Output path wrong (not co-located in run folder) or wrong basename.
- More than **50** records written without truncation flag, or oversized unbounded paste of raw API.

---

## G. Scope violation

- Second HTTP GET, pagination loop, or fetch to any host other than `www.federalregister.gov` for this slice.
- Use of LLM / AI for any field value.
- Scanner, ranking, scoring, selection, or “priority” language in machine fields.
- Reading `bridge_universe_scanner_result_*.json` or Markdown reviews to drive fetch or snapshot content.
- New dashboard, provider layer, scheduler, or orchestration code.
- Any change to lane posture files or registry/approval JSON.

---

## H. Replacement / pipeline

This slice **does not** replace T89 ingress, T98 runner, T104 snapshot, T105 review, T108 gate, T110/T114 queues, or any validator. It **adds** one optional factual artifact per run when the operator runs the script.

---

## I. T115 prompt confirmation

**T115** (Prompt **#413**) added **only** governance docs + config pointer + control-doc updates. **No** executable capture code in **T115**.

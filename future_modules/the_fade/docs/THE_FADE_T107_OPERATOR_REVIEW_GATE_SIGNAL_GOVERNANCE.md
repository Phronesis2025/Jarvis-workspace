# THE FADE — T107 Operator Review Gate Signal (Governance Lock)

**Label:** `THE_FADE_PHASE3_T107_GOVERNANCE_LOCK_OPERATOR_REVIEW_GATE_SIGNAL`  
**Prompt #:** 399  
**Tranche #:** 107  
**Phase:** 3 — local pipeline (operator tooling adjacent to happy-path runs)  
**Updated:** 2026-04-08T20:30:00+00:00

**Authority:** This file is **governance and boundary only**. It **does not** implement executable code. **T107** locks **exactly one** future implementation slice: a **single** local script that reads **one** completed run folder and writes **one** machine-readable gate artifact. **No** scanner execution, **no** ranking/scoring/selection, **no** AI/LLM, **no** new network I/O, **no** lane/registry/approval edits.

---

## 1. Slice identity (exactly one implementation tranche later)

| Property | Value |
|----------|--------|
| Slice name | Operator review gate signal (mechanical) |
| Future build tranche | **One** tranche only — implement **only** what this doc + `THE_FADE_T107_OPERATOR_REVIEW_GATE_SIGNAL_ACCEPTANCE_CRITERIA.md` describe |
| Scope | **Local-only** post-run hygiene signal for the operator; **not** a scanner; **not** a trading or investment signal |

---

## 2. Input: exactly one run folder

The later script **must** accept **exactly one** run directory per invocation, resolved only as a direct child of:

`future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`

Rules:

- Folder name **must** start with `run_`.
- Path **must** be under `outputs/local_happy_path_runs/` (same resolution discipline as `build_operator_review_from_run_folder.py` / `build_source_snapshot_from_run_folder.py` / `build_source_backed_operator_review_from_run_folder.py`).
- **No** cross-folder reads, **no** directory walks outside that single run folder, **no** history scans.

---

## 3. Allowed read set (bounded)

The implementation **may** read **only** these files **inside** the chosen run folder:

1. `run_summary.json`
2. **Exactly one** `fr_universe_scanner_request_*.json` (copied ingress request)
3. **Exactly one** `bridge_universe_scanner_result_*.json` (copied mechanical bridge result)
4. `source_snapshot.json`

**Optional read (discouraged for the first gate-signal build):** `source_backed_operator_review.md` — **only** if a future governance amendment proves JSON-only reads insufficient. For the **first governed gate-signal implementation tranche** after **T107**, **do not** read `source_backed_operator_review.md` and **do not** require Markdown parsing.

---

## 4. Output: exactly one gate artifact (fixed name)

| Property | Value |
|----------|--------|
| Artifact filename | `operator_review_gate.json` |
| Location | **Same** run folder as inputs |
| Overwrite | Implementation may overwrite this file on re-run for that folder (idempotent regenerate) |

**No** second JSON gate file, **no** alternate basename, **no** global output directory.

---

## 5. Fixed implementation path (single entrypoint)

| Property | Value |
|----------|--------|
| **Single script path** | `future_modules/the_fade/review/local_run/build_operator_review_gate_signal_from_run_folder.py` |
| Optional README | `future_modules/the_fade/review/local_run/README_operator_review_gate.md` (short usage only) |
| Optional helper | **At most one** additional `*.py` in **the same directory**, **only** if strictly necessary, **must** be explicitly named in the implementation tranche commit message and in acceptance criteria |

**Forbidden:** second CLI entrypoint elsewhere, package/framework scaffold, shared “reporting library,” or moving logic into unrelated trees.

---

## 6. Allowed gate artifact content (factual + mechanical only)

The JSON **may** include **only** bounded, on-disk-derived fields, for example:

- **Run identity:** `run_folder_name` (string), and/or `run_id` from `run_summary.json` when present as a string
- **Request identity:** `request_id` from request JSON or `source_snapshot.json` (same string if both present — copy one documented source order)
- **Source label:** `source_name` from `source_snapshot.json` when present (string)
- **Mechanical result fields** (from copied result JSON): `scanner_status` (string), `candidate_outputs_count` (non-negative integer), `deferred_count` (non-negative integer; count of rows in `candidate_outputs` where `status` is the string `deferred`, or **exactly** the mechanical rule documented in the implementation — must be transparent)
- **results_count:** **only** if the key `results_count` exists in `source_snapshot.json` and its value is a JSON number integer; otherwise omit the key or set `null` per acceptance criteria (must be one documented rule)
- **Presence flags** (booleans): e.g. `source_snapshot_present`, `run_summary_present`, `request_file_matched_one`, `result_file_matched_one`
- **Gate outputs (required keys):**
  - `review_gate_status` — one of a **closed enum** defined in acceptance criteria (e.g. mechanical `open_for_operator_review` vs `do_not_open_mechanical_failure`)
  - `review_gate_reasons` — array of **machine codes** (strings from a **fixed** vocabulary in acceptance criteria), **no** free-form prose
- **Governance strings (required):**
  - `explicit_non_scanner_statement` — fixed literal stating this artifact is **not** a scanner decision and **not** scanner output
  - `explicit_non_trading_signal_statement` — fixed literal stating this artifact is **not** a trading or investment signal or recommendation

**Forbidden in the artifact:** natural-language recommendations, prioritized queues, scores, ranks, “confidence,” narrative summaries, URLs fetched at runtime, data not read from the allowed files above.

---

## 7. Allowed gate rule style (transparent mechanical rules only)

The implementation **must** document in code comments **and** emit in `review_gate_reasons` the **exact** predicates used. Allowed ingredients **include** (not limited to, but **must stay mechanical**):

- Required files exist and are valid JSON when parsed
- `run_summary.json` field `status` equals the string `PASS` (if `status` missing or other value → mechanical failure path)
- `source_snapshot.json` exists
- `scanner_status` from the copied result JSON equals the string `pending`
- `candidate_outputs` exists, is a JSON array, and `len(candidate_outputs) > 0`
- `deferred_count` equals `len(candidate_outputs)` **or** `deferred_count > 0` per **one** documented rule consistent with the T96 bridge contract (pick **one** in implementation tranche; document in acceptance criteria addendum if needed)
- Parse/count failures → mechanical failure reasons

**Example intent (non-normative):** `open_for_operator_review` when all required artifacts exist, JSON parses, summary `PASS`, snapshot present, `scanner_status` is `pending`, and `candidate_outputs_count > 0`. Any violation → `do_not_open_mechanical_failure` with explicit reason codes.

**Normative:** The **exact** boolean composition is **locked** in `THE_FADE_T107_OPERATOR_REVIEW_GATE_SIGNAL_ACCEPTANCE_CRITERIA.md` so implementers cannot improvise fuzzy rules.

---

## 8. Explicitly forbidden (gate-signal implementation tranche and forever adjacent)

- AI/LLM summarization or “smart” text
- Recommendations, trade ideas, prioritization across runs or candidates
- Ranking, scoring, selection logic beyond fixed mechanical predicates above
- New network calls, ingress re-invocation, provider clients, credentials
- Scanner execution, universe scan claims, request-to-result generation (bridge already ran; gate **reads** only)
- Dashboard/UI, schedulers, workers, runtime orchestration platforms
- Lane reopen, evidence collection, edits to `mvp_lane_approval.json` or `mvp_lane_evidence_registry.json`
- Multi-slice bundling, second entrypoint, reporting framework buildup
- Pretending the gate is a scanner, decision engine, or trading signal

---

## 9. Relationship to prior slices

- **After** T100 operator run surface, T102/T104/T106 review and snapshot artifacts may exist in the run folder. The gate script **does not** replace them and **does not** invoke the runner, ingress, bridge, or validators.
- This slice adds **one** JSON signal file for operator triage only.

---

## 10. Non-claims

T107 **does not** implement the gate script. T107 **does not** authorize scanner/runtime/dashboard/provider work. T107 **does not** change scoped MVP approval or lane posture. Executable gate work remains **not done** until a **later** governed build tranche that cites these **T107** documents.

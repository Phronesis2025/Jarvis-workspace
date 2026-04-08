# THE FADE — T111 First Operator-Meaningful Filtering Signal (Governance Lock)

**Label:** `THE_FADE_PHASE3_T111_GOVERNANCE_LOCK_FIRST_OPERATOR_MEANINGFUL_FILTERING_SIGNAL`  
**Prompt #:** 405  
**Tranche #:** 111  
**Phase:** 3 — local pipeline (operator tooling adjacent to happy-path runs)  
**Updated:** 2026-04-08T22:28:11+00:00

**Authority:** This file is **governance and boundary only**. It **does not** implement executable code. **T111** locks **exactly one** future implementation slice: a **single** local script that processes **one** completed run folder and writes **one** small machine-readable **attention** (filtering) signal JSON. The signal is a **transparent mechanical index** of facts already on disk — **not** a scoring engine, **not** a ranking system, **not** AI, **not** a universe-scanner result, **not** a trading or investment recommendation.

---

## 1. Slice identity (exactly one implementation tranche later)

| Property | Value |
|----------|--------|
| Slice name | First operator-meaningful filtering (attention) signal |
| Future build tranche | **One** tranche only — implement **only** this doc + `THE_FADE_T111_FIRST_OPERATOR_MEANINGFUL_FILTERING_SIGNAL_ACCEPTANCE_CRITERIA.md` |
| Scope | **Local-only**; **one** run folder in → **one** `operator_attention_signal.json` out; **no** cross-run aggregation in this slice |

---

## 2. Run folder input (bounded)

The later script **must** accept exactly **one** run directory per invocation, resolved to a **direct child** of:

`future_modules/the_fade/outputs/local_happy_path_runs/`

**Name rule:** The directory basename **must** match `run_<YYYYMMDDTHHMMSSZ>` (same UTC Zulu convention as T99–T110).

**Forbidden:** Batch processing multiple runs, scanning `local_happy_path_runs/` without an explicit single-folder argument, reading sibling run folders, reading outside the resolved run directory (except writing the signal file **inside** that directory).

---

## 3. Allowed per-run read set (bounded)

Inside **only** the resolved run folder, the implementation **may** read **only**:

1. **`operator_review_gate.json`** — **required** for a normal successful path: must exist and parse as a JSON object for PASS criteria in acceptance; source for `review_gate_status`, `review_gate_reasons` (copy **not** required in signal artifact except as bounded fields below), `request_id`, `source_name`, `candidate_outputs_count`, `deferred_count`, and any `results_count` **if** present as a JSON integer in the gate file (implementation may copy gate `results_count` when present; **snapshot** remains authoritative for `results_count` when both exist — see acceptance for precedence rule).
2. **`source_snapshot.json`** — when present and parseable: **only** for factual fields already stored there, principally **`results_count`** as a JSON integer (and **no** full-text mining of snapshot bodies beyond typed top-level keys listed in acceptance).
3. **`run_summary.json`** — **optional read, only** for the mechanical checks documented in acceptance: when the file **exists**, the implementation **may** read **only** top-level `status` (string). If `run_summary.json` is **absent**, **no** `run_summary`-based reasons are emitted and **no** failure is inferred solely from absence. **No** other use of `run_summary.json` in this slice without a future governance amendment.

**Forbidden in this slice:** Markdown (`operator_review.md`, `source_backed_operator_review.md`, …), `fr_universe_scanner_request_*.json`, `bridge_universe_scanner_result_*.json`, ingress/bridge/runner/validator invocation, reading `operator_review_queue.json`, network I/O.

---

## 4. Output: exactly one signal artifact (fixed name, co-located)

| Property | Value |
|----------|--------|
| Artifact filename | `operator_attention_signal.json` |
| **Path** | `future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/operator_attention_signal.json` (same folder as the input run) |
| Overwrite | Implementation overwrites this file on each successful run (idempotent regenerate) |

**No** second signal file, **no** alternate basename, **no** writing outside the run folder.

---

## 5. Fixed implementation path (single entrypoint)

| Property | Value |
|----------|--------|
| **Single script path** | `future_modules/the_fade/review/local_run/build_operator_attention_signal_from_run_folder.py` |
| Optional README | `future_modules/the_fade/review/local_run/README_operator_attention_signal.md` (short usage only) |
| Optional helper | **At most one** additional `*.py` in **the same directory**, **only** if strictly necessary, **must** be explicitly named in the implementation tranche and acceptance criteria |

**Forbidden:** second CLI entrypoint, HTTP servers, dashboards, schedulers, calling `build_operator_review_gate_signal_from_run_folder.py` or queue builder (signal is **read-only** aggregation of existing disk state).

---

## 6. Allowed signal artifact content (factual + mechanical only)

Top-level object **may** include **only** fields listed in the acceptance criteria, including at minimum:

- **`generated_at_utc`** — ISO-8601 UTC from local clock at write time.
- **`signal_schema_version`** — fixed literal set in acceptance (e.g. `t111_v1`).
- **`run_folder_name`** — basename of the run directory.
- **`run_id`**, **`request_id`**, **`source_name`** — copied **only** when present as strings (or string rules) in allowed inputs per acceptance.
- **`review_gate_status`** — copied from gate when gate parsed.
- **`results_count`** — **only** when taken per acceptance precedence (snapshot vs gate).
- **`candidate_outputs_count`**, **`deferred_count`** — **only** as JSON integers from `operator_review_gate.json` when present.
- **`operator_attention_status`** — **exactly one** value from the **closed vocabulary** in §7.
- **`operator_attention_reasons`** — array of **distinct** strings, **each** a member of the **closed reason code set** in acceptance (**no** free-form prose).
- **`explicit_non_scanner_statement`**, **`explicit_non_trading_signal_statement`** — required fixed literals from acceptance.

**Forbidden:** priority scores, ranks, confidence, natural-language recommendations, trade ideas, fuzzy labels (“high priority,” “interesting,” “skip”), URLs fetched at runtime, invented counts.

---

## 7. Signal decision vocabulary (closed)

**`operator_attention_status`** **must** be **exactly one** of:

| Value | Meaning (operator-facing, non-normative English) |
|-------|--------------------------------------------------|
| `elevated_manual_attention` | Mechanical rules say this open gate run has at least one **elevation trigger** (see acceptance). |
| `standard_manual_attention` | Gate is open for operator review but **no** elevation trigger fired. |
| `do_not_elevate_mechanical_failure` | Mechanical failure path: gate missing/invalid, gate reports `do_not_open_mechanical_failure`, or `run_summary` checks fail per acceptance. |

**`operator_attention_reasons`:** **only** codes from the closed set in `THE_FADE_T111_FIRST_OPERATOR_MEANINGFUL_FILTERING_SIGNAL_ACCEPTANCE_CRITERIA.md` (**no** other strings).

---

## 8. Allowed signal logic style (purely mechanical)

Rules **may** use **only** boolean/integer comparisons on fields already on disk, such as:

- `review_gate_status == "open_for_operator_review"` vs `== "do_not_open_mechanical_failure"`.
- Presence and parse success of `operator_review_gate.json`.
- `deferred_count > 0` (integer from gate).
- `candidate_outputs_count > 0` (integer from gate).
- `results_count` from `source_snapshot.json` when it exists and is a JSON integer `> 0` (per acceptance; **no** inference from text bodies).
- Optional: `run_summary.json` present and `status == "PASS"`.

**Forbidden:** weighted sums, lexicographic “priority,” machine-learning labels, sentiment, qualitative judgments, heuristics not fully enumerated in acceptance.

---

## 9. Forbidden (this governance tranche and the later build)

- AI/LLM summarization or classification  
- Recommendations, trade ideas, investment advice  
- Ranking/scoring/selection across runs (this slice is **per-run** only)  
- New data fetches, provider clients, subprocess network tools  
- Dashboard/UI, runtime orchestration, jobs/workers  
- Lane reopen; evidence collection; edits to `mvp_lane_approval.json` or `mvp_lane_evidence_registry.json`  
- Multi-slice bundling; hidden intelligence creep; broad reporting frameworks  
- Pretending the artifact is a scanner output, execution decision, or automated triage engine  

---

## 10. Anti-drift rules

- **One** implementation slice only.  
- **One** script only (**one** optional helper **max**).  
- **One** signal artifact only per run folder.  
- **One** run folder per invocation.  
- **No** “while we’re here” extras (no queue changes, no gate regeneration, no pipeline calls).  

---

## 11. T111-specific note

**Tranche T111 (this prompt):** governance + acceptance criteria **only** — **no** signal script code. Executable attention-signal work is **explicitly not done** until a **later** build tranche that cites these documents.

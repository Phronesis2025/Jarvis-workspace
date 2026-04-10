# THE FADE — T117 First Real Scanner Rule (Governance Lock)

**Label:** `THE_FADE_PHASE3_T117_GOVERNANCE_LOCK_FIRST_REAL_SCANNER_RULE`  
**Prompt #:** 417  
**Tranche #:** 117  
**Phase:** 3 — local pipeline (first **mechanical** scanner rule; **not** a scanner engine)  
**Updated:** 2026-04-09T22:00:00+00:00

**Authority:** This file is **governance and boundary only**. It **does not** implement executable code. **T117** locks **exactly one** future implementation tranche: a **single** local script that reads **one** completed run folder’s **`source_records_snapshot.json`**, applies **one** explicit **mechanical** eligibility rule to each captured Federal Register row, and writes **one** machine-readable **`first_real_scanner_rule_evaluation.json`**. This is the **first** on-disk definition of a **real** scanner **rule** (eligibility over captured records) — it is **not** a ranking/scoring/selection engine, **not** multi-rule intelligence, **not** AI/LLM output, and **not** a trading or investment recommendation.

**Companion:** `THE_FADE_T117_FIRST_REAL_SCANNER_RULE_ACCEPTANCE_CRITERIA.md`  
**Machine-readable pointer:** `future_modules/the_fade/config/phase3_t117_first_real_scanner_rule.json`

---

## 1. Slice identity (exactly one implementation tranche later)

| Property | Value |
|----------|--------|
| Slice name | First real scanner rule (single mechanical eligibility rule) |
| Future build tranche | **One** tranche only — implement **only** this doc + the acceptance criteria doc |
| Scope | **Local-only**; **one** run folder in → **one** `first_real_scanner_rule_evaluation.json` out per invocation |

The implementation **must** target **exactly one** existing completed run directory per invocation, resolved to a **direct child** of:

`future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`

**Prerequisite:** That folder **must** contain a **`source_records_snapshot.json`** produced per **T115/T116** ( **`artifact_kind`** `the_fade_t115_source_records_snapshot_v1` ) so that **`source_records`**, **`fetch_timestamp_utc`**, and related fields exist for mechanical evaluation.

**Forbidden:** Batch implicit scan of all `run_*` folders; reading sibling run folders; cross-folder reads; new network I/O; reading Markdown; reading `bridge_universe_scanner_result_*.json` for this slice unless a future governance amendment explicitly allows it (default: **forbidden**).

---

## 2. Allowed future implementation outputs (hard cap)

| Kind | Path / name | Notes |
|------|-------------|-------|
| **Single entrypoint script** | `future_modules/the_fade/review/local_run/build_first_real_scanner_rule_from_run_folder.py` | **No** second CLI entrypoint |
| **Optional README** | `future_modules/the_fade/review/local_run/README_first_real_scanner_rule.md` | Short usage only |
| **Optional tiny helper** | **At most one** additional `*.py` in the **same directory**, **only** if strictly necessary; name **must** be fixed in implementation + acceptance |
| **Per-run output artifact** | `first_real_scanner_rule_evaluation.json` | **Exactly** this basename, **inside** the chosen run folder only |

**Forbidden:** Second evaluation filename, provider clients, dashboards, schedulers, multi-rule modules, framework buildup.

---

## 3. Fixed implementation path and evaluation artifact name (pinned)

| Property | Value |
|----------|--------|
| **Script path** | `future_modules/the_fade/review/local_run/build_first_real_scanner_rule_from_run_folder.py` |
| **Artifact** | `first_real_scanner_rule_evaluation.json` |

---

## 4. Allowed read surface (one run folder only)

The implementation **may** read **only**:

1. **`source_records_snapshot.json`** — **required** (source of **`source_records`**, **`fetch_timestamp_utc`**, **`request_id`**, **`run_folder_name`**, **`source_name`**, etc.).
2. **`source_snapshot.json`** — **optional**, **only** if the implementation tranche documents a **single** justified use in acceptance (e.g. reconciling **`run_id`** when absent from snapshot top-level — default: **prefer** fields inside **`source_records_snapshot.json`** first; **do not** open **`source_snapshot.json`** unless acceptance lists the exact keys allowed).

**Forbidden:** Markdown, queue/gate JSON, request/result JSON **unless** future governance amends this slice; any path outside the resolved run folder (except script directory + stdlib).

---

## 5. The first real scanner rule (pinned — one rule only)

For **each** object in **`source_records`** inside **`source_records_snapshot.json`**, evaluate **mechanical** eligibility. A record is **`eligible_by_rule`** only if **all** of the following hold; otherwise it is **`excluded_by_rule`** with **one or more** closed reason codes (see §7).

### 5.1 Identity and shape

- **`document_number`:** present, type **string**, and **strip()** is non-empty.
- **`title`:** present, type **string**, and **strip()** is non-empty.
- **`publication_date`:** present, type **string**, **strip()** non-empty, and **parseable** as a **calendar date** using implementation logic fixed in acceptance (recommend: first **10** characters `YYYY-MM-DD` when valid, else full ISO date parsing **date-only** in UTC semantics).

### 5.2 Document type allowlist

- Determine **document type label** as: use **`document_type`** if present and non-empty string after strip; else use **`type`** if present and non-empty string after strip; else **neither** (failed type check).
- That label must match **exactly** (case-sensitive) **one** of:
  - `Rule`
  - `Proposed Rule`
  - `Notice`

### 5.3 Recency window (UTC calendar — pinned)

Let **`fetch_timestamp_utc`** be the string field of the same name in **`source_records_snapshot.json`**. Parse it to obtain **`D_fetch`**, the **UTC calendar date** of that instant (date component only, no local timezone).

Let **`D_pub`** be the **UTC calendar date** parsed from the record’s **`publication_date`** per §5.1.

The record satisfies the recency rule if **`D_pub`** is **in the inclusive set**:

`{ D_fetch, D_fetch - 1 calendar day, D_fetch - 2 calendar days }`

(computed in **UTC proleptic Gregorian** calendar arithmetic).

**Interpretation:** “**Previous two UTC calendar days including the fetch date**” = fetch-day and the **two** immediately preceding UTC dates (**three** dates total). Records outside this window are excluded with **`publication_date_out_of_window`**.

### 5.4 Evaluation order (deterministic)

When multiple failures apply, the implementation **must** emit **all** applicable exclusion reason codes for that record (see acceptance for ordering if desired); **eligible** path requires **no** failed clause.

---

## 6. Allowed evaluation artifact content (bounded)

The JSON **must** include at minimum:

- **`generated_at_utc`** — ISO-8601 UTC from local clock at write time.
- **`rule_schema_version`** — fixed literal **`t117_v1`** (unless acceptance amends in same tranche).
- **`run_id`** — from **`source_records_snapshot.json`** / **`run_folder_name`** / optional **`source_snapshot.json`** per acceptance (string or null).
- **`run_folder_name`** — basename of run directory.
- **`source_name`** — copy from snapshot when present (e.g. `Federal Register`).
- **`fetch_timestamp_utc`** — verbatim copy from **`source_records_snapshot.json`**.
- **`rule_metadata`** — small object: at minimum **`rule_id`:** **`first_real_scanner_rule_t117_v1`**, **`description`** fixed literal summarizing §5 in one sentence.
- **`eligible_count`**, **`excluded_count`** — non-negative integers; sum equals length of **`source_records`** input array.
- **`eligible_records`**, **`excluded_records`** — arrays of **bounded** row objects (see acceptance for allowed per-row keys).
- Per row: **`document_number`**, **`publication_date`**, **`title`**, **`document_type`** and/or **`type`** as copied from input when present, **`html_url`**, **`pdf_url`** when present, **`scanner_rule_status`**, **`scanner_rule_reasons`** (array of strings from closed set).
- **`explicit_non_engine_statement`** — required fixed literal: **“This artifact is one bounded mechanical scanner-rule evaluation for a single local run folder. It is not a full scanner engine, not ranking or scoring, not selection, and not a recommendation.”**

**Forbidden:** Free-form “insights,” priority scores, ranks, confidence, trade ideas, narrative recommendations.

---

## 7. Scanner rule vocabulary (closed sets)

### 7.1 `scanner_rule_status`

Exactly one of:

| Value | Meaning |
|-------|--------|
| `eligible_by_rule` | All clauses in §5 satisfied for this record. |
| `excluded_by_rule` | At least one clause failed. |

### 7.2 `scanner_rule_reasons` (strings)

**When `eligible_by_rule`:** exactly **`["meets_first_real_scanner_rule"]`** (order fixed).

**When `excluded_by_rule`:** one or more distinct strings from:

| Code | When |
|------|------|
| `missing_document_number` | §5.1 document_number fails |
| `missing_title` | §5.1 title fails |
| `missing_publication_date` | absent or empty after strip |
| `invalid_publication_date` | present but not parseable as date |
| `document_type_not_allowed` | type label not in allowlist |
| `publication_date_out_of_window` | §5.3 fails |

**Forbidden:** Any reason string not in the tables above.

---

## 8. Remains forbidden (later implementation tranche)

- AI/LLM summarization or generation  
- Recommendations, trade ideas  
- Scoring, ranking, selection engines  
- Additional rules, weighted blends, or “policy tuning” beyond §5  
- New HTTP/network calls  
- Provider adapters, dashboards, UI, orchestration, jobs  
- Lane reopen; registry/approval edits  
- Pretending this artifact is a complete scanner product  

---

## 9. Anti-drift

- **One** governance tranche (**T117**) → **one** implementation tranche.  
- **One** script, **one** rule (§5), **one** artifact name, **one** run folder per invocation.  
- **No** “while we’re here” extras.

---

## 10. Non-claims

**T117** does **not** implement the rule script, does **not** authorize a scanner **engine** or production pipeline, and does **not** substitute for PASS/FAIL execution against acceptance in a future build tranche.

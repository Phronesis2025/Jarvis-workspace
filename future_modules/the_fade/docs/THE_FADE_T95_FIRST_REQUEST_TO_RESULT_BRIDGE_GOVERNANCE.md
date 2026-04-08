# THE FADE — T95 first request→result bridge slice (governance lock)

**Prompt #:** 375  
**Phase #:** 3 — **request-to-result governance** (T95 **docs only**; **no** bridge code in this tranche)  
**Tranche #:** 95  
**Label:** `THE_FADE_PHASE3_T95_GOVERNANCE_LOCK_FIRST_REQUEST_TO_RESULT_BRIDGE_SLICE`  

**Updated:** 2026-04-07T22:05:00+00:00  

---

## Purpose

**T89** writes **`UniverseScannerRequest`** under **`inputs/phase3_universe_scanner_requests/`**. **T91** validates ingress request packets offline. **T94** validates **`UniverseScannerResult`** under **`outputs/phase3_universe_scanner_results/`** offline. There is **still** **no** code that **reads** a stored request packet and **writes** a corresponding result packet.

**T95** governs **exactly one** future implementation tranche that may add **only** a **bounded mechanical bridge**: **one** schema-valid request file **in** → **one** schema-valid result file **out**, with **no** scanner semantics, **no** network, **no** ranking/selection, and **no** claim that a real universe scan occurred.

**T95 does not implement the bridge**, does not reopen lanes, and does not edit **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`**, or lane charters. **Scoped MVP (T80)** remains binding.

**Companion:** `THE_FADE_T95_FIRST_REQUEST_TO_RESULT_BRIDGE_ACCEPTANCE_CRITERIA.md`.  
**Machine-readable note:** `phase2_mvp_approval_scope_decision.json` → **`post_t95_first_request_to_result_bridge_governance`**.

---

## 1. Next implementation slice — exact definition

**Governed slice name:** **Phase 3 — first request→result bridge (single packet, mechanical envelope only).**

**In scope for exactly one future implementation tranche** (not T95 itself):

| Rule | Detail |
|------|--------|
| **Inputs** | **One** JSON file, read-only, under **`future_modules/the_fade/inputs/phase3_universe_scanner_requests/`** (root only — not `fixtures_invalid/`). The file **must** already conform to **`universe_scanner_request.schema.json`**; the bridge **may** validate against that schema before write **or** require the operator to have run **`validate_ingress_request_packets.py`** first — **no** repair/auto-fix of the request packet. |
| **Outputs** | **One** new JSON file written under **`future_modules/the_fade/outputs/phase3_universe_scanner_results/`** (root only — not under `fixtures_invalid/`), schema-valid per **`universe_scanner_result.schema.json`**, with a **durable, documented filename pattern** (e.g. includes `request_id` and UTC timestamp). **No** second result file in that tranche. |
| **Local only** | **No** HTTP, sockets, subprocesses to network tools, provider adapters, dashboard/UI, schedulers, workers, queues, or runtime orchestration. |
| **No multi-source** | **No** reads beyond the **single** request file, the **two** contract schemas (read-only), and the bridge script/README. **No** Federal Register re-fetch, **no** second ingress source, **no** fusion. |
| **No lane / registry / approval edits** | **No** edits to **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`**, or evidence logs as part of the bridge tranche. |
| **No scanner** | **No** ranking, scoring, selection, prioritization, normalization frameworks, or “tiny scanner” loops disguised as mapping. |

---

## 2. Allowed artifact types (future tranche only)

| Category | Constraint |
|----------|------------|
| **One primary bridge script** | **Exactly one** path: **`future_modules/the_fade/bridge/first_request_to_result/build_universe_scanner_result_from_single_request.py`**. **`if __name__ == "__main__"`** allowed **only** to parse args, run the bridge once, and exit with a non-zero code on failure. |
| **Optional usage notes** | **At most one** **`future_modules/the_fade/bridge/first_request_to_result/README.md`** — short only: how to run, input/output paths, honesty strings, what the bridge **does not** do. |
| **Second surface** | **Forbidden** — no duplicate entrypoint, no parallel “helper” CLI under another package for the same job. |
| **Extra framework** | **Forbidden** unless a **single** small internal function in the **same** script is strictly necessary (e.g. shared JSON load); **no** new pip-installable package, **no** plugin architecture. |

---

## 3. What the bridge may do (mechanical mapping only)

### 3.1 Envelope / metadata

- **`request_id`:** copy **exactly** from the request (must match schema UUID format).
- **`produced_at_utc`:** set **once** at write time using the **local** process clock (RFC 3339 UTC **Z**). **No** network time.
- **`scanner_status`:** **must** be **`pending`** only — the bridge **must not** emit **`completed`** (that would imply a finished scan).
- **`contract_version`:** copy **exactly** from **`UniverseScannerRequest.contract_version`** (must satisfy result schema pattern).

### 3.2 `candidate_outputs` (required by schema) — placeholder semantics

The result schema **requires** **`candidate_outputs`** (array). The bridge **does not** perform a scan. Placeholder rules:

| Request shape | Bridge behavior |
|---------------|-----------------|
| **`candidate_symbols` present** | Emit **exactly one** row per entry **in array order** (no reordering, no deduplication, no subset). Each row: **`symbol`** = string from request; **`row_status`** = **`deferred`**; **`omission_reason`** = fixed literal **`bridge_T95_placeholder_not_a_scan`**. |
| **`candidate_source_packet_ref` only** (no `candidate_symbols`) | Emit **exactly one** row: **`symbol`** = **`BRIDGE_OPAQUE_CANDIDATE_REF`**; **`row_status`** = **`deferred`**; **`omission_reason`** = **`bridge_T95_placeholder_not_a_scan_opaque_candidate_ref`**. |

**Optional** result fields **`warnings`**, **`exclusions`**, **`notes`**, **`normalized_label`**: **optional**; if **`warnings`** is present it **must** include **at least** one explicit string stating that the packet was produced by the **non-scanner bridge** only (exact wording may be documented in README).

**Forbidden for `candidate_outputs`:** **`included`** or **`excluded`** row_status in this slice (only **`deferred`**), any logic that chooses which symbols “win”, any scoring, any read of live market/FR/API data to fill rows.

### 3.3 Validation before write

The bridge **should** validate the outgoing JSON against **`universe_scanner_result.schema.json`** in-process before write (e.g. same **Draft7** pattern as offline validators) **or** document that the operator **must** run **`validate_universe_scanner_result_packets.py`** after — **prefer** in-process check to guarantee one valid file out.

---

## 4. Forbidden in the later implementation tranche

| Forbidden | Rationale |
|-----------|-----------|
| **Ranking / scoring / selection / prioritization** | Scanner behavior |
| **Symbol prioritization or filtering** | Business logic |
| **Multi-source ingestion or fusion** | Out of slice |
| **Provider adapters, dashboard, UI** | Product surface |
| **Runtime orchestration, jobs, workers, scheduling** | Out of slice |
| **Network I/O** | Out of slice |
| **Lane reopen, evidence collection, registry/approval edits** | Phase 2 boundary |
| **Multi-slice bundling** | Bridge + validator refactor + scanner stub in one tranche |
| **“Tiny scanner”** | Disguised execution |
| **Emitting `scanner_status: completed`** | Implies real scan |
| **Reading more than one request file** | Breaks one-in-one-out |
| **Writing more than one new result file** | Breaks one-in-one-out |
| **Deriving result rows from live source data** | Only the **already-written** request JSON may inform the bridge |

---

## 5. Fixed paths (authoritative)

| Role | Path |
|------|------|
| **Bridge script (future)** | **`future_modules/the_fade/bridge/first_request_to_result/build_universe_scanner_result_from_single_request.py`** |
| **Optional README (future)** | **`future_modules/the_fade/bridge/first_request_to_result/README.md`** |
| **Request directory (read)** | **`future_modules/the_fade/inputs/phase3_universe_scanner_requests/`** (single file under root) |
| **Result directory (write)** | **`future_modules/the_fade/outputs/phase3_universe_scanner_results/`** (single new file under root) |
| **Request schema (read-only)** | **`future_modules/the_fade/contracts/phase3_universe_scanner_io/schemas/universe_scanner_request.schema.json`** |
| **Result schema (read-only)** | **`future_modules/the_fade/contracts/phase3_universe_scanner_io/schemas/universe_scanner_result.schema.json`** |

---

## 6. Relationship to prior tranches

- **T91 / T94** remain **validation-only**; the bridge tranche **does not** replace them.  
- **T89** ingress **unchanged** in meaning; the bridge **does not** call the FR ingress tool.  
- **T93 Model B** seeds for **offline** validation are **separate** from bridge-produced results; a bridge-written result is **not** required to be a “static seed” — but it **must** still satisfy **T95** honesty rules (**`pending`**, **`deferred`** rows only, fixed omission reasons).

---

## 7. Anti-drift rules

1. **One implementation slice only** — singular until new governance defines another slice.  
2. **One bridge path only** — the script path in §5.  
3. **One request file in, one result file out** — no batching.  
4. **No “while we’re here”** — no ingress refactor, no validator merge, no scanner starter.  
5. **No widening** — bridge **must not** become the home for execution scanner logic.  

---

## 8. Non-claims

- T95 **does not** run or implement the bridge.  
- T95 **does not** authorize a universe scanner, production result pipeline, or runtime product.  
- T95 **does not** prove production readiness.

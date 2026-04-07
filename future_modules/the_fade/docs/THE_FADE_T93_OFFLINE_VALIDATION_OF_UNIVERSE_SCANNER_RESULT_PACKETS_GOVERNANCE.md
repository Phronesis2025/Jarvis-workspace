# THE FADE — T93 offline validation of `UniverseScannerResult` packets (governance lock)

**Prompt #:** 368 (boundary repair **#369**)  
**Phase #:** 3 — **post-ingress-validation governance** (T93 **docs only**; **no** validator code in this tranche)  
**Tranche #:** 93  
**Label:** `THE_FADE_PHASE3_T93_GOVERNANCE_LOCK_OFFLINE_VALIDATION_OF_UNIVERSE_SCANNER_RESULT_PACKETS`  

**Updated:** 2026-04-07T19:29:42+00:00  

---

## Purpose

**T85** defines static **`UniverseScannerResult`** contract shape; **T87** validates **shipped contract examples** only; **T91** validates **ingress-written request** JSON. There is **still** **no** production path that **writes** result packets from requests or from a scanner. **T93** governs **exactly one next slice**: **offline-only validation** of **`UniverseScannerResult`** JSON under **one** governed directory — **no** request→result, **no** scanner semantics, **no** network.

**Seeding model (Prompt #369 repair — explicit):** **Model B — bounded static seeding.** The **later T93-authorized implementation tranche** **may** add **at most three** valid **`*.json`** files in the **root** of **`outputs/phase3_universe_scanner_results/`**, **only** as **static hand-placed or copy-only** artifacts (e.g. copied from **`contracts/phase3_universe_scanner_io/examples/universe_scanner_result.example.json`** with **no** semantic fill from live data). Those files **exist only** to support **offline schema validation** (positive PASS lines). They **must not** be produced by **any** code that reads **`UniverseScannerRequest`**, ingress **`inputs/phase3_universe_scanner_requests/`**, or scanner outputs; they **must not** imply scanner execution. **Alternatively**, the root may contain **zero** valid packets — the validator **must** define behavior for **no** root `*.json` (e.g. success with explicit “nothing to validate”). The **validator script itself** **must not** write or create root-level result JSON — **reads only**.

**T93 does not implement anything**, does not reopen lanes, does not authorize emitting `UniverseScannerResult` from `UniverseScannerRequest` or from any scanner, and does not edit **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`**, or lane charters. **Scoped MVP (T80)** remains binding and **not** production maturity.

**Companion:** `THE_FADE_T93_OFFLINE_VALIDATION_OF_UNIVERSE_SCANNER_RESULT_PACKETS_ACCEPTANCE_CRITERIA.md`.  
**Machine-readable note:** `phase2_mvp_approval_scope_decision.json` → **`post_t93_offline_validation_of_universe_scanner_result_packets_governance`**.

**Governs from:** Post–**T91** checkpoint and Prompt **#367** reality check (next honest move = governance lock for offline result-packet validation only). **Prompt #369** narrows **valid root-level packet** rules only — **no** change to validator path, governed directory, or forbidden scanner/request→result boundary.

---

## 1. Next implementation slice — exact definition

**Governed slice name:** **Phase 3 — offline validation of on-disk `UniverseScannerResult` packets only.**

**In scope for exactly one future implementation tranche** (not T93 itself):

- **Local filesystem only** — reads under:
  - **`future_modules/the_fade/outputs/phase3_universe_scanner_results/`** (result packets + optional bounded invalid fixtures per §2)
  - **`future_modules/the_fade/contracts/phase3_universe_scanner_io/schemas/universe_scanner_result.schema.json`** (**read-only**)
- **Validation only** — each targeted JSON instance must be checked for conformance to **`universe_scanner_result.schema.json`** only (**not** request schema as a combined pipeline).
- **No request→result or scanner-backed generation** — **no** code path that **creates** or **fills** `UniverseScannerResult` from **`UniverseScannerRequest`**, ingress, FR payloads, or scanner logic. **Model B** allows **at most three** valid root JSON files **only** as **static hand-placed or copy-only** seeds per **§2** — **not** “generation” in the pipeline sense.
- **No request-to-result behavior** — **no** pairing step, **no** “derive result from request id,” **no** join across directories beyond **reading files named on disk** (validator may **not** read request directory to validate results).
- **No scanner business logic** — no ranking, scoring, selection, or interpretation of `candidate_outputs` beyond schema conformance checking.
- **No orchestration** — no schedulers, workers, queues.
- **No networking** — no HTTP, sockets, subprocess to remote tools.
- **No provider, dashboard, runtime product** — no adapters, UI, deployment wiring.
- **No lane reopen, evidence collection, registry/approval edits.**
- **No mutation of result packets** — validator **must not** rewrite, “fix,” or overwrite result files or contract files.
- **Output boundary** — **exit code** + **stdout/stderr** only.

---

## 2. Allowed artifact types (future tranche only)

| Category | Constraint |
|----------|------------|
| **One primary validator entry** | **Exactly one** script at **`future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/validate_universe_scanner_result_packets.py`** (path **fixed** unless a **future** governance tranche renames it). **`if __name__ == "__main__"`** allowed **only** to run validation and exit non-zero on failure. |
| **Optional usage notes** | **`future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/README_universe_scanner_result_packets.md`** — **short** only: how to run the validator, which paths it reads, what it does **not** do. |
| **Optional invalid fixtures** | **At most five** JSON files under **`future_modules/the_fade/outputs/phase3_universe_scanner_results/fixtures_invalid/`**, each **documented** in **`README_universe_scanner_result_packets.md`** (why it must fail). **No** network-generated content. |
| **Optional valid root seeds (Model B)** | **At most three** `*.json` files **directly** in the **root** of **`outputs/phase3_universe_scanner_results/`** — **only** if added as **static hand-placed or copy-only** artifacts; **must** be listed in **`README_universe_scanner_result_packets.md`** with source (e.g. “copied from `examples/universe_scanner_result.example.json`”). **Must not** be produced by the validator script. **Must not** be derived from **`UniverseScannerRequest`** or ingress. **Do not** imply scanner execution. |

**Validation target rule (future tranche):** Validate **every** `*.json` file **directly** in **`outputs/phase3_universe_scanner_results/`** (root only — **not** inside `fixtures_invalid/`). **Zero** root `*.json` is allowed — validator **must** document empty-root behavior (typically exit **0** with explicit message). **Hard cap:** **≤ 3** valid root `*.json` files in any implementation state. Additionally, if `fixtures_invalid/` exists, each file there **must** **fail** schema validation (documented expected failure class in README). Filenames must include **`_result_`** and a reason token (e.g. `_type_`, `_required_`) consistent with T91-style fixture naming.

**Explicitly forbidden:** Second validator entrypoint for this job, absorbing this into **`validate_ingress_request_packets.py`** without new governance, CI workflow files unless **separate** governance.

---

## 3. What the later validator may do

- Read **only**:
  - **`outputs/phase3_universe_scanner_results/*.json`** (root-level result packets — **optional**; may be **empty**)
  - **`schemas/universe_scanner_result.schema.json`**
  - **`outputs/phase3_universe_scanner_results/fixtures_invalid/*.json`** if present (expect invalid)
- Validate **result** packets against **result** schema **only**.
- Emit **exit code** and **stdout/stderr**; **non-zero** if any root-level packet is invalid or any `fixtures_invalid/` file incorrectly passes.
- **No writes** to result packets, contracts, or examples — **including** **no** creation of valid root-level result JSON by the validator (seeds, if any, are **hand-placed/copy-only** outside the validator’s write path).

---

## 4. Forbidden in the later implementation tranche

| Forbidden | Rationale |
|-----------|-----------|
| **Request→result generation** | Product pipeline |
| **Emitting `UniverseScannerResult` from `UniverseScannerRequest`** | Smuggled pipeline |
| **Scanner ranking / scoring / selection** | Business logic |
| **Multi-source ingestion** | Out of slice |
| **Provider adapters / dashboard / runtime orchestration** | Product surface |
| **Lane / registry / approval edits** | Phase 2 boundary |
| **Multi-slice bundling** | Validator + generator in one tranche |
| **“Tiny scanner”** | Disguised execution |
| **Second validator surface** | Parallel entrypoint |
| **Packet rewrite / auto-fix** | Mutates governed artifacts |
| **More than three valid root `*.json`** | Violates Model B cap |
| **Validator writes root result JSON** | Seeds must not be created by the validator |

---

## 5. Anti-drift rules

1. **One implementation slice only** — singular until new governance defines another slice.  
2. **One validator path only** — **`validate_universe_scanner_result_packets.py`**.  
3. **One result-packet directory only** — **`outputs/phase3_universe_scanner_results/`** (root + optional `fixtures_invalid/`).  
4. **Validation only** — no cross-directory “wiring” to requests.  
5. **No “while we’re here”** — no ingress or T87 contract-validator refactors in the same tranche.  
6. **No hidden transformation** — read JSON, validate, report; **no** write-back.  

---

## 6. Relationship to prior tranches

- **T87** validates **contract examples** under **`contracts/phase3_universe_scanner_io/examples/`**; **T93 slice** validates **module result artifacts** under **`outputs/phase3_universe_scanner_results/`** — **different directories**, **not** merged without governance.  
- **T82–T91** history in **`phase2_mvp_approval_scope_decision.json`** — **unchanged** in meaning; T93 **adds** **`post_t93_…`** only.

---

## 7. Non-claims

- T93 **does not** run the result-packet validator — it **authorizes** a **future** tranche to **add** it.  
- T93 **does not** authorize scanner execution, request→result pipelines, or production result emission. **Model B** seeds are **not** a production path — **static validation aids only**.  
- T93 **does not** prove production readiness.

# THE FADE — T90 offline validation of ingress-written request packets (governance lock)

**Prompt #:** 365  
**Phase #:** 3 — **post-live-ingress governance** (T90 **docs only**; **no** validator code in this tranche)  
**Tranche #:** 90  
**Label:** `THE_FADE_PHASE3_T90_GOVERNANCE_LOCK_OFFLINE_VALIDATION_OF_INGRESS_REQUEST_PACKETS`  

**Updated:** 2026-04-07T16:38:40+00:00  

---

## Purpose

**T89** delivers live Federal Register ingress that writes schema-valid **`UniverseScannerRequest`** JSON under **`future_modules/the_fade/inputs/phase3_universe_scanner_requests/`**. **T90** governs **exactly one next slice**: **offline-only validation** of those **ingress-written request packets** — **no** result generation, **no** scanner semantics, **no** network.

**T90 does not implement anything**, does not reopen lanes, does not authorize scanner execution or request-to-result behavior, and does not edit **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`**, or lane charters. **Scoped MVP (T80)** remains binding and **not** production maturity.

**Companion:** `THE_FADE_T90_OFFLINE_VALIDATION_OF_INGRESS_REQUEST_PACKETS_ACCEPTANCE_CRITERIA.md`.  
**Machine-readable note:** `phase2_mvp_approval_scope_decision.json` → **`post_t90_offline_validation_of_ingress_request_packets_governance`**.

**Governs from:** Post–**T89** checkpoint (**68db029**) and Prompt **#364** reality check (next honest move = governance lock for ingress-request validation only).

---

## 1. Next implementation slice — exact definition

**Governed slice name:** **Phase 3 — offline validation of ingress-written `UniverseScannerRequest` packets only.**

**In scope for exactly one future implementation tranche** (not T90 itself):

- **Local filesystem only** — reads under:
  - **`future_modules/the_fade/inputs/phase3_universe_scanner_requests/`** (ingress packets + optional bounded invalid fixtures per §2)
  - **`future_modules/the_fade/contracts/phase3_universe_scanner_io/schemas/universe_scanner_request.schema.json`** (**read-only**)
- **Validation only** — each targeted JSON instance must be checked for conformance to **`universe_scanner_request.schema.json`** only (**not** result schema, **not** example files as required pass targets unless governance explicitly lists them — default: validate **all** ingress packet files per §2).
- **No result packet generation** — **no** `UniverseScannerResult`, **no** result schema validation as a “success path” for scanner output.
- **No scanner business logic** — no symbol ranking, lane mapping, universe expansion, or request→result transformation.
- **No orchestration** — no schedulers, workers, queues.
- **No networking** — no HTTP, sockets, subprocess to remote tools.
- **No provider, dashboard, runtime product** — no adapters, UI, deployment wiring.
- **No lane reopen, evidence collection, registry/approval edits.**
- **No mutation of inputs** — validator **must not** rewrite, “fix,” or overwrite ingress packets or contract files.
- **Output boundary** — **exit code** + **stdout/stderr** only.

---

## 2. Allowed artifact types (future tranche only)

| Category | Constraint |
|----------|------------|
| **One primary validator entry** | **Exactly one** script at **`future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/validate_ingress_request_packets.py`** (path **fixed** unless a **future** governance tranche renames it). **`if __name__ == "__main__"`** allowed **only** to run validation and exit non-zero on failure. |
| **Optional usage notes** | **`future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/README_ingress_request_packets.md`** — **short** only: how to run the validator, which paths it reads, what it does **not** validate. |
| **Optional invalid fixtures** | **At most five** JSON files under **`future_modules/the_fade/inputs/phase3_universe_scanner_requests/fixtures_invalid/`**, each **documented** in **`README_ingress_request_packets.md`** (why it must fail). **No** network-generated content. |

**Validation target rule (future tranche):** Validate **every** `*.json` file **directly** in **`inputs/phase3_universe_scanner_requests/`** (root only — **not** inside `fixtures_invalid/`). Additionally, if `fixtures_invalid/` exists, each file there **must** **fail** schema validation (documented expected failure class in README).

**Explicitly forbidden:** Second validator script, modifying **`validate_universe_scanner_io_contracts.py`** to absorb this responsibility without new governance, CI workflow files unless **separate** governance.

---

## 3. What the later validator may do

- Read **only**:
  - **`inputs/phase3_universe_scanner_requests/*.json`** (root-level ingress packets)
  - **`schemas/universe_scanner_request.schema.json`**
  - **`inputs/phase3_universe_scanner_requests/fixtures_invalid/*.json`** if present (expect invalid)
- Validate **request** packets against **request** schema **only**.
- Emit **exit code** and **stdout/stderr**; **non-zero** if any root-level packet is invalid or any `fixtures_invalid/` file incorrectly passes.
- **No writes** to ingress packets, contracts, or examples.

---

## 4. Forbidden in the later implementation tranche

| Forbidden | Rationale |
|-----------|-----------|
| **Request→result / result emission** | Scanner boundary |
| **`UniverseScannerResult` output** | Out of slice |
| **Scanner ranking / scoring / selection** | Business logic |
| **Multi-source ingestion** | T89 single-source discipline |
| **Provider adapters / dashboard / runtime orchestration** | Product surface |
| **Lane / registry / approval edits** | Phase 2 boundary |
| **Multi-slice bundling** | Validator + ingress rewrite + scanner in one tranche |
| **“Tiny scanner”** | Disguised execution |
| **Second validator surface** | Parallel entrypoint for same job |
| **Packet rewrite / auto-fix** | Mutates governed inputs |

---

## 5. Anti-drift rules

1. **One implementation slice only** — singular until new governance defines another slice.  
2. **One validator path only** — **`validate_ingress_request_packets.py`**.  
3. **Validation only** — no semantic interpretation of FR or symbols.  
4. **No “while we’re here”** — no refactors of ingress tool or T87 contract validator in the same tranche.  
5. **No hidden transformation** — read JSON, validate, report; **no** write-back.  

---

## 6. Relationship to prior tranches

- **T87** validates **contract tree** examples/schemas; **T90 slice** validates **ingress output directory** — **complementary**, **not** a merge into one mega-validator without governance.  
- **T82–T89** history in **`phase2_mvp_approval_scope_decision.json`** — **unchanged** in meaning; T90 **adds** **`post_t90_…`** only.

---

## 7. Non-claims

- T90 **does not** run the ingress-request validator — it **authorizes** a **future** tranche to **add** it.  
- T90 **does not** authorize scanner execution or result packets.  
- T90 **does not** prove production readiness.

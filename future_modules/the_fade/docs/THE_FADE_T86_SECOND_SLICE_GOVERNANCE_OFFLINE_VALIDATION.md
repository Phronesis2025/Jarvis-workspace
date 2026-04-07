# THE FADE — T86 second implementation slice (offline contract validation governance)

**Prompt #:** 354  
**Phase #:** 3 — **second implementation slice governance** (T86 **docs only**; **no** validator code in this tranche)  
**Tranche #:** 86  
**Label:** `THE_FADE_PHASE3_T86_GOVERNANCE_LOCK_SECOND_SLICE_OFFLINE_CONTRACT_VALIDATION`  

**Updated:** 2026-04-07T12:32:37+00:00  

---

## Purpose

**T85** completed the **first** governed implementation slice: **static** universe-scanner I/O contracts under `future_modules/the_fade/contracts/phase3_universe_scanner_io/` (**T84** boundary). **T86** governs **exactly one second slice**: **offline-only validation** of that **existing** package — **no** new contract semantics, **no** scanner execution, **no** network.

**T86 does not implement anything**, does not reopen lanes, does not authorize scanner/runtime/dashboard/providers, and does not edit **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`**, or lane charters. **Scoped MVP (T80)** remains binding and **not** production maturity.

**Companion:** `THE_FADE_T86_SECOND_SLICE_ACCEPTANCE_CRITERIA.md`.  
**Machine-readable note:** `phase2_mvp_approval_scope_decision.json` → **`post_t86_second_slice_governance_offline_validation`**.

**Governs from:** Post–**T85** checkpoint (**07624a9**) and Prompt **#353** review (single next move = governance lock for offline validation).

---

## 1. Second implementation slice — exact definition

**Governed slice name:** **Phase 3 universe-scanner I/O — offline contract validation only.**

**In scope for exactly one future implementation tranche** (not T86 itself):

- **Local files only** — read paths under `future_modules/the_fade/contracts/phase3_universe_scanner_io/` (existing governed contract files, plus bounded `fixtures_invalid/` only if created by the validator tranche).
- **Validation only** — confirm JSON instances conform to **`universe_scanner_request.schema.json`** and **`universe_scanner_result.schema.json`** using a **local** validator (e.g. **`jsonschema`** loaded from disk; **no** HTTP fetch of meta-schemas unless **stdlib/file-only** resolution — prefer **bundled** draft-07 behavior without network).
- **No scanner business logic** — no interpretation of symbols, no lane mapping, no “scan” or “universe expansion,” no transformation of request → result except **what is strictly required** to **parse JSON and call the schema validator** (no semantic fill-ins).
- **No orchestration** — no schedulers, workers, queues, retries across machines.
- **No networking** — no `requests`, `httpx`, `urllib.request`, sockets, DNS, subprocess to curl, etc.
- **No provider, dashboard, runtime product** — no adapters, UI, APIs, deployment manifests.
- **No lane reopen, evidence collection, registry/approval edits.**
- **No contract artifact writes** — validator tranche may **not** modify `schemas/`, `examples/`, `types/`, or the contract-package `README.md`; any contract change requires a separate later governance tranche.
- **Output boundary** — validator may emit **exit code** and **stdout/stderr** only.

---

## 2. Allowed artifact types (future tranche only)

| Category | Constraint |
|----------|------------|
| **One primary validator entry** | **Exactly one** Python module **or** script at **`future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/validate_universe_scanner_io_contracts.py`** (path **fixed** unless a **future** governance tranche renames it). It **may** expose **`if __name__ == "__main__"`** **only** to run validation and exit with non-zero on failure — **not** to perform any other Phase 3 behavior. |
| **Optional negative fixtures** | **At most five** JSON files under **`future_modules/the_fade/contracts/phase3_universe_scanner_io/fixtures_invalid/`**, each **documented** in **`tools/README.md`** (which schema it targets, why it must fail). **No** network-generated content. |
| **Optional usage notes** | **`future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/README.md`** — **short** only: how to run the validator, what it checks, what it does **not** check. **Not** a Phase 3 roadmap. |

**Explicitly forbidden in the implementation tranche:** Second validator script, test suite spread across `stock_module/`, CI workflow files **unless** a **separate** governance tranche authorizes CI — **not** part of this slice (keep slice to **tools/** + **fixtures_invalid/** only).

---

## 3. Forbidden in the second implementation tranche (even if “small”)

| Forbidden | Rationale |
|-----------|-----------|
| **Scanner execution logic** | Enumerating universes, producing real scan results, merging lanes |
| **Request → result generation** | Any logic that fabricates a **`UniverseScannerResult`** from a **`UniverseScannerRequest`** beyond schema round-trip tests **if** explicitly bounded — **prefer** no generation; **only** validate provided files |
| **Scheduling / jobs / workers** | Runtime orchestration |
| **Network calls** | Any remote I/O |
| **Provider / dashboard** | Product surfaces |
| **Lane reopen / evidence / registry / approval** | Phase 2 boundary |
| **Multi-slice bundling** | Validator **plus** scanner stub **plus** config in one tranche |
| **Contract artifact edits** | Any write/rewrite of governed contract artifacts (`schemas/`, `examples/`, `types/universe_scanner_io_types.pyi`, contract `README.md`) |
| **Widening** | Any attempt to use validator work to alter contract semantics; all contract changes require a separate governance tranche |

---

## 4. Anti-drift rules

1. **One second slice only** — this slice is **singular** until **new** governance defines a third slice.  
2. **Validation only** — if it does not **fail closed** on invalid JSON against the **existing** schemas, it is **out of scope**.  
3. **No “tiny scanner”** — no naming, UX, or code paths that **simulate** a scan.  
4. **No second surface** — no parallel CLI under `scripts/` for the same job without new governance.  
5. **Contract package boundary** — all new files stay under **`contracts/phase3_universe_scanner_io/tools/`** and **`fixtures_invalid/`** (and **optional** `tools/README.md` only).
6. **Read-only contract package** — validator tranche reads governed contract files and bounded invalid fixtures only; it may not write governed contract files.

---

## 5. Relationship to prior tranches

- **T82–T85** history and **`post_t82`**, **`post_t83`**, **`post_t84`**, **`post_t85`** blocks in **`phase2_mvp_approval_scope_decision.json`** — **unchanged** in meaning; T86 **adds** **`post_t86_…`** only.  
- **T84** first slice = static contracts (**done** in T85). **T86** second slice = **offline validation** of that tree (**not** done until a **future** implementation tranche).

---

## 6. Non-claims

- T86 **does not** run the validator — it **only** **authorizes** a **future** tranche to **add** it.  
- T86 **does not** prove a universe scanner works.  
- T86 **does not** authorize executable Phase 3 beyond this **single** validation slice.

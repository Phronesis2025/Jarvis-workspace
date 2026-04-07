# THE FADE — T86 second slice acceptance criteria (offline validation)

**Prompt #:** 354  
**Tranche #:** 86  
**Label:** `THE_FADE_PHASE3_T86_GOVERNANCE_LOCK_SECOND_SLICE_OFFLINE_CONTRACT_VALIDATION`  

**Updated:** 2026-04-07T12:32:37+00:00  

**Governance source:** `THE_FADE_T86_SECOND_SLICE_GOVERNANCE_OFFLINE_VALIDATION.md`  

---

## Scope

These criteria apply to **one future implementation tranche** that claims the **T86 governed second slice** (offline contract validation only). **T86 itself** (Prompt **#354**) is **governance only** — it **satisfies no** implementation success criteria below.

---

## Success (all should be true after that future tranche)

1. **Validator exists** — **`tools/validate_universe_scanner_io_contracts.py`** present and **when run** (from repo root or documented cwd) validates:
   - **`examples/universe_scanner_request.example.json`** against **`schemas/universe_scanner_request.schema.json`**
   - **`examples/universe_scanner_result.example.json`** against **`schemas/universe_scanner_result.schema.json`**
   - Exit code **0** on success.
2. **Contract package unchanged** — No edits to governed contract artifacts: `schemas/`, `examples/`, `types/universe_scanner_io_types.pyi`, or contract-package `README.md`.
3. **Local-only and read-bounded** — Validator uses **only** filesystem reads under **`contracts/phase3_universe_scanner_io/`** and validates only governed artifacts plus bounded `fixtures_invalid/` if present; emits exit code and stdout/stderr only.
4. **Negative fixtures** — If **`fixtures_invalid/`** exists: **each** file **fails** validation against the **named** target schema; **≤ 5** files; each listed in **`tools/README.md`** with one-line intent.
5. **No forbidden integrations** — No edits to **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`**, lane charters; no new evidence collection; no dashboard/provider/runtime orchestration.
6. **Honest labeling** — Commit / note states **only** T86 second slice (offline validation), **not** “scanner shipped.”

---

## Failure (any one is sufficient)

1. **Examples do not validate** — Success path does not pass after the tranche.  
2. **Network** — Any introduced network I/O in the validator or its dependencies **as invoked by this tranche’s code path**.  
3. **Contract edits** — Any write or rewrite of governed contract artifacts (`schemas/`, `examples/`, `types/universe_scanner_io_types.pyi`, contract `README.md`).  
4. **Scope write leakage** — Any writes outside bounded validator scope (`tools/`, optional `fixtures_invalid/`, optional `tools/README.md`).  
5. **Scanner / business logic** — Request→result synthesis, symbol resolution, lane logic, or “demo scan” output.  
6. **Wrong location** — Validator primary entry **not** at the governed path (unless **new** governance moved it).  
7. **Bundle creep** — Same tranche adds scanner stubs, Phase 2 scripts, or stock-module integration.

---

## Scope violation (stop and revert / governance escalation)

1. **Second surface** — Duplicate validator under another path doing overlapping work.  
2. **Contract artifact mutation** — Any validator-tranche edit to governed contract files (`schemas/`, `examples/`, `types/`, contract `README.md`) without separate governance.  
3. **Request-to-result behavior** — Any code that generates scanner results or implements request→result semantics.  
4. **“Tiny scanner”** — Any code path named or structured as a scan runner.  
5. **Second helper surface** — Any additional tool, wrapper, or parallel entrypoint beyond the governed validator path.  
6. **Multi-slice** — Validator **plus** executable Phase 3 feature in one commit/tranche.

---

## Anti-drift checklist (before merge of future tranche)

- [ ] Grep validator for `http`, `urllib`, `requests`, `socket`, `subprocess` — **should be clean** (stdlib file open OK).  
- [ ] No `mvp_lane` string edits in diff.  
- [ ] File count in **`fixtures_invalid/`** ≤ **5**.  
- [ ] **`tools/README.md`** ≤ **~1 screen** of prose.

---

## Non-claims

Passing these criteria **does not** mean Phase 3 scanner exists, production readiness, or lane approval expansion.

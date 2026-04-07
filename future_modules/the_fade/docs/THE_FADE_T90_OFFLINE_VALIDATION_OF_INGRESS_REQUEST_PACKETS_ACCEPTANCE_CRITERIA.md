# THE FADE — T90 offline ingress-request validation acceptance criteria

**Prompt #:** 365  
**Tranche #:** 90  
**Label:** `THE_FADE_PHASE3_T90_GOVERNANCE_LOCK_OFFLINE_VALIDATION_OF_INGRESS_REQUEST_PACKETS`  

**Updated:** 2026-04-07T16:38:40+00:00  

**Governance source:** `THE_FADE_T90_OFFLINE_VALIDATION_OF_INGRESS_REQUEST_PACKETS_GOVERNANCE.md`  

---

## Scope

These criteria apply to **one future implementation tranche** that claims the **T90 governed slice** (offline validation of ingress-written `UniverseScannerRequest` packets only). **T90 itself** (Prompt **#365**) is **governance only** — it **satisfies no** implementation success criteria below.

---

## Success (all should be true after that future tranche)

1. **Validator exists** at **`contracts/phase3_universe_scanner_io/tools/validate_ingress_request_packets.py`** and, when run, validates **every** `*.json` in **`inputs/phase3_universe_scanner_requests/`** (root only, not `fixtures_invalid/`) against **`schemas/universe_scanner_request.schema.json`**.  
2. **Local-only** — **no** network I/O in the validator code path; **read-only** access to schema + input JSON files.  
3. **Request schema only** — **no** validation pass/fail logic tied to **`universe_scanner_result.schema.json`** or emission of result payloads.  
4. **No mutation** — validator does **not** write, rewrite, or “fix” ingress packets or contract files.  
5. **No contract writes** — schemas/examples/types/contract README remain unchanged by this tranche.  
6. **Exit behavior** — exit code **0** if all root-level packets valid and (if present) all `fixtures_invalid/` files invalid as documented; **non-zero** otherwise.  
7. **Optional fixtures** — If **`fixtures_invalid/`** exists: **≤ 5** files; each fails validation; each documented in **`README_ingress_request_packets.md`**.  
8. **Honest labeling** — Commit/note states **only** T90 ingress-request validation slice, **not** “scanner shipped.”

---

## Failure (any one is sufficient)

1. **Invalid root packet passes** — Any `*.json` in ingress root directory is not schema-valid but tranche claims success.  
2. **Network** — Any network I/O introduced for this validator.  
3. **Result path** — Any `UniverseScannerResult` generation or result-schema validation as product output.  
4. **Mutation** — Any write to ingress packets or contract artifacts.  
5. **Wrong path** — Validator primary entry not at the governed path (unless new governance moved it).  
6. **Wrong scope** — Validator validates non-request schemas as required success targets (e.g. bundled result examples) without explicit governance.

---

## Scope violation (stop and revert / governance escalation)

1. **Second surface** — Duplicate validator or wrapper script doing overlapping work.  
2. **Scanner smuggle** — Ranking, “scan,” or request→result logic in validator.  
3. **Auto-fix** — Rewriting packets to pass schema.  
4. **Multi-slice** — Validator tranche + ingress rewrite + scanner stub in one change.  

---

## Anti-drift checklist (before merge of future tranche)

- [ ] Grep validator for `http`, `urllib`, `requests`, `socket` — **clean** (stdlib file I/O only).  
- [ ] No `open(..., "w")` or equivalent targeting ingress or contract paths.  
- [ ] No `mvp_lane` edits.  
- [ ] **`fixtures_invalid/`** count ≤ **5**.  

---

## Non-claims

Passing these criteria **does not** mean a universe scanner exists, production readiness, or lane approval expansion.

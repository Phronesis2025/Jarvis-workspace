# THE FADE — T93 offline `UniverseScannerResult` packet validation acceptance criteria

**Prompt #:** 368 (boundary repair **#369**)  
**Tranche #:** 93  
**Label:** `THE_FADE_PHASE3_T93_GOVERNANCE_LOCK_OFFLINE_VALIDATION_OF_UNIVERSE_SCANNER_RESULT_PACKETS`  

**Updated:** 2026-04-07T19:29:42+00:00  

**Governance source:** `THE_FADE_T93_OFFLINE_VALIDATION_OF_UNIVERSE_SCANNER_RESULT_PACKETS_GOVERNANCE.md`  

**Valid root packet model:** **Model B — bounded static seeding** (see governance Purpose + §2). **Not** Model A (strict zero valid root files allowed in the implementation tranche).

---

## Scope

These criteria apply to **one future implementation tranche** that claims the **T93 governed slice** (offline validation of on-disk `UniverseScannerResult` packets only). **T93 itself** (Prompt **#368**, repair **#369**) is **governance only** — it **satisfies no** implementation success criteria below.

---

## Success (all should be true after that future tranche)

1. **Validator exists** at **`contracts/phase3_universe_scanner_io/tools/validate_universe_scanner_result_packets.py`** and, when run, validates **every** `*.json` in **`outputs/phase3_universe_scanner_results/`** (root only, not `fixtures_invalid/`) against **`schemas/universe_scanner_result.schema.json`**. If **zero** root `*.json` exist, **documented** empty-root behavior is **PASS** (exit **0**) with explicit stdout (e.g. `nothing to validate`).  
2. **Local-only** — **no** network I/O in the validator code path; **read-only** access to schema + result JSON files.  
3. **Result schema only** — **no** validation logic that **requires** reading **`UniverseScannerRequest`** or ingress **`inputs/phase3_universe_scanner_requests/`** to pass.  
4. **Validator does not write result JSON** — the validator **does not** use **`open(..., "w")`** or equivalent to create or overwrite **root** or **`fixtures_invalid/`** result files.  
5. **No request→result or scanner-backed generation** — **no** code in the tranche that **creates** or **fills** result JSON from requests, ingress, or scanner logic.  
6. **Model B seed cap** — **at most three** valid root-level `*.json` files in **`outputs/phase3_universe_scanner_results/`**; if any exist, each is **schema-valid** and **documented** in **`README_universe_scanner_result_packets.md`** as **static hand-placed or copy-only** (with stated source, e.g. contract example path); **none** imply scanner execution.  
7. **No mutation** — validator does **not** rewrite or “fix” result packets or contract files.  
8. **No contract writes** — schemas/examples/types/contract README remain unchanged by this tranche.  
9. **Exit behavior** — exit code **0** if all root-level packets valid (or empty root per item 1) and (if present) all `fixtures_invalid/` files invalid as documented; **non-zero** otherwise.  
10. **Optional invalid fixtures** — If **`fixtures_invalid/`** exists: **≤ 5** files; each fails validation; each documented in **`README_universe_scanner_result_packets.md`**.  
11. **Honest labeling** — Commit/note states **only** T93 result-packet validation slice, **not** “scanner shipped” or “request→result live.”

---

## Failure (any one is sufficient)

1. **Invalid root packet passes** — Any `*.json` in the result root directory is not schema-valid but tranche claims success.  
2. **Network** — Any network I/O introduced for this validator.  
3. **Request→result or scanner generation** — Any code path that **creates** or **fills** result JSON from **`UniverseScannerRequest`**, ingress, or scanner logic.  
4. **Validator writes root or fixture result JSON** — The validator script **creates** or **overwrites** any result JSON under the governed directory.  
5. **Contract/schema unintended edits** — Any change to governed contract artifacts beyond the allowed tranche scope.  
6. **More than three valid root `*.json`** — **Model B** cap **exceeded**.  
7. **Wrong path** — Validator primary entry not at the governed path (unless new governance moved it).  
8. **Wrong scope** — Validator validates request packets or merges request+result pipeline behavior.

---

## Scope violation (stop and revert / governance escalation)

1. **Second surface** — Duplicate validator or overlapping entrypoint for the same job.  
2. **Pipeline smuggle** — Code that loads paired request JSON to build or “check” result JSON.  
3. **Auto-fix** — Rewriting packets to pass schema.  
4. **Multi-slice** — Result validator tranche + result generator stub in one change.  
5. **Fourth valid root seed** — More than **three** valid root `*.json` files in the governed directory.  

---

## Anti-drift checklist (before merge of future tranche)

- [ ] Grep validator for `http`, `urllib`, `requests`, `socket` — **clean** (stdlib file I/O only).  
- [ ] No `open(..., "w")` or equivalent **in the validator** targeting result or contract paths.  
- [ ] No `mvp_lane` edits.  
- [ ] Valid root `*.json` count **≤ 3**; **`fixtures_invalid/`** count ≤ **5**.  

---

## Non-claims

Passing these criteria **does not** mean a universe scanner exists, production readiness, or lane approval expansion.

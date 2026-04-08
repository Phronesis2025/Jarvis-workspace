# THE FADE — T95 first request→result bridge — acceptance criteria (future tranche)

**Prompt #:** 375  
**Tranche #:** 95 (governance lock); criteria apply to **one future** implementation tranche  
**Label:** `THE_FADE_PHASE3_T95_GOVERNANCE_LOCK_FIRST_REQUEST_TO_RESULT_BRIDGE_SLICE`  

**Updated:** 2026-04-07T22:05:00+00:00  

**Governance source:** `THE_FADE_T95_FIRST_REQUEST_TO_RESULT_BRIDGE_GOVERNANCE.md`  

**Note:** **T95** is **governance only**. No criterion below is satisfied by T95 itself.

---

## Scope

These criteria apply to **one future implementation tranche** that claims the **T95 governed slice** (first mechanical request→result bridge). **T95** (Prompt **#375**) satisfies **no** implementation success criteria below.

---

## Success (all should be true after that future tranche)

1. **Bridge exists** at **`future_modules/the_fade/bridge/first_request_to_result/build_universe_scanner_result_from_single_request.py`** and, when invoked per README, reads **exactly one** JSON file from **`inputs/phase3_universe_scanner_requests/`** (root only) and writes **exactly one** new JSON file to **`outputs/phase3_universe_scanner_results/`** (root only).  
2. **Schema-valid request** — input file conforms to **`universe_scanner_request.schema.json`** at read time (validated in-script or pre-validated by operator with **no** silent mutation).  
3. **Schema-valid result** — output file conforms to **`universe_scanner_result.schema.json`** before the tranche claims success (in-script validation preferred).  
4. **`scanner_status`** on the written result is **`pending`** only.  
5. **`candidate_outputs`** follows **T95 §3.2** — **only** **`deferred`** rows; **only** the mechanical mapping from **`candidate_symbols`** or the single-row opaque-ref rule; **fixed** omission_reason literals as in governance.  
6. **One-in-one-out** — no batch directories, no multiple request reads, no multiple result writes in the same tranche deliverable.  
7. **Local-only** — **no** network I/O, **no** provider/dashboard/runtime/orchestration code in the bridge path.  
8. **No ranking/selection** — grep-level: no sorting-for-priority, no scoring, no “pick top N”, no inclusion/exclusion beyond the mechanical rules.  
9. **No lane/registry/approval edits** — **`mvp_lane_approval.json`** and **`mvp_lane_evidence_registry.json`** unchanged by the tranche.  
10. **Optional README only** — at most **`future_modules/the_fade/bridge/first_request_to_result/README.md`**; no second bridge entrypoint.  
11. **Honest labeling** — commit/message/docs state **only** the bounded bridge slice, **not** “scanner shipped” or “production result path.”

---

## Failure (any one is sufficient)

1. **Invalid request or result** — either packet fails its schema when the tranche claims success.  
2. **Wrong counts** — more than one request read or more than one result write **per invocation** / per defined CLI contract.  
3. **`scanner_status` not `pending`** — e.g. **`completed`** emitted.  
4. **Row_status `included` / `excluded`** in bridge output — violates placeholder-only rule.  
5. **Network or multi-source** — any HTTP/socket/subprocess remote behavior in the bridge.  
6. **Ranking/selection logic** — any non-mechanical symbol handling.  
7. **Wrong path** — primary entry not at the governed script path (unless new governance moved it).  
8. **Second surface** — duplicate CLI or overlapping module for the same bridge job.  
9. **Registry/approval touched** — unintended edits to lane JSON.  
10. **Bundling** — scanner stub, runtime wiring, or unrelated refactors shipped as the same “bridge” tranche.

---

## Scope violation (stop and revert / governance escalation)

1. **Bridge writes or overwrites ingress request packets** or contract schemas.  
2. **Bridge invokes Federal Register ingress** or any live fetch.  
3. **Result rows derived from live APIs** or from data not present in the single request JSON.  
4. **“Tiny scanner”** — loops that look like evaluation/ranking beyond mechanical per-symbol deferred rows.  
5. **Multi-slice bundling** — bridge + new validator + ingress changes in one governed claim without new governance.  

---

## Anti-drift checklist (before merge of future tranche)

- [ ] Grep bridge for `http`, `urllib`, `requests`, `socket` — **clean**.  
- [ ] Confirm **one** script path matches governance.  
- [ ] Confirm **`scanner_status`** is **`pending`** only in code paths that emit results.  
- [ ] Confirm **`row_status`** in emitted rows is **`deferred`** only.  
- [ ] No `mvp_lane` path edits in diff.  

---

## Non-claims

Passing these criteria **does not** mean a universe scanner exists, production readiness, or lane approval expansion.

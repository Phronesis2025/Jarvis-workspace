# THE FADE — T84 first implementation slice acceptance criteria

**Prompt #:** 346  
**Tranche #:** 84  
**Label:** `THE_FADE_PHASE3_T84_FIRST_IMPLEMENTATION_GOVERNANCE_LOCK`  

**Updated:** 2026-04-07T14:00:00+00:00  

**Governance source:** `THE_FADE_T84_FIRST_IMPLEMENTATION_SLICE_GOVERNANCE.md`  

---

## Scope

These criteria apply to **one future implementation tranche** that claims the **T84 governed slice** (static universe-scanner I/O contract only). **T84 itself** (Prompt **#346**) is **governance only** — it **satisfies no** implementation success criteria below.

---

## Success (all should be true after that future tranche)

1. **Artifact class match** — New files are **only** schema/spec files, static example payloads, and/or non-executing typed contract stubs **as defined in T84 §2**.
2. **Location** — New artifacts live under `future_modules/the_fade/` (preferably `future_modules/the_fade/contracts/phase3_universe_scanner_io/` unless a **narrower** governed path exception exists).
3. **No execution** — No scanner loop, scheduler, worker, CLI `main`, or **network I/O** in **new** code added for this slice.
4. **No integration** — No dashboard, no production config, no provider wiring, no edits to **`mvp_lane_approval.json`** or **`mvp_lane_evidence_registry.json`**, no lane charter changes, no new evidence collection.
5. **Contract coherence** — Schemas/examples/stubs **align** with each other (same field names and documented semantics; examples validate against schema where applicable, or discrepancies are **explicitly** documented as intentional edge-case samples).
6. **Honest labeling** — Commit message / governed note (if any) states that the tranche is **only** the T84 first slice — **not** “Phase 3 started” broadly.

---

## Failure (any one is sufficient)

1. **Executable scanner or runtime** — Any new code that runs a scan, pulls remote data, or orchestrates repeated work.
2. **Network** — Any new `requests`, `httpx`, `urllib`, socket, or subprocess call to external services **introduced for this tranche**.
3. **Dashboard or operator surface** — Any UI or HTTP server added for Phase 3 monitoring/control.
4. **Provider / production** — Credential files, live endpoint wiring, or deployment manifests **for Phase 3**.
5. **Lane / registry churn** — Any change to **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`**, or lane charters **under the guise of** this slice.
6. **Evidence collection** — New Phase 2 observes, audits, or registry dimension updates bundled here.
7. **Incomplete contract** — Deliverables do not **actually** define scanner I/O (e.g. only empty placeholders with no fields) **and** the tranche claims slice completion — treat as **failed** or **not done**, not success.

---

## Scope violation (stop and revert / governance escalation)

Treat as **scope violation** (not merely “failure to finish”):

1. **Second surface** — Contract artifacts **plus** a runner, stub scanner that executes, or “temporary” script that hits the network.
2. **Multi-slice bundling** — Same tranche adds contract **and** runtime **and**/or dashboard **and**/or provider config.
3. **“While we’re here”** — Unrelated refactors, dependency bumps, or new modules outside `future_modules/the_fade/` contract tree **without** separate governance.
4. **Widening** — Using this slice to justify **any** Phase 3 behavior beyond **static** I/O definition.

**Response:** Stop implementation; document violation; **do not** merge as T84 slice success; require **new** governance for any corrected or expanded work.

---

## Anti-drift checklist (before merge of future tranche)

- [ ] Only one slice’s worth of files; no second feature set  
- [ ] No `__main__` / CLI entry in new Python **unless** purely `pass` or doc-only (prefer **no** `__main__`)  
- [ ] No imports of HTTP clients or async task runners in new contract modules  
- [ ] No changes to files listed as **forbidden** in T84 §3  
- [ ] README (if any) is **short** and contract-scoped  

---

## Non-claims

- Passing these criteria **does not** mean Phase 3 is **complete**, **production-ready**, or **approved beyond** this one static slice.
- **Further** Phase 3 work requires **new** explicit governance tranches.

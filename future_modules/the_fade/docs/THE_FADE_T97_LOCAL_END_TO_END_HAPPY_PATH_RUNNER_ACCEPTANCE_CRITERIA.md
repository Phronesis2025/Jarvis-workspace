# THE FADE — T97 local end-to-end happy-path runner — acceptance criteria (future tranche)

**Prompt #:** 381  
**Tranche #:** 97 (governance lock); criteria apply to **one future** implementation tranche  
**Label:** `THE_FADE_PHASE3_T97_GOVERNANCE_LOCK_LOCAL_END_TO_END_HAPPY_PATH_RUNNER`  

**Updated:** 2026-04-08T11:48:34+00:00  

**Governance source:** `THE_FADE_T97_LOCAL_END_TO_END_HAPPY_PATH_RUNNER_GOVERNANCE.md`  

**Note:** **T97** is **governance only**. No criterion below is satisfied by T97 itself.

---

## Scope

These criteria apply to **one future implementation tranche** that claims the **T97 governed slice** (local sequential runner over existing tools). **T97** (Prompt **#381**) satisfies **no** implementation success criteria below.

---

## Success (all should be true after that future tranche)

1. **Runner exists** at **`future_modules/the_fade/runner/local_happy_path/run_local_end_to_end_happy_path.py`** and, when run, **sequentially** invokes the **four** governed existing tools **in order** (ingress → ingress validation → bridge → result validation) **without** reimplementing their core logic.  
2. **Exit codes:** runner exits **0** iff **all** four subprocesses exit **0**; otherwise non-zero.  
3. **Console-only product:** runner adds **no** new persisted artifact types beyond what the four tools already write; **stdout/stderr** report steps, **PASS/FAIL**, and **identifiable paths** for the request and result packets produced in the run.  
4. **No new network in runner:** runner code path has **no** `urllib`, `requests`, `socket`, or raw HTTP **except** as may exist **inside** the **unchanged** T89 ingress when invoked.  
5. **Bridge input:** runner supplies the bridge with **only** a **basename** for a file under **`inputs/phase3_universe_scanner_requests/`**, obtained by a **documented** rule in **`README.md`** (e.g. parse ingress success line or newest `fr_universe_scanner_request_*.json` per governance).  
6. **Honest labeling:** README states **not** a scanner, **not** production orchestration; commit/message does not claim scanner ship.  
7. **Optional argument:** if present, **at most one** bounded passthrough (e.g. **`--per-page`** to ingress within **1..20** only), documented in README.  
8. **No lane/registry/approval edits** in the tranche diff.  
9. **At most** optional **`README.md`** in **`runner/local_happy_path/`** and **at most one** optional tiny helper **`.py`** in that directory if strictly necessary — **named** in README.

---

## Failure (any one is sufficient)

1. **Wrong path** — primary entry not at the governed runner path.  
2. **Skipped or reordered steps** — not ingress → validate requests → bridge → validate results.  
3. **False success** — runner exits **0** after a failed subprocess.  
4. **Rewritten tools** — ingress/validator/bridge logic copied or inlined to “speed up” the run.  
5. **New network** — runner opens sockets/HTTP beyond delegating to T89.  
6. **Scanner/ranking/selection** — any new logic that prioritizes symbols, scores, or “completes” a scan.  
7. **Second entrypoint** — duplicate CLI for the same job.  
8. **Runtime/platform** — scheduler, worker, dashboard, or provider wiring introduced as part of this slice.

---

## Scope violation (stop and revert / governance escalation)

1. **Bundling** — runner tranche + edits to **`mvp_lane_approval.json`** / **`mvp_lane_evidence_registry.json`**.  
2. **Multi-pipeline** — optional “fast path” that skips validation or ingress.  
3. **Evidence collection** — writing lane evidence or registry fields from the runner.  

---

## Anti-drift checklist (before merge of future tranche)

- [ ] Grep runner (excluding subprocess target paths) for `http`, `urllib`, `requests`, `socket` — **clean** of **new** client use in runner file(s).  
- [ ] Exactly **one** primary script path matches governance.  
- [ ] Subprocess order matches **§1** sequence in governance.  
- [ ] No `mvp_lane` path edits.  

---

## Non-claims

Passing these criteria **does not** mean a universe scanner exists, production readiness, or lane approval expansion.

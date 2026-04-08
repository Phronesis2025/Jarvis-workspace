# THE FADE — T99 clean local operator run surface — acceptance criteria (future tranche)

**Prompt #:** 385  
**Tranche #:** 99 (governance lock); criteria apply to one future implementation tranche  
**Label:** `THE_FADE_PHASE3_T99_GOVERNANCE_LOCK_CLEAN_LOCAL_OPERATOR_RUN_SURFACE`  

**Updated:** 2026-04-08T12:28:27+00:00  

**Governance source:** `THE_FADE_T99_CLEAN_LOCAL_OPERATOR_RUN_SURFACE_GOVERNANCE.md`

**Note:** T99 is governance only. No implementation criterion below is satisfied by T99 itself.

---

## Scope

These criteria apply to exactly one future implementation tranche that claims the T99 operator-surface slice.

---

## Success (all required)

1. **Entrypoint path:** one operator script exists exactly at  
   `future_modules/the_fade/operator/local_run/run_clean_local_happy_path.py`.
2. **Wrap behavior only:** operator script invokes T98 runner  
   `future_modules/the_fade/runner/local_happy_path/run_local_end_to_end_happy_path.py`  
   and does not reimplement ingress/validation/bridge/result logic.
3. **Clean run folder:** each invocation creates one folder under  
   `future_modules/the_fade/outputs/local_happy_path_runs/`  
   named `run_<YYYYMMDDTHHMMSSZ>/`.
4. **Run artifact identification:** request/result packets for that invocation are easy to identify and present in the run folder (copied artifacts allowed by governance).
5. **Concise summary artifact:** exactly one `run_summary.json` is written in that run folder and includes run id, status, and request/result paths.
6. **Console summary:** operator sees concise PASS/FAIL + run folder + summary path.
7. **Failure propagation:** non-zero exit if wrapped run fails or run-artifact identification fails.
8. **Bounded optionals only:** at most optional README and at most one optional tiny helper in same directory.
9. **No lane/registry/approval edits:** no changes to `mvp_lane_approval.json` or `mvp_lane_evidence_registry.json`.

---

## Failure (any one is sufficient)

1. Wrong entrypoint path or multiple operator entrypoints.
2. Reimplemented pipeline logic instead of wrapping T98 runner.
3. No per-run clean folder convention or unclear run ownership of artifacts.
4. No concise run summary output.
5. Exit code 0 despite a failed wrapped run.
6. Added scanner/ranking/scoring/selection behavior.
7. Added scheduler/worker/provider/dashboard/orchestration platform behavior.

---

## Scope violation (stop / governance escalation)

1. Bundling with scanner/runtime/provider/dashboard features.
2. Any lane reopen or evidence collection behavior added.
3. Any approval/registry file edits.
4. More than one implementation slice hidden in the same tranche.

---

## Anti-drift checklist (future tranche review)

- [ ] One entrypoint only at governed fixed path.
- [ ] T98 runner is wrapped (not replaced).
- [ ] One run-folder convention only (`outputs/local_happy_path_runs/run_<timestamp>/`).
- [ ] One concise summary artifact format only (`run_summary.json`).
- [ ] No scanner/provider/dashboard/runtime/scheduler expansion.

---

## Non-claims

Passing these criteria does not mean scanner readiness, production orchestration readiness, or lane approval expansion.

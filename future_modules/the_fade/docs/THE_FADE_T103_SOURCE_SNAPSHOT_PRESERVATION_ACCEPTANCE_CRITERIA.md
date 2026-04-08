# THE FADE — T103 source snapshot preservation — acceptance criteria (future tranche)

**Prompt #:** 393  
**Tranche #:** 103 (governance lock); criteria apply to one future implementation tranche  
**Label:** `THE_FADE_PHASE3_T103_GOVERNANCE_LOCK_SOURCE_SNAPSHOT_PRESERVATION`  

**Updated:** 2026-04-08T16:36:15+00:00  

**Governance source:** `THE_FADE_T103_SOURCE_SNAPSHOT_PRESERVATION_GOVERNANCE.md`

**Note:** T103 is governance only. No implementation criterion below is satisfied by T103 itself.

---

## Scope

These criteria apply to exactly one future implementation tranche that claims the T103 source snapshot preservation slice.

---

## Success (all required)

1. **Script path:** one script exists exactly at  
   `future_modules/the_fade/review/local_run/build_source_snapshot_from_run_folder.py`.
2. **Single-folder input:** script processes exactly one run folder per invocation under  
   `future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`.
3. **Read boundary:** script reads only:
   - `run_summary.json` in that run folder  
   - exactly one `fr_universe_scanner_request_*.json` in that run folder  
   - exactly one `bridge_universe_scanner_result_*.json` in that run folder  
   - optionally `operator_review.md` in that run folder (must not be required for PASS)
4. **No cross-folder reads:** script does not read `inputs/`, `outputs/phase3_universe_scanner_results/`, or other paths unless a **later governance tranche** explicitly extends the boundary (out of scope for T103).
5. **Output boundary:** writes exactly one JSON file named `source_snapshot.json` in that same run folder.
6. **Factual-only content:** snapshot contains only bounded factual fields and transparent mechanical extraction from on-disk data per governance section 5.
7. **No network / no AI:** script performs **no** network calls and **no** AI/LLM usage.
8. **No scanner claims:** snapshot explicitly states it is factual source context, **not** a scanner decision artifact.
9. **Bounded optionals only:** at most optional README and at most one optional tiny helper `.py` in the script directory.
10. **No lane/registry/approval edits:** no changes to `mvp_lane_approval.json` or `mvp_lane_evidence_registry.json`.

---

## Failure (any one is sufficient)

1. Wrong script path or multiple review/snapshot entrypoints for this slice.  
2. Reads any file outside the governed run-folder read boundary.  
3. Writes more than one snapshot artifact, wrong filename, or writes outside the run folder.  
4. Uses AI/LLM or free-form paraphrase of Federal Register content.  
5. Performs network/data fetches or invokes ingress/tools via subprocess for this slice.  
6. Adds recommendations, trade ideas, ranking/scoring/selection, or prioritization.  
7. Implies scanner completion, intelligence, or production readiness from a snapshot.  
8. Fabricates document titles, IDs, or lists not literally present in read-boundary fields.

---

## Scope violation (stop / governance escalation)

1. Bundling with scanner/runtime/provider/dashboard functionality.  
2. Any lane reopen or evidence collection behavior added.  
3. Any approval/registry file edits.  
4. Multiple slices hidden in the same tranche.

---

## Anti-drift checklist (future tranche review)

- [ ] One script only at governed fixed path.  
- [ ] One run folder processed per invocation.  
- [ ] One snapshot artifact only (`source_snapshot.json`) in run folder.  
- [ ] Factual extraction + transparent mechanical counts only.  
- [ ] No AI/LLM, no network, no scanner claims.  
- [ ] No cross-folder history scans.

---

## Non-claims

Passing these criteria does not imply scanner readiness, recommendation capability, production orchestration readiness, or lane approval expansion.

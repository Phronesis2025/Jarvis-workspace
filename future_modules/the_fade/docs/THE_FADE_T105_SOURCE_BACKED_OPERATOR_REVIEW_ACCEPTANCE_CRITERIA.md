# THE FADE — T105 source-backed operator review — acceptance criteria (future tranche)

**Prompt #:** 396  
**Tranche #:** 105 (governance lock); criteria apply to one future implementation tranche  
**Label:** `THE_FADE_PHASE3_T105_GOVERNANCE_LOCK_SOURCE_BACKED_OPERATOR_REVIEW`  

**Updated:** 2026-04-08T17:28:17+00:00  

**Governance source:** `THE_FADE_T105_SOURCE_BACKED_OPERATOR_REVIEW_GOVERNANCE.md`

**Note:** T105 is governance only. No implementation criterion below is satisfied by T105 itself.

---

## Scope

These criteria apply to exactly one future implementation tranche that claims the T105 source-backed operator review slice.

---

## Success (all required)

1. **Script path:** one script exists exactly at  
   `future_modules/the_fade/review/local_run/build_source_backed_operator_review_from_run_folder.py`.
2. **Single-folder input:** script processes exactly one run folder per invocation under  
   `future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`.
3. **Read boundary:** script reads only these files **in that run folder**, and all must exist for PASS:
   - `run_summary.json`  
   - exactly one `fr_universe_scanner_request_*.json`  
   - exactly one `bridge_universe_scanner_result_*.json`  
   - `operator_review.md`  
   - `source_snapshot.json`
4. **No cross-folder reads:** script does not read `inputs/`, other `outputs/` subtrees, or arbitrary history.
5. **Output boundary:** writes exactly one markdown file named `source_backed_operator_review.md` in that same run folder.
6. **Factual-only merge:** output presents bounded factual run/pipeline fields and bounded factual source fields; simple transparent mechanical counts only from result JSON.
7. **results_count rule:** if `results_count` appears in the markdown, it must be taken **only** from the numeric field already present in `source_snapshot.json` (no new parsing of Federal Register payloads).
8. **No network / no AI:** script performs no network calls and no AI/LLM usage.
9. **No scanner claims:** output explicitly states it is not a scanner decision artifact / not a decision engine.
10. **Bounded optionals only:** at most optional README and at most one optional tiny helper `.py` in the script directory.
11. **No lane/registry/approval edits:** no changes to `mvp_lane_approval.json` or `mvp_lane_evidence_registry.json`.

---

## Failure (any one is sufficient)

1. Wrong script path or multiple entrypoints for this slice.  
2. Reads files outside the five-file run-folder boundary.  
3. Writes more than one review artifact, wrong filename, or writes outside the run folder.  
4. Uses AI/LLM or inference-heavy summarization.  
5. Performs network/data fetches.  
6. Adds recommendations, trade ideas, prioritization, ranking/scoring/selection.  
7. Implies scanner completion, validation of markets, or automated decisions.  
8. Computes or fabricates `results_count` without using the value from `source_snapshot.json`.

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
- [ ] Five governed inputs only; all required for PASS.  
- [ ] One review artifact only (`source_backed_operator_review.md`) in run folder.  
- [ ] Factual merge + transparent mechanical counts only.  
- [ ] No AI/LLM, no network, no scanner claims.  

---

## Non-claims

Passing these criteria does not imply scanner readiness, recommendation capability, production orchestration readiness, or lane approval expansion.

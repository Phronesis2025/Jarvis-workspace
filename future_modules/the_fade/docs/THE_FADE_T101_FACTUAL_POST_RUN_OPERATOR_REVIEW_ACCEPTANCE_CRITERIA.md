# THE FADE — T101 factual post-run operator review — acceptance criteria (future tranche)

**Prompt #:** 390  
**Tranche #:** 101 (governance lock); criteria apply to one future implementation tranche  
**Label:** `THE_FADE_PHASE3_T101_GOVERNANCE_LOCK_FACTUAL_POST_RUN_OPERATOR_REVIEW`  

**Updated:** 2026-04-08T14:44:04+00:00  

**Governance source:** `THE_FADE_T101_FACTUAL_POST_RUN_OPERATOR_REVIEW_GOVERNANCE.md`

**Note:** T101 is governance only. No implementation criterion below is satisfied by T101 itself.

---

## Scope

These criteria apply to exactly one future implementation tranche that claims the T101 factual post-run review slice.

---

## Success (all required)

1. **Script path:** one review script exists exactly at  
   `future_modules/the_fade/review/local_run/build_operator_review_from_run_folder.py`.
2. **Single-folder input:** script processes exactly one run folder per invocation under  
   `future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`.
3. **Read boundary:** script reads only:
   - `run_summary.json`,
   - copied request JSON in that run folder,
   - copied result JSON in that run folder.
4. **Output boundary:** writes exactly one markdown review file named `operator_review.md` in that same run folder.
5. **Factual-only extraction:** output contains only bounded factual fields and transparent counts from on-disk data.
6. **No network / no AI:** script performs no network calls and no AI/LLM summarization.
7. **No scanner claims:** output explicitly states it is factual post-run review, not scanner decision artifact.
8. **Bounded optionals only:** at most optional README and at most one optional tiny helper in same directory.
9. **No lane/registry/approval edits:** no changes to `mvp_lane_approval.json` or `mvp_lane_evidence_registry.json`.

---

## Failure (any one is sufficient)

1. Wrong script path or multiple entrypoints.
2. Reads files outside governed run folder boundary.
3. Writes more than one review artifact or wrong artifact name.
4. Uses AI/LLM or inference-heavy summarization.
5. Performs network/data fetches.
6. Adds recommendations, trade ideas, ranking/scoring/selection content.
7. Implies scanner completion or intelligence claims.

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
- [ ] One review artifact only (`operator_review.md`) in run folder.
- [ ] Factual extraction + transparent counts only.
- [ ] No AI/LLM, no network, no scanner claims.

---

## Non-claims

Passing these criteria does not imply scanner readiness, recommendation capability, production orchestration readiness, or lane approval expansion.

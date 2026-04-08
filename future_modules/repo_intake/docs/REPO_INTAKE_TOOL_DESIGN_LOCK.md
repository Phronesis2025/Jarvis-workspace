# REPO INTAKE TOOL DESIGN LOCK

**Updated:** 2026-04-08  
**Status:** Design-locked; v1 bounded triage implementation now active  
**Type:** Future workflow / operator tooling  
**Scope:** Bounded GitHub repo intake, triage, and deeper-review recommendation

---

## 1. Purpose

The Repo Intake / Triage Worker is a **bounded operator-support worker** for reviewing GitHub repositories and deciding whether they are worth deeper investigation.

Its purpose is to:

- accept one or more GitHub repo URLs
- run a bounded repo triage pass
- classify the repo using fixed review profiles
- surface direct evidence, danger flags, and top files to inspect
- recommend whether deeper review is justified
- write durable markdown + JSON results

This worker exists to reduce operator review time and improve signal-vs-hype filtering.

---

## 2. What it is not

This worker is not:

- a broad autonomous web/repo roaming agent
- a roadmap authority
- a build approval engine
- a replacement for operator judgment
- a dashboard-first feature
- a repo code execution system

The worker may recommend.  
It may not silently approve adoption or expand build scope.

---

## 3. Current status

**Status:** Design-locked / not active

This worker is recognized as future workflow / operator tooling only.

It is **not** part of the current core phase-1 Jarvis proof loop.

It must not displace the phase-1 mission of proving the boring WCS packet -> Cursor -> QA -> logging loop.

---

## 4. Worker classification

**Type:** Future workflow / operator tooling worker

This is not a core runtime worker for current phase-1 execution.

---

## 5. Inputs

### Minimum required inputs

- `repo_url`
- `profile`
- `operator_note`

### Optional inputs

- `depth_mode`
- `keywords_of_interest`
- `known_bad_signals`

---

## 6. Outputs

### Minimum required outputs

- `repo_intake_result.json`
- `repo_intake_report.md`

### Optional deeper-review outputs

- `repo_deep_review_result.json`
- `repo_deep_review_report.md`

---

## 7. Shared classification scale

All repo intake reviews must use exactly one of:

- `materially_useful`
- `marginal`
- `too_fuzzy`
- `reject`

No additional rating labels are allowed without intentional revision.

---

## 8. Starting review profiles

The initial active review profiles are:

1. `generic_repo_triage`
2. `workflow_tooling`
3. `prediction_market_execution`

Deferred but recognized later profiles:

- `agent_control_plane`
- `market_data_research_pipeline`

---

## 9. Shared scoring model

All starting profiles use the same top-level scoring structure:

- `repo_reality_score` (0–50)
- `our_fit_score` (0–40)
- `novelty_flag` (0–10, not part of normal score)
- `fatal_flags` (override / downgrade logic)

---

## 10. Shared scoring intent

The score exists to support:

1. deeper review or not
2. best-fit classification
3. risk if overvalued

The score does not exist to simulate certainty or approve architecture truth.

---

## 11. Shared output requirements

Every repo intake result must contain:

- repo identity
- profile used
- summary of what the repo appears to be
- direct repo-evidence findings
- top positive signals
- top negative signals
- danger flags
- top files to inspect first
- best fit for us
- what to steal
- what not to steal
- deeper-review recommendation
- deeper-review questions

---

## 12. Hard limits

The minimum honest version of this worker must not:

- execute repo code
- install repo dependencies automatically
- run arbitrary setup scripts
- touch secrets, wallets, or signing flows
- browse broadly beyond bounded repo review scope
- promote a repo directly into active build scope
- start as a dashboard-first surface

---

## 13. Review profile truth

Review profiles are machine-readable and governed by the repo intake profile contract JSON.

Any change to profile names, score dimensions, weights, thresholds, or fatal flags must be updated in both:

- markdown design lock
- machine-readable profile contract

---

## 14. Shared scoring structure

### 14.1 Repo Reality Score (0–50)

This measures what is actually present and directly verifiable inside the repo.

### 14.2 Our Fit Score (0–40)

This measures how much the repo solves a real problem for us or exposes reusable patterns.

### 14.3 Novelty Flag (0–10)

This is not part of the normal score.

It is an escalation flag for unusual but credible new ideas that may deserve deeper review even if normal fit is only medium.

### 14.4 Fatal flags

Fatal flags may override normal scoring and downgrade a repo to `too_fuzzy` or `reject`.

---

## 15. Shared classification thresholds

### materially_useful
- Repo Reality Score >= 32
- Our Fit Score >= 24
- no fatal flags triggered

### marginal
- Repo Reality Score >= 24
- Our Fit Score >= 16

### too_fuzzy
Use when:
- evidence is too thin
- fit is unclear
- danger is too high
- novelty exists but proof is weak

### reject
Use when:
- repo substance is weak
- hype dominates mechanism
- danger is clear and controls are weak
- no real problem is solved for us

---

## 16. Starting profile definitions

### 16.1 generic_repo_triage

**Purpose:** Fast first-pass repo judgment.

#### Repo Reality dimensions
- `code_substance` (0–15)
- `repo_clarity` (0–10)
- `evidence_quality` (0–10)
- `maintenance_seriousness` (0–5)
- `safety_boundedness` (0–10)

#### Our Fit dimensions
- `problem_relevance` (0–15)
- `reuse_potential` (0–10)
- `workflow_runtime_clarity` (0–10)
- `complexity_penalty` (0 to -5)

#### Fatal flags
- `readme_hype_with_weak_code`
- `obvious_secret_sloppiness`
- `fake_pnl_as_proof`
- `no_clear_mechanism`
- `docs_bundle_masks_thin_repo`

---

### 16.2 workflow_tooling

**Purpose:** Judge tools that improve build/review/research workflow.

#### Repo Reality dimensions
- `operator_leverage_surface` (0–15)
- `local_first_replaceability` (0–10)
- `repo_substance` (0–10)
- `evidence_quality` (0–10)
- `safety_privacy_discipline` (0–5)

#### Our Fit dimensions
- `friction_reduction_for_us` (0–15)
- `integration_ease` (0–10)
- `reusable_pattern_value` (0–10)
- `lockin_complexity_penalty` (0 to -5)

#### Fatal flags
- `cloud_lockin_disguised_as_utility`
- `weak_repo_strong_marketing`
- `tool_tries_to_be_entire_stack`
- `no_clear_operator_pain_solved`

---

### 16.3 prediction_market_execution

**Purpose:** Judge repos that touch prediction-market execution, orderbooks, market making, arbitrage, or skills.

#### Repo Reality dimensions
- `execution_market_surface` (0–15)
- `safety_risk_discipline` (0–15)
- `data_microstructure_realism` (0–10)
- `evidence_quality` (0–10)
- `danger_penalty` (0 to -10)

#### Our Fit dimensions
- `pattern_extraction_value` (0–15)
- `research_workflow_relevance` (0–10)
- `portability` (0–10)
- `prematurity_penalty` (0 to -5)

#### Fatal flags
- `copy_trading_main_value_prop`
- `direct_secret_or_key_sloppiness`
- `no_paper_mode`
- `no_risk_controls`
- `pnl_flex_as_proof`
- `live_execution_without_kill_logic`
- `magical_ai_makes_money_framing`
- `no_clear_separation_between_data_auth_execution_and_monitoring`

---

## 17. Repo Intake / Triage Worker note

Repo Intake / Triage is approved as future workflow tooling only.

It may support:

- GitHub repo review
- reusable pattern extraction
- deeper-review recommendation
- keeper/watchlist maintenance

It may not:

- execute repo code
- self-approve adoption
- silently expand active build scope
- replace operator judgment

---

## 18. Worker workflow contract

### 18.1 Worker statuses

The worker must use only these statuses:

- `queued`
- `triage_in_progress`
- `triage_complete`
- `deep_review_requested`
- `deep_review_in_progress`
- `deep_review_complete`
- `escalated`
- `rejected`

No additional status labels are allowed without intentional contract revision.

### 18.2 Final dispositions

The final disposition must be exactly one of:

- `materially_useful`
- `marginal`
- `too_fuzzy`
- `reject`

### 18.3 Stop conditions

The worker must stop and surface an explicit stop reason when:

- repo URL is invalid or unreachable
- repo cannot be classified with available evidence
- repo appears unsafe to inspect further
- repo requires code execution to verify core claims
- repo scope exceeds bounded intake review

### 18.4 Escalation conditions

The worker should escalate for operator judgment when:

- `novelty_flag` is high but fit is unclear
- repo appears materially useful but classification confidence is low
- README/docs claims conflict with code evidence
- a fatal flag is triggered but repo still appears strategically interesting

### 18.5 Minimum workflow

The minimum bounded workflow is:

1. intake
2. triage
3. optional deep review
4. final disposition

Expressed as:

`intake -> triage -> optional deep review -> final disposition`

---

## 19. Current implemented state (v1)

Current local implementation supports:

- single-repo bounded static triage run
- batch triage run over multiple items
- per-repo JSON + markdown outputs
- batch summary JSON + markdown outputs
- supported profiles: `generic_repo_triage`, `workflow_tooling`, `prediction_market_execution`
- prediction-market scoring refinement for mechanics-oriented static signals

Current run commands:

- single: `py -3 future_modules/repo_intake/scripts/run_repo_intake.py --input future_modules/repo_intake/inputs/example_repo_intake_input.json`
- batch: `py -3 future_modules/repo_intake/scripts/run_repo_intake_batch.py --input future_modules/repo_intake/inputs/example_repo_intake_batch.json`

---

## 20. Current deferred items

Intentionally deferred:

- deep-review runtime flow and artifacts generation
- repo cloning and any target-repo code execution
- dependency installation in target repos
- dashboard/API/server surface
- async/concurrent processing model

This remains a bounded first-pass operator-support tool.

---

## 21. Batch behavior

Batch runner behavior is continue-on-error:

- one failing item must not stop the full batch
- successful items still generate normal per-repo outputs
- batch summary records success and failure counts
- failed items include `repo_url`, `profile_used` when available, `status=failed`, and `error_message`

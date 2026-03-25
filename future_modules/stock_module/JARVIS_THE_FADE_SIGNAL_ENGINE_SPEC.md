# JARVIS_THE_FADE_SIGNAL_ENGINE_SPEC.md

**Document Type:** Signal Engine Technical Specification  
**Status:** Proposed Canonical Spec  
**Version:** 1.0  
**Last Updated:** 2026-03-23  
**Owner:** Jason  
**Project Context:** Jarvis future worker / stock intelligence side quest

---

# 1. Purpose of This Document

This document defines the **signal-engine layer** of THE FADE in precise terms.

It covers:
- the Universe Scanner
- source-lane definitions
- the Minimal Viable Data Stack
- normalized event structure
- direction-model rules
- lane scoring
- contra-signal logic
- fusion/conflict logic
- signal packet contracts
- escalation behavior
- the first bounded proof slice

This document is the **core worker/system logic spec** for the scout layer.

It is not:
- the plain-English overview
- the full-stack build checklist
- the storage/layout spec
- the paper-trading spec
- the dashboard spec

---

# 2. Scope of This Spec

## 2.1 In scope

This spec covers the logic from:

**candidate generation → source ingestion → normalized events → lane scoring → contra checks → fusion/conflict resolution → signal packet**

## 2.2 Out of scope

This spec does **not** define:
- research brief internals
- risk gate internals
- paper trade execution logic
- portfolio accounting
- daily summary generation
- learning-report generation
- live broker execution

Those belong in downstream specs.

## 2.3 Structural rule

THE FADE worker is the **scout**.

Its job is to output a valid, auditable **signal packet**.

It does not:
- execute trades
- place broker orders
- own the full product stack
- silently decide position size or capital allocation

---

# 3. Canonical Design Decisions

These decisions are mandatory in this spec.

## 3.1 v2 direction models are canonical

Where v2 direction models differ from earlier rubric assumptions, **v2 wins**.

This must be stated explicitly to avoid future contradictions.

That means the signal engine should treat the v2 Lane A rules as the current truth, not the older rubric where they conflict.

## 3.2 Initial thresholds and weights are policy defaults, not proven laws

Every threshold, weight, and penalty in this document is an **initial policy default** unless explicitly marked otherwise.

They are starting points.
They are not proven truths.
They may later be changed through operator-approved calibration.

## 3.3 Minimal Viable Data Stack is mandatory

The first implementation must use a constrained source stack.
Do not let API sprawl hijack the build.

## 3.4 Conflict is a valid output

Conflict is not an error case.
Conflict is a legitimate signal result.

## 3.5 First proof slice must stay narrow

The first proof slice is signal-packet only.
No downstream research, paper trading, or daily summary logic belongs in the first signal-engine proof.

---

# 4. Signal Engine Role in the Full Stack

## 4.1 Upstream
The signal engine receives:
- candidates from the Universe Scanner
- evidence from configured source lanes

## 4.2 Downstream
The signal engine outputs:
- signal packets
- conflict packets
- escalation events

## 4.3 Relationship to downstream modules
Downstream systems may consume signal packets for:
- operator triage
- research handoff
- paper-trade candidacy

But those downstream steps are not part of the signal engine itself.

---

# 5. Universe Scanner Specification

## 5.1 Purpose
The Universe Scanner creates the candidate asset list that THE FADE will inspect.

This exists because relying entirely on manual ticker selection is weak and bottlenecked.

## 5.2 Scanner responsibilities
The scanner must:
- generate candidate tickers/assets
- apply first-pass eligibility rules
- avoid obvious junk candidates
- output a bounded candidate set for the scout to evaluate

## 5.3 Scanner output contract

### `scanner_candidate_set`
Required fields:
- `scan_id`
- `created_at`
- `scan_reason`
- `market_session_context`
- `candidate_count`
- `candidates`

### candidate object
Required fields:
- `ticker`
- `asset_type`
- `scanner_reasons`
- `scanner_score`
- `freshness_context`
- `source_tags`
- `notes`

## 5.4 Candidate eligibility rules
Initial candidate selection may consider:
- structured/public-signal mention
- official/disclosure signal
- market-context anomaly
- prior watchlist carry-forward
- manually seeded operator priority

## 5.5 Candidate exclusion rules
Candidates should be excluded if:
- symbol is invalid or unresolvable
- asset mapping is ambiguous
- evidence is stale beyond configured limits
- no qualifying scanner reason exists
- data quality is too poor to continue

## 5.6 First proof slice scanner rule
For first proof, the scanner may be deliberately simple:
- one bounded candidate list
- a small number of candidates
- deterministic output
- no complex ranking required

---

# 6. Source Lane Framework

## 6.1 Lane model
Each source lane must be treated as its own evidence class.

Do not merge all sources into one undifferentiated soup.

Each lane has:
- a purpose
- a trust profile
- a freshness profile
- a scoring method
- a direction model
- escalation rules

## 6.2 Lane registry
The system must maintain a lane registry containing:
- `lane_id`
- `lane_name`
- `lane_type`
- `enabled_for_mvp`
- `trust_tier`
- `freshness_class`
- `direction_model_default`
- `scoring_method`
- `required_fields`
- `failure_policy`

## 6.3 Virtual / Shadow Lanes (Analytical Redundancy)

### Purpose
Virtual / Shadow Lanes provide analytical redundancy when a primary lane is unavailable, degraded, stale, or temporarily missing.

They are not equal replacements for primary evidence.
They are fallback inference lanes used to preserve signal continuity while reducing confidence appropriately.

### Examples
- if Official / Disclosure lane is unavailable, proxy evidence may be drawn from:
  - options flow
  - unusual volume
  - news acceleration
  - social sentiment shift
- if market-context freshness is delayed, shadow context may use:
  - delayed market regime proxy
  - correlated asset behavior
  - sector-relative behavior

### Core rule
Shadow evidence may preserve continuity, but it must:
- be labeled as inferred
- carry a lower trust tier
- apply a confidence penalty
- never silently masquerade as primary evidence
- never upgrade a signal beyond policy-allowed caps when primary evidence is absent

### Required fields for inferred evidence
Suggested additions to normalized or intermediate records:
- `is_shadow_lane`
- `primary_lane_missing`
- `proxy_basis`
- `inference_confidence`
- `confidence_penalty_applied`

### Escalation rule
If a critical primary lane is missing and only shadow evidence is available:
- the system may continue in reduced-confidence mode
- but it must either:
  - cap the signal class
  - or escalate for review depending on policy
---

# 7. Lane Definitions

## 7.1 Lane A — Public Figure / Persona Signals

### Purpose
Capture curated public-figure signals that may have predictive or contrarian value.

### Characteristics
- fast-moving
- narrative-heavy
- prone to noise
- useful only when scored and contextualized

### Examples
- Pelosi
- Cramer
- Arthur Hayes
- Crypto Capo
- Eric Trump

### v2 direction-model rule
The signal engine must use the **v2 direction-model assignments** as canonical.

### Required operational rule
If the v2 doc changes a direction model from the older rubric, that newer assignment must be treated as the active source of truth.

### Lane A sub-source registry
Each source must define:
- `source_name`
- `asset_scope`
- `direction_model`
- `score_cap`
- `freshness_limit_hours`
- `trust_modifier`
- `context_only` boolean
- `requires_market_confirmation` boolean

### Lane A requirements
- no unregistered source may score
- no source may score without explicit direction model
- undefined direction model must escalate
- stale source events must not score as fresh

---

## 7.2 Lane B — Official / Structured Signals

### Purpose
Capture cleaner, slower, more defensible signal evidence.

### Examples
- congressional disclosures
- SEC filings
- insider disclosures
- company announcements

### Characteristics
- higher trust
- slower
- structured
- often lagged
- useful for signal confirmation and context

### Rules
- timestamps must be explicit
- lag class must be explicit
- event freshness must be computed
- stale but still contextually useful events must be marked as such, not treated as fresh

---

## 7.3 Lane C — Market Context

### Purpose
Capture whether the market itself is supporting or contradicting the narrative.

### Examples
- price change
- volume spike
- gap behavior
- realized volatility
- trend state
- relative strength/weakness
- intraday expansion vs daily structure

### Characteristics
- fast
- highly relevant
- noisy if overfitted
- required for avoiding pure narrative signals

### Rules
- market-context calculations must be reproducible
- session context must be explicit
- stale market snapshots invalidate the lane for fast signals
- lane should help confirm or weaken other signals, not replace them

---

## 7.4 Lane D — News / Headline / Content Signals

### Purpose
Capture news-type evidence and broader content signals.

### Examples
- headlines
- transcript extracts
- article mentions
- structured earnings-coverage snippets

### Characteristics
- useful for context
- can be noisy
- often derivative of other lanes
- should rarely act as sole driver of a strong signal

### Rules
- relevance must be explicit
- source quality must be tracked
- duplicate-news amplification must be controlled
- derivative content must not be overcounted as independent evidence

---

## 7.5 Lane E — Internal Context

### Purpose
Bring in internal context and memory.

### Examples
- Research Swarm outputs
- prior signal packets
- prior research briefs
- prior winning/losing signal patterns
- operator notes

### Characteristics
- context-only in MVP
- useful for memory
- useful for replay
- not a substitute for live structured evidence

### Rules
- internal context may enrich
- internal context may not silently dominate fusion
- stale internal context must be marked clearly
- internal context must not be treated as fresh signal proof by default

---

# 8. Minimal Viable Data Stack

## 8.1 Required for MVP
The first signal-engine implementation must include only:

- **one official/disclosure lane**
- **one market-context lane**
- **one curated public-signal lane**
- **Research Swarm as context-only enrichment**

## 8.2 Explicitly deferred
These are deferred unless later justified:
- X/Twitter-heavy direct dependence
- scraping-heavy fragile signal sources
- premium data-vendor sprawl
- options/short-interest complexity
- broad multi-vendor redundancy

## 8.3 MVP data-stack design rule
If a proposed first implementation cannot run without many external paid data services, it fails MVP scope discipline.

---

# 9. Event Normalization Specification

## 9.1 Purpose
Convert all raw source evidence into one common structure.

This is non-negotiable.

## 9.2 Normalized event contract

### `normalized_signal_event`
Required fields:
- `event_id`
- `task_id`
- `ticker`
- `asset_type`
- `source_lane`
- `source_name`
- `direction_hint`
- `event_time`
- `ingested_at`
- `freshness_hours`
- `raw_text`
- `parsed_summary`
- `evidence_url`
- `evidence_path`
- `trust_tier`
- `lag_class`
- `parser_confidence`
- `notes`

### Allowed `direction_hint`
- `bullish`
- `bearish`
- `neutral`
- `uncertain`

### Allowed `asset_type`
- `equity`
- `crypto`
- `etf`
- `macro`
- `other`

## 9.3 Optional recommended fields
- `currency`
- `market_session`
- `region`
- `exchange`
- `sector`
- `source_event_id`
- `source_author`
- `derived_from`
- `is_duplicate_candidate`

## 9.4 Normalization rules
- all timestamps must be normalized
- missing fields must remain explicit
- parser uncertainty must be recorded
- duplicate candidates must be detectable
- every normalized event must retain a trace back to original evidence

## 9.5 Bad event behavior
If a raw source cannot be normalized:
- do not silently drop it without record
- either:
  - write a failed-normalization record
  - or escalate according to source failure policy

---

# 10. Direction Model Rules

## 10.1 Purpose
Direction models define how a source signal should be interpreted.

## 10.2 Allowed models
- `FOLLOW`
- `INVERSE`
- `CONTEXT_ONLY`
- `REGIME_CONDITIONAL`

## 10.3 Direction-model registry
Every scoring source must have:
- `source_name`
- `direction_model`
- `canonical_from_version`
- `last_reviewed_at`
- `operator_approval_required_for_change`

## 10.4 Canonical rule
If v2 changed a source’s direction model from the earlier rubric, v2 is the active truth.

## 10.5 Change-control rule
Direction-model changes must not be made casually.
Any future change requires:
- explicit review
- updated registry
- updated justification
- operator approval

## 10.6 Undefined direction rule
If a source has no defined direction model:
- it must not score
- it must escalate

---

# 11. Lane Scoring Specification

## 11.1 Purpose
Convert normalized events into lane-level scorecards.

## 11.2 Lane scorecard contract

### `lane_scorecard`
Required fields:
- `task_id`
- `ticker`
- `source_lane`
- `source_name`
- `score`
- `max_score`
- `direction_model`
- `conditions_hit`
- `conditions_missed`
- `bullish_subscore`
- `bearish_subscore`
- `freshness_ok`
- `evidence_count`
- `confidence_band`
- `notes`

## 11.3 Optional recommended fields
- `trust_modifier_applied`
- `lag_penalty_applied`
- `duplicate_penalty_applied`
- `requires_confirmation`
- `context_only`
- `score_reason_summary`

## 11.4 Scoring rules
- each lane scores independently
- score reasoning must be visible
- freshness must affect score eligibility
- duplicate/derivative evidence must not be double-counted
- context-only lanes may enrich but should not dominate fusion

## 11.5 Confidence bands
Allowed confidence bands:
- `low`
- `medium`
- `high`

Confidence band must be tied to:
- evidence completeness
- freshness
- source quality
- direction-model certainty
- internal scoring clarity

## 11.6 Initial scoring-policy rule
All weights, penalties, score caps, and thresholds are **initial policy defaults** unless later validated and promoted through review.

---

# 12. Contra-Signal Engine Specification

## 12.1 Purpose
Deliberately identify evidence against the primary signal narrative.

## 12.2 Why this exists
Without a contra engine, the system becomes a confirmation machine.

## 12.3 Contra engine responsibilities
- identify opposing evidence
- identify crowding or contradiction
- identify stale primary signals
- identify market action that weakens the thesis
- reduce false confidence
- force conflict when appropriate

## 12.4 Contra result contract

### `contra_signal_result`
Required fields:
- `task_id`
- `ticker`
- `contra_score`
- `contra_reasons`
- `penalty_applied`
- `force_conflict`
- `notes`

## 12.5 Contra rules
- contra checks must be explicit
- contra evidence must be traceable
- contra output must not be hidden inside fusion math
- strong contra cases may force conflict classification

---

# 13. Fusion and Conflict Specification

## 13.1 Purpose
Combine lane scorecards and contra results into the final signal judgment.

## 13.2 Fusion inputs
- scanner candidate context
- lane scorecards
- contra result
- optional market-session context
- optional regime context

## 13.3 Fusion outputs
- final signal class
- composite score
- conflict flag
- source breakdown
- evidence paths
- operator-facing summary

## 13.4 Allowed final signal classes
- `STRONG_BULLISH`
- `BULLISH`
- `WEAK_BULLISH`
- `NO_SIGNAL`
- `WEAK_BEARISH`
- `BEARISH`
- `STRONG_BEARISH`
- `CONFLICT`

## 13.5 Conflict rules
Conflict should trigger when:
- major lanes disagree materially
- contra engine forces conflict
- evidence freshness mismatch is severe
- direction models pull materially against each other
- required confirmation is absent in a way that invalidates certainty

## 13.6 Fusion-policy rule
Fusion thresholds, penalties, and lane weights are **initial defaults**.
They must be treated as configurable policy, not permanent truth.

## 13.7 Fusion reproducibility rule
Given the same inputs and same policy defaults, the fusion engine must produce the same output.

## 13.8 Regime-Aware Lane Weighting (Dempster-Shafer / Competence Model)

### Purpose
Static lane weighting is too rigid for changing market conditions.

The signal engine should support a regime-aware weighting layer that assigns **Competence Scores** to lanes based on the current environment.

### Core concept
Instead of using one fixed average across lanes, the fusion engine should:
1. classify the current regime
2. assign a competence score to each lane for that regime
3. tilt fusion weight toward the most competent lanes
4. still preserve explicit conflict logic

### Example regimes
- high volatility
- low volatility / flat
- trend expansion
- risk-on
- risk-off
- event-driven / headline-dominant
- low-liquidity

### Competence score concept
Each lane should have:
- `competence_score`
- `regime_label`
- `confidence_in_competence`
- `last_calibrated_at`

### Dempster-Shafer style use
The system may use a Dempster-Shafer-inspired evidence fusion layer where lanes contribute:
- support for bullish outcome
- support for bearish outcome
- support for uncertainty/conflict

This should not become mystical math theater.

It should be implemented as:
- explicit belief mass assignments
- explicit conflict mass
- explicit regime-adjusted competence weights
- clear fallback behavior when evidence is too contradictory

### Safety rule
Regime-aware weighting must not:
- erase conflict
- allow weak shadow lanes to dominate strong primary lanes
- silently mutate lane competence without versioned calibration

### Canonical rule
Competence-weighted fusion is allowed as a policy layer, but all competence values remain **initial defaults** until validated through outcome history.

---

# 14. Signal Packet Contract

## 14.1 Purpose
Define the scout’s final output.

## 14.2 Core packet contract

### `signal_packet`
Required fields:
- `signal_packet_id`
- `task_id`
- `ticker`
- `asset_type`
- `composite_score`
- `signal`
- `source_breakdown`
- `conflict_flag`
- `evidence_paths`
- `operator_notes`
- `completed_at`

## 14.3 Recommended additional fields
- `selected_for_research`
- `selected_for_paper_trade`
- `resolution_status`
- `resolution_notes`
- `market_context_snapshot`
- `contra_summary`
- `scanner_summary`
- `policy_version`
- `direction_model_version`

## 14.4 Signal packet rules
- every signal packet must be auditable
- evidence paths must resolve
- source breakdown must be preserved
- conflict state must be explicit
- packet must support operator review without requiring hidden internal logic

---

# 15. Escalation and Failure Matrix

## 15.1 Purpose
Prevent silent corruption and make failures explicit.

## 15.2 Escalation classes
- `SOURCE_UNAVAILABLE`
- `SOURCE_STALE`
- `MALFORMED_EVENT`
- `NORMALIZATION_FAILURE`
- `UNDEFINED_DIRECTION_MODEL`
- `MISSING_REQUIRED_LANE`
- `FUSION_CONFLICT`
- `INVALID_PACKET_OUTPUT`
- `UNKNOWN_SYSTEM_ERROR`

## 15.3 Failure matrix

| Failure Type | Required Behavior | Can Continue? |
|---|---|---|
| Source unavailable | record lane failure and continue only if lane is non-critical | maybe |
| Source stale | mark stale, downgrade/penalize, possibly continue | maybe |
| Malformed event | write failed event record and escalate | maybe |
| Undefined direction model | escalate immediately | no |
| Missing required lane | escalate or force weak/conflict depending on policy | maybe |
| Invalid normalized event | reject event and log failure | maybe |
| Fusion contradiction beyond threshold | emit conflict packet | yes |
| Invalid signal packet output | stop packet write and escalate | no |

## 15.4 Critical-stop rule
The engine must stop and escalate when:
- direction model is undefined
- output packet is invalid
- evidence paths are broken in a way that invalidates auditability
- required policy registry is missing or unreadable

---

# 16. Policy Registries

The signal engine should rely on explicit registries.

## 16.1 Required registries
- lane registry
- direction-model registry
- threshold/weight policy registry
- escalation-policy registry
- scanner-policy registry

## 16.2 Registry design rules
- versioned
- readable
- operator-reviewable
- auditable
- no silent mutation

---

# 17. First Bounded Proof Slice — Detailed Definition

## 17.1 Included in first proof
- Universe Scanner
- one official/disclosure lane
- one market-context lane
- one curated public-signal lane
- Research Swarm as context-only enrichment
- event normalization
- lane scoring
- contra-signal checks
- fusion/conflict logic
- signal packet writing
- operator review only

## 17.2 Excluded from first proof
- research brief integration
- risk gate integration
- paper trading
- daily summary
- learning reports
- live execution

## 17.3 Proof goals
The first proof slice must demonstrate:
- at least one candidate can become a valid signal packet
- at least one conflict case can be emitted cleanly
- no fabricated data is used
- source-lane scoring is explainable
- signal packet is operator-reviewable

## 17.4 Proof failure conditions
The first proof slice fails if:
- signal packets are not reproducible
- source-lane scoring is opaque
- undefined direction models appear
- stale/missing data is silently treated as valid
- conflict logic is weak or hidden

---

# 18. Output Review Requirements

The signal engine must make it possible for the operator to review:
- why the signal exists
- which lanes matter most
- which lanes are conflicting
- what evidence was used
- whether the packet is strong, weak, or conflicted
- whether further research is worth it

If the output cannot support that review, the engine is not ready.

---

# 19. Explicitly Deferred in This Spec

The following are intentionally deferred outside the signal-engine scope:
- brief-writing logic
- risk gate logic
- paper trade engine
- position accounting
- daily summary engine
- learning/calibration reports
- broker execution

This spec only defines what the scout layer must do correctly.

---

# 20. Success Criteria for This Spec

This spec is satisfied only when the signal engine can do all of the following:

- produce scanner candidates
- ingest MVP lane evidence
- normalize events cleanly
- score lanes independently
- apply v2 direction models cleanly
- apply contra checks cleanly
- fuse lanes into explainable output
- emit valid signal packets
- emit valid conflict outputs
- escalate failures honestly
- remain bounded and auditable

## 20.1 Dual-Engine Heartbeat Monitoring

The scout layer must support dual-engine operational resilience.

### Required model
- `Alpha` = primary engine
- `Beta` = secondary engine

### Required heartbeat behavior
The monitor must track:
- packet production heartbeat
- engine health heartbeat
- adapter heartbeat
- schema-validation heartbeat

### Failover rule
If the primary engine stops producing valid packets within policy-defined tolerance:
- the monitor must mark Alpha degraded
- auto-promote Beta
- record the failover event
- preserve audit trace
- surface the failover in system health state

### Required success condition
The scout is not considered operationally resilient until:
- Alpha/Beta heartbeat monitoring exists
- failover is proven in test
- packet continuity is preserved under primary-engine failure

---

# 21. Final Summary

This signal-engine spec defines the real scout layer of THE FADE.

Its job is narrow and important:
- generate candidates
- ingest signals
- normalize evidence
- score lanes
- apply contra logic
- resolve agreement vs conflict
- output a structured signal packet

It must do that well before any downstream layer earns attention.

The most important controls in this spec are:
- v2 direction models are canonical
- the MVP data stack stays constrained
- thresholds and weights are defaults, not truths
- conflict is a valid output
- the first proof slice stays narrow
- failures escalate instead of being hidden

If this layer is weak, the rest of the product stack becomes trash.

---
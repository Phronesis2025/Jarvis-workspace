# JARVIS_THE_FADE_BUILD_CHECKLIST.md

**Document Type:** Master Build Checklist  
**Status:** Proposed Canonical Checklist  
**Version:** 1.0  
**Last Updated:** 2026-03-23  
**Owner:** Jason  
**Project Context:** Jarvis future worker / stock intelligence side quest

---

# 1. Purpose of This Document

This document is the **master build checklist** for the THE FADE system.

It exists to define:
- the correct build order
- what belongs in each phase
- what must be proven before moving forward
- what is deferred
- what is out of scope
- how to avoid building the wrong things in the wrong order

This is not the narrative overview document.  
This is not the detailed implementation spec.  
This is the **control checklist**.

---

# 2. Governing Build Rules

## 2.1 Build discipline rules

The following rules govern this checklist:

1. **Do not build the full product at once.**
2. **Do not skip the signal packet proof slice.**
3. **Do not jump to paper trading before the scout layer is trustworthy.**
4. **Do not jump to live trading before extended paper-trade proof.**
5. **Do not treat initial weights/thresholds as proven truths.**
6. **Do not add source-lane sprawl in MVP.**
7. **Do not let dashboard work outrun actual system behavior.**
8. **Do not hide a weak core with fancy review UI.**
9. **Do not let future worker work outrun Jarvis phase discipline.**

## 2.2 Jarvis gating rule

This roadmap is recognized design direction, not immediate unlimited execution scope.

The broader Jarvis rules still apply:
- the core WCS/Phase-1 loop remains the primary trust-building path
- future workers should not outrun core loop stability
- this module should not be activated in a way that bypasses those constraints

This checklist describes **how to build correctly when the work is in scope**, not permission to ignore Jarvis gating.

---

# 3. Canonical Scope Split

The system is split into these major build areas:

1. **Scout foundation**
2. **Scout proof slice**
3. **Signal review surface**
4. **Research handoff**
5. **Paper trading**
6. **Daily summaries**
7. **Learning/calibration**
8. **Hardening**
9. **Live-readiness review**
10. **Tiny live pilot**

The most important control idea is this:

> **Later phases do not matter if the signal packet layer is weak.**

---

# 4. Minimal Viable Data Stack Rule

## 4.1 Required for MVP

The first real build should require only:

- one official/disclosure lane
- one market-data lane
- one curated public-signal lane
- Research Swarm as context only

## 4.2 Explicitly deferred for MVP

Do not require these for first proof:
- heavy X/Twitter dependence
- scraping-fragile lanes
- oversized paid-vendor stacks
- options/short-interest complexity unless proven necessary
- broad multi-vendor redundancy

## 4.3 Checklist implication

If a phase or task implicitly depends on too many third-party sources too early, that task fails scope discipline and must be deferred or split.

---

# 5. First Bounded Proof Slice

This is the first proof slice of THE FADE itself.

## 5.1 Included
- Universe Scanner
- Minimal Viable Data Stack
- Event normalization
- Lane scoring
- Contra-signal checks
- Signal fusion / conflict resolution
- Signal packet writing
- Operator review only

## 5.2 Explicitly excluded
- research brief integration
- risk gate integration
- paper trading
- daily summary engine
- learning layer
- live execution

## 5.3 Why this slice is first

Because if the signal packet logic is bad:
- the research layer is wasted
- the paper-trade layer lies
- the daily summary becomes noise
- the learning layer learns garbage

---

# 6. Checklist Status Legend

Use these status labels in execution tracking:

- **NOT_STARTED**
- **IN_PROGRESS**
- **PROOF_PENDING**
- **PROVEN**
- **BLOCKED**
- **DEFERRED**
- **SUPERSEDED**

---

# 7. Master Build Phases

# Phase 0 — Canon Reset and Design Lock

## Goal
Lock the canonical direction before implementation starts.

## Why this phase exists
The old stock-module framing was too generic.  
This reset phase prevents building against a stale identity.

## Tasks
- [ ] Approve THE FADE as the scout-layer name
- [ ] Approve full-stack split:
  - [ ] scout
  - [ ] research
  - [ ] paper trading
  - [ ] daily summary
  - [ ] learning
- [ ] Approve that the worker contract and full product architecture are separate concerns
- [ ] Approve v2 direction models as canonical
- [ ] Approve Minimal Viable Data Stack
- [ ] Approve first bounded proof slice
- [ ] Approve paper-trade simulation realism requirement
- [ ] Approve that live execution remains future-only

## Exit Criteria
- [ ] Canonical naming approved
- [ ] Module boundaries approved
- [ ] Source-lane scope approved
- [ ] First proof slice approved
- [ ] Build can proceed without identity confusion

## Phase Status
**Target state:** PROVEN before implementation work begins

---

# Phase 1 — Scout Contracts and Data Foundations

## Goal
Define the core contracts and baseline structures needed for the scout layer.

## Tasks
- [ ] Define Universe Scanner purpose and output contract
- [ ] Define normalized event schema
- [ ] Define lane scorecard schema
- [ ] Define signal packet schema
- [ ] Define conflict packet/escalation shape
- [ ] Define task packet contract
- [ ] Define source-lane identity list
- [ ] Define direction-model registry for lane rules
- [ ] Define initial weight/default policy registry
- [ ] Mark weights and thresholds as **initial defaults**, not proven truths
- [ ] Define escalation matrix
- [ ] Define failure reasons and error states
- [ ] Define minimal state/storage assumptions for scout outputs

## Exit Criteria
- [ ] All required scout contracts exist
- [ ] Direction models are explicit and non-contradictory
- [ ] Initial defaults are clearly marked as provisional
- [ ] Failure states are defined
- [ ] No worker logic depends on undefined packet structures

## Phase Status
**Target state:** PROVEN before first runner implementation

---

# Phase 2 — Source Lane Adapters (MVP Only)

## Goal
Implement only the minimum source adapters needed for first proof.

## Tasks
### Universe / candidate generation
- [ ] Define first-pass candidate selection rules
- [ ] Define scanner output shape
- [ ] Define candidate freshness rules

### Public-signal lane
- [ ] Implement one curated public-signal lane for MVP
- [ ] Validate event capture and parsing
- [ ] Validate direction-model application

### Official/disclosure lane
- [ ] Implement one official/disclosure lane
- [ ] Validate disclosure ingestion
- [ ] Validate event extraction into normalized structure

### Market-data lane
- [ ] Implement one market-data lane
- [ ] Validate price/volume context ingestion
- [ ] Validate market-context normalization

### Internal context lane
- [ ] Define Research Swarm context lookup for MVP
- [ ] Validate context-only enrichment
- [ ] Confirm it does not silently override live source truth

## Explicitly deferred in this phase
- [ ] additional premium lanes
- [ ] broad scraping lanes
- [ ] fragile social scraping dependencies
- [ ] options/short-interest complexity
- [ ] bulk redundant data-vendor support

## Exit Criteria
- [ ] At least one candidate can pass through scanner and all MVP lanes
- [ ] All MVP lanes produce normalized events
- [ ] No lane silently fabricates missing values
- [ ] Source reliability is good enough to continue

## Phase Status
**Target state:** PROVEN before scoring engine proof

---

# Phase 3 — Normalization and Lane Scoring

## Goal
Turn raw lane evidence into structured, scored lane outputs.

## Tasks
- [ ] Implement normalized event writer
- [ ] Validate normalized event schema
- [ ] Implement lane scorecard generation
- [ ] Implement lane freshness checks
- [ ] Implement trust-tier handling
- [ ] Implement lag-class handling
- [ ] Implement lane-specific score logging
- [ ] Implement condition-hit / condition-missed recording
- [ ] Implement missing-data behavior
- [ ] Implement malformed-event escalation

## Critical quality checks
- [ ] Same source event always maps to the same normalized shape
- [ ] Same normalized shape scores consistently
- [ ] Lane scoring remains explainable
- [ ] No early global-score flattening

## Exit Criteria
- [ ] Raw events normalize correctly
- [ ] Lane scorecards validate
- [ ] Missing/stale/malformed inputs escalate correctly
- [ ] Lane-level audit trail exists

## Phase Status
**Target state:** PROVEN before fusion logic proof

---

# Phase 4 — Contra-Signal and Fusion Engine

## Goal
Fuse lane scorecards into a valid signal packet with conflict handling.

## Tasks
- [ ] Implement contra-signal checks
- [ ] Implement fusion logic
- [ ] Implement conflict rules
- [ ] Implement final signal classification
- [ ] Implement signal packet output writer
- [ ] Implement operator-note placeholder handling
- [ ] Implement evidence-path linking
- [ ] Implement conflict escalation path
- [ ] Validate bearish as well as bullish outputs
- [ ] Validate no-signal and weak outputs
- [ ] Validate conflict beats fake certainty

## Quality requirements
- [ ] Fusion math is explicit
- [ ] Contra effects are visible
- [ ] Conflict thresholds are explicit
- [ ] Signal classes are reproducible
- [ ] Defaults are still clearly labeled as provisional policy

## Exit Criteria
- [ ] One ticker can move from lane scorecards to a valid signal packet
- [ ] Conflict packets are produced correctly
- [ ] Weak/no-signal cases work
- [ ] Strong signal case works
- [ ] Operator review can happen from the signal packet alone

## Phase Status
**Target state:** PROVEN = first bounded proof slice complete

---

# Phase 5 — Signal Review Surface

## Goal
Make signal packets reviewable in a clean operator-facing surface.

## Tasks
- [ ] Define signal review dashboard sections
- [ ] Show signal classification clearly
- [ ] Show source breakdown
- [ ] Show conflict state
- [ ] Show evidence links
- [ ] Show freshness
- [ ] Show operator notes
- [ ] Show triage status
- [ ] Support no-signal / weak / conflict / bullish / bearish states cleanly
- [ ] Keep the page plain-English and operator-friendly

## Guardrails
- [ ] Do not add fake analytics
- [ ] Do not build paper-trade widgets yet
- [ ] Do not build research widgets yet unless phase 6 is in scope
- [ ] Do not let UI redesign outrun real scout behavior

## Exit Criteria
- [ ] Operator can review packets cleanly
- [ ] Conflict is obvious
- [ ] Evidence is accessible
- [ ] Dashboard matches actual packet fields

## Phase Status
**Target state:** PROVEN before research handoff work

---

# Phase 6 — Research Handoff

## Goal
Connect strong signal packets to the downstream research layer.

## Tasks
- [ ] Define signal → research handoff contract
- [ ] Define when research is allowed
- [ ] Define when research is blocked
- [ ] Connect signal packet to brief generation
- [ ] Connect brief to risk gate
- [ ] Link research outputs back to originating signal packet
- [ ] Reflect research linkage in dashboard review

## Rules
- [ ] Not every signal goes to research
- [ ] Weak/no-signal/conflict packets must not silently become research runs
- [ ] Research remains downstream, not primary entry logic

## Exit Criteria
- [ ] One strong signal can produce linked brief + risk gate artifacts
- [ ] Signal → brief → risk review traceability exists
- [ ] Dashboard reflects linkage cleanly

## Phase Status
**Target state:** PROVEN before paper-trade engine work

---

# Phase 7 — Paper Trade Engine

## Goal
Simulate approved trade candidates without touching real money.

## Tasks
### Trade-candidate contract
- [ ] Define trade candidate packet
- [ ] Define entry rule fields
- [ ] Define stop/invalidation fields
- [ ] Define target/time-stop fields
- [ ] Define operator approval field

### Execution simulation
- [ ] Implement paper trade open logic
- [ ] Implement paper trade close logic
- [ ] Implement open-position tracking
- [ ] Implement closed-trade tracking
- [ ] Implement trade linkage back to signal packet
- [ ] Implement trade linkage to brief/risk artifacts

### Required realism rules
- [ ] Define entry fill assumptions
- [ ] Define exit fill assumptions
- [ ] Define slippage assumptions
- [ ] Define spread assumptions
- [ ] Define fee assumptions
- [ ] Define overnight gap handling
- [ ] Define partial-fill handling
- [ ] Define stale quote handling

### Guardrails
- [ ] Max trades per day
- [ ] Max exposure per ticker
- [ ] Max exposure per sector
- [ ] Max daily paper loss
- [ ] Duplicate-trade block
- [ ] Cooldown after consecutive losses

## Exit Criteria
- [ ] First paper trade lifecycle is proven
- [ ] P&L records correctly
- [ ] Fill assumptions are explicit
- [ ] Every paper trade links back to its originating signal

## Phase Status
**Target state:** PROVEN before daily summary automation

---

# Phase 8 — Daily Summary Engine

## Goal
Produce the exact daily summary the operator wants.

## Tasks
### Daily balance
- [ ] Calculate starting balance
- [ ] Calculate ending balance
- [ ] Calculate realized P&L
- [ ] Calculate unrealized P&L
- [ ] Calculate daily P&L
- [ ] Calculate cumulative P&L

### Trade summary
- [ ] Count trades opened today
- [ ] Count trades closed today
- [ ] Summarize winners/losers
- [ ] Identify biggest gain/loss
- [ ] Summarize open positions
- [ ] Summarize average hold time

### Signal summary
- [ ] Count signals generated
- [ ] Count ignored/watch/research/paper-trade candidates
- [ ] Count conflict packets
- [ ] Summarize source-lane contribution

### Outputs
- [ ] Generate markdown daily summary
- [ ] Generate JSON daily summary
- [ ] Add dashboard daily summary surface
- [ ] Add operator plain-English summary block

## Exit Criteria
- [ ] End-of-day summary generates automatically
- [ ] Ending balance is visible
- [ ] Daily positive/negative result is obvious
- [ ] Daily trade list is visible
- [ ] Source-lane summary is visible

## Phase Status
**Target state:** PROVEN before learning layer work

---

# Phase 9 — Learning / Calibration Layer

## Goal
Learn from paper-trade and signal outcomes without self-mutating out of control.

## Tasks
- [ ] Define learning report schema
- [ ] Compute lane hit rates
- [ ] Compute false-positive rates
- [ ] Compute conflict usefulness
- [ ] Detect noisy lanes
- [ ] Detect regime-dependent behavior
- [ ] Add half-life logic for aging signal usefulness
- [ ] Add look-ahead bias protections
- [ ] Suggest weight adjustments
- [ ] Suggest threshold adjustments
- [ ] Suggest rule adjustments
- [ ] Add operator approval workflow for all recommended changes

## Guardrails
- [ ] No silent weight changes
- [ ] No silent threshold changes
- [ ] No silent rule mutation
- [ ] No direct self-authorized trade changes

## Exit Criteria
- [ ] System produces learning reports
- [ ] Reports identify useful vs noisy lanes
- [ ] Suggested changes require operator approval
- [ ] Replay and outcome analysis are stable enough to trust

## Phase Status
**Target state:** PROVEN before live-readiness review

---

# Phase 10 — Hardening and Replay

## Goal
Make the system stable enough for extended paper-mode operation.

## Tasks
- [ ] Build replay test set
- [ ] Build regression checks
- [ ] Add stale-data checks
- [ ] Add malformed-data alarms
- [ ] Add source-outage handling
- [ ] Add health-check reporting
- [ ] Add contract validation checks
- [ ] Add signal packet audit logs
- [ ] Add paper-trade audit logs
- [ ] Add daily summary validation checks
- [ ] Add failure matrix handling

## Exit Criteria
- [ ] Replay cases are stable
- [ ] Errors escalate cleanly
- [ ] Data corruption is visible
- [ ] Extended paper operation is trustworthy

## Phase Status
**Target state:** PROVEN before live-readiness review

---

# Phase 11 — Autonomous Transition

## Goal
Transition the system from fully human-gated paper operation into bounded policy-driven autonomy.

## Purpose
This phase exists to prove that the system can:
- route decisions automatically
- maintain scout continuity under failure
- accelerate learning with synthetic support
- remain bounded by safety controls

## Tasks
- [ ] Deploy MAB Policy Agent for auto-routing
- [ ] Define route-selection policy thresholds
- [ ] Validate auto-routing against historical paper-trade performance
- [ ] Activate Virtual Lane redundancy for the Scout
- [ ] Validate inferred/shadow evidence continuity behavior
- [ ] Cap shadow-lane confidence correctly when primaries are absent
- [ ] Enable LLM-based synthetic feedback for faster learning
- [ ] Keep synthetic feedback explicitly labeled and sandboxed
- [ ] Validate Autonomous Policy Calibration inside the Safety Sandbox
- [ ] Final verification of Heartbeat Monitor failover
- [ ] Validate Alpha/Beta scout failover under failure conditions
- [ ] Confirm Safety Governor can override autonomous routing
- [ ] Confirm manual fallback remains available when safety gates fire

## Exit Criteria
- [ ] MAB routing works under bounded policy
- [ ] virtual/shadow lanes preserve continuity without faking certainty
- [ ] synthetic feedback is useful but not over-authoritative
- [ ] autonomous calibration is sandboxed and logged
- [ ] heartbeat failover is proven
- [ ] Safety Governor can block or downgrade autonomy

## Phase Status
**Target state:** PROVEN before live-readiness review

---

# Phase 12 — Live-Readiness Review

## Goal
Decide whether the system deserves tiny live trading permission.

## Tasks
- [ ] Define live-trade policy
- [ ] Define max live position size
- [ ] Define max live daily loss
- [ ] Define manual approval workflow
- [ ] Define kill switch behavior
- [ ] Define broker adapter contract
- [ ] Review paper-trade duration requirement
- [ ] Review minimum trade-count requirement
- [ ] Review paper performance thresholds
- [ ] Review risk metrics
- [ ] Review operator trust criteria

## Hard Rule
No live activation unless all required gates are explicitly passed.

## Exit Criteria
- [ ] Long paper history exists
- [ ] Performance gates are met
- [ ] Controls are proven
- [ ] Manual override is proven
- [ ] Operator explicitly authorizes live pilot

## Phase Status
**Target state:** PROVEN before any live pilot

---

# Phase 13 — Tiny Live Pilot

## Goal
Run the smallest possible real-money proof under hard constraints.

## Tasks
- [ ] Connect one broker adapter
- [ ] Keep position size tiny
- [ ] Require manual confirmation
- [ ] Log every order
- [ ] Log every fill
- [ ] Compare live vs paper assumptions
- [ ] Review pilot outcomes
- [ ] Decide whether to continue, revise, or stop

## Guardrails
- [ ] Kill switch tested
- [ ] No automatic scaling
- [ ] No strategy mutation during pilot
- [ ] No live pilot without current human review

## Exit Criteria
- [ ] Live pilot behaves as expected
- [ ] Logs are trustworthy
- [ ] Operator can stop system immediately
- [ ] No scale-up until long review is complete

## Phase Status
**Target state:** FUTURE ONLY

---

# 8. Phase-by-Phase Dependency Map

## Dependency chain
- Phase 0 must complete before Phase 1
- Phase 1 must complete before Phase 2
- Phase 2 must complete before Phase 3
- Phase 3 must complete before Phase 4
- Phase 4 must complete before Phase 5
- Phase 5 must complete before Phase 6
- Phase 6 must complete before Phase 7
- Phase 7 must complete before Phase 8
- Phase 8 must complete before Phase 9
- Phase 9 must complete before Phase 10
- Phase 10 must complete before Phase 11
- Phase 11 must complete before Phase 12
- Phase 12 must complete before Phase 13

## Hard dependency rule
If a lower layer is weak, later layers must not be used to hide that weakness.

Examples:
- bad signal packets cannot be rescued by better dashboards
- bad paper-trade assumptions cannot be rescued by daily summaries
- bad learning reports cannot be rescued by more complexity

---

# 9. Current Expected Implementation Priority

If implementation began in the correct order, the priority would be:

1. Phase 0 — Canon Reset
2. Phase 1 — Contracts/Foundation
3. Phase 2 — MVP Source Adapters
4. Phase 3 — Normalization and Lane Scoring
5. Phase 4 — Fusion / Conflict / Signal Packet
6. Phase 5 — Signal Review Surface
7. Phase 6 — Research Handoff
8. Phase 7 — Paper Trading
9. Phase 8 — Daily Summary
10. Phase 9 — Learning
11. Phase 10 — Hardening
12. Phase 11 — Live-Readiness Review
13. Phase 12 — Tiny Live Pilot

---

# 10. What Is Explicitly Deferred

The following items are intentionally deferred until later phases:

- live trading
- broker execution
- broad source-vendor sprawl
- complex multi-asset automation
- oversized strategy-optimization logic
- hidden autonomous calibration
- UI complexity not justified by real artifacts
- dashboard work that outruns actual packet/trade state

---

# 11. Checklist of Canonical “Must Be True” Conditions

These conditions must remain true across the whole build:

- [ ] THE FADE worker remains the scout layer
- [ ] The full stack is larger than the worker
- [ ] v2 direction models are treated as canonical
- [ ] Minimal Viable Data Stack stays constrained
- [ ] first proof slice stays narrow
- [ ] initial thresholds/weights remain labeled as defaults
- [ ] conflict is treated as a valid output
- [ ] paper trading comes before live trading
- [ ] learning remains approval-gated
- [ ] daily summary remains a required operator surface
- [ ] implementation remains gated by Jarvis phase discipline

---

# 12. Final Summary

This checklist is the control layer for building THE FADE correctly.

It exists to prevent:
- identity drift
- source sprawl
- premature execution
- fake confidence
- dashboard theater
- learning chaos
- live-trading delusion

The correct path is:

1. prove the scout
2. make the signal packet reviewable
3. connect deeper research
4. paper trade selected candidates
5. summarize every day
6. learn carefully
7. harden
8. only much later decide whether tiny live trading is justified

That is the disciplined path from start to finish.

---


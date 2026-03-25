# JARVIS_THE_FADE_REVISION_NOTES_v2_TO_CANON.md

**Document Type:** Revision Notes / Canon Transition Memo  
**Status:** Proposed Canonical Change Memo  
**Version:** 1.0  
**Last Updated:** 2026-03-23  
**Owner:** Jason  
**Project Context:** Jarvis future worker / stock intelligence side quest

---

# 1. Purpose of This Document

This document explains how the revised THE FADE design moved from:
- the earlier rubric and PRD drafts
to
- the current canonical document set

It exists to prevent future confusion when older documents say one thing and the new canonical documents say another.

This is not:
- the system overview
- the build checklist
- the signal-engine spec
- the architecture/storage spec
- the trading/review spec
- the dashboard spec

This is the **change memo** that explains what changed, what stayed, what was deferred, and what now counts as the source of truth.

---

# 2. Canonical Document Set

The current canonical document set is:

1. `JARVIS_THE_FADE_SYSTEM_OVERVIEW.md`
2. `JARVIS_THE_FADE_BUILD_CHECKLIST.md`
3. `JARVIS_THE_FADE_SIGNAL_ENGINE_SPEC.md`
4. `JARVIS_THE_FADE_ARCHITECTURE_AND_STORAGE_SPEC.md`
5. `JARVIS_THE_FADE_TRADING_AND_REVIEW_SPEC.md`
6. `JARVIS_THE_FADE_DASHBOARD_SPEC.md`

This revision-notes document exists only to explain how and why those files now supersede earlier blended documents.

---

# 3. Core Reason for the Rewrite

The earlier documents had a real problem:

They were trying to do **too many jobs at once**.

They mixed:
- worker contract
- full product architecture
- roadmap
- dashboard concept
- paper-trading design
- live-readiness logic

into one large document.

That was inefficient and dangerous because it created confusion about:
- what THE FADE worker actually is
- what the full product stack is
- what belongs in the first proof slice
- what is immediate build scope versus future direction

The canonical rewrite fixes that by splitting the system into multiple documents with clean boundaries.

---

# 4. What Stayed the Same

The rewrite did **not** throw away the core good ideas.

These ideas remain intact:

## 4.1 THE FADE remains a signal-first system
The product is still built around:
- signal intake
- signal scoring
- conflict handling
- operator review

## 4.2 Human gating remains mandatory
The operator still remains the decision-maker.

The system is still:
- advisory
- review-driven
- non-self-executing
- non-autonomous in live mode

## 4.3 Multi-source input remains central
The system still uses multiple source lanes rather than trusting one source type.

## 4.4 Downstream research still exists
The research brief and risk gate still survive.
They are still useful.
They are just no longer treated as the entire stock product.

## 4.5 Paper trading still exists as a required future stage
Paper trading remains the first execution-like stage and still comes before any live-trading consideration.

## 4.6 Learning remains controlled
The system still learns through:
- source evaluation
- threshold review
- calibration suggestions

But not through uncontrolled self-mutation.

---

# 5. What Changed

This section explains the most important canonical changes.

## Autonomous Confidence Metrics

The Daily Summary Page should include a small but explicit **Autonomous Confidence Metrics** section.

### Purpose
This section shows how much of the day’s system behavior was handled automatically versus routed to manual review through safety controls.

### Required fields
- `system_autonomy_level`
- `policy_routed_decisions`
- `manual_review_decisions`
- `safety_gate_interventions`
- `autonomous_paper_trades_opened`
- `autonomous_paper_trades_blocked`
- `confidence_threshold_used`
- `safety_override_count`

### Display rule
`System Autonomy Level` should be shown as a simple percentage or bounded score from 0–100%.

Interpretation:
- **0%** = fully manual workflow
- **100%** = fully policy-routed workflow within allowed autonomy bounds

### Plain-English helper text
- `System Autonomy Level` → “How much of the day’s decision flow was handled by the policy engine instead of manual review.”
- `Safety Gate Interventions` → “How many decisions were stopped or redirected by the system’s hard safety rules.”

### Important rule
This metric must not imply “trust” on its own.

A higher autonomy level does not automatically mean the system is better.  
It only means more decisions were routed automatically rather than manually.

---

# 5.2 The old “generic stock research module” framing is no longer primary

## Old framing
The previous stock side quest functioned like:
- confirm one symbol
- generate brief
- run risk gate
- review downstream artifacts

## New framing
That work is now treated as **downstream analyst support**, not the main scout system.

The new front door is:
- Universe Scanner
- THE FADE scout
- signal packet review

This is one of the most important canonical shifts.

---

# 5.3 The Universe Scanner is now a first-class part of the architecture

## Old problem
Manual ticker choice was too much of a front-end bottleneck.

## New canonical rule
The system should have a Universe Scanner that:
- generates candidate tickers/assets
- creates a bounded working set
- feeds the scout layer

This moves the system closer to a real signal engine and away from manual symbol feeding.

---

# 5.4 The Contra-Signal Engine is now a required layer

## Old problem
Without a contra layer, the system risks becoming a confirmation machine.

## New canonical rule
The system must deliberately check for:
- contradictory evidence
- weakening factors
- crowding
- lack of confirmation
- reasons the idea is wrong

The contra layer is no longer optional concept fluff.
It is part of the canonical signal-engine design.

---

# 5.5 Conflict is explicitly treated as a valid result

## Old problem
Earlier versions could easily drift toward flattening everything into one final score.

## New canonical rule
`CONFLICT` is a legitimate final output state.

The system must not force contradictory lanes into fake clean certainty.

This is now a formal rule in the signal-engine design.

---

# 5.6 Bearish classifications are now explicit

## Old problem
Earlier concepts leaned too heavily toward bullish-only logic.

## New canonical rule
The system supports both bullish and bearish classifications, including:
- weak bullish
- strong bullish
- weak bearish
- strong bearish
- conflict
- no signal

The signal engine is no longer implicitly one-directional.

---

# 5.7 v2 direction models are canonical

## Old problem
There were direction-model contradictions between earlier rubric logic and the revised v2 design.

## New canonical rule
**v2 direction models win.**

Where v2 direction-model assignments differ from older material, the new canonical documents treat v2 as the active truth.

This avoids future confusion about which direction model should actually be used.

---

# 5.8 Initial thresholds and weights are now explicitly provisional

## Old problem
Earlier threshold values, lane weights, and classification rules were too easy to read as permanent truth.

## New canonical rule
All thresholds, weights, and fusion policies are now explicitly labeled as:
- **initial policy defaults**
- not proven truths
- subject to later operator-approved calibration

This is a major improvement because it stops the system design from pretending guessed defaults are sacred law.

---

# 5.9 Autonomous transition is now formally recognized

## Old problem
Earlier versions were strongly human-gated but did not cleanly describe how the system would evolve into bounded autonomy later.

## New canonical rule
The canonical document set now recognizes a **Final Stage** where the broader product stack may operate as a **Policy-Driven Autonomous Agent**.

This includes:
- policy-based signal routing
- bounded autonomous paper-trade decisions
- sandboxed autonomous policy calibration
- safety-governed escalation and shutdown behavior

## Important boundary
This does **not** mean immediate autonomy.

The system still requires:
- long paper-trade proof
- strong safety controls
- explicit autonomy metrics
- Heartbeat Monitor failover
- Safety Governor policy
- live-readiness approval before any live execution is considered

## Why this matters
This change makes the autonomy path explicit instead of vague, while still preserving:
- phase discipline
- safety-first control
- operator override authority

---

# 5.10 The MVP data stack is now constrained on purpose

## Old problem
Earlier thinking risked too many source dependencies too early.

## New canonical rule
The system now explicitly defines a **Minimal Viable Data Stack**:
- one official/disclosure lane
- one market-data lane
- one curated public-signal lane
- Research Swarm as context only

Everything else is deferred unless justified.

This is one of the biggest practical improvements in the canonical rewrite.

---

# 5.11 The first bounded proof slice is now explicitly narrow

## Old problem
Earlier documents made it too easy to think the whole stack should be built at once.

## New canonical rule
The first proof slice is **signal-packet only**.

Included:
- Universe Scanner
- minimal source lanes
- normalization
- scoring
- contra logic
- fusion/conflict
- signal packet writing
- operator review

Explicitly excluded:
- research
- risk gate
- paper trading
- daily summary
- learning
- live trading

That is now a hard build-discipline rule.

---

# 5.12 Paper trading is now defined with explicit realism requirements

## Old problem
Earlier documents discussed paper trading but did not define simulation assumptions tightly enough.

## New canonical rule
Paper-trade simulation now requires explicit rules for:
- entry fills
- exit fills
- spread
- slippage
- fees
- overnight gaps
- partial fills
- stale quote handling

This is a major correction because daily P&L is worthless if simulation assumptions are vague.

---

# 5.13 Shadow lanes, ghost lanes, and resilience controls are now explicit

## Old problem
Earlier versions did not define enough structural redundancy or control-group logic.

## New canonical rule
The system now explicitly recognizes:

### Virtual / Shadow Lanes
Used to preserve signal continuity when a primary lane is missing, but always with:
- reduced trust
- reduced confidence
- explicit inferred-evidence labeling

### Ghost Lane Registry
Used as a control group showing what the system would have done without policy/risk restrictions.

### Dual-Engine Heartbeat Monitoring
Used to preserve scout continuity through:
- Alpha/Beta engine structure
- failover promotion
- packet continuity monitoring

### Safety Governor Policy
Used as the top hard-limit authority for:
- autonomy throttling
- trade/routing blocks
- fallback to manual review
- system pause conditions

## Why this matters
These changes make the system more realistic, more testable, and less fragile.

---

# 5.14 The dashboard is now formally part of the system design

## Old problem
Dashboard thinking existed, but it was not separated cleanly enough from system logic.

## New canonical rule
The dashboard now has its own spec and must:
- reflect the real module flow
- update when operator visibility changes
- remain operator-first
- avoid trading-terminal cosplay
- remain manual-review-only in tone

This is now a formal design rule, not just a preference.

---

# 5.15 Dashboard autonomy visibility is now explicit

## Old problem
Earlier dashboard planning focused on signals, research, and paper-trade outputs, but not on the system’s autonomy state.

## New canonical rule
The dashboard now explicitly tracks:
- System Autonomy Level
- policy-routed decisions
- manual-review decisions
- safety-gate interventions
- autonomous paper-trade actions vs blocked actions

## Why this matters
If the system becomes more autonomous over time, operator visibility into that autonomy level is mandatory.

Without it, the dashboard would hide one of the most important state changes in the whole system.

---

# 5.16 Architecture and storage are now explicit

## Old problem
Earlier docs still left too much ambiguity around:
- where packets live
- what is mutable vs immutable
- how the dashboard reads data
- how state differs from outputs

## New canonical rule
The architecture/storage model is now explicit:
- docs
- schemas
- config
- scripts
- outputs
- state
- logs
- replay
- dashboard contracts

This is a major improvement in build-readiness.

---

# 6. What Was Removed or Downgraded

This section explains what is no longer treated as primary.

## 6.1 The old “brief-first” mindset
Removed as the main product identity.

The brief is still useful, but it is no longer the front door.

## 6.2 Generic watchlist-first framing
Downgraded.

The new system is signal-first, not generic-watchlist-first.

## 6.3 Broad source-vendor sprawl in MVP
Downgraded.

A constrained MVP data stack is now canonical.

## 6.4 Implicit live-trading optimism
Removed.

Live trading is now firmly treated as future-only.

## 6.5 Dashboard-first overbuilding
Downgraded.

Dashboard work must reflect actual module truth and must not outrun system capability.

---

# 7. What Was Deferred

The following remain intentionally deferred:

- live execution
- broker integration
- large-scale vendor sprawl
- advanced portfolio optimization
- broad batch automation
- autonomous strategy rewriting
- oversized analytics surfaces
- execution controls not supported by real backend logic

These are not banned forever.
They are simply not part of the current canonical build priority.

---

# 8. Existing Stock Side-Quest Work: Status After Rewrite

The current stock side-quest work is **not thrown away**.

It is repositioned.

## 8.1 Existing work that still matters
- research brief generation
- risk gate review
- downstream review dashboard work
- artifact review flows
- manual downstream pipeline behavior

## 8.2 New canonical role of that work
That work now belongs to the **downstream analyst layer**.

It is no longer the main worker identity.

## 8.3 What this means
The previous stock module work becomes:
- useful infrastructure
- useful downstream review logic
- useful operator review experience

But not the canonical front-end scout system.

---

# 9. Current Canonical Build Order After Rewrite

The canonical build order is now:

1. Canon reset and design lock
2. Scout contracts and data foundations
3. MVP source lanes
4. Normalization and lane scoring
5. Contra + fusion + signal packet proof
6. Signal review surface
7. Research handoff
8. Paper-trade engine
9. Daily summaries
10. Learning/calibration
11. Hardening
12. Live-readiness review
13. Tiny live pilot

This order supersedes any loose assumption that research, paper trading, and live readiness should all be advanced together early.

---

# 10. Canonical Relationship to Jarvis

## 10.1 What remains true
The rewritten documents still respect Jarvis’s broader rules:
- workers must be bounded
- packet contracts matter
- auditability matters
- escalation matters
- no fake autonomy
- future workers should not outrun core trust-building

## 10.2 What this memo clarifies
These docs describe the **correct architecture and roadmap**.

They do **not** mean the module should suddenly outrun Jarvis phase discipline.

That rule still stands.

---

# 11. Which Documents to Trust First

If there is a conflict between older blended docs and the new canonical set, trust in this order:

1. `JARVIS_THE_FADE_SIGNAL_ENGINE_SPEC.md`
2. `JARVIS_THE_FADE_BUILD_CHECKLIST.md`
3. `JARVIS_THE_FADE_ARCHITECTURE_AND_STORAGE_SPEC.md`
4. `JARVIS_THE_FADE_TRADING_AND_REVIEW_SPEC.md`
5. `JARVIS_THE_FADE_DASHBOARD_SPEC.md`
6. `JARVIS_THE_FADE_SYSTEM_OVERVIEW.md`

Use older PRD/rubric material only as historical reference unless it is explicitly carried forward by the canonical files.

---

# 12. Summary Table of Changes

| Area | Old State | New Canonical State |
|---|---|---|
| Worker identity | mixed with broader product | worker is scout layer only |
| Product identity | generic stock research framing | signal-first full-stack architecture |
| Front door | watchlist / downstream research | Universe Scanner + scout signal packet |
| Routing layer | manual triage only | Policy Agent / MAB Router added for later-stage routing |
| Contradiction handling | weaker | explicit conflict state |
| Direction models | mixed across documents | v2 canonical |
| Weights/thresholds | easy to misread as permanent | explicitly provisional defaults |
| MVP sources | drift risk | constrained MVP data stack |
| Proof slice | too broad | signal-packet-only first slice |
| Redundancy | lightly implied | shadow lanes + heartbeat failover explicit |
| Paper trading | underdefined realism | explicit simulation assumptions required |
| Governance | human-gated only | staged path to bounded autonomy with Safety Governor |
| Dashboard | implied/partial | formal dashboard spec + autonomy visibility |
| Storage/state | underdefined | explicit architecture/storage model |

---

# 13. Final Summary

This memo exists to make one thing clear:

**The new canonical design is not just a cleaned-up wording pass. It is a structural correction.**

The major corrections are:
- splitting worker vs full product stack
- making the scout layer primary
- repositioning the old stock-module brief/risk work downstream
- formally adopting v2 direction models
- constraining the MVP data stack
- narrowing the first proof slice
- tightening simulation realism
- formalizing dashboard and storage design

If future confusion appears between older documents and the current canon, this memo should be used to explain why the canonical document set now takes precedence.

---
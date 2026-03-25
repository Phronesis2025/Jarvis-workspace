# JARVIS_THE_FADE_TRADING_AND_REVIEW_SPEC.md

**Document Type:** Trading, Simulation, and Review Specification  
**Status:** Proposed Canonical Spec  
**Version:** 1.0  
**Last Updated:** 2026-03-23  
**Owner:** Jason  
**Project Context:** Jarvis future worker / stock intelligence side quest

---

# 1. Purpose of This Document

This document defines the **downstream review, paper-trading, daily-summary, and learning layers** of THE FADE stack.

It covers:
- signal → research handoff
- research brief role
- risk gate role
- trade candidate creation
- paper-trade engine
- portfolio/position tracking
- daily summaries
- learning/calibration
- live-readiness gates
- future live pilot constraints

This document exists because the scout layer alone is not the whole system.

It is not:
- the plain-English overview
- the build checklist
- the signal-engine spec
- the architecture/storage spec
- the dashboard layout spec

This is the **downstream action-and-review spec**.

---

# 2. Role of This Layer in the Full Stack

## 2.1 Upstream
This layer begins after the scout layer has already produced a valid signal packet.

Its inputs are:
- signal packets
- operator triage decisions
- optional signal packet evidence links
- optional state snapshots

## 2.2 Downstream
This layer produces:
- research briefs
- risk gate reviews
- trade candidates
- paper trade records
- portfolio snapshots
- daily summaries
- learning reports
- live-readiness review artifacts

## 2.3 Structural rule
This layer is **downstream** of the signal engine.

It must not become the new front door.

That means:
- no brief without a signal packet
- no paper trade without a signal packet
- no learning report without paper-trade history
- no live-readiness claim without extended paper-trade proof

---

# 3. Canonical Downstream Design Decisions

These rules are mandatory.

## 3.1 Research is optional follow-up, not default for every packet
Not every signal deserves a research brief.

## 3.2 Risk gate is required before paper-trade candidacy for research-routed ideas
If a signal goes through deep research, it should also go through risk review before it becomes a trade candidate.

## 3.3 Paper trading is the first execution-like layer
Paper trading is the first place where the system simulates position-taking.

## 3.4 Daily summary is mandatory
The operator explicitly wants a daily summary showing:
- what it traded
- what happened each day
- whether the day ended positive or negative
- current or ending balance

This is a required product surface, not an optional nice-to-have.

## 3.5 Learning and calibration authority by stage

### Early and mid stages
In early and mid stages, learning suggests changes but does not self-authorize them.

That means:
- thresholds do not change automatically
- weights do not change automatically
- route policy does not change automatically
- live-trade logic does not change automatically

### Final Stage — Autonomous Policy Calibration
In the **Final Stage**, the system may enter **Autonomous Policy Calibration** within a bounded **Safety Sandbox**.

This allows the system to self-adjust:
- thresholds
- lane weights
- route preferences
- confidence gates

But only when all of the following are true:
- a statistically significant paper-trade history exists
- minimum trade count threshold is met (for example 100+ closed paper trades)
- confidence threshold for calibration validity is met (for example 95% confidence)
- the Safety Governor remains active
- hard limits are not violated
- every change is versioned, logged, and reversible

### Hard rule
Autonomous calibration is allowed only inside the sandboxed policy layer.

It must not:
- bypass hard risk limits
- bypass kill-switch logic
- silently authorize live execution
- rewrite source definitions
- rewrite direction models without explicit higher-order approval

## 3.6 Live trading remains future-only
No live broker execution is part of MVP.

---

# 4. Signal → Research Handoff

## 4.1 Purpose
Move selected signals into deeper due diligence.

## 4.2 When research is allowed
A signal may be sent to research when:
- operator triage chooses `SEND_TO_RESEARCH`
- operator triage chooses `PAPER_TRADE_CANDIDATE` but deeper review is required first
- policy requires research for a certain signal class

## 4.3 When research is blocked
Research should be blocked when:
- signal packet is invalid
- evidence paths are broken
- signal is `NO_SIGNAL`
- signal is weak and policy forbids deeper review
- conflict is unresolved and policy requires resolution first

## 4.4 Research handoff contract

### `research_handoff_packet`
Required fields:
- `research_handoff_id`
- `signal_packet_id`
- `task_id`
- `ticker`
- `signal`
- `composite_score`
- `source_breakdown`
- `conflict_flag`
- `selected_reason`
- `created_at`
- `operator_notes`
- `evidence_paths`

### Recommended fields
- `priority`
- `market_context_snapshot`
- `contra_summary`
- `triage_status`
- `requested_outputs`
- `policy_version`

---

# 5. Research Brief Specification (Downstream Role)

## 5.1 Purpose
Create a deeper operator-readable review of the selected signal.

## 5.2 Research brief responsibilities
The brief should answer:
- why this ticker is on watch
- what the main thesis is
- what catalysts matter
- what risks matter
- what evidence matters most
- what open questions remain
- what the current confidence band is

## 5.3 Research brief output contract

### `stock_research_brief`
Required fields:
- `brief_id`
- `signal_packet_id`
- `task_id`
- `ticker`
- `created_at`
- `thesis_or_watch_reason`
- `catalyst_summary`
- `risk_summary`
- `evidence_sources`
- `open_questions`
- `confidence_band`
- `review_recommendation`

### Allowed `confidence_band`
- `low`
- `medium`
- `high`

### Allowed `review_recommendation`
Suggested values:
- `monitor`
- `wait`
- `research_more`
- `candidate_for_paper_trade`
- `do_not_trade`

## 5.4 Research brief rules
- brief must link back to signal packet
- brief must not fabricate evidence
- brief must be auditable
- brief is advisory only
- brief is not a trade order
- brief is not a signal packet replacement

---

# 6. Risk Gate Specification

## 6.1 Purpose
Attempt to invalidate, downgrade, or caution the candidate before it becomes a trade.

## 6.2 Risk gate responsibilities
The risk gate should identify:
- blockers
- caution flags
- unresolved questions
- reasons to delay or avoid action
- reasons the signal may be misread or early

## 6.3 Risk gate output contract

### `risk_gate_review`
Required fields:
- `risk_gate_id`
- `signal_packet_id`
- `brief_id`
- `task_id`
- `ticker`
- `created_at`
- `overall_status`
- `summary`
- `flags`
- `blockers`
- `caution_notes`
- `operator_warning`

### Allowed `overall_status`
Suggested values:
- `pass`
- `caution`
- `flag`
- `block`

## 6.4 Risk gate rules
- no risk gate without an originating brief
- risk gate must remain advisory
- block/caution/flag status must be clear
- empty flags must be handled explicitly
- research and risk gate must not be collapsed into one artifact

---

# 7. Trade Candidate Layer

## 7.1 Purpose
Convert a reviewed signal into an explicit paper-trade candidate.

## 7.2 Why this layer exists
This prevents direct signal → trade leaps without a clear candidate artifact.

## 7.3 Trade candidate output contract

### `trade_candidate_packet`
Required fields:
- `trade_candidate_id`
- `signal_packet_id`
- `brief_id`
- `risk_gate_id`
- `ticker`
- `direction`
- `created_at`
- `reason_summary`
- `confidence_band`
- `operator_approved`
- `paper_trade_allowed`
- `notes`

### Recommended fields
- `entry_rule`
- `stop_rule`
- `target_rule`
- `time_stop_rule`
- `max_risk`
- `regime_label`
- `trade_priority`

## 7.4 Trade candidate rules
- candidate must link back to signal packet
- if research/risk gate exists, candidate must link to both
- operator approval state must be explicit
- no paper trade should exist without a candidate packet unless policy explicitly says otherwise

---

# 8. Paper Trade Engine

## 8.1 Purpose
Simulate trade execution and lifecycle without risking real money.

## 8.2 Core rule
Paper trading is **required** before live trading is even considered.

## 8.3 Paper trade record contract

### `paper_trade_record`
Required fields:
- `paper_trade_id`
- `trade_candidate_id`
- `signal_packet_id`
- `ticker`
- `side`
- `entry_timestamp`
- `entry_price`
- `position_size`
- `status`
- `decision_reason`
- `risk_gate_status`
- `brief_id`
- `exit_timestamp`
- `exit_price`
- `gross_pnl`
- `net_pnl`
- `exit_reason`

### Allowed `status`
- `open`
- `closed`
- `cancelled`
- `invalidated`

## 8.4 Recommended additional fields
- `stop_rule`
- `target_rule`
- `time_stop_rule`
- `slippage_applied`
- `fees_applied`
- `spread_assumption`
- `market_session_context`
- `regime_label`
- `entry_fill_type`
- `exit_fill_type`

---

# 9. Paper Trade Simulation Assumptions

This section is mandatory.

Without explicit simulation rules, paper-trade P&L can lie.

## 9.1 Entry fill rules
The system must define how a paper entry is simulated.

Allowed policies might include:
- next bar open
- next bar VWAP approximation
- marketable price with spread/slippage penalty
- limit-style fill only if touched

One must be chosen and documented.

## 9.2 Exit fill rules
The system must define how exits are simulated.

Exit triggers may include:
- stop hit
- target hit
- time stop
- operator manual close
- end-of-day forced close
- regime invalidation

## 9.3 Spread assumptions
The simulation must state:
- whether bid/ask spread is modeled
- how spread is approximated if true bid/ask is unavailable
- whether spread differs by asset class or liquidity bucket

## 9.4 Slippage assumptions
The simulation must define:
- fixed slippage model
- volatility-adjusted slippage model
- liquidity-adjusted slippage model
- asset-class-specific rules

## 9.5 Fee assumptions
The simulation must define:
- commission model
- fee inclusion/exclusion
- whether fees are fixed, percentage-based, or mocked as zero for specific proof phases

## 9.6 Overnight gap handling
The simulation must define what happens when:
- a stop would have triggered overnight
- a target would have triggered overnight
- the next available fill is much worse than planned
- a position is still open across sessions

## 9.7 Partial fill handling
The simulation must define:
- whether partial fills are modeled
- whether partial fills are ignored in MVP
- when partial fills become required realism

## 9.8 Stale quote handling
The simulation must define:
- when quotes are too stale to trust
- whether stale-quote trades are blocked
- whether the system marks those trades invalid or deferred

## 9.9 MVP realism rule
For MVP, assumptions may be simplified, but they must be:
- explicit
- consistent
- applied uniformly
- visible in trade logs

No hidden fill fantasy.

---

# 10. Position and Portfolio Tracking

## 10.1 Purpose
Track current and historical paper positions.

## 10.2 Position record
Each open position should track:
- ticker
- side
- entry timestamp
- entry price
- size
- current mark
- unrealized P&L
- associated signal packet
- associated trade candidate

## 10.3 Portfolio snapshot contract

### `portfolio_snapshot`
Required fields:
- `snapshot_id`
- `as_of`
- `starting_balance`
- `ending_balance`
- `cash_balance`
- `open_positions`
- `closed_positions_today`
- `realized_pnl`
- `unrealized_pnl`
- `daily_pnl`
- `cumulative_pnl`
- `largest_winner_today`
- `largest_loser_today`
- `max_drawdown`
- `win_rate`
- `average_hold_time`

## 10.4 Portfolio rules
- snapshots must be reproducible
- realized vs unrealized P&L must not be mixed
- every trade must be linkable
- balances must not be silently recalculated without traceability

---

# 11. Daily Summary Engine

## 11.1 Purpose
Generate the operator’s daily review.

This is a required product layer.

## 11.2 Daily summary outputs
- `daily_summary_<date>.json`
- `daily_summary_<date>.md`
- dashboard daily summary state

## 11.3 Daily summary contract

### `daily_summary`
Required fields:
- `summary_id`
- `date`
- `starting_balance`
- `ending_balance`
- `daily_pnl`
- `cumulative_pnl`
- `realized_pnl`
- `unrealized_pnl`
- `open_positions_count`
- `closed_trades_count`
- `signals_generated`
- `signals_ignored`
- `signals_watch_only`
- `signals_sent_to_research`
- `signals_sent_to_paper_trade`
- `conflict_packets_count`
- `lane_contribution_summary`
- `operator_notes`
- `risk_alerts`
- `data_quality_issues`

## 11.4 Required daily report fields for operator review

### Account summary
- date
- starting balance
- ending balance
- daily P&L
- cumulative P&L
- realized P&L
- unrealized P&L

### Trade summary
- trades opened today
- trades closed today
- symbols traded today
- winners today
- losers today
- biggest gain
- biggest loss
- average hold time for closed trades

### Signal summary
- total signals generated
- ignored signals
- watch-only signals
- research-routed signals
- paper-trade candidates
- conflict count
- no-signal count

### Source-lane summary
- lane contribution snapshot
- top positive lane
- top noisy lane
- top conflict lane

### Plain-English summary block
Examples:
- “Today the system took 3 paper trades.”
- “Ending balance was +$214 versus start.”
- “One conflict packet was escalated.”
- “Lane C provided the strongest supporting signals.”
- “No live trades were placed.”

## 11.5 Daily summary rules
- daily balance direction must be obvious
- day must clearly read as positive, negative, or flat
- operator must be able to see what was traded and why
- daily summary must be generated from structured artifacts, not vibes

---

# 12. Learning and Calibration Layer

## 12.1 Purpose
Help the system improve without letting it self-authorize risky behavior.

## 12.2 Learning layer inputs
- signal packets
- conflict packets
- research briefs
- risk gate reviews
- paper trade records
- portfolio snapshots
- daily summaries

## 12.3 Learning report contract

### `learning_report`
Required fields:
- `learning_report_id`
- `period_start`
- `period_end`
- `source_lane_performance`
- `signal_threshold_review`
- `false_positive_patterns`
- `conflict_pattern_review`
- `regime_notes`
- `recommended_weight_changes`
- `recommended_threshold_changes`
- `recommended_rule_changes`
- `operator_approval_required`

## 12.4 Learning objectives
The learning layer should answer:
- which lanes help most
- which lanes are noisy
- which thresholds are too loose/tight
- which conflict patterns should block trades more aggressively
- which regimes break current assumptions
- which signals look good but fail in paper mode

## 12.5 Learning guardrails
- no silent policy changes
- no silent weight changes
- no silent threshold changes
- no direct live execution control
- no self-authorized trade sizing changes

## 12.6 Regime-aware learning
The learning layer should account for:
- trend regime
- volatility regime
- news-heavy regime
- low-liquidity regime
- risk-on / risk-off conditions

## 12.7 Half-life rule
Signal usefulness should decay over time.
Old patterns should not carry equal weight forever.

## 12.8 Look-ahead bias rule
Learning reports must not rely on future information when evaluating prior decisions.

## 12.9 Synthetic Feedback Acceleration via Local LLM

### Purpose
Paper-trade feedback is slow.

To accelerate heuristic learning before enough paper-trade history exists, the system may use a **local LLM** to generate synthetic triage analysis on historical signal packets and subsequent price action.

### Example model
A local model such as:
- Llama 3
- or similar locally hosted model

### Role
The local LLM does not replace real paper-trade results.

Its role is to generate:
- synthetic triage scores
- heuristic explanations
- pattern summaries
- provisional ranking suggestions

### Allowed outputs
Suggested fields:
- `synthetic_triage_score`
- `synthetic_reason_summary`
- `synthetic_confidence`
- `historical_pattern_match`
- `llm_warning_flags`

### Hard rule
Synthetic feedback is heuristic only.

It must:
- never be treated as equivalent to real trade outcomes
- never directly authorize live execution
- never overwrite real paper-trade performance statistics
- always be labeled as synthetic

### Best use
Synthetic feedback is most useful for:
- early ranking assistance
- preliminary rule review
- faster idea triage
- spotting possible patterns before enough live paper data accumulates

### Safety rule
If synthetic feedback materially disagrees with real paper-trade evidence, real paper-trade evidence wins.

---

# 13. Review and Approval Points

The operator must remain in control at these points:

1. signal packet review
2. conflict resolution
3. research escalation
4. trade candidate approval
5. live-readiness review
6. calibration-change approval
7. any future live pilot approval

This is a non-negotiable system property.

---

# 14. Paper-Trade Guardrails

## 14.1 Required controls
- max paper trades per day
- max exposure per ticker
- max exposure per sector
- max daily loss
- duplicate-trade block
- cooldown after consecutive losses
- stale-data trade block
- unresolved-conflict trade block

## 14.2 Optional later controls
- regime-specific position caps
- volatility-based size reductions
- market-halt awareness
- liquidity bucket restrictions

## 14.3 Guardrail rule
If a guardrail fires, the trade should:
- not open
- or be explicitly marked blocked/invalidated
- and the reason must be logged

---

# 15. Live-Readiness Review

## 15.1 Purpose
Determine whether the system deserves a tiny live pilot.

## 15.2 Live-readiness is a review phase, not a default progression
Completing paper trading does not automatically authorize live trading.

## 15.3 Live-readiness review inputs
- paper-trade history
- daily summaries
- learning reports
- guardrail history
- system health history
- operator review notes

## 15.4 Required live-readiness questions
- Has the system produced enough paper trades?
- Are the results stable enough to trust?
- Are drawdowns controlled?
- Are conflicts handled properly?
- Are daily summaries trustworthy?
- Are simulation assumptions realistic enough?
- Are the controls good enough for even a tiny real-money pilot?

## 15.5 Required live-readiness outputs
- `live_readiness_review_<date>.json`
- explicit pass/fail decision
- explicit operator signoff field
- list of blockers
- next-step recommendation

---

# 16. Tiny Live Pilot Rules

## 16.1 Status
Future only.

## 16.2 Purpose
Run the smallest possible real-money pilot after long proof.

## 16.3 Live pilot rules
- tiny size only
- manual confirmation required
- hard kill switch required
- one broker only at first
- order/fill logging mandatory
- live-vs-paper comparison mandatory
- no auto-scaling
- no hidden rule mutation during pilot

## 16.4 Live pilot stop conditions
- drawdown breach
- control failure
- unexpected execution behavior
- unreliable summaries
- operator trust failure
- broken audit trail

---

# 17. Required Downstream Storage Artifacts

This spec assumes the architecture/storage system supports the following artifacts:

- research briefs
- risk gate reviews
- trade candidate packets
- paper trade records
- portfolio snapshots
- daily summaries
- learning reports
- live-readiness reviews

Each must:
- have a stable ID
- link back upstream
- be schema-backed
- be auditable

---

# 18. Current Relationship to Existing Stock Module Work

## 18.1 What survives
The current stock side-quest already proved:
- research brief generation
- risk gate generation
- dashboard review of downstream artifacts
- pipeline-style chaining in the downstream analyst lane

Those are useful.

## 18.2 New role
Under this new system, those pieces become:
- downstream analyst support
- not the primary scout
- not the front-door stock worker identity

## 18.3 Design consequence
The scout layer should eventually become the real entry point.
The existing brief/risk work becomes the optional deep-review layer for stronger signals.

---

# 19. First Proof Slice for This Downstream Layer

This spec does not own the first system proof slice.

But once the scout is proven, the first downstream proof slice should be:

1. one valid signal packet
2. one research handoff
3. one research brief
4. one risk gate review
5. no paper trading yet

Then the first paper-trade proof slice should be:

1. one approved trade candidate
2. one simulated entry
3. one simulated exit
4. one valid paper trade record
5. one correct portfolio snapshot
6. one correct daily summary

That is the correct downstream build order.

---

# 20. Success Criteria for This Spec

This spec is satisfied only when the downstream stack can do all of the following:

- accept valid signal packets
- create research handoff packets
- generate valid research briefs
- generate valid risk gate reviews
- create explicit trade candidates
- simulate paper trades under defined assumptions
- track positions and balances correctly
- generate daily summaries with clear positive/negative day outcome
- produce learning reports that suggest changes but do not self-authorize them
- keep live trading disabled until explicit later review

---

# 21. Final Summary

This spec defines the second half of THE FADE system.

The signal engine finds and scores opportunities.  
This downstream layer does everything after that:

- research
- skepticism
- trade simulation
- position tracking
- daily reporting
- learning
- live-readiness review

The most important corrections baked into this spec are:
- research is downstream, not the front door
- paper trade simulation assumptions are explicit
- daily summaries are mandatory
- learning is approval-gated
- live trading stays future-only
- existing stock brief/risk-gate work is preserved, but repositioned

If this layer is built before the scout is proven, it becomes noise.  
If this layer is built after the scout is proven, it becomes the right operational feedback engine.

---


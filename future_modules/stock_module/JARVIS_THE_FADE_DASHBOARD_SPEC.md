# JARVIS_THE_FADE_DASHBOARD_SPEC.md

**Document Type:** Dashboard Specification  
**Status:** Proposed Canonical Spec  
**Version:** 1.0  
**Last Updated:** 2026-03-23  
**Owner:** Jason  
**Project Context:** Jarvis future worker / stock intelligence side quest

---

# 1. Purpose of This Document

This document defines the **dashboard surfaces, views, states, operator workflows, data requirements, and UI rules** for THE FADE system.

It exists to answer:
- what pages the dashboard needs
- what each page is for
- what data each page reads
- what must be visible to the operator
- what must be hidden or deferred
- how the dashboard reflects the real current module state
- how the dashboard evolves from scout-only proof to full paper-trading and review stack

This is not:
- the system overview
- the build checklist
- the signal-engine behavior spec
- the architecture/storage spec
- the trading/review rules spec

This is the **operator visibility specification**.

---

# 2. Dashboard Design Principles

## 2.1 Operator-first, not trader-cosplay
The dashboard must help the operator review the system.

It must **not**:
- look like a trading terminal
- pretend to be an execution screen
- add fake analytics
- bury key warnings under clutter

## 2.2 Reflect live module truth
Whenever the live module flow changes in a way that affects operator visibility, the dashboard must be updated to reflect that new truth.

This is a hard rule.

Examples:
- if multiple output sets now exist, the dashboard cannot remain stuck in “latest only” mode
- if risk-gate output becomes part of the live lane, the dashboard must surface it
- if signal packets become the front door, the dashboard must reflect that

## 2.3 Plain English beats jargon
Labels should be understandable to a normal operator.

Use helper text for:
- confidence band
- conflict
- risk gate status
- lane contribution
- selected review
- daily P&L

## 2.4 Manual-review-only status must stay obvious
The dashboard should repeatedly make clear:
- this is advisory
- this does not place trades
- this is not live execution
- the operator still decides what to do

## 2.5 One source of truth per surface
Pages should read from explicit contracts and structured loaders, not ad hoc file scraping.

---

# 3. Dashboard Role in the Full System

The dashboard is the **operator visibility layer** for THE FADE stack.

It does not:
- own signal logic
- own scoring logic
- own paper-trade logic
- own learning logic

It displays and organizes those outputs for review.

The dashboard should support these stages:

1. signal review
2. research review
3. paper-trade review
4. daily summary review
5. system health / warnings

---

# 4. Core Dashboard Pages

The full dashboard should eventually contain five main pages.

## 4.1 Signal Review Page
**Purpose:** review current signal packets and scout outputs

## 4.2 Research Review Page
**Purpose:** review deeper research briefs and risk-gate outputs

## 4.3 Paper Trade Review Page
**Purpose:** review simulated trades and current/open positions

## 4.4 Daily Summary Page
**Purpose:** review end-of-day results, balance, trade counts, and lane-performance summaries

## 4.5 System Health / Operations Page
**Purpose:** review source health, stale data, broken pipelines, and escalation/failure state

---

# 5. MVP Dashboard Scope

The full dashboard should not be built at once.

## 5.1 Dashboard MVP
For the first bounded scout proof slice, the dashboard only needs:

- **Signal Review Page**
- minimal system-health visibility
- conflict visibility
- operator-readable packet details

## 5.2 Explicitly deferred from dashboard MVP
- research review page
- paper trade page
- daily summary page
- performance charts
- learning dashboards
- live-trading controls

## 5.3 Why
The dashboard must not outrun the real system.

If the signal packet layer is not proven yet, building paper-trade or daily-performance dashboards is premature UI theater.

---

# 6. Page-by-Page Specification

# 6.1 Signal Review Page

## Purpose
This is the front-door operator review page for THE FADE scout layer.

Once the redesigned system is live, **this becomes the true stock-module entry surface**, not the downstream brief page.

## What it must show
For each signal packet:
- ticker
- signal classification
- composite score
- conflict state
- source breakdown
- freshness
- evidence links
- operator notes
- triage status

## Recommended sections
### A. Page header
- title
- subtitle
- manual-review warning

### B. Signal queue summary
- total current signal packets
- strong signals
- weak signals
- no-signal packets
- conflict packets

### C. Available signal reviews
A list or selector of recent signal packets:
- ticker
- created time
- signal class
- conflict flag
- source-lane highlights

### D. Selected signal details
- signal summary
- source breakdown
- evidence list
- contra summary
- operator note area
- current triage status

### E. Conflict callout
If conflict is present:
- make it visually obvious
- explain why conflict matters
- block false certainty

## Helper text examples
- `Conflict` → “Important source lanes disagree. This setup needs extra care and may not be actionable.”
- `Composite score` → “A combined signal score based on the current lane rules. This is a review aid, not a guarantee.”
- `Available reviews` → “Recent signal packets generated by the current scout pipeline.”

## Empty state
If no signal packets exist:
- show a clean empty message
- explain that the scout layer has not produced any packets yet
- do not invent fake data

---

# 6.2 Research Review Page

## Purpose
Review downstream deep-dive artifacts for signals that were escalated to research.

## What it must show
- linked signal packet
- research brief
- risk gate
- evidence
- open questions
- review recommendation

## Recommended sections
### A. Page header
- title
- explanation that this is downstream deep review

### B. Available research reviews
- ticker
- created time
- confidence band
- risk gate status

### C. Selected research brief
- why it is on watch
- catalysts
- risks
- evidence
- open questions
- recommendation

### D. Selected risk gate
- overall status
- summary
- flags
- blockers
- caution notes

### E. Manual-review warning
- this is not execution
- this does not place trades
- the operator still decides what happens next

## Empty state
If no research artifacts exist:
- explain that no signal has been escalated to research yet
- do not crash
- do not fabricate placeholders

---

# 6.3 Paper Trade Review Page

## Purpose
Show simulated trade activity and current open/closed paper positions.

## What it must show
- open positions
- recently closed trades
- trade rationale linkback to signal packet
- realized/unrealized P&L
- trade entry/exit details
- why the trade existed

## Recommended sections
### A. Portfolio summary
- current paper balance
- realized P&L
- unrealized P&L
- open positions count
- closed trades today

### B. Open positions
- ticker
- side
- entry
- current mark
- unrealized P&L
- originating signal

### C. Closed trades
- ticker
- side
- entry/exit
- realized P&L
- exit reason
- originating signal

### D. Trade detail view
- signal packet link
- brief link
- risk gate link
- stop/target/time-stop
- slippage/spread assumptions used

## Warning requirement
Must clearly say:
- these are paper trades
- these are simulated
- fills depend on simulation assumptions
- this is not a live broker account

---

# 6.4 Daily Summary Page

## Purpose
Give the operator the fast daily review they explicitly want.

## This page is mandatory once paper trading exists.

## What it must show
- date
- starting balance
- ending balance
- daily P&L
- cumulative P&L
- number of trades
- winners/losers
- biggest gain/loss
- signals generated
- conflicts escalated
- source-lane summary
- plain-English operator summary

## Recommended sections
### A. Account summary card row
- starting balance
- ending balance
- daily result
- cumulative result

### B. Trade activity summary
- trades opened
- trades closed
- winners
- losers
- largest winner
- largest loser

### C. Signal activity summary
- signals generated
- ignored
- watch only
- sent to research
- sent to paper trade
- conflict packets

### D. Lane contribution summary
- best-performing lane
- noisiest lane
- most conflict-prone lane

### E. Plain-English daily note
Examples:
- “The system ended today +$183 on paper.”
- “Two paper trades closed green, one closed red.”
- “Lane C contributed most to winning signals.”
- “One conflict packet was escalated and not traded.”

## Visual rule
It must be immediately obvious whether the day ended:
- positive
- negative
- flat

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

# 6.5 System Health / Operations Page

## Purpose
Show whether the system is healthy enough to trust.

## What it must show
- adapter health
- stale-source warnings
- schema-validation warnings
- unresolved failures
- latest successful run times
- policy/version info
- review-surface readiness

## Recommended sections
### A. Adapter health
- lane-by-lane availability
- last successful fetch
- stale warnings

### B. Validation status
- schema failures
- malformed events
- packet failures
- unresolved escalations

### C. Current blockers
- missing required lane
- invalid signal packet output
- undefined direction model
- missing review index

### D. Version and policy panel
- direction model version
- fusion policy version
- dashboard contract version

## Why this page matters
A beautiful signal dashboard is worthless if the data is stale or broken.

---

# 7. Dashboard Routes

Recommended route map:

- `/fade-signals`
- `/fade-research`
- `/fade-paper-trades`
- `/fade-daily-summary`
- `/fade-health`

If you want to keep old stock-side-quest routes temporarily during migration, do it explicitly and treat them as transitional, not canonical.

---

# 8. Dashboard Data Sources

The dashboard should read from structured loaders backed by:
- `state/`
- explicit review indexes
- stable output pairing logic
- dashboard contract schemas

It should not depend on:
- random directory scraping
- undocumented latest-by-mtime shortcuts as long-term logic
- hidden pairing assumptions
- arbitrary file names without contract rules

## Required review indexes
Recommended dashboard-read inputs:
- `signal_review_index.json`
- `research_review_index.json`
- `paper_trade_index.json`
- `daily_summary_index.json`
- `system_health_snapshot.json`

---

# 9. Review Pairing Rules

This matters because your previous stock lane already ran into pairing and “latest file” issues.

## 9.1 Signal page pairing
Signal packets are primary and do not require downstream pairing.

## 9.2 Research page pairing
Research brief and risk gate should be linked by:
- `signal_packet_id`
- or a strong shared ID
- not only by latest file or file name if stronger linkage exists

## 9.3 Paper trade pairing
Every paper trade must link back to:
- `trade_candidate_id`
- `signal_packet_id`

## 9.4 Daily summary inputs
Daily summary should aggregate from structured artifacts, not heuristic guesswork.

## Rule
Filename-based pairing may be acceptable for transitional proof stages, but stronger ID-based linkage is the canonical long-term expectation.

---

# 10. Operator Workflow Through the Dashboard

## 10.1 Scout-only phase
Operator opens:
- `/fade-signals`
- reviews packets
- checks conflicts
- decides whether anything is worth escalation

## 10.2 Research phase
Operator opens:
- `/fade-research`
- reviews the brief and risk gate
- decides whether the idea is worth paper trading

## 10.3 Paper-trade phase
Operator opens:
- `/fade-paper-trades`
- reviews open and closed paper positions
- checks rationale and performance

## 10.4 End-of-day phase
Operator opens:
- `/fade-daily-summary`
- checks ending paper balance
- checks daily positive/negative result
- reviews trades and source-lane contribution

## 10.5 Maintenance phase
Operator opens:
- `/fade-health`
- checks stale sources, failures, and system readiness

---

# 11. Dashboard MVP Build Order

## MVP Dashboard Phase 1
Build:
- `/fade-signals`
- basic `/fade-health`
- no research page yet
- no paper-trade page yet
- no daily summary page yet

## MVP Dashboard Phase 2
After research handoff is live:
- add `/fade-research`

## MVP Dashboard Phase 3
After paper trading is real:
- add `/fade-paper-trades`
- add `/fade-daily-summary`

## MVP Dashboard Phase 4
After hardening:
- expand `/fade-health`

This is the correct order.

---

# 12. Required UI States

Every page must handle these states cleanly:

- loading
- empty
- present data
- partial data
- stale data
- invalid data / escalation-required

No page should:
- crash
- fabricate data
- silently suppress known bad state
- show false precision

---

# 13. Required Manual-Review Messaging

These messages or their equivalents must appear where relevant:

## Signal page
- “These are advisory signal packets for operator review.”

## Research page
- “This is deeper review, not an execution decision.”

## Paper trade page
- “These are simulated trades, not live broker positions.”

## Daily summary page
- “This summary reflects paper-trade performance only.”

## Health page
- “This page shows whether the system is safe to trust operationally.”

The dashboard must repeatedly make clear that:
- this is not auto-trading
- the operator remains in charge

---

# 14. Dashboard Rules That Prevent Bad Design

## 14.1 No fake analytics
Do not invent:
- hidden model certainty
- fake edge scores
- performance metrics unsupported by actual artifacts

## 14.2 No trading-terminal cosplay
Do not make this look like:
- a flashy execution console
- a fake Bloomberg clone
- a chart-heavy hype screen

## 14.3 No operator-confusing jargon unless explained
If a term is necessary, add helper text.

## 14.4 No dashboard drift
If the module flow changes materially, the dashboard must be updated to match the new truth.

This is a hard rule.

---

# 15. Dashboard Data Quality Warnings

Pages should surface warnings like:
- missing required lane
- stale market data
- signal packet conflict
- missing research brief
- missing risk gate
- missing daily summary
- invalid trade record
- review index stale

Warnings should be visible, not buried.

---

# 16. Migration from Current Stock Dashboard State

## Current downstream-only state
You already had:
- stock intake review
- stock brief review
- multi-review selector for downstream artifacts

That work is still useful.

## New canonical direction
Under THE FADE, the dashboard should evolve so that:
- signal review becomes the front door
- research review becomes downstream
- paper-trade and daily summary views come later

## Migration rule
Do not throw away useful downstream pages.  
Reposition them under the new system architecture.

---

# 17. What the Dashboard Must Not Do Yet

Until the system actually supports these capabilities, the dashboard must not pretend they exist:

- live broker execution
- auto-trade approval
- self-updating strategy logic
- real performance attribution beyond recorded artifacts
- cross-asset portfolio optimization
- high-frequency monitoring screens

If the backend does not truly support it, the dashboard must not fake it.

---

# 18. Success Criteria for the Dashboard

The dashboard is successful when the operator can:

1. review current signal packets clearly
2. identify conflicts quickly
3. inspect deeper research when available
4. inspect paper trades when they exist
5. see daily ending balance and daily positive/negative result
6. understand which lanes contributed most
7. tell whether the system is healthy enough to trust
8. do all of this without the UI pretending to be an execution engine

---

# 19. Final Summary

The THE FADE dashboard should be built as the **operator review surface for the full stack**.

Its first job is to make the scout layer reviewable.  
Its next job is to connect deeper research cleanly.  
Its later jobs are to display paper-trade history, daily results, and system health.

The critical rules are:
- keep it operator-first
- keep it plain-English
- keep manual-review-only status obvious
- make the dashboard reflect the real module state whenever the live flow changes
- never let UI complexity outrun the actual system

That is the correct dashboard design for this module.

---
# JARVIS\_THE\_FADE\_MASTER\_BUILD\_CHECKLIST.md

**Document Type:** Master Build Checklist  
**Status:** Proposed Canonical Control Checklist (live progress below)  
**Version:** 1.17  
**Last Updated:** 2026-03-26T18:07:50.4742908-05:00  
**Owner:** Jason  
**Project Context:** Jarvis future worker / stock intelligence side quest

**Live use:** Re-read **Live Progress Snapshot** and **Live phase-status table** on major checkpoints; they override stale assumptions elsewhere in this file until that section is revised.

\---

## Live Progress Snapshot (authoritative)

Workspace branch: `the-fade-phase1-tranche1-foundation`.

The **eight THE FADE design canon** Markdown files (`JARVIS_THE_FADE_*.md`) **must remain** in `future_modules/stock_module/` -- foundational module docs; **do not move or delete** (index: `future_modules/the_fade/docs/CANON_INDEX.md`).

| Item | Current truth |
|------|----------------|
| MVP gate | **Phase 2** -- MVP lane approval and source reliability |
| `mvp_lane_approval.json` | `approved`: **false**; `approved_mvp_lanes`: **empty** |
| Active lane focus | **`lane_b_official_disclosure`** (lane B) |
| Phase 3 (Universe Scanner) | **Not started** |
| Phase 3 unlock | **Blocked** until MVP gate satisfied; no automatic unlock from bounded evidence |
| Lane B vs gate sufficiency | **Not close** -- lane-level evidence remains **partial**; MVP approval **not** justified |
| Reliability vs `required_reliability_threshold` (0.8) | **No honest comparison yet** -- **`reliability`** dimension is **partial**; **Tranche 21** stricter standard **preserved**; **Tranche 24 interim pilot** (Federal Register only): **8** counted (**`t22_fr_000`**, **`t22_fr_001`**, **`t24_fr_pilot_01`**, **`t24_fr_pilot_02`**, **`t24_fr_pilot_03`**, **`t24_fr_pilot_04`**, **`t24_fr_pilot_05`**, **`t24_fr_pilot_06`**); **6** / **6** pilot slots done (final interim slot complete); **<=8** ceiling; **no** **0.8** claim; pilot complete and does **not** justify approval re-evaluation (approval remains false) |
| Lane B MVP disclosure **provider** | **Not locked** -- `mvp_lane_approval.json` **`TBD_OFFICIAL_DISCLOSURE_PROVIDER`**. Tranche **19** clarified mixed URLs (Federal Register vs SEC vs issuer IR) are **not** one provider path. |
| Lane B post-pilot decision (Tranche **26**) | **Parked** -- promising-but-unapproved (`approved:false`). **Next authorized Phase 2 move:** schedule a **future full Tranche 21** Federal Register reliability window when operator availability allows (gate protocol in `MVP_SOURCE_RELIABILITY_AUDIT.md`); **not** approval and **not** Phase 3. |

**Phase 2 work completed and committed (checkpoint list):** approval gate prep; deferred approval decision; lane B evidence pack + refinement passes; honest blocker documentation; controlled evidence protocol; minimal harness build + hardening; simulated rehearsal + correction + reproducibility cleanup; real evidence path audit; minimal real evidence path spec + correction; lane B real observation slice build; canon recovery from stash snapshot into `future_modules/stock_module/`; post-canon dirty-state cleanup (registry/log/contra alignment); **Tranche 18** reliability-window honesty pass (`docs/MVP_LANE_EVIDENCE_LOG.md`, `docs/MVP_SOURCE_RELIABILITY_AUDIT.md` -- four countable `observe` tries in one session; **no** valid 0.8 gate statistic); **Tranche 19** lane B provider/source class clarification (log + audit + `LANE_B_MINIMAL_REAL_EVIDENCE_PATH_SPEC.md` -- **one** source class per reliability pass; provisional next target **Federal Register API** only for that pass, not mixed with SEC/issuer); **Tranche 20** single-source reliability pass (Federal Register API only; 5 attempts / 5 successes / 0 failures; still **no** honest comparison to 0.8 yet); **Tranche 21** pre-audit reliability window protocol defined (Federal Register API-only; 48h UTC window; 2h cadence; count normalized_signal_event as success vs scout_failure as failure; compare to 0.8 only after >=20 counted attempts) -- **stricter target preserved** in audit; **Tranche 22-23** -- **2** counted attempts on original UTC grid (`t22_fr_000`, `t22_fr_001`); **Tranche 24** -- **availability-constrained interim pilot** (**CDT** schedule; **<=8** ceiling); Prompts **#75/#78/#80/#82/#86/#88** -- all six pilot slots observed (`t24_fr_pilot_01`, `t24_fr_pilot_02`, `t24_fr_pilot_03`, `t24_fr_pilot_04`, `t24_fr_pilot_05`, `t24_fr_pilot_06`); cumulative **8** counted / **8** successes / **0** failures in this slice; **final interim pilot result** only; **not** full pre-audit gate window; **no** 0.8 conclusion; **Tranche 25 closeout audit complete** (interim pilot done: 6/6 slots, 8/8 successes; proved positive interim success-path signal; did **not** satisfy the original Tranche 21 gate protocol; therefore does **not** justify any `required_reliability_threshold` **0.8** comparison or any approval re-evaluation; approval remains **not justified**); **Tranche 26** post-pilot go/no-go: lane B **parked** promising-but-unapproved; **GO** to **schedule** a future full **Tranche 21** gate run when feasible (**NO-GO** on approval re-evaluation and **NO-GO** on Phase 3 until gate evidence meets standard).

**Real observation slice:** implemented (`lane_b_real_observation_slice.py`) -- **does not** justify approval re-evaluation or MVP lane selection by itself.

**Registry nuance:** `reliability` for lane B is **partial** (Tranche 18/20; micro-sample only). `stale_outage_behavior` and `context_dominance_risk` may show **recorded (bounded)** -- still **not** approved-lane proof, **not** production completeness, and **does not** unlock Phase 3.

**Discipline:** Use this master checklist for periodic checkpointing to avoid scope drift.

\---

## Live phase-status table (master phases)

| Phase (see ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§5 Locked Tranche Order) | Status |
|-------------------------------------|--------|
| Phase 0 -- Canon Lock + Build Map | **COMPLETE** (effective for current build path) |
| Phase 1 -- Scout Contracts and Policy Foundations | **COMPLETE FOR CURRENT PROOF PATH** |
| Phase 2 -- MVP Data Stack and Source Reliability Pre-Audit | **ACTIVE** |
| Phases 3-16 -- Universe Scanner through Tiny Live Pilot | **NOT STARTED** -- **BLOCKED** on MVP gate (no Phase 3 work started) |

\---

# 1\. Purpose of This Document

This document is the **locked master build checklist** for THE FADE system.

It exists to prevent:

* scope drift
* architecture drift
* dashboard drift
* premature autonomy
* paper-trade fantasy before signal proof
* random new ideas from derailing the build sequence

This is the control document for the full build.

It defines:

* the full tranche order
* what uses Plan Mode
* what uses step-by-step execution
* where proof gates exist
* what is deferred
* what must not be built early

\---

# 2\. Master Build Rule

## Use both Cursor modes, but at different levels

* **Plan Mode** = for **tranche planning**, dependency mapping, scope cutting, proof-gate design, and file/module ordering
* **Step-by-step mode** = for **actual implementation**, proof, doc-lock, dashboard update when needed, and bounded commit/push

That is the hybrid build method.

## Hard rule

Do **not** use Plan Mode to try to build the whole system in one giant shot.

Do **not** use step-by-step mode with no architecture map.

The correct process is:

1. plan the tranche
2. review the plan
3. build the tranche step-by-step
4. prove the tranche
5. update docs/dashboard if needed
6. commit the tranche
7. move to the next tranche

\---

# 3\. Legend

* **\[PLAN]** = use Cursor Plan Mode
* **\[STEP]** = execute in normal step-by-step mode
* **\[DOC]** = doc-lock required
* **\[DASH]** = dashboard must be checked/updated if operator visibility changes
* **\[PROOF]** = hard proof gate before next tranche
* **\[DEFER]** = explicitly not in scope yet

\---

# 4\. Absolute Red-Line Rules

These rules apply across the whole build.

* \[ ] Do not skip the scout proof slice
* \[ ] Do not build paper trading before the signal packet layer is trustworthy
* \[ ] Do not build autonomy before paper proof and hardening
* \[ ] Do not let dashboard work outrun backend truth
* \[ ] Do not let shadow lanes pretend to be primary evidence
* \[ ] Do not let synthetic feedback outrank real paper-trade results
* \[ ] Do not let Safety Governor become advisory only
* \[ ] Do not let "fewest steps" turn into giant risky build chunks
* \[ ] Do not outrun Jarvis phase discipline
* \[ ] Do not treat initial weights/thresholds as proven truth
* \[ ] Do not let new ideas override the locked tranche order without deliberate review

\---

# 5\. Locked Tranche Order

This is the master order.

1. Phase 0 -- Canon Lock + Build Map
2. Phase 1 -- Scout Contracts and Policy Foundations
3. Phase 2 -- MVP Data Stack and Source Reliability Pre-Audit
4. Phase 3 -- Universe Scanner
5. Phase 4 -- Event Normalization
6. Phase 5 -- Lane Scoring
7. Phase 6 -- Contra-Signal Engine
8. Phase 7 -- Fusion / Conflict / Signal Packet
9. Phase 8 -- Signal Review Dashboard
10. Phase 9 -- Research Handoff + Downstream Analyst Layer
11. Phase 10 -- Paper Trade Engine
12. Phase 11 -- Daily Summary and Operator Review Loop
13. Phase 12 -- Learning / Calibration
14. Phase 13 -- Hardening / Replay / Health
15. Phase 14 -- Autonomous Transition
16. Phase 15 -- Live-Readiness Review
17. Phase 16 -- Tiny Live Pilot

\---

# Phase 0 -- Canon Lock + Build Map

**Mode:** \[PLAN]  
**Why first:** if the architecture is not locked now, the build will drift later.

## Purpose

Turn the document set into a real implementation graph.

## Checklist

* \[ ] Confirm canonical document set is the source of truth
* \[ ] Resolve any remaining contradictions across docs
* \[ ] Freeze the first bounded proof slice
* \[ ] Freeze the Minimal Viable Data Stack
* \[ ] Freeze the module boundary:

  * \[ ] THE FADE scout
  * \[ ] downstream research/risk
  * \[ ] paper trading
  * \[ ] daily summaries
  * \[ ] learning
  * \[ ] later autonomy/live-readiness
* \[ ] Create dependency map
* \[ ] Identify dashboard impacts by tranche
* \[ ] Identify schema/contracts needed first
* \[ ] Identify reusable old stock side-quest work
* \[ ] Identify obsolete old stock framing

## Plan Mode output required

* \[ ] tranche list
* \[ ] dependency graph
* \[ ] file/module creation order
* \[ ] proof gates
* \[ ] dashboard impact notes
* \[ ] deferred list

## Proof gate \[PROOF]

* \[ ] The whole build can be described in ordered tranches without contradiction
* \[ ] The first proof slice is narrow and explicit
* \[ ] No downstream phase is pretending to be MVP

\---

# Phase 1 -- Scout Contracts and Policy Foundations

**Mode:** \[PLAN] then \[STEP]

## Purpose

Define the scout-layer contracts and policy foundations.

## Plan Mode focus

* schemas
* config registries
* lane registry
* direction-model registry
* threshold/weight defaults
* escalation matrix
* output artifact contracts

## Step-by-step checklist

* \[ ] Define `fade\_task\_packet` contract
* \[ ] Define `scanner\_candidate\_set` contract
* \[ ] Define `normalized\_signal\_event` contract
* \[ ] Define `lane\_scorecard` contract
* \[ ] Define `contra\_signal\_result` contract
* \[ ] Define `signal\_packet` contract
* \[ ] Define `conflict\_packet` contract
* \[ ] Define failure artifact contract
* \[ ] Define lane registry
* \[ ] Define direction-model registry
* \[ ] Define threshold/weight policy registry
* \[ ] Define scanner policy
* \[ ] Define escalation policy
* \[ ] Define Safety Governor baseline structure
* \[ ] Define Heartbeat Monitor contract placeholders
* \[ ] Mark all weights/thresholds as initial defaults

## Deliverables

* \[ ] scout schemas
* \[ ] policy/config files
* \[ ] validation rules
* \[ ] failure-state definitions

## Proof gate \[PROOF]

* \[ ] Every core scout artifact has a schema
* \[ ] Direction models are explicit
* \[ ] Failure conditions are explicit
* \[ ] No downstream code is needed yet

\---

# Phase 2 -- MVP Data Stack and Source Reliability Pre-Audit

**Mode:** \[PLAN] then \[STEP]

## Purpose

Constrain the system to a realistic MVP data stack.

## Plan Mode focus

* exact MVP sources
* exact deferred sources
* fallback logic
* field availability
* reliability risks

## Step-by-step checklist

* \[ ] Pick one official/disclosure lane for MVP
* \[ ] Pick one market-data lane for MVP
* \[ ] Pick one curated public-signal lane for MVP
* \[ ] Define Research Swarm as context-only
* \[ ] Create source reliability scorecard for each MVP source
* \[ ] Define freshness windows per lane
* \[ ] Define lag classes per lane
* \[ ] Define trust tiers per lane
* \[ ] Define deferred source list
* \[ ] Define outage behavior per lane
* \[ ] Define stale-data behavior per lane

## Deliverables

* \[ ] MVP lane source list
* \[ ] source reliability audit
* \[ ] deferred source register
* \[ ] freshness/trust rules

## Proof gate \[PROOF]

* \[ ] MVP data stack is small enough to build
* \[ ] No phase-1 dependence on vendor sprawl
* \[ ] Missing/stale source behavior is defined before adapter implementation

\---

# Phase 3 -- Universe Scanner

**Mode:** \[PLAN] then \[STEP]

## Purpose

Create the candidate-generation front end.

## Plan Mode focus

* candidate generation rules
* scanner passes
* daily cap
* scanner output artifact
* proof cases

## Step-by-step checklist

* \[ ] Implement candidate-set contract
* \[ ] Implement first-pass scanner policy
* \[ ] Build Pass A
* \[ ] Build Pass B
* \[ ] Build Pass C only if it is inside MVP scope
* \[ ] Defer non-MVP passes
* \[ ] Implement scanner output writer
* \[ ] Implement candidate exclusion rules
* \[ ] Implement candidate cap
* \[ ] Implement scanner logging

## Deliverables

* \[ ] scanner script
* \[ ] scanner output artifacts
* \[ ] scanner validation

## Proof gate \[PROOF]

* \[ ] Scanner produces bounded candidate lists
* \[ ] No invented candidates
* \[ ] Output is reusable by the scout layer

\---

# Phase 4 -- Event Normalization

**Mode:** \[STEP]

## Purpose

Convert raw evidence into one normalized event structure.

## Step-by-step checklist

* \[ ] Implement normalized event schema validator
* \[ ] Implement raw ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ normalized mapping for official lane
* \[ ] Implement raw ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ normalized mapping for market lane
* \[ ] Implement raw ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ normalized mapping for curated public-signal lane
* \[ ] Implement context-only normalization for Research Swarm enrichment
* \[ ] Implement duplicate/derivative detection fields
* \[ ] Implement parser-confidence handling
* \[ ] Implement failed-normalization artifact writer
* \[ ] Implement evidence-path preservation

## Deliverables

* \[ ] normalized event writer
* \[ ] failed event writer
* \[ ] lane-specific mapping logic

## Proof gate \[PROOF]

* \[ ] One source event from each MVP lane can be normalized
* \[ ] Normalization failures are explicit
* \[ ] Evidence traceability is intact

\---

# Phase 5 -- Lane Scoring

**Mode:** \[STEP]

## Purpose

Convert normalized events into lane-level scorecards.

## Step-by-step checklist

* \[ ] Implement lane scorecard contract
* \[ ] Implement Lane A scoring
* \[ ] Implement Lane B scoring
* \[ ] Implement Lane C scoring
* \[ ] Implement Lane E enrichment limits
* \[ ] Apply v2 direction models as canonical
* \[ ] Apply freshness penalties
* \[ ] Apply lag penalties
* \[ ] Apply trust modifiers
* \[ ] Apply duplicate penalties
* \[ ] Record conditions hit/missed
* \[ ] Record score rationale

## Deliverables

* \[ ] lane scorecard writer
* \[ ] score validation
* \[ ] score rationale output

## Proof gate \[PROOF]

* \[ ] One ticker can receive lane scorecards from available lanes
* \[ ] Scoring is explainable
* \[ ] Undefined direction models escalate instead of silently scoring

\---

# Phase 6 -- Contra-Signal Engine

**Mode:** \[STEP]

## Purpose

Add adversarial / contradiction checks before fusion.

## Step-by-step checklist

* \[ ] Implement contra-result contract
* \[ ] Define contra checks
* \[ ] Implement contradiction detection
* \[ ] Implement weakening factors
* \[ ] Implement market-behavior contradiction checks
* \[ ] Implement forced conflict conditions
* \[ ] Implement contra artifact output
* \[ ] Link contra output to signal packet pipeline

## Deliverables

* \[ ] contra-result artifacts
* \[ ] forced-conflict behavior
* \[ ] auditable contra reasons

## Proof gate \[PROOF]

* \[ ] The engine can produce a non-trivial contra result
* \[ ] A candidate can be downgraded or forced into conflict
* \[ ] Contra logic is visible, not hidden

\---

# Phase 7 -- Fusion / Conflict / Signal Packet

**Mode:** \[PLAN] then \[STEP]

## Purpose

Produce the first real scout output.

## Plan Mode focus

* fusion order
* conflict thresholds
* regime-aware weighting policy
* shadow-lane treatment
* final signal classes
* packet output sequence
* proof scenarios

## Step-by-step checklist

* \[ ] Implement fusion engine
* \[ ] Implement conflict logic
* \[ ] Implement bearish and bullish classifications
* \[ ] Implement no-signal/weak outputs
* \[ ] Implement regime-aware weighting defaults
* \[ ] Implement shadow-lane confidence caps
* \[ ] Implement signal packet writer
* \[ ] Implement conflict packet writer
* \[ ] Implement escalation path for invalid output
* \[ ] Implement heartbeat production metrics for scout output

## Deliverables

* \[ ] valid signal packet
* \[ ] valid conflict packet
* \[ ] scout health signals

## Proof gate \[PROOF]

* \[ ] First full scout proof slice passes
* \[ ] Conflict is explicit
* \[ ] Weak/no-signal paths work
* \[ ] Scout output is operator-reviewable

\---

# Phase 8 -- Signal Review Dashboard

**Mode:** \[PLAN] then \[STEP] \[DASH]

## Purpose

Make scout outputs reviewable by the operator.

## Plan Mode focus

* review page
* review index/state loader
* packet detail layout
* conflict callout
* health warnings
* empty/partial states

## Step-by-step checklist

* \[ ] Build signal review index loader
* \[ ] Build `/fade-signals`
* \[ ] Show signal classes
* \[ ] Show source breakdown
* \[ ] Show evidence links
* \[ ] Show conflict state
* \[ ] Show contra summary
* \[ ] Show freshness
* \[ ] Show triage state
* \[ ] Build minimal `/fade-health`
* \[ ] Add stale-source warning display
* \[ ] Add invalid-packet warning display

## Deliverables

* \[ ] operator-reviewable signal page
* \[ ] minimal health page

## Proof gate \[PROOF]

* \[ ] Operator can review signal packets cleanly
* \[ ] Dashboard shows actual packet truth
* \[ ] No fake analytics

\---

# Phase 9 -- Research Handoff + Downstream Analyst Layer

**Mode:** \[PLAN] then \[STEP]

## Purpose

Connect strong signals to research brief and risk gate.

## Plan Mode focus

* signal ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ research handoff
* reuse of existing brief/risk-gate work
* linkage fields
* file/path migration if needed
* dashboard consequences

## Step-by-step checklist

* \[ ] Define research handoff packet
* \[ ] Link signal packet ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ brief trigger
* \[ ] Link brief ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ risk gate trigger
* \[ ] Link signal packet IDs through downstream artifacts
* \[ ] Reposition existing brief/risk-gate logic as downstream analyst layer
* \[ ] Validate linkage from signal packet to downstream outputs
* \[ ] Build `/fade-research`
* \[ ] Show brief + risk gate linked to selected signal

## Deliverables

* \[ ] one linked signal ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ brief ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ risk gate path
* \[ ] research review surface

## Proof gate \[PROOF]

* \[ ] One signal packet successfully flows into downstream review
* \[ ] No orphaned brief/risk outputs
* \[ ] Research is clearly downstream

\---

# Phase 10 -- Paper Trade Engine

**Mode:** \[PLAN] then \[STEP]

## Purpose

Start simulated execution.

## Plan Mode focus

* trade candidate contract
* entry/exit assumptions
* fill rules
* position lifecycle
* P\&L accounting
* portfolio snapshots
* safety limits

## Step-by-step checklist

* \[ ] Define trade candidate packet
* \[ ] Define entry rule structure
* \[ ] Define stop/invalidation rule
* \[ ] Define target rule
* \[ ] Define time-stop rule
* \[ ] Implement paper trade open logic
* \[ ] Implement paper trade close logic
* \[ ] Implement spread model
* \[ ] Implement slippage model
* \[ ] Implement fee model
* \[ ] Implement overnight gap rule
* \[ ] Implement stale-quote behavior
* \[ ] Implement position tracker
* \[ ] Implement portfolio snapshot writer
* \[ ] Implement paper-trade hard limits
* \[ ] Link every trade back to signal packet + brief/risk artifacts

## Deliverables

* \[ ] paper trade records
* \[ ] open/closed position tracking
* \[ ] reliable P\&L logic

## Proof gate \[PROOF]

* \[ ] First paper trade lifecycle is reproducible
* \[ ] P\&L is believable under explicit simulation assumptions
* \[ ] No trade exists without upstream linkage

\---

# Phase 11 -- Daily Summary and Operator Review Loop

**Mode:** \[PLAN] then \[STEP] \[DASH]

## Purpose

Create the daily review surface the operator wants.

## Plan Mode focus

* summary schema
* daily aggregation logic
* dashboard view
* plain-English summary
* autonomy metrics later if relevant

## Step-by-step checklist

* \[ ] Define daily summary schema
* \[ ] Compute starting balance
* \[ ] Compute ending balance
* \[ ] Compute realized/unrealized P\&L
* \[ ] Compute daily/cumulative P\&L
* \[ ] Count opened/closed trades
* \[ ] Count winners/losers
* \[ ] Count signals by class
* \[ ] Count conflicts
* \[ ] Compute lane contribution summary
* \[ ] Generate markdown summary
* \[ ] Generate JSON summary
* \[ ] Build `/fade-daily-summary`
* \[ ] Make positive/negative day obvious
* \[ ] Add plain-English operator summary block

## Deliverables

* \[ ] daily summary artifacts
* \[ ] daily summary page

## Proof gate \[PROOF]

* \[ ] One full day can be summarized from artifacts alone
* \[ ] End-of-day balance is obvious
* \[ ] Operator can see what traded and why

\---

# Phase 12 -- Learning / Calibration

**Mode:** \[PLAN] then \[STEP]

## Purpose

Start learning without losing control.

## Plan Mode focus

* learning report contract
* hit-rate analysis
* false-positive analysis
* conflict usefulness
* half-life logic
* synthetic feedback role
* sandbox boundaries

## Step-by-step checklist

* \[ ] Define learning report schema
* \[ ] Compute lane hit rates
* \[ ] Compute conflict usefulness
* \[ ] Compute false-positive patterns
* \[ ] Compute regime-segmented results
* \[ ] Add half-life tracking
* \[ ] Add look-ahead bias protections
* \[ ] Implement synthetic LLM feedback as heuristic-only
* \[ ] Implement calibration suggestion output
* \[ ] Require explicit approval for non-final-stage changes
* \[ ] Log every recommended change

## Deliverables

* \[ ] learning reports
* \[ ] policy-calibration suggestions
* \[ ] approval workflow for changes

## Proof gate \[PROOF]

* \[ ] System can explain which lanes help or hurt
* \[ ] Learning does not silently mutate policy
* \[ ] Real outcomes outrank synthetic feedback

\---

# Phase 13 -- Hardening / Replay / Health

**Mode:** \[PLAN] then \[STEP]

## Purpose

Make the system stable enough for longer paper operation.

## Plan Mode focus

* replay pack
* regression coverage
* outage handling
* health checks
* heartbeat monitoring
* failure artifact policy

## Step-by-step checklist

* \[ ] Build replay cases
* \[ ] Build expected-output checks
* \[ ] Add stale-data alarms
* \[ ] Add malformed-event alarms
* \[ ] Add source outage handling
* \[ ] Add signal packet validation regression tests
* \[ ] Add paper-trade regression tests
* \[ ] Add daily summary validation checks
* \[ ] Implement Alpha/Beta scout heartbeat monitoring
* \[ ] Implement failover event recording
* \[ ] Surface health state in `/fade-health`

## Deliverables

* \[ ] replay/test pack
* \[ ] health artifacts
* \[ ] failover monitoring
* \[ ] stronger operational trust

## Proof gate \[PROOF]

* \[ ] Replay runs are reproducible
* \[ ] Engine failover works in test
* \[ ] Major failure states surface cleanly

\---

# Phase 14 -- Autonomous Transition

**Mode:** \[PLAN] then \[STEP]

## Purpose

Transition from fully human-gated paper operation into bounded policy-driven autonomy.

## Plan Mode focus

* Policy Agent / MAB Router
* autonomy thresholds
* Safety Governor interaction
* shadow-lane rules
* Ghost Lane control group
* sandboxed autonomous calibration
* autonomy metrics

## Step-by-step checklist

* \[ ] Deploy MAB Policy Agent for auto-routing
* \[ ] Define route-selection thresholds
* \[ ] Validate routing against historical performance
* \[ ] Activate Virtual / Shadow Lane redundancy
* \[ ] Cap shadow-lane certainty
* \[ ] Implement Ghost Lane registry
* \[ ] Implement autonomous policy calibration sandbox
* \[ ] Ensure Safety Governor overrides routing
* \[ ] Ensure Heartbeat Monitor can fail over Alpha ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Beta
* \[ ] Add autonomy metrics to daily summary/dashboard
* \[ ] Force manual fallback when safety gates fire

## Deliverables

* \[ ] bounded autonomous routing
* \[ ] resilience controls
* \[ ] autonomy metrics
* \[ ] control-group analysis artifacts

## Proof gate \[PROOF]

* \[ ] Policy routing works in bounded mode
* \[ ] Safety Governor wins over autonomy
* \[ ] Shadow lanes do not fake primary confidence
* \[ ] Autonomy is measurable, not vague

\---

# Phase 15 -- Live-Readiness Review

**Mode:** \[PLAN] then \[STEP]

## Purpose

Decide whether the system deserves tiny live trading permission.

## Plan Mode focus

* review artifact set
* threshold validation
* safety-governor checks
* kill-switch requirements
* operator override path
* broker-adapter contract

## Step-by-step checklist

* \[ ] Verify paper-trade count threshold
* \[ ] Verify paper duration threshold
* \[ ] Verify regime coverage threshold
* \[ ] Verify expectancy threshold
* \[ ] Verify drawdown threshold
* \[ ] Verify no recent data-quality failures
* \[ ] Verify learning stability
* \[ ] Define live size limits
* \[ ] Define daily live loss limit
* \[ ] Define kill switch
* \[ ] Define manual override path
* \[ ] Create live-readiness review artifact
* \[ ] Explicit pass/fail review

## Deliverables

* \[ ] live-readiness review report
* \[ ] pass/fail recommendation
* \[ ] blockers list

## Proof gate \[PROOF]

* \[ ] Hard gates are actually met
* \[ ] Operator can reject live pilot even if metrics pass

\---

# Phase 16 -- Tiny Live Pilot

**Mode:** \[PLAN] then \[STEP]

## Purpose

Run the smallest possible real-money proof.

## Plan Mode focus

* broker adapter
* tiny-size rules
* manual confirmation
* logging
* paper vs live comparison
* abort conditions

## Step-by-step checklist

* \[ ] Connect one broker in safe/sandbox-first manner
* \[ ] Keep max single position tiny
* \[ ] Keep max total exposure tiny
* \[ ] Require explicit operator confirmation
* \[ ] Log every order/fill
* \[ ] Compare every live trade to paper expectation
* \[ ] Review 30-day pilot
* \[ ] Decide continue / revise / kill

## Deliverables

* \[ ] tiny live trade artifacts
* \[ ] live vs paper comparison reports
* \[ ] pilot review report

## Proof gate \[PROOF]

* \[ ] No uncontrolled behavior
* \[ ] Kill switch works
* \[ ] Operator can stop instantly
* \[ ] No scaling until extended review passes

\---

# 6\. Immediate Start Point

## Start with:

* \[ ] Phase 0
* \[ ] Phase 1
* \[ ] Phase 2
* \[ ] Phase 3
* \[ ] Phase 4
* \[ ] Phase 5
* \[ ] Phase 6
* \[ ] Phase 7

In plain English:

1. lock canon and dependencies
2. define contracts
3. constrain MVP data stack
4. build scanner
5. normalize events
6. score lanes
7. run contra logic
8. fuse and emit real signal packets

## Explicitly do not start with:

* \[ ] paper trading
* \[ ] daily summary
* \[ ] autonomy routing
* \[ ] live readiness
* \[ ] dashboard work beyond signal review

\---

# 7\. Final Summary

This is the locked master build checklist for THE FADE.

Use it to control:

* phase order
* scope discipline
* dashboard timing
* proof gates
* autonomy timing
* overall implementation direction

The build method is locked:

**Plan Mode at tranche start ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Step-by-step execution inside the tranche ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ proof gate ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ docs/dashboard update if needed ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ commit ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ next tranche**

If the process follows this checklist, the system stays:

* bounded
* coherent
* auditable
* phase-disciplined
* resistant to shiny-object drift

\---



# MVP Source Reliability Audit (Phase 2)

**Prompt #:** 192  
**Phase #:** 2  
**Tranche #:** 45  

Updated: 2026-03-31T23:00:00+00:00

## Purpose

This document prepares the **Phase 2 MVP approval gate** for THE FADE scout layer.

It is **not an approval statement**. **No MVP lanes are approved yet.**

**Remaining Phase 2 execution order (Prompt #134):** `future_modules/the_fade/docs/THE_FADE_PHASE2_REMAINING_GATE_PLAN.md`.
**T40 note:** This prompt performs governance/registry truth-closure only; it adds no new lane evidence and does not change approval authority.
**T41 note:** Lane C first bounded bootstrap fixture audit is now executed as THE FADE-local policy tracing only (no live market-data integration), and does not change approval authority.
**T42 note:** Lane C second bounded bootstrap fixture audit (FOLLOW conflict-mismatch trace) is THE FADE-local only; it does not prove live market-data integration and does not change approval authority.
**T43 note:** Post-T42 Lane C decision stop is a governance lock only (PATH B) to pause further Lane C bootstrap spend for now and return to broader Phase 2 governance; it adds no new lane evidence and does not change approval authority.
**T44 note (Prompt #187):** Post-T43 governance truth-closure aligns `mvp_lane_evidence_registry.json` and control docs to the dual-pause checkpoint (T39A Lane E pause + T43 Lane C pause); it adds no new lane evidence and does not change approval authority.
**T45 decision note (Prompt #191):** Broader Phase 2 decision review — **PATH B** selected; next bounded work is **Lane B** failure-path / stale-outage explicit behavior trace (local fixtures / stored-shape replay only; **no** new network collection). **Definition only** — no tranche execution in Prompt **#191**; no approval change.
**T45 execution note (Prompt #192):** Bounded Lane B failure-path / stale-outage **fixture trace** executed — `tranche45_lane_b_failure_path_stale_outage_trace_audit.{json,md}`. Proves explicit policy mapping labels for four **local** negative-path cases only; **does not** prove production outage behavior or satisfy standard **#4** fully; no approval change.

## Authority

- Approval gate authority (binding): `future_modules/the_fade/config/mvp_lane_approval.json`
- This doc describes candidates and the approval standard the operator must use.

## Candidate MVP lanes under review (not approved yet)

The MVP gate covers exactly four lanes in scope for the scout-layer proof:

1. Official / disclosure lane (candidate for Lane B)
2. Market-data lane (candidate for Lane C)
3. Curated public-signal lane (candidate for Lane A)
4. Research Swarm as context-only enrichment (candidate for Lane E)

Provider/API/vendor names are intentionally **not locked** until `mvp_lane_approval.json` is approved (`approved: true`).

## Approval standard (what must be true to promote a candidate to MVP)

A candidate can be promoted to MVP only if all checks pass:

1. **Reliability:** during the pre-audit window, the adapter/source fails rarely enough that the lane is not dominated by outages (measured against `required_reliability_threshold` in the approval gate file).
2. **Freshness discipline:** the lane produces evidence with timestamps that can be marked fresh vs stale using a defined freshness window.
3. **Normalization viability:** raw events from the lane can be normalized into `normalized_signal_event` without silent drops.
4. **Stale/outage behavior is explicit:** when the lane is stale or unavailable, the system can either downgrade confidence or escalate per `escalation_policy.json` without fabricating values.
5. **No domination by context-only enrichment:** Research Swarm context-only reads must not override primary lane truth.

## Status buckets (current)

Use these buckets; none are approved yet:

- Approved for MVP now: none (`mvp_lane_approval.json` has `approved: false`)
- Deferred pending more evidence: none locked
- Not approved: all candidates listed above are pending approval

## Operator action required

1. Fill `mvp_lane_approval.json` with operator-chosen MVP lanes.
2. After operator signoff, re-run this audit to reflect the approved lane set.

## Lane B (`lane_b_official_disclosure`) -- reliability window (evidenced to date)

**Source of truth for counts:** `docs/MVP_LANE_EVIDENCE_LOG.md` and append-only  
`future_modules/the_fade/outputs/lane_b_real_observation/tranche21_fr_slot_runs.jsonl`  
(plus `future_modules/the_fade/scripts/run_tranche21_fr_slot.py` for collector semantics).

**Summary (Tranche 30 reconciliation):** Historical **Tranche 16** mixed-host session remains **not** a valid **0.8** statistic. **Tranche 22-23:** **2** counted FR attempts. **Tranche 24** interim pilot: **8** counted / **8** successes / **0** failures (**not** the full pre-audit window). **Full Tranche 21 Federal Register window (on disk):** **22** **counted** full-window records matching `window_start_utc=2026-03-27T16:00:00Z` and `window_end_utc=2026-03-29T16:00:00Z`; **22** successes; **0** failures; all **22** **timing-valid** for counted-slot use. **One** separate line (`task_id` **`t30_valid_002`**) is **out-of-window smoke** — **excluded** from the **22**-slot tally. **Honest 0.8 comparison:** `counted_attempts >= 20` is **met** for **this full-window slice only**, so **`reliability = successes / counted_attempts`** may be **stated** (**22/22** on observed outcomes) **without** claiming pass/fail of the **whole MVP gate**. **This is not approval** — `mvp_lane_approval.json` remains **`approved: false`**, **`approved_mvp_lanes: []`** until changed there. **Phase 3** remains **blocked**. Other gate dimensions stay **partial** unless separately evidenced.

## Lane B -- provider / source class (Tranche 19)

**Source of truth:** `docs/MVP_LANE_EVIDENCE_LOG.md` → **Lane B provider / source path (Tranche 19)**.

**Key points:** `mvp_lane_approval.json` does **not** lock a disclosure provider (`TBD_OFFICIAL_DISCLOSURE_PROVIDER`). Tranche 16 mixed **Federal Register API**, **SEC/sec.gov**, and **issuer IR** -- **not** one provider path. **Do not** treat mixed URLs as a single reliability statistic.

**Next bounded reliability work (when run):** **one** source class per pass -- **provisional** recommendation: **U.S. Federal Register public API** only for that pass (see log for rationale). **SEC/issuer** disclosure is a **different** class and requires its own pass and declared traffic if used.

## Lane B single-source reliability slice (Tranche 20 -- Prompt #63)

This tranche documents **single provider / source-class** reliability evidence only (no SEC URLs, no issuer IR URLs, no mixed provider tally).

- Source class: **U.S. Federal Register public API**
- Exact endpoint repeated:
  - `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest`
- Countable `observe` attempts documented in the evidence log:
  - **5 attempts** (`t20_fb_001`-`t20_fb_005`)
  - **Successes:** 5 (`event_id` emitted; `lag_class: fresh`)
  - **Failures:** 0 (`scout_failure` not emitted in this pass)

Comparison to `required_reliability_threshold` (0.8):
- **Not honestly justified yet**: this pass does **not** evidence a **calendar pre-audit window** or comparable adapter/source draws as required by the gate standard. Reliability remains **partial / conservative** for approval purposes.

## Lane B pre-audit reliability window protocol (Tranche 21 -- Prompt #65)

**Scope:** Lane B reliability dimension only; **single** source-class discipline.

**Locked source class for this protocol:** U.S. Federal Register public API only.

**Exact endpoint family allowed (use this exact URL each attempt):**
`https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest`

### Window length (UTC, strict)
- **Window length:** exactly **48 hours**
- **Window start (`window_start_utc`):** the operator records the **ISO8601 UTC timestamp** when the **first** `observe` attempt of the window starts.
- **Window end (`window_end_utc`):** `window_start_utc + 48h`

### Attempt cadence (UTC, strict)
- **Attempt cadence:** exactly **1 attempt every 2 hours**
- **Attempt schedule:** attempt `i` is executed at `window_start_utc + (i * 2h)` for `i = 0..23`
- **Inclusion rule:** only attempts that complete and produce a valid tool JSON object on stdout are **counted**. If the local run fails (tool crash / no JSON), that attempt is **not** counted and must be re-run before `window_end_utc` (so the operator can still reach the minimum counted-attempt requirement below).

### Success vs failure counting rule (what is counted)
Count based on the **tool outcome class** returned by `lane_b_real_observation_slice.py observe`:
- **Success:** the attempt returns a `normalized_signal_event` (i.e. no `scout_failure` object).
- **Failure:** the attempt returns a `scout_failure` (this includes timeout, TLS/DNS failures, HTTP `>= 400`, empty body, and any other fetch/normalization failure as encoded by the script).

### Handling timeouts, HTTP errors, malformed responses
Use the tool's encoded outcome class:
- Any timeout / TLS / DNS / HTTP `>= 400` / empty body / fetch exception that results in `scout_failure` counts as **failure**.
- If the tool emits malformed/unparseable output (no valid JSON), that attempt is **not counted** (treated as operator execution invalid) and should be re-run within the window.

### What "honest comparison to 0.8" requires
- **Minimum counted attempts required:** at least **20** counted attempts (successes + failures) from the window schedule.
- **Reliability metric used for the comparison:** `reliability = successes / counted_attempts`
- **Comparison is allowed only if** `counted_attempts >= 20`. Otherwise, do **not** compute or claim pass/fail vs `required_reliability_threshold` **0.8**.

### Minimum evidence needed before any 0.8 claim
- The operator must record in `docs/MVP_LANE_EVIDENCE_LOG.md`:
  - `window_start_utc`, `window_end_utc`
  - total counted attempts
  - successes vs failures (with task ids or a compact list)

**Approval remains NOT granted** by this protocol definition alone; it only makes future reliability comparisons honest and repeatable.

## Lane B availability-constrained interim pilot (Tranche 24 -- Prompt #73)

**This section amends operator execution planning only.** It does **not** replace, weaken, or satisfy the **Lane B pre-audit reliability window protocol (Tranche 21)** above. The **48-hour UTC window**, **24** attempts on a **2h** grid, and **>= 20** counted attempts before any **0.8** comparison remain the **stricter target standard** for a **full** pre-audit gate window.

**Reclassification (honest):** Real operator availability **cannot** complete the original Tranche 21 schedule. The work **continues** as an **availability-constrained interim reliability pilot** (lane B, Federal Register API **only**, same exact endpoint as Tranche 21). This pilot is **for deciding whether continued testing is worth doing** -- **not** for MVP gate proof.

**Source class (unchanged):** U.S. Federal Register public API only -- exact URL:
`https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest`

### Historical counted attempts (original UTC schedule -- Tranche 22-23)

Already executed and logged: **`t22_fr_000`**, **`t22_fr_001`** -- **2** counted attempts, **2** successes, **0** failures (see `docs/MVP_LANE_EVIDENCE_LOG.md`).

### Interim pilot -- live results (Tranche 24)

| Metric | Value (after Prompt **#88**) |
|--------|------------------------------|
| Pilot slots completed | **6** / **6** (8:13:55 PM, 6:13:55 AM, 8:13:55 AM, 10:13:55 AM, 12:13:55 PM, 2:13:55 PM CDT slots) |
| Latest `task_id` | **`t24_fr_pilot_06`** |
| Cumulative counted (Tranche **22-23** + pilot) | **8** |
| Successes / failures | **8** / **0** |

Detail: `docs/MVP_LANE_EVIDENCE_LOG.md` -> **Pilot slot 6 (Prompt #88)**.

### Revised pilot execution plan (CDT) -- remaining slots

| Pilot slot | Local time (CDT) |
|------------|------------------|
| Tonight (evening) | **8:13:55 PM** CDT -- **executed** (Prompt **#75**, `t24_fr_pilot_01`) |
| Tomorrow | **6:13:55 AM** CDT -- **executed** (Prompt **#78**, `t24_fr_pilot_02`) |
| Tomorrow | **8:13:55 AM** CDT -- **executed** (Prompt **#80**, `t24_fr_pilot_03`) |
| Tomorrow | **10:13:55 AM** CDT -- **executed** (Prompt **#82**, `t24_fr_pilot_04`) |
| Tomorrow | **12:13:55 PM** CDT -- **executed** (Prompt **#86**, `t24_fr_pilot_05`) |
| Tomorrow | **2:13:55 PM** CDT -- **executed** (Prompt **#88**, `t24_fr_pilot_06`) |

### What this pilot can and cannot prove

- **Maximum counted attempts (if every pilot slot is executed and counts):** **2** (Tranche **22-23**) **+ 6** (pilot schedule) **= 8** total -- **8** counted so far (**6** pilot slots done; interim pilot complete).
- **Tranche 25 closeout:** interim pilot is complete and provided a **positive interim success-path signal** for the locked Federal Register API source class, but it **did NOT** satisfy the original **Tranche 21 gate protocol** and therefore **does not** justify any **approval re-evaluation** (**approval remains false**).
- **Does NOT justify** comparison to the original **`required_reliability_threshold` 0.8** gate statistic **from the pilot slice alone** (pilot **cannot** reach **>= 20** counted attempts; it is **not** the full pre-audit protocol).
- **Tranche 30:** A **separate** **full-window** run produced **22** counted / **22** successes / **0** failures on disk — see **Lane B** summary at top of this file; **still not** MVP approval.
- **Does NOT** (by itself) satisfy **non-reliability** MVP dimensions.
- **May** inform a **go / no-go** on whether to schedule a **future** full-protocol window when availability allows (**historical** once the window ran).

**Source of truth for detail:** `docs/MVP_LANE_EVIDENCE_LOG.md` -> **Lane B availability-constrained interim pilot (Tranche 24 -- Prompt #73)**.

**Approval remains NOT granted.**

## Lane B post-pilot go/no-go (Tranche 26) -- updated after full window on disk

- **Park:** lane B stays **promising-but-unapproved** (`mvp_lane_approval.json` remains `approved: false`) until operator updates that file.
- **Execution status:** The **full Tranche 21** Federal Register reliability window is **complete on disk** (see **Lane B** summary above and **Tranche 30** entries in `MVP_LANE_EVIDENCE_LOG.md`). **Governed markdown** reconciled under Prompt **#102** — **not** an approval flip.
- **Advance (checkpoint):** Operator **full-dimension gate review** completed (Prompt **#113** lock). **Tranche 31** and **Tranche 32** Lane B FR **freshness** passes **executed** (see below). Further Phase **2** dimensions (normalization, stale/outage **system** behavior, etc.) — **governed prompts only**. Edits to **`mvp_lane_approval.json`** only if justified later — **not** Phase 3 until the gate says so.

## Gate-decision alignment note (Tranche 30 -- Prompt #103)

- **Current-review-now only:** apply critic/adversarial review, audit-before-trust, and risk-first scrutiny against over-reading the FR full-window slice.
- **Future guardrails only (not active build scope):** auth primitives and permission layers, isolated sub-account/restricted permissions, MCP-first infra filter with anti-affiliate rule, sim-first/dry-run-first bridge, and position sizing/drawdown controls.
- **Parking lot only (not authorized now):** any critic-agent implementation, MCP tooling implementation, exchange/live execution integration, or execution-adjacent build work.
- **State unchanged:** this triage does not change approval authority; `mvp_lane_approval.json` remains `approved: false`, and **Phase 3 remains blocked**.
- **Final signoff lock (Prompt #113):** final operator review confirms the same outcome: FR full-window slice is strong (**22/22/0**, `t30_valid_002` excluded), but whole-gate closure is still not justified; approval remains false.

## Planned next bounded tranche — Lane B freshness discipline (Tranche 31 -- Prompt #117)

- **Purpose:** Close the **freshness** gap for the same Lane B Federal Register slice that already supports an honest **reliability** tally — by **writing down** an operator-approved freshness window and showing how each **full-window** observation classifies (**fresh vs stale**) against it, using fields already present in `tranche21_fr_slot_runs.jsonl` (and per-run snapshots as needed).
- **Evidence question:** Under the declared rule, are all **22** gate-relevant full-window slots **fresh**? If any are **stale** or **borderline**, is that documented honestly (no silent upgrade)?
- **Likely touch points (when executed):** `docs/MVP_LANE_EVIDENCE_LOG.md`, this file, `THE_FADE_PROCESS_CHECKLIST.md`, `THE_FADE_CONTEXT_ANCHOR.md`, `THE_FADE_HANDOFF_BUNDLE_LATEST.md`, append-only JSONL / snapshots (read-only classification); optional small helper script in a **later** governed prompt — **not** part of Prompt **#117**.
- **Success:** Written freshness window definition + per-slot classification table (or equivalent) for the **22** lines + explicit notes on edge cases; conservative language if the rule strains on any row.
- **Not success:** Claiming MVP approval, whole-gate closure, production stale/outage **system** behavior, normalization completeness, or conflict/context-dominance proof from this tranche alone.
- **Stop when:** Window is defined, classification is applied to all **22** rows, and docs are updated — or an honest **blocker** is recorded (e.g., ambiguous timestamps) without fabricating freshness.
- **Still would not prove:** Stale/outage **escalation/downgrade paths** at scale; forced outage statistics; other source classes (SEC/issuer); Phase 3 readiness.

## Tranche 31 execution outcome — Lane B Federal Register freshness (Prompt #121)

- **Executed:** Yes — bounded classification on **22** full-window JSONL lines (**`t30_valid_002`** excluded). Snapshots: `future_modules/the_fade/outputs/lane_b_real_observation/run_*_tranche21_fr_slot_snapshot.json`; log: `tranche21_fr_slot_runs.jsonl`.
- **Rule (summary):** `T_obs = actual_started_at_utc`; `publication_date` from **`results[0]`** in snapshot `response_preview_utf8`; `T_pub` = that date at **00:00 UTC**; `Δ = T_obs − T_pub`; **fresh** if `0 ≤ Δ ≤ 48h`; **stale** if `Δ > 48h`; **cannot classify** if `Δ < 0` (advance listing vs date-only field). Detail: `MVP_LANE_EVIDENCE_LOG.md` → **Tranche 31 freshness** section.
- **Counts:** **12** fresh, **0** stale, **10** cannot classify honestly.
- **Does not satisfy** the full MVP approval standard by itself — mixed outcome; **no** production stale/outage system proof; **`mvp_lane_approval.json`** unchanged (**`approved: false`**); **Phase 3** still **blocked**.

## Tranche 32 execution outcome — freshness ambiguity resolution (Prompt #129)

- **Executed:** Yes — **10**-row cohort (`t21_fr_full_20260328T160000Z` … `t21_fr_full_20260329T100000Z`). **Evidence:** per-run snapshots (`response_preview_utf8` / parseable **`results[0]`**) **+** one bounded GET `https://www.federalregister.gov/api/v1/documents/2026-06133.json`. Optional helper: `future_modules/the_fade/scripts/_tranche32_ambiguity_review.py`.
- **Per-row outcome (strict Tranche 31 buckets):** **still cannot classify honestly** — **all 10**. Document API confirms **`publication_date`** / **`effective_on`** but **no** finer publication instant for the midnight-UTC **`Δ`** model; **`signing_date`:** **`null`** in fetched JSON.
- **Tranche-level totals (unchanged):** **12** fresh, **0** stale, **10** still cannot classify honestly (**22** full-window rows; **`t30_valid_002`** excluded).
- **Explicit limitation:** Honest **binary** fresh/stale under the Tranche **31** rule **without** additional **advance / public-inspection** operator policy — **not** established here.
- **Does not prove:** Normalization breadth; production stale/outage **system** behavior; Phase **3** readiness; MVP approval. **`mvp_lane_approval.json`** unchanged (**`approved: false`**).

## Tranche 33 — Lane B freshness policy decision (Prompt #132)

- **Decision:** **`ADOPT_ONE_POLICY`** — **`strict_midnight_utc`** is the **operator-facing** Phase **2** Lane B freshness interpretation for **binary** scoring (same rule as Tranche **31**). **Machine-readable:** `future_modules/the_fade/config/lane_b_phase2_freshness_policy_decision.json`.
- **Not adopted as primary:** **`publication_day_fresh`**, **`publication_end_of_day_utc`** (both yield **22/22 fresh** on this window — **overstates** freshness vs Tranche **32** limitation); **`advance_listing_bucket`** — descriptive only, not primary gate verdict.
- **Counts under adopted policy:** **12** fresh, **0** stale, **10** **cannot classify honestly** (**22** rows; **`t30_valid_002`** excluded).
- **Park:** **Freshness-only** Phase **2** tranche workstream **parked** unless governance or evidence **sources** change.
- **Does not prove:** MVP approval; whole-gate closure; Phase **3** readiness.

## Tranche 34 — Lane B normalization breadth audit (Prompt #133)

- **Executed:** Yes — `future_modules/the_fade/scripts/audit_lane_b_normalization_breadth.py`; output `outputs/lane_b_real_observation/tranche34_normalization_breadth_audit.json` (+ `.md`). **No** network.
- **Population:** **22** full-window JSONL lines (**`t30_valid_002`** excluded). Field set grounded in `run_tranche21_fr_slot.py` contracts + **`results[0]`** use in **`response_preview_utf8`**.
- **Findings:** JSONL + snapshot shell fields **complete**; **`response_sha256`** present; **full** `json.loads` of **`response_preview_utf8`:** **0**/**22** (truncated previews); regex **`document_number`** in **`results[0]`** region: **22**/**22**; **3** distinct **`document_number`** values in-window.
- **Verdict:** **Solid** for **collector** identity/timing/outcome + **checksum**; **partial** for **rich** structured normalization from stored snapshots alone — **not** normalization breadth **closed**; **not** MVP approval; **not** Phase **3**.



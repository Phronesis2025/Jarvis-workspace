# MVP Source Reliability Audit (Phase 2)

**Prompt #:** 82  
**Phase #:** 2  
**Tranche #:** 24  

Updated: 2026-03-26T10:37:35.2097793-05:00

## Purpose

This document prepares the **Phase 2 MVP approval gate** for THE FADE scout layer.

It is **not an approval statement**. **No MVP lanes are approved yet.**

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

**Source of truth for counts:** `docs/MVP_LANE_EVIDENCE_LOG.md` (Tranche 18 micro-sample; Tranche 20 single-source slice; Tranche **22-23** original UTC grid attempts; Tranche **24** interim pilot schedule and ceilings).

**Summary:** Historical **Tranche 16** session: **four** HTTPS tries (**one** HTTP 200, **three** HTTP 403 across URL classes) -- **not** a valid **0.8** statistic. **Tranche 22-23** executed **two** counted attempts (`t22_fr_000`, `t22_fr_001`) under the **original** Tranche 21 UTC schedule (Federal Register API only). **Tranche 24** includes an **availability-constrained interim reliability pilot** (**not** the full 48h / 24-attempt / **>=20**-count pre-audit gate window; **stricter Tranche 21 protocol** preserved above). **Prompt #82** executed **pilot slot 4** (`t24_fr_pilot_04`) -- cumulative **6** counted / **6** successes / **0** failures for this Federal Register window+pilot slice. **No** honest comparison to **`required_reliability_threshold` 0.8** from this pilot. Reliability remains **partial / conservative** for gate purposes.

## Lane B -- provider / source class (Tranche 19)

**Source of truth:** `docs/MVP_LANE_EVIDENCE_LOG.md` Ã¢â€ â€™ **Lane B provider / source path (Tranche 19)**.

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

| Metric | Value (after Prompt **#82**) |
|--------|------------------------------|
| Pilot slots completed | **4** / **6** (8:13:55 PM, 6:13:55 AM, 8:13:55 AM, 10:13:55 AM CDT slots) |
| Latest `task_id` | **`t24_fr_pilot_04`** |
| Cumulative counted (Tranche **22-23** + pilot) | **6** |
| Successes / failures | **6** / **0** |

Detail: `docs/MVP_LANE_EVIDENCE_LOG.md` -> **Pilot slot 4 (Prompt #82)**.

### Revised pilot execution plan (CDT) -- remaining slots

| Pilot slot | Local time (CDT) |
|------------|------------------|
| Tonight (evening) | **8:13:55 PM** CDT -- **executed** (Prompt **#75**, `t24_fr_pilot_01`) |
| Tomorrow | **6:13:55 AM** CDT -- **executed** (Prompt **#78**, `t24_fr_pilot_02`) |
| Tomorrow | **8:13:55 AM** CDT -- **executed** (Prompt **#80**, `t24_fr_pilot_03`) |
| Tomorrow | **10:13:55 AM** CDT -- **executed** (Prompt **#82**, `t24_fr_pilot_04`) |
| Tomorrow | **12:13:55 PM** CDT |
| Tomorrow | **2:13:55 PM** CDT |

### What this pilot can and cannot prove

- **Maximum counted attempts (if every pilot slot is executed and counts):** **2** (Tranche **22-23**) **+ 6** (pilot schedule) **= 8** total -- **6** counted so far (**4** pilot slots done).
- **Does NOT justify** comparison to the original **`required_reliability_threshold` 0.8** gate statistic (pilot **cannot** reach **>= 20** counted attempts; it is **not** the full pre-audit protocol).
- **Does NOT** satisfy the Tranche 21 pre-audit window completion criteria.
- **May** inform a **go / no-go** on whether to schedule a **future** full-protocol window when availability allows.

**Source of truth for detail:** `docs/MVP_LANE_EVIDENCE_LOG.md` -> **Lane B availability-constrained interim pilot (Tranche 24 -- Prompt #73)**.

**Approval remains NOT granted.**



# MVP Source Reliability Audit (Phase 2)

**Prompt #:** 67  
**Phase #:** 2  
**Tranche #:** 22  

Updated: 2026-03-25T16:14:11.7508065-05:00

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

## Lane B (`lane_b_official_disclosure`) — reliability window (evidenced to date)

**Source of truth for counts:** `docs/MVP_LANE_EVIDENCE_LOG.md` (Tranche 18 micro-sample; Tranche 20 single-source slice; **Tranche 22 live pre-audit window**).

**Summary:** Historical **Tranche 16** session: **four** HTTPS tries (**one** HTTP 200, **three** HTTP 403 across URL classes) — **not** a valid **0.8** statistic. **Tranche 22 (Prompt #67)** started a **defined calendar pre-audit window** (Federal Register API only; see **Lane B pre-audit window — live status** below); **only attempt 0** is executed so far — **no** honest comparison to **`required_reliability_threshold` 0.8** until **≥20** counted attempts. Reliability remains **partial / conservative** for gate purposes.

## Lane B — provider / source class (Tranche 19)

**Source of truth:** `docs/MVP_LANE_EVIDENCE_LOG.md` → **Lane B provider / source path (Tranche 19)**.

**Key points:** `mvp_lane_approval.json` does **not** lock a disclosure provider (`TBD_OFFICIAL_DISCLOSURE_PROVIDER`). Tranche 16 mixed **Federal Register API**, **SEC/sec.gov**, and **issuer IR** — **not** one provider path. **Do not** treat mixed URLs as a single reliability statistic.

**Next bounded reliability work (when run):** **one** source class per pass — **provisional** recommendation: **U.S. Federal Register public API** only for that pass (see log for rationale). **SEC/issuer** disclosure is a **different** class and requires its own pass and declared traffic if used.

## Lane B single-source reliability slice (Tranche 20 — Prompt #63)

This tranche documents **single provider / source-class** reliability evidence only (no SEC URLs, no issuer IR URLs, no mixed provider tally).

- Source class: **U.S. Federal Register public API**
- Exact endpoint repeated:
  - `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest`
- Countable `observe` attempts documented in the evidence log:
  - **5 attempts** (`t20_fb_001`–`t20_fb_005`)
  - **Successes:** 5 (`event_id` emitted; `lag_class: fresh`)
  - **Failures:** 0 (`scout_failure` not emitted in this pass)

Comparison to `required_reliability_threshold` (0.8):
- **Not honestly justified yet**: this pass does **not** evidence a **calendar pre-audit window** or comparable adapter/source draws as required by the gate standard. Reliability remains **partial / conservative** for approval purposes.

## Lane B pre-audit reliability window protocol (Tranche 21 — Prompt #65)

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
Use the tool’s encoded outcome class:
- Any timeout / TLS / DNS / HTTP `>= 400` / empty body / fetch exception that results in `scout_failure` counts as **failure**.
- If the tool emits malformed/unparseable output (no valid JSON), that attempt is **not counted** (treated as operator execution invalid) and should be re-run within the window.

### What “honest comparison to 0.8” requires
- **Minimum counted attempts required:** at least **20** counted attempts (successes + failures) from the window schedule.
- **Reliability metric used for the comparison:** `reliability = successes / counted_attempts`
- **Comparison is allowed only if** `counted_attempts >= 20`. Otherwise, do **not** compute or claim pass/fail vs `required_reliability_threshold` **0.8**.

### Minimum evidence needed before any 0.8 claim
- The operator must record in `docs/MVP_LANE_EVIDENCE_LOG.md`:
  - `window_start_utc`, `window_end_utc`
  - total counted attempts
  - successes vs failures (with task ids or a compact list)

**Approval remains NOT granted** by this protocol definition alone; it only makes future reliability comparisons honest and repeatable.

## Lane B pre-audit window — live status (Tranche 22 — Prompt #67)

**Kickoff only:** This section records that the **first** real calendar window under the Tranche 21 protocol has **started**. It does **not** claim pass/fail vs **0.8**.

**Source class:** U.S. Federal Register public API only — exact URL:
`https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest`

| Field | Value |
|-------|--------|
| `window_start_utc` | `2026-03-25T21:13:55Z` |
| `window_end_utc` | `2026-03-27T21:13:55Z` |
| Scheduled attempts (`i = 0..23`) | **24** (2h cadence) |
| **Executed and counted so far** | **1** — attempt **0** only (`task_id` **`t22_fr_000`**) |
| Attempt 0 outcome | **`normalized_signal_event`** (success; HTTP **200**) |
| Remaining scheduled attempts | **23** — **not** run in this pass (no fabricated results) |

**0.8 comparison:** **Forbidden until** `counted_attempts >= 20` per Tranche 21 rules. Current counted attempts: **1**. **No** reliability ratio vs `required_reliability_threshold` **0.8** may be stated.

**Source of truth for schedule and detail:** `docs/MVP_LANE_EVIDENCE_LOG.md` → **Lane B pre-audit reliability window — live kickoff (Tranche 22)**.

**Approval remains NOT granted.**


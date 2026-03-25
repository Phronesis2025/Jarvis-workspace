# MVP Source Reliability Audit (Phase 2)

**Prompt #:** 63  
**Phase #:** 2  
**Tranche #:** 20  

Updated: 2026-03-25T15:11:26.1862208-05:00

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

**Source of truth for counts:** `docs/MVP_LANE_EVIDENCE_LOG.md` → section **Lane B reliability window evidence (Tranche 18)**.

**Summary:** No **calendar pre-audit window** is defined or executed yet for lane B. The only **countable** real HTTPS `observe` attempts currently in the log are **four** tries in one **2026-03-25** session (**one** HTTP 200 success, **three** HTTP 403 failures across different URL classes). That micro-sample **cannot** be compared honestly to **`required_reliability_threshold` 0.8** — see the log for explicit reasoning. Reliability remains **partial / conservative** for gate purposes until a named window and comparable repeated observations exist.

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


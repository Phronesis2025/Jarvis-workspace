# MVP Source Reliability Audit (Phase 2)

**Prompt #:** 59  
**Phase #:** 2  
**Tranche #:** 18  

Updated: 2026-03-25T14:48:28.8068011-05:00

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


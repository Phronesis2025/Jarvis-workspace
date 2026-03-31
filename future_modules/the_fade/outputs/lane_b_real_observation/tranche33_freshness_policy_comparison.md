# Tranche 33 — Freshness policy comparison (Lane B FR full window)

**Not approval.** This file is a **policy comparator** on stored evidence only. It does **not** select a winning policy, does **not** close the MVP gate, and does **not** unlock Phase 3.

## Population

- **22** JSONL lines matching full window (`2026-03-27T16:00:00Z` … `2026-03-29T16:00:00Z`).
- **`t30_valid_002`** excluded.
- **No network** — script reads JSONL + snapshots only.

## Policies

- **`strict_midnight_utc`:** Same as Tranche 31: T_pub = publication_date at 00:00:00 UTC; fresh if 0<=Δ<=48h; stale if Δ>48h; cannot_classify if Δ<0.
- **`publication_day_fresh`:** If UTC date(obs) <= publication_date -> fresh; if date(obs) > publication_date, compare Δ = T_obs - T_pub(midnight) and stale only if Δ>48h.
- **`advance_listing_bucket`:** If Δ<0 vs publication_date@00:00 UTC -> label advance_listing (explicit bucket); else same 48h fresh/stale as strict.
- **`publication_end_of_day_utc`:** T_pub_end = 23:59:59.999999 UTC on publication_date; if T_obs <= T_pub_end -> fresh; else Δ from T_pub_end, stale if Δ>48h.

## Aggregate counts by policy

| Policy | Counts |
|--------|--------|
| `strict_midnight_utc` | `{"cannot_classify": 10, "fresh": 12}` |
| `publication_day_fresh` | `{"fresh": 22}` |
| `advance_listing_bucket` | `{"advance_listing": 10, "fresh": 12}` |
| `publication_end_of_day_utc` | `{"fresh": 22}` |

## Ambiguous under `strict_midnight_utc` (Δ<0 vs pub midnight)

- `t21_fr_full_20260328T160000Z`
- `t21_fr_full_20260328T180000Z`
- `t21_fr_full_20260328T200000Z`
- `t21_fr_full_20260328T220000Z`
- `t21_fr_full_20260329T000000Z`
- `t21_fr_full_20260329T020000Z`
- `t21_fr_full_20260329T040000Z`
- `t21_fr_full_20260329T060000Z`
- `t21_fr_full_20260329T080000Z`
- `t21_fr_full_20260329T100000Z`

## Per-row matrix

| task_id | strict_midnight_utc | publication_day_fresh | advance_listing_bucket | publication_end_of_day_utc |
|---|---|---|---|---|
| `t21_fr_full_20260327T160000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260327T180000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260327T200000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260327T220000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260328T000000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260328T020000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260328T040000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260328T060000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260328T080000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260328T100000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260328T120000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260328T140000Z` | fresh | fresh | fresh | fresh |
| `t21_fr_full_20260328T160000Z` | cannot_classify | fresh | advance_listing | fresh |
| `t21_fr_full_20260328T180000Z` | cannot_classify | fresh | advance_listing | fresh |
| `t21_fr_full_20260328T200000Z` | cannot_classify | fresh | advance_listing | fresh |
| `t21_fr_full_20260328T220000Z` | cannot_classify | fresh | advance_listing | fresh |
| `t21_fr_full_20260329T000000Z` | cannot_classify | fresh | advance_listing | fresh |
| `t21_fr_full_20260329T020000Z` | cannot_classify | fresh | advance_listing | fresh |
| `t21_fr_full_20260329T040000Z` | cannot_classify | fresh | advance_listing | fresh |
| `t21_fr_full_20260329T060000Z` | cannot_classify | fresh | advance_listing | fresh |
| `t21_fr_full_20260329T080000Z` | cannot_classify | fresh | advance_listing | fresh |
| `t21_fr_full_20260329T100000Z` | cannot_classify | fresh | advance_listing | fresh |

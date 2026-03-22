# Watchlist Packet Format

Input format for Stock Module v1.

---

## Packet Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| packet_id | Y | string | Unique identifier |
| created_at | Y | string (ISO 8601) | Timestamp |
| symbols | Y | array of strings | Ticker symbols (e.g., AAPL, MSFT) |
| watch_reason | N | string | Why these symbols are being watched |
| time_horizon | N | string | e.g., "short-term", "long-term" |
| risk_tolerance | N | string | e.g., "conservative", "moderate" |
| constraints | N | object | Additional limits or filters |
| notes | N | string | Human-readable context |

---

## Packet Purpose

The watchlist packet tells the module:
- Which symbols to research
- Why they matter (watch reason)
- Any constraints that affect the brief (time horizon, risk tolerance)

---

## Example Input Types

- **Single symbol:** `["AAPL"]`
- **Sector watch:** `["AAPL", "MSFT", "GOOGL"]` with watch_reason "tech earnings season"
- **Thesis-driven:** `["NVDA"]` with watch_reason "AI chip demand thesis"

---

## Constraints

- Symbols must be valid tickers (format validation; no live validation against exchange)
- Max symbols per packet: TBD (suggest 1–10 for v1)
- No broker account IDs, no order parameters, no position data

---

## Required vs Optional

**Required:** packet_id, created_at, symbols

**Optional:** watch_reason, time_horizon, risk_tolerance, constraints, notes

Optional fields improve brief quality but are not mandatory for a valid packet.

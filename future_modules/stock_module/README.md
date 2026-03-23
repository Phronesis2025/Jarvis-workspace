# Stock Module v1

**Status:** prototype; first viable slice proven through brief + risk gate, both visible on `/stock-briefs`. **Last updated:** 2026-03-23 (doc-lock Prompt #115).  
**Location:** `future_modules/stock_module/`

## Purpose

Stock Module v1 is a read-only market research worker. It produces bounded research briefs from ticker/watchlist packets and optional risk-gate reviews on those briefs. **It is not a trading engine** — no orders, no execution, no broker APIs.

## Current proven flow (all manual)

1. **RS intake** — Dashboard `/stock-intake` shows candidate symbols and draft watchlist from Research Swarm outputs (`stock_symbol_review_summary.json`, `draft_watchlist_packet_from_rs.json`).
2. **Confirm one symbol** — `confirm_watchlist_symbol.py --symbol <SYM>` reads the RS draft, writes a one-symbol packet under `inputs/` (proven: AAPL).
3. **Run pipeline wrapper (brief + risk gate)** — `run_pipeline.py --packet ../inputs/confirmed_watchlist_packet_aapl.json` runs `run_research_brief.py` then `run_risk_gate.py` on the produced brief (still one symbol). Outputs: `outputs/stock_research_brief_<stem>.json` and paired `outputs/risk_gate_review_<matching_suffix>.json`.
4. **Review on dashboard** — `/stock-briefs` shows the **latest** research brief (by file mtime) and the **paired** risk-gate file when it exists (`risk_gate_review_<same_suffix>.json` as `run_risk_gate.py` names it). Plain-English text for pass / caution / flag; missing risk-gate state tells the operator to run `run_risk_gate.py`. **Manual-review-only** messaging on the page.

One symbol per brief run. Operator approves each step.

## Key scripts

- `scripts/confirm_watchlist_symbol.py` — RS draft → one-symbol packet  
- `scripts/run_research_brief.py` — One-symbol packet → research brief JSON  
- `scripts/run_risk_gate.py` — Research brief JSON → risk gate review JSON  
- `scripts/run_pipeline.py` — Thin orchestrator: brief then risk gate  

## Proof artifacts (example path)

- `inputs/confirmed_watchlist_packet_aapl.json`  
- `outputs/stock_research_brief_confirmed_watchlist_packet_aapl.json`  
- `outputs/risk_gate_review_confirmed_watchlist_packet_aapl.json`  

## Dashboard routes

- `/stock-intake` — RS → Stock intake (symbols table, draft watchlist, next-step hints)  
- `/stock-briefs` — Latest brief + matching risk-gate review (or guidance if the paired risk file is missing); not a trading UI  

## Current scope

- **Read-only** — Packets and files in/out; no live market feed  
- **No execution** — Nothing on the dashboard or in these scripts places trades  
- **Pipeline wrapper** — `run_pipeline.py` is a thin manual chain; still manual-review-only, one symbol per run  
- **No history/switcher** — Only the latest brief by mtime; pairing is by filename suffix, not `report_id`  

## What it does not do

- No batching across symbols in one brief run  
- No automation of operator decisions  
- No real-time prices or guaranteed data freshness  

## Operating stance

- **Packet-first** — Watchlist in, brief (+ optional gate file) out  
- **Evidence-backed** — Brief expects cited sources in normal runs  
- **Human review** — Brief and risk gate are advisory flags for a person  

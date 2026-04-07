# THE FADE — T84 first Phase 3 implementation slice (governance lock)

**Prompt #:** 346  
**Phase #:** 3 — **implementation governance** (this tranche is **docs only**; **no** code)  
**Tranche #:** 84  
**Label:** `THE_FADE_PHASE3_T84_FIRST_IMPLEMENTATION_GOVERNANCE_LOCK`  

**Updated:** 2026-04-07T14:00:00+00:00  

---

## Purpose

**T83** named **one** candidate first implementation slice: **static Phase 3 universe-scanner I/O contract artifacts only** (`THE_FADE_PHASE3_ENTRY_PLAN_T83.md` §2). **T84** converts that planning candidate into a **governed implementation boundary** so a **single future build tranche** may add **only** those static artifacts — **nothing else**.

**T84 does not implement anything**, does not reopen lanes, does not authorize broader Phase 3 (runtime, dashboard, providers, production), and does not change **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`**, or **`lane_posture_policy`**. **Scoped MVP approval (T80)** remains binding and **not** production maturity.

**Companion:** `THE_FADE_T84_FIRST_IMPLEMENTATION_SLICE_ACCEPTANCE_CRITERIA.md` (success / failure / scope violation).  
**Machine-readable note:** `phase2_mvp_approval_scope_decision.json` → **`post_t84_first_implementation_slice_governance`**.

---

## 1. First implementation slice — exact definition

**Governed slice name:** **Phase 3 universe-scanner I/O contract (static only).**

**In scope for exactly one future implementation tranche** (not T84 itself):

- **Static** descriptions of **inputs and outputs** for a **future** universe scanner: shapes, fields, required vs optional, and documented semantics **at the contract layer only**.
- **No** executable scanner loop, **no** orchestration, **no** runtime entrypoints that perform work beyond **import-safe** definition of types/schemas (see §2).
- **No** network I/O, **no** external API clients, **no** scheduled jobs, **no** subprocess calls.
- **No** dashboard UI or backend, **no** production deployment wiring, **no** provider credentials or environment plumbing for live systems.
- **No** edits to **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`**, or lane charters; **no** new evidence collection.

**Recommended filesystem home** (for the future build tranche; T84 does not create it):  
`future_modules/the_fade/contracts/phase3_universe_scanner_io/`  
The future tranche may use this path or a **narrower** subpath under `future_modules/the_fade/` **only if** the governed prompt explicitly allows a path adjustment — **without** widening artifact **types** beyond §2.

---

## 2. Allowed artifact types (future tranche only)

A future tranche implementing this slice may add **only** the following **categories**, all **non-executing** as the primary deliverable:

| Category | Examples (not exhaustive) |
|----------|---------------------------|
| **Schema / spec files** | JSON Schema (`.json`), OpenAPI YAML/JSON **fragment** describing only scanner I/O, AsyncAPI fragment if static |
| **Example payloads** | Static `.json` / `.yaml` examples that **illustrate** valid or invalid shapes; **no** live fetch to populate them |
| **Typed contract stubs** | Language-specific **interface-only** artifacts: e.g. `TypedDict`, `dataclass`, `Protocol`, TypeScript `interface`, or `.pyi` stubs — **provided** they contain **no** runtime I/O, **no** `main`, **no** calls to `requests`/`httpx`/`urllib`/sockets, **no** thread/process schedulers |

**Explicitly allowed supporting text in the same tranche:**

- **Short README or index** under the same directory tree **only** to explain how to read the schemas and examples — **not** a full product spec or multi-phase roadmap.

**Not allowed as “just documentation”:** Markdown or prose used to **smuggle** executable instructions, runbooks for live systems, or dashboard wireframes that imply implementation — keep docs **bounded** to contract readability.

---

## 3. Forbidden in the first implementation tranche (even if “small”)

The following remain **forbidden** in the **first** implementation tranche that claims this slice:

| Forbidden | Rationale |
|-----------|-----------|
| **Executable scanner logic** | Any code path that enumerates a universe, pulls data, or coordinates scans |
| **Scheduled jobs / workers / cron** | Runtime orchestration |
| **Network calls / external APIs** | Including “just one” health check |
| **Dashboard surfaces** | UI, API routes for operators, charts |
| **Production wiring** | Docker/K8s/terraform, prod env files, secrets |
| **Provider credentials / env plumbing** | Including `.env.example` that names live credential keys for MVP lanes |
| **Multi-slice bundling** | Contract **plus** scanner stub **plus** config runner in one tranche |
| **Code outside the contract boundary** | Refactors elsewhere, new Phase 2 collectors, stock-module integration |

Anything above is a **scope violation** (see acceptance criteria doc).

---

## 4. Anti-drift rules

1. **One implementation slice only** — this governed slice is **singular** until a **new** governance tranche defines a **second** slice.
2. **No “while we’re here” extras** — no drive-by fixes, no dependency upgrades bundled for convenience, no new scripts.
3. **No second surface** — no parallel “tiny runtime” or “debug CLI” in the same tranche.
4. **No code outside the contract boundary** — all new files must **clearly** serve **only** static I/O contract definition.

---

## 5. Relationship to prior checkpoints

- **T82** — planning-only permission history and **`phase3_entry_planning_only_definition`** remain **unchanged** in meaning; T83 executed that planning class.
- **T83** — candidate slice is **superseded as governance** by **T84** for **what** the first build tranche may do (T84 is **narrower or equal**, not a roadmap expansion).
- **T80** — scoped MVP approval **does not** authorize anything beyond **this single static slice** for Phase 3 **build**; broader Phase 3 still **blocked** until **future** governance.

---

## 6. Non-claims

- T84 **does not** mean the slice **has been built** — only that the **boundary** for **one** future tranche is **locked on disk**.
- T84 **does not** authorize a **second** implementation tranche without new governance.
- T84 **does not** clear registry partialities or imply Phase 2 evidence is complete.

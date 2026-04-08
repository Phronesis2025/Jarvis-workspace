# THE FADE — T97 local end-to-end happy-path runner (governance lock)

**Prompt #:** 381  
**Phase #:** 3 — **local pipeline governance** (T97 **docs only**; **no** runner code in this tranche)  
**Tranche #:** 97  
**Label:** `THE_FADE_PHASE3_T97_GOVERNANCE_LOCK_LOCAL_END_TO_END_HAPPY_PATH_RUNNER`  

**Updated:** 2026-04-08T11:48:34+00:00  

---

## Purpose

The repo already contains, separately: **T89** Federal Register ingress (**`build_universe_scanner_request_from_federal_register.py`**), **T91** ingress-request offline validator, **T96** mechanical request→result bridge, and **T94** result-packet offline validator. There is **no** single governed script that runs these in **one** explicit **local** **happy-path** sequence with **console-only** reporting.

**T97** governs **exactly one** future implementation tranche that may add **only** a **thin sequential runner** that **invokes** those **existing** tools — **no** new scanner, **no** new ranking/selection, **no** orchestration platform, **no** dashboard/provider expansion.

**T97 does not implement the runner**, does not reopen lanes, and does not edit **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`**, or lane charters. **Scoped MVP (T80)** remains binding.

**Companion:** `THE_FADE_T97_LOCAL_END_TO_END_HAPPY_PATH_RUNNER_ACCEPTANCE_CRITERIA.md`.  
**Machine-readable note:** `phase2_mvp_approval_scope_decision.json` → **`post_t97_local_end_to_end_happy_path_runner_governance`**.

---

## 1. Next implementation slice — exact definition

**Governed slice name:** **Phase 3 — local end-to-end happy-path runner (sequential orchestration of existing bounded tools only).**

**In scope for exactly one future implementation tranche** (not T97 itself):

| Rule | Detail |
|------|--------|
| **Role** | **One** Python script that **subprocess**-invokes (or equivalent **one-shot** `python path/to/tool.py` calls) the **four** existing tools **in fixed order** — **no** in-process reimplementation of ingress, validation, or bridge logic. |
| **Sequence** | **(1)** `future_modules/the_fade/ingress/federal_register/build_universe_scanner_request_from_federal_register.py` — **as shipped** (bounded FR fetch + one request write). **(2)** `future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/validate_ingress_request_packets.py` — **as shipped**. **(3)** `future_modules/the_fade/bridge/first_request_to_result/build_universe_scanner_result_from_single_request.py` — **as shipped**, passing the **basename** of the **request JSON** produced in step **(1)** (runner must obtain that basename by a **documented, boring** rule — e.g. parse ingress **stdout** `PASS: wrote ...` line, or select the **lexicographically greatest** `fr_universe_scanner_request_*.json` in the governed inputs root **after** step **(1)**; **no** manual path smuggling from unrelated directories). **(4)** `future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/validate_universe_scanner_result_packets.py` — **as shipped**. |
| **Output boundary** | **Stdout/stderr** only for human-readable **step labels**, **PASS/FAIL**, and **paths** (request file, result file). **Exit code** non-zero if **any** step fails. **No** new artifact formats beyond what the four tools already write. |
| **Network** | The runner **script** adds **no** HTTP, sockets, or new API clients. **(Network may occur only inside the existing T89 ingress tool**, unchanged.) |
| **Local-only** | **No** scheduler, **no** worker queue, **no** provider adapters, **no** dashboard/UI, **no** “platform” orchestration. |
| **No lane / registry / approval edits** | **No** edits to **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`**, or evidence logs as part of the runner tranche. |

---

## 2. Allowed artifact types (future tranche only)

| Category | Constraint |
|----------|------------|
| **One primary runner script** | **Exactly:** **`future_modules/the_fade/runner/local_happy_path/run_local_end_to_end_happy_path.py`**. **`if __name__ == "__main__"`** only to run the sequence and exit. |
| **Optional usage notes** | **At most:** **`future_modules/the_fade/runner/local_happy_path/README.md`** — how to run, prerequisites (`jsonschema`, Python), **honesty** (not a scanner), and **failure** semantics. |
| **Optional tiny helper** | **At most one** additional **named** `.py` in **the same directory** if strictly necessary (e.g. shared subprocess wrapper) — **must** be listed in README; **no** package sprawl. |
| **Second entrypoint** | **Forbidden**. |

---

## 3. What the runner may do

- Invoke the **four** tools above **sequentially**, **waiting** for each to complete before the next.
- **Print** clear step boundaries and final **PASS** only if all four exit **0**.
- **Propagate failure:** if any step exits non-zero, runner exits non-zero **without** claiming success.
- **Optional bounded operator argument:** **at most one** optional flag governed in README, e.g. forward **`--per-page`** to ingress **only**, within ingress’s **existing** documented bounds (**1..20**). **No** other passthrough surface without new governance.

---

## 4. Forbidden in the later implementation tranche

| Forbidden | Rationale |
|-----------|-----------|
| **Scanner execution / ranking / scoring / selection** | Product logic |
| **Request enrichment** from live sources **beyond** invoking the **existing** T89 ingress | New pipeline |
| **Multi-source fusion** | Out of slice |
| **New provider adapters / dashboard / UI** | Out of slice |
| **Runtime orchestration platform** (K8s, Celery, cron installer, etc.) | Out of slice |
| **Parallel branches / optional alternate pipelines** | Scope creep |
| **Rewriting** ingress, validators, or bridge **inside** the runner | DRY violation of tranche boundaries |
| **Lane reopen, evidence collection, registry/approval edits** | Phase 2 boundary |
| **Multi-slice bundling** | Runner + scanner stub |
| **“Tiny scanner”** disguised as glue code | Anti-drift |

---

## 5. Fixed paths (authoritative)

| Role | Path |
|------|------|
| **Runner script (future)** | **`future_modules/the_fade/runner/local_happy_path/run_local_end_to_end_happy_path.py`** |
| **Optional README (future)** | **`future_modules/the_fade/runner/local_happy_path/README.md`** |
| **Ingress (existing)** | **`future_modules/the_fade/ingress/federal_register/build_universe_scanner_request_from_federal_register.py`** |
| **Ingress-request validator (existing)** | **`future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/validate_ingress_request_packets.py`** |
| **Bridge (existing)** | **`future_modules/the_fade/bridge/first_request_to_result/build_universe_scanner_result_from_single_request.py`** |
| **Result validator (existing)** | **`future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/validate_universe_scanner_result_packets.py`** |

---

## 6. Success semantics (future tranche)

- All **four** invocations complete with exit code **0**.
- **One** new request packet path and **one** new result packet path are **identifiable** from runner output (or unambiguous from tool stdout).
- Runner **does not** print or imply **“scanner completed”**, **“universe resolved”**, or intelligence claims — **local glue + honesty** only.

---

## 7. Relationship to prior tranches

- **T89–T96** artifacts and meanings **unchanged**; the runner **composes** them **only**.  
- **Model B** / root JSON caps for **`outputs/phase3_universe_scanner_results/`** remain **operator truth** — runner must **not** bypass the bridge’s cap check by deleting files silently without documentation; prefer **honest failure** or documented **precondition** in README.

---

## 8. Anti-drift rules

1. **One implementation slice** — single runner tranche until new governance.  
2. **One runner path** — §5 script path only.  
3. **Sequential happy-path only** — no extra branches.  
4. **No “while we’re here”** — no ingress/validator/bridge edits bundled as the same tranche.  
5. **No widening** into **system** orchestration or **scanner** logic.  

---

## 9. Non-claims

- T97 **does not** implement the runner.  
- T97 **does not** authorize a universe scanner, production pipeline, or dashboard.  
- T97 **does not** prove production readiness.

# B1 Local Website Defect Watcher v1

Bounded read-only watcher for visible website defects. First monitored site: https://www.wcsbasketball.site/. See `B1_WCS_DEFECT_WATCHER_V1_SPEC.md` for the full contract.

## Usage

```powershell
python scripts/run_local_website_defect_watcher.py --config <path>
```

Example:

```powershell
python scripts/run_local_website_defect_watcher.py --config future_modules/local_website_defect_watcher/examples/b1_wcs_watcher_config.example.json
```

**Requires:** `pip install playwright` and `python -m playwright install chromium`

## Output

Run output is written under `scratch/local_website_defect_watcher/<watcher_id>/<run_id>/`:

- `run_result.json` — Full run result
- `screenshots/` — Screenshot evidence
- `console_errors.json` — Captured console errors (third-party noise filtered)
- `evidence_manifest.json` — Consolidated evidence
- `proposed_defect_packets/` — Proposed packets (operator review required)

The watcher creates proposed packets only. It never auto-approves or creates backlog items. v1 verifies direct route reachability, not nav-link clicking.

## Proof status

Proven 2026-03-19. Fresh proof run after signal hardening: 0 findings, 0 proposed packets, 4 screenshots, 0 console errors, recommended_action=dismiss.

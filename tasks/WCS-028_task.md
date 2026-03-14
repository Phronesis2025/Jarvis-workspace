# TASK PACKET

## Header
- Task ID: WCS-028
- Project: WCS
- Title: Style test: change home hero eyebrow accent color for BUILT FOR
- Bucket: ugly
- Priority: P3
- Risk: low
- Status: ready

## Repo
- Repo Path: `C:\dev\wcsv2.0-new`
- Branch Name: `jarvis-task-wcs-028`

## Problem Summary
Style test: change home hero eyebrow accent color for BUILT FOR.

## Goal
Resolve: Style test: change home hero eyebrow accent color for BUILT FOR, with the smallest safe change that satisfies QA.

## Suspected Files
- Home hero section /

## Acceptance Criteria
- The scoped issue is resolved: Style test: change home hero eyebrow accent color for BUILT FOR
- App builds successfully with npm run build
- Local app can be opened for verification
- Targeted change is visible or behaves correctly on the relevant page/flow
- Changes remain tightly limited to the suspected files unless a clearly related helper/config file must also be updated

## QA Plan
- Run npm run build
- Start local app with npm run dev
- Run Playwright smoke QA if available
- Verify the targeted change locally in the browser

## System Impact
Low risk. This should avoid unrelated production-facing behavior changes unless strictly necessary. Primary expected scope: Home hero section /.

## Stop Conditions
- Required file cannot be found
- Build fails for unrelated reasons
- Task scope expands beyond the targeted fix

## Notes
Home hero section /

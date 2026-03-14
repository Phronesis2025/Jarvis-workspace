# TASK PACKET

## Header
- Task ID: WCS-016
- Project: WCS
- Title: Flip TestSiteBanner background from black to white
- Bucket: ugly
- Priority: P1
- Risk: low
- Status: done

## Repo
- Repo Path: `C:\dev\wcsv2.0-new`
- Branch Name: `jarvis-task-wcs-016`

## Problem Summary
Flip TestSiteBanner background from black to white.

## Goal
Resolve: Flip TestSiteBanner background from black to white, with the smallest safe change that satisfies QA.

## Suspected Files
- src/components/TestSiteBanner.tsx

## Acceptance Criteria
- The scoped issue is resolved: Flip TestSiteBanner background from black to white
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
Low risk. This should avoid unrelated production-facing behavior changes unless strictly necessary. Primary expected scope: src/components/TestSiteBanner.tsx.

## Stop Conditions
- Required file cannot be found
- Build fails for unrelated reasons
- Task scope expands beyond the targeted fix

## Notes
src/components/TestSiteBanner.tsx

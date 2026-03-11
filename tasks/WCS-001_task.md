# TASK PACKET

## Header
- Task ID: WCS-001
- Project: WCS
- Title: Fix testimonial typo in PlayerTestimonials quote
- Bucket: ugly
- Priority: P2
- Risk: low
- Status: ready

## Repo
- Repo Path: `C:\dev\wcsv2.0-new`
- Branch Name: `jarvis-task-wcs-001`

## Problem Summary
Michael J.'s quote repeats the phrase "the player" and reads awkwardly.

## Goal
Replace the duplicate phrase with clearer wording that keeps the testimonial natural and aligned with the site's tone.

## Suspected Files
- `src/components/PlayerTestimonials.tsx`

## Acceptance Criteria
- Quote no longer repeats "the player" unnecessarily
- App builds successfully with `npm run build`
- Home page loads locally after the change
- Updated testimonial text appears correctly on the rendered page

## QA Plan
- Start local app
- Open `/`
- Confirm testimonial text renders with corrected wording
- Confirm no console-breaking behavior from the change
- Confirm build passes

## System Impact
Low risk. Copy change on the home page testimonial component only.

## Stop Conditions
- Required file cannot be found
- Build fails for unrelated reasons
- Testimonial content is loaded from an unexpected remote source

## Notes
Suggested replacement options:
- "The coaches care about the player, not just the performance."
- "The coaches care about the whole player, not just their stats."

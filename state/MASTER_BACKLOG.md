# MASTER_BACKLOG

| Task ID | Project | Bucket | Priority | Risk | Status | Title | Notes |
|---|---|---|---|---|---|---|---|
| WCS-001 | WCS | ugly | P2 | low | done | Fix testimonial typo in PlayerTestimonials quote | src/components/PlayerTestimonials.tsx |
| WCS-002 | WCS | broken | P1 | medium | done | Fix stats section showing 0 for all metrics | src/components/StatsSection.tsx |
| WCS-003 | WCS | broken | P1 | medium | done | Add timeout/fallback handling for long loading states | TodaysEvents.tsx, LogoMarquee.tsx |
| WCS-004 | WCS | ugly | P2 | low | done | Improve empty Around the WCS state | src/components/TeamUpdates.tsx |
| WCS-005 | WCS | broken | P1 | medium | done | Make footer email signup form functional | src/components/Footer.tsx |
| WCS-006 | WCS | ugly | P3 | low | ready | Fix hero headline accessibility spacing/aria label | src/components/Hero.tsx |
| WCS-007 | WCS | ugly | P3 | low | ready | Hide test site banner in production | src/components/TestSiteBanner.tsx |
| WCS-008 | WCS | ugly | P3 | low | ready | Clarify navbar Coaches link label for logged-out users | src/components/Navbar.tsx |
| WCS-009 | WCS | broken | P2 | medium | done | Improve LogoMarquee response.ok handling and fallback | src/components/LogoMarquee.tsx |
| WCS-010 | WCS | broken | P2 | medium | done | Show fallback message instead of hiding TodaysEvents on error | src/components/TodaysEvents.tsx |
| WCS-011 | WCS | broken | P1 | low | done | Stabilize local Playwright smoke QA for home page | tests/e2e, playwright config, global setup for http://localhost:3000 |
| WCS-013 | WCS | broken | P2 | low | ready | Hide links to unfinished /shop page | Public navigation or CTA paths should not expose /shop until the page is built out |
| WCS-014 | WCS | broken | P2 | low | ready | Hide links to unfinished /news page | Public links should not expose /news until the page is built out |
| WCS-015 | WCS | broken | P2 | medium | ready | Investigate /schedules Supabase realtime auth console error | Scout detected websocket auth failure on public /schedules page: Supabase realtime connection attempted without valid credentials |
| WCS-016 | WCS | ugly | P1 | low | done | Flip TestSiteBanner background from black to white | src/components/TestSiteBanner.tsx |
| WCS-017 | WCS | ugly | P1 | low | done | Flip TestSiteBanner background from white back to black | src/components/TestSiteBanner.tsx |
| WCS-018 | WCS | ugly | P1 | low | done | Flip TestSiteBanner text color from white to black | src/components/TestSiteBanner.tsx |
| WCS-019 | WCS | ugly | P1 | low | done | Flip TestSiteBanner text color from black back to white | src/components/TestSiteBanner.tsx |
| WCS-020 | WCS | broken | P2 | low | ready | Normalize public footer copyright year across home/about pages | Public footer component or page-level footer rendering for / and /about |
| WCS-021 | WCS | broken | P2 | low | ready | Fix malformed Coach es label rendering on public team cards | Public /teams card label rendering |
| WCS-022 | WCS | broken | P2 | medium | ready | Fill missing grade labels on public team cards that currently show only Grade | Public /teams team metadata rendering |
| WCS-023 | WCS | broken | P2 | medium | ready | Correct impossible team grade mappings on public /teams cards | Public /teams data/rendering for Red, Warriors, and similar bad grade labels |
| WCS-024 | WCS | broken | P2 | low | ready | Remove or rename placeholder WCS Errors team from public teams page | Public /teams team list or seeded display data |
| WCS-025 | WCS | broken | P2 | medium | ready | Investigate and fix duplicated calendar rendering on public /schedules page | Public /schedules calendar component/layout |
| WCS-026 | WCS | ugly | P2 | low | ready | Improve empty-state copy for No events today on schedules page | Public /schedules today-events empty state |
| WCS-027 | WCS | ugly | P2 | low | ready | Improve empty-state copy for No drills available on drills page | Public /drills empty state |
| WCS-028 | WCS | ugly | P3 | low | ready | Fake test: add basketball emoji to hero subtitle | src/components/Hero.tsx |
| WCS-029 | WCS | ugly | P3 | low | ready | Fake test: add fire emoji to hero CTA button label | src/components/Hero.tsx |
| WCS-030 | WCS | ugly | P3 | low | ready | Fake test: add temporary TEST MODE badge below hero headline | src/components/Hero.tsx |
| WCS-031 | WCS | ugly | P3 | low | ready | Fake test: add trophy emoji to about page promo heading | src/app/about/page.tsx |
| WCS-032 | WCS | ugly | P3 | low | ready | Fake test: add visible TEST: prefix to schedules empty-state heading | src/app/schedules/page.tsx |
| WCS-033 | WCS | ugly | P3 | low | ready | Fake test: add visible TEST: prefix to drills empty-state heading | src/app/drills/page.tsx |
| WCS-034 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to public team card label | src/components/ClientTeams.tsx |
| WCS-035 | WCS | ugly | P3 | low | ready | Fake test: add temporary highlight border to hero section | src/components/Hero.tsx |
| WCS-036 | WCS | ugly | P3 | low | ready | Fake test: add star emoji to about mission heading | src/app/about/page.tsx |
| WCS-037 | WCS | ugly | P3 | low | ready | Fake test: add medal emoji to about page section heading | src/app/about/page.tsx |
| WCS-038 | WCS | ugly | P3 | low | ready | Fake test: add calendar emoji to schedules empty-state message | src/app/schedules/page.tsx |
| WCS-039 | WCS | ugly | P3 | low | ready | Fake test: add basketball emoji to schedules page title or filter label | src/app/schedules/page.tsx |
| WCS-040 | WCS | ugly | P3 | low | done | Style test: change home hero subheading letter spacing | src/components/Hero.tsx |
| WCS-041 | WCS | ugly | P3 | low | ready | Fake test: add trophy emoji to hero CTA button label | src/components/Hero.tsx |
| WCS-042 | WCS | ugly | P3 | low | done | Fake test: add temporary TEST MODE badge on about page | src/app/about/page.tsx |
| WCS-043 | WCS | ugly | P3 | low | ready | Fake test: add visible TEST: prefix to drills page heading | src/app/drills/page.tsx |
| WCS-044 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to about page section divider | src/app/about/page.tsx |
| WCS-045 | WCS | ugly | P3 | low | ready | Fake test: add temporary highlight border to about page section | src/app/about/page.tsx |
| WCS-046 | WCS | ugly | P3 | low | ready | Fake test: add temporary test badge to one team card | src/components/ClientTeams.tsx |
| WCS-047 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to team card metadata label | src/components/ClientTeams.tsx |
| WCS-048 | WCS | ugly | P3 | low | ready | Fake test: add calendar emoji to schedules page empty-state | src/app/schedules/page.tsx |
| WCS-049 | WCS | ugly | P3 | low | ready | Fake test: add visible TEST: to schedules empty-state heading | src/app/schedules/page.tsx |
| WCS-050 | WCS | ugly | P3 | low | ready | Fake test: add drill emoji to drills empty-state heading | src/app/drills/page.tsx |
| WCS-051 | WCS | ugly | P3 | low | ready | Fake test: add visible TEST: to drills empty-state message | src/app/drills/page.tsx |
| WCS-052 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to home section heading | src/components/Hero.tsx |
| WCS-053 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to about section heading | src/app/about/page.tsx |
| WCS-054 | WCS | ugly | P3 | low | ready | Fake test: add temporary TEST prefix to team card label | src/components/ClientTeams.tsx |
| WCS-055 | WCS | ugly | P3 | low | ready | Fake test: add temporary highlight border to one team card | src/components/ClientTeams.tsx |
| WCS-056 | WCS | ugly | P3 | low | ready | Fake test: add temporary TEST MODE badge to teams section | src/components/ClientTeams.tsx |
| WCS-057 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to teams section heading | src/components/ClientTeams.tsx |
| WCS-058 | WCS | ugly | P3 | low | ready | Fake test: add temporary bright marker to schedules empty state | src/app/schedules/page.tsx |
| WCS-059 | WCS | ugly | P3 | low | ready | Fake test: add temporary bright marker to drills empty state | src/app/drills/page.tsx |
| WCS-060 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to about page CTA or link | src/app/about/page.tsx |
| WCS-061 | WCS | ugly | P3 | low | ready | Fake test: add temporary TEST MODE text to footer | src/components/Footer.tsx |

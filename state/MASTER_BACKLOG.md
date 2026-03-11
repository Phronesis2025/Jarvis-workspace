# MASTER\_BACKLOG

|Task ID|Project|Bucket|Priority|Risk|Status|Title|Notes|
|-|-|-|-|-|-|-|-|
|WCS-001|WCS|ugly|P2|low|done|Fix testimonial typo in PlayerTestimonials quote|src/components/PlayerTestimonials.tsx|
|WCS-002|WCS|broken|P1|medium|done|Fix stats section showing 0 for all metrics|src/components/StatsSection.tsx|
|WCS-003|WCS|broken|P1|medium|done|Add timeout/fallback handling for long loading states|TodaysEvents.tsx, LogoMarquee.tsx|
|WCS-004|WCS|ugly|P2|low|done|Improve empty Around the WCS state|src/components/TeamUpdates.tsx|
|WCS-005|WCS|broken|P1|medium|ready|Make footer email signup form functional|src/components/Footer.tsx|
|WCS-006|WCS|ugly|P3|low|ready|Fix hero headline accessibility spacing/aria label|src/components/Hero.tsx|
|WCS-007|WCS|ugly|P3|low|ready|Hide test site banner in production|src/components/TestSiteBanner.tsx|
|WCS-008|WCS|ugly|P3|low|ready|Clarify navbar Coaches link label for logged-out users|src/components/Navbar.tsx|
|WCS-009|WCS|broken|P2|medium|ready|Improve LogoMarquee response.ok handling and fallback|src/components/LogoMarquee.tsx|
|WCS-010|WCS|broken|P2|medium|ready|Show fallback message instead of hiding TodaysEvents on error|src/components/TodaysEvents.tsx|
|WCS-011|WCS|broken|P1|low|done|Stabilize local Playwright smoke QA for home page|tests/e2e, playwright config, global setup for http://localhost:3000|
|||||||||

| WCS-013 | WCS | broken | P2 | low | ready | Hide links to unfinished /shop page | Public navigation or CTA paths should not expose /shop until the page is built out |

| WCS-014 | WCS | broken | P2 | low | ready | Hide links to unfinished /news page | Public links should not expose /news until the page is built out |

| WCS-015 | WCS | broken | P2 | medium | ready | Investigate /schedules Supabase realtime auth console error | Scout detected websocket auth failure on public /schedules page: Supabase realtime connection attempted without valid credentials |


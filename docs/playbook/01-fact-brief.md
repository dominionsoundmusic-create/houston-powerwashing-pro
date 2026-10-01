# Prompt 1: Client fact brief

Source of truth: INTAKE.md (completed questionnaire), SERVICES.md, approved logo and favicons.
Status key: **C** confirmed · **D** missing but deferrable · **X** contradictory · **B** launch-blocking

| Item | Value | Status |
|---|---|---|
| Official business name | Houston Power Washing Pro, a d/b/a of Dominion Digital Group | C |
| Display name | Houston Power Washing Pro | C |
| What it is | Free phone line and referral service. Never cleans, quotes, schedules, supervises or guarantees. May be paid a referral fee (disclosed). | C |
| Primary category | Pressure washing and soft washing referral line, Houston area | C |
| Services | 9 services, 6 guides (SERVICES.md) | C |
| Most important services | Residential pressure washing, house/soft washing, roof cleaning, driveway cleaning, commercial | C |
| Services not offered | Painting, sealing/staining as main job, window cleaning, gutter repair/installation, water-damage restoration, indoor mold remediation, equipment sales/rentals | C |
| Service area | Houston (Harris County and surrounding counties) + 12 city pages | C |
| Areas not to claim | Anywhere outside the Houston area; all Dallas-area cities removed | C |
| Address | DO NOT DISPLAY | C (omitted) |
| Phone | (832) 662-4107, tel:+18326624107 | C |
| Email | UNKNOWN, not displayed | D |
| Hours | Phone answered 24/7 by an automated assistant; online requests any time | C |
| Year established | 2026 | C |
| Owner | Dominion Digital Group; no individual named | C |
| Primary CTA | Call (832) 662-4107 | C |
| Secondary CTA | Send a Cleaning Request (Netlify form "houston-powerwashing-contact") | C |
| Brand colors | Navy #0B1A33, water blue #00B4E6, amber #F0A500, tint #E8F4FD | C |
| Logo / favicons | images/logo.svg (290x64, has white wordmark so needs a dark background); favicon.svg/.ico, apple-touch-icon.png | C |
| Typography | Clean modern sans-serif (Inter, system fallback) | C |
| Top bar quote | "I believe the unbelievable, I receive the impossible, because it's doable." Jesse Duplantis | C |
| Footer | "© 2026 Dominion Digital Group. All rights reserved." + "Designed by Dominion Web Design Pro" link (new tab) | C |
| Language | EN / ES toggle (Google Translate) | C |
| Reviews / testimonials / ratings | None. Not added. | C |
| Licenses / certifications / insurance | None claimed. Texas: pressure washing is not a TDLR-licensed trade (search-verified, see docs/research/topics.md). City of Houston Health Dept issues a pressure washer permit for special-waste/grease work. | C |
| Guarantees, prices, stats, years, job counts | None. Not added. Cost guides quote third-party published ranges only, with publisher named. | C |
| Social / GBP | None yet. Data-driven slots hidden while empty. | D |
| Analytics | UNKNOWN. Not installed. | D |
| Map / scheduler / review widget | None | C |
| Photos | 10 existing images in images/ (AI-style stock look, not client job photos); rest planned in docs/image-list.md | D |
| Hero video | None available; image heroes used | D |
| Domain / canonical | https://houstonpowerwashingpro.com | C |
| Partner company name | Must never appear | C |

## Contradictions found
- None in the intake itself. Old site's homepage listed Dallas-area cities (removed; old site archived only).
- Old privacy policy described scheduling and appointment texts, which contradicts "never schedules". Rewritten.

## Launch blockers
- None in the facts. Remaining pre-launch items: Maurice to review the privacy policy and terms; generate the planned images; spot-check research source URLs (agents could only read search extracts).

Ready for the architecture step.

# Houston Power Washing Pro: pages, slugs and target keywords

Source: Ubersuggest, United States, pulled Sep 30 2026 (12 seeds, Suggestions + Questions). The spreadsheet is in docs/keyword-research/. Vol = searches per month. SD = SEO difficulty.
Build ONE page per row, one at a time, in this order. Every page is written for its own topic and keyword.

## Homepage
Target: "power washing houston texas" (1,900, SD 20), "power washing houston tx" (1,600, SD 24), "pressure washing houston" (1,300, SD 25), "pressure washing houston texas" (1,300, SD 30), "pressure washing companies in houston" (1,600, SD 27), "pressure washing services near me" (49,500, SD 20, national). The brand is Houston POWER Washing Pro, and "power washing Houston" is the larger search, so the homepage title and H1 lead with power washing and also cover pressure washing.

## Service pages (Prompt 9) at /services/<slug>/
| # | Service | Slug | Main keyword | Vol | SD |
|---|---|---|---|---|---|
| 1 | Residential Pressure Washing | pressure-washing | pressure washing houston / pressure washing houston services / professional pressure washing houston | 1,300 / 70 / 0 | 25 / 6 |
| 2 | House Washing and Soft Washing | house-washing | house washing houston / house power washing houston / soft washing houston / what is soft pressure washing | 70 / 20 / 20 / 40 | 22 / 5 / 23 / 18 |
| 3 | Roof Cleaning | roof-cleaning | roof cleaning houston texas / roof cleaning houston / roof cleaning houston tx / soft wash roof cleaning houston | 320 / 210 / 140 | 21 / 13 / 23 |
| 4 | Driveway and Sidewalk Cleaning | driveway-cleaning | driveway cleaning houston / driveway cleaning houston tx / driveway pressure washing houston | 90 / 70 / 10 | 14 / 5 / 5 |
| 5 | Commercial Pressure Washing | commercial-pressure-washing | commercial pressure washing houston / commercial pressure washing houston tx / commercial pressure washing companies near me / commercial power washing houston | 110 / 110 / 170 / 20 | 24 / 24 / 22 / 28 |
| 6 | Fence Cleaning | fence-cleaning | fence cleaning houston (wood fences, mildew, graying) | low | low |
| 7 | Deck and Patio Cleaning | deck-cleaning | deck cleaning / patio cleaning houston | low | low |
| 8 | Gutter Cleaning and Brightening | gutter-cleaning | gutter cleaning (outside stains and clogged runs) | low | low |
| 9 | Oil and Rust Stain Removal | oil-stain-removal | oil stain removal driveway / rust stain removal concrete | low | low |

The commercial page is NEW (the current site has none). Pages 6 to 9 exist on the current site; rebuild them fresh.

## Guide pages (Prompt 9, same standard as a service page) at /guides/<slug>/
| # | Guide | Slug | Main keyword | Vol | SD |
|---|---|---|---|---|---|
| 10 | How Much Does Pressure Washing Cost? | pressure-washing-cost | how much does pressure washing cost / pressure washing cost per square foot / pressure washing houston prices | 1,300 / 50 / 30 | 30 / 26 / 10 |
| 11 | How to Get a Pressure Washing Quote | pressure-washing-quote | pressure washing quote | 590 | 14 |
| 12 | How Often Should You Pressure Wash a House? | how-often-pressure-wash-house | how often pressure wash house / how often to power wash a house / how often soft wash house | 390 / 10 / 0 | 31 / 5 |
| 13 | Power Washing vs Pressure Washing | power-washing-vs-pressure-washing | what is the difference between power washing and pressure washing | 90 | 23 |
| 14 | Does Pressure Washing Damage Concrete? | does-pressure-washing-damage-concrete | does pressure washing damage concrete / what psi pressure washer to clean concrete | 110 / 30 | 15 / 19 |
| 15 | How Much Does Roof Cleaning Cost? | roof-cleaning-cost | roof cleaning houston cost | 0 (exists on current site) | 4 |

## City pages (Prompt 11) at /service-areas/<slug>/
Order = keyword volume plus the Search Console impressions the current city pages already earn (Cypress 532, Spring 240, Katy 202, Pearland 157, Conroe 68 impressions in 28 days).
| # | City | Slug | Main keyword | Vol | SD |
|---|---|---|---|---|---|
| 1 | The Woodlands | the-woodlands | pressure washing the woodlands / ...tx / ...texas / woodlands pressure washing | 320 / 320 / 260 / 90 | 26 / 20 / 18 / 38 |
| 2 | Katy | katy | pressure washing katy tx / pressure washing katy / katy pressure washing pros | 320 / 260 / 30 | 24 / 25 / 19 |
| 3 | Sugar Land | sugar-land | pressure washing sugar land / ...tx | 260 / 260 | 25 / 27 |
| 4 | Cypress | cypress | cypress pressure washing / pressure washing cypress / ...tx | 110 / 70 / 70 | 26 / 13 / 15 |
| 5 | Pearland | pearland | pressure washing pearland / ...texas | 140 / 140 | 22 / 23 |
| 6 | Spring | spring | pressure washing spring tx | (GSC: 240 impressions) | |
| 7 | Conroe | conroe | pressure washing conroe tx | (GSC: 68 impressions) | |
| 8 | Tomball | tomball | pressure washing tomball tx | | |
| 9 | Kingwood | kingwood | pressure washing kingwood tx | | |
| 10 | League City | league-city | pressure washing league city tx | | |
| 11 | Friendswood | friendswood | pressure washing friendswood tx | | |
| 12 | Missouri City | missouri-city | pressure washing missouri city tx | | |

Each city page must be researched for that city (public sources: city government, HOA and deed-restriction rules, county, utility, weather, local landmarks, storm history) and written for that city. Never the same page with the name swapped.

## Questions to answer somewhere on the site (FAQ blocks, with FAQPage schema)
how often pressure wash house (390) · how long does pressure washing take (30) · how long does pressure washing last (10) · does pressure washing kill weeds (10) · does power washing damage wood (10) · will pressure washing kill plants · how do pressure washing companies charge (20) · what is commercial pressure washing · how often to pressure wash a driveway · what pressure washer to clean siding (answer as: hire a soft wash company; do not give DIY machine advice) · who does pressure washing in my area (40) · power washing in my area (320)

## Old URLs that must 301 to their new home (put them in _redirects)
The live site's URLs, both with and without .html and trailing slash where they existed:
/pressure-washing/ → /services/pressure-washing/
/pressure-washing/<city>-tx and /pressure-washing/<city>-tx.html → /service-areas/<city>/ (conroe, cypress, friendswood, katy, kingwood, league-city, missouri-city, pearland, spring, sugar-land, the-woodlands)
/cypress-pressure-washing/ → /service-areas/cypress/
/tomball-pressure-washing/ → /service-areas/tomball/
/house-washing and /house-washing.html → /services/house-washing/
/roof-cleaning/ → /services/roof-cleaning/
/driveway-cleaning/ → /services/driveway-cleaning/
/fence-cleaning/ → /services/fence-cleaning/
/deck-cleaning/ → /services/deck-cleaning/
/gutter-cleaning and /gutter-cleaning.html → /services/gutter-cleaning/
/oil-stain-removal and .html → /services/oil-stain-removal/
/pressure-washing-cost and .html → /guides/pressure-washing-cost/
/pressure-washing-quote and .html → /guides/pressure-washing-quote/
/roof-cleaning-cost and .html → /guides/roof-cleaning-cost/
/terms and /terms.html → /terms-of-use/
/privacy-policy.html → /privacy-policy/
/contact/thanks/ → /thank-you/
/power-washing and /power-washing/* → / (the homepage now targets power washing)
/roof-soft-wash and /roof-soft-wash/* → /services/roof-cleaning/
The old /blog/... redirects in the current _redirects file: keep them, but point each at its new URL above.
Remove the old wildcard rules that sent /pressure-washing/*, /deck-cleaning/*, /driveway-cleaning/* and /fence-cleaning/* to hubs, because the new site has real pages under different paths. Netlify serves real files before redirects, so make sure no rule shadows a new page.

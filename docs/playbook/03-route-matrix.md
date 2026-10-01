# Prompt 3: Baseline, route matrix and build plan

## Baseline
- Before this build the repo root held the old live site as loose HTML (now archived in docs/old-site/, not published).
- There was no build, typecheck or test tooling, so there were no pre-existing failures to record. The old site had templated city pages, retired auto-blog posts and Dallas-area cities on the homepage (all retired).
- Unrelated work preserved: images/, favicons, _redirects (rewritten per SERVICES.md), the keyword research spreadsheet.

## Route matrix

| Route | Page | Static/dynamic | Config source | Page type | In navigation | In sitemap | Indexing |
|---|---|---|---|---|---|---|---|
| / | Home | static | src/pages/index.html | home | Logo | yes | index |
| /services/ | Services overview | static | src/pages/services.html | page | Header/footer | yes | index |
| /service-areas/ | Service areas overview | static | src/pages/service-areas.html | page | Header/footer | yes | index |
| /how-it-works/ | How it works | static | src/pages/how-it-works.html | page | Header/footer | yes | index |
| /about/ | About | static | src/pages/about.html | about | Header/footer | yes | index |
| /faq/ | FAQ | static | src/pages/faq.html | page | Header/footer | yes | index |
| /contact/ | Contact | static | src/pages/contact.html | contact | Header/footer | yes | index |
| /privacy-policy/ | Privacy policy | static | src/pages/privacy-policy.html | legal | Header/footer | yes | index |
| /terms-of-use/ | Terms of use | static | src/pages/terms-of-use.html | legal | Header/footer | yes | index |
| /services/pressure-washing/ | Residential Pressure Washing | dynamic (data-driven listing, own content file) | site.json services + src/pages/services/pressure-washing.html | service | Services menu + footer | yes | index |
| /services/house-washing/ | House Washing and Soft Washing | dynamic (data-driven listing, own content file) | site.json services + src/pages/services/house-washing.html | service | Services menu + footer | yes | index |
| /services/roof-cleaning/ | Roof Cleaning | dynamic (data-driven listing, own content file) | site.json services + src/pages/services/roof-cleaning.html | service | Services menu + footer | yes | index |
| /services/driveway-cleaning/ | Driveway and Sidewalk Cleaning | dynamic (data-driven listing, own content file) | site.json services + src/pages/services/driveway-cleaning.html | service | Services menu + footer | yes | index |
| /services/commercial-pressure-washing/ | Commercial Pressure Washing | dynamic (data-driven listing, own content file) | site.json services + src/pages/services/commercial-pressure-washing.html | service | Services menu + footer | yes | index |
| /services/fence-cleaning/ | Fence Cleaning | dynamic (data-driven listing, own content file) | site.json services + src/pages/services/fence-cleaning.html | service | Services menu + footer | yes | index |
| /services/deck-cleaning/ | Deck and Patio Cleaning | dynamic (data-driven listing, own content file) | site.json services + src/pages/services/deck-cleaning.html | service | Services menu + footer | yes | index |
| /services/gutter-cleaning/ | Gutter Cleaning and Brightening | dynamic (data-driven listing, own content file) | site.json services + src/pages/services/gutter-cleaning.html | service | Services menu + footer | yes | index |
| /services/oil-stain-removal/ | Oil and Rust Stain Removal | dynamic (data-driven listing, own content file) | site.json services + src/pages/services/oil-stain-removal.html | service | Services menu + footer | yes | index |
| /guides/pressure-washing-cost/ | How Much Does Pressure Washing Cost? | dynamic | site.json guides + src/pages/guides/pressure-washing-cost.html | guide | Guides menu + footer | yes | index |
| /guides/pressure-washing-quote/ | How to Get a Pressure Washing Quote | dynamic | site.json guides + src/pages/guides/pressure-washing-quote.html | guide | Guides menu + footer | yes | index |
| /guides/how-often-pressure-wash-house/ | How Often Should You Pressure Wash a House? | dynamic | site.json guides + src/pages/guides/how-often-pressure-wash-house.html | guide | Guides menu + footer | yes | index |
| /guides/power-washing-vs-pressure-washing/ | Power Washing vs Pressure Washing | dynamic | site.json guides + src/pages/guides/power-washing-vs-pressure-washing.html | guide | Guides menu + footer | yes | index |
| /guides/does-pressure-washing-damage-concrete/ | Does Pressure Washing Damage Concrete? | dynamic | site.json guides + src/pages/guides/does-pressure-washing-damage-concrete.html | guide | Guides menu + footer | yes | index |
| /guides/roof-cleaning-cost/ | How Much Does Roof Cleaning Cost? | dynamic | site.json guides + src/pages/guides/roof-cleaning-cost.html | guide | Guides menu + footer | yes | index |
| /service-areas/the-woodlands/ | The Woodlands | dynamic | site.json cities + src/pages/service-areas/the-woodlands.html | city | Areas menu + footer | yes | index |
| /service-areas/katy/ | Katy | dynamic | site.json cities + src/pages/service-areas/katy.html | city | Areas menu + footer | yes | index |
| /service-areas/sugar-land/ | Sugar Land | dynamic | site.json cities + src/pages/service-areas/sugar-land.html | city | Areas menu + footer | yes | index |
| /service-areas/cypress/ | Cypress | dynamic | site.json cities + src/pages/service-areas/cypress.html | city | Areas menu + footer | yes | index |
| /service-areas/pearland/ | Pearland | dynamic | site.json cities + src/pages/service-areas/pearland.html | city | Areas menu + footer | yes | index |
| /service-areas/spring/ | Spring | dynamic | site.json cities + src/pages/service-areas/spring.html | city | Areas menu + footer | yes | index |
| /service-areas/conroe/ | Conroe | dynamic | site.json cities + src/pages/service-areas/conroe.html | city | Areas menu + footer | yes | index |
| /service-areas/tomball/ | Tomball | dynamic | site.json cities + src/pages/service-areas/tomball.html | city | Areas menu + footer | yes | index |
| /service-areas/kingwood/ | Kingwood | dynamic | site.json cities + src/pages/service-areas/kingwood.html | city | Areas menu + footer | yes | index |
| /service-areas/league-city/ | League City | dynamic | site.json cities + src/pages/service-areas/league-city.html | city | Areas menu + footer | yes | index |
| /service-areas/friendswood/ | Friendswood | dynamic | site.json cities + src/pages/service-areas/friendswood.html | city | Areas menu + footer | yes | index |
| /service-areas/missouri-city/ | Missouri City | dynamic | site.json cities + src/pages/service-areas/missouri-city.html | city | Areas menu + footer | yes | index |
| /thank-you/ | Form success | static | src/pages/thank-you.html | utility | no | no | noindex |
| /404.html | Not found | static | src/pages/404.html | utility | no | no | noindex (404 status from Netlify) |

No /guides/ overview route was approved, so none was built: the Guides menu is a dropdown button, and the guide breadcrumb points to the guides section of /services/ (#guides).

## Old routes
Every old URL 301s to its new home through src/static/_redirects (copied to dist/_redirects). No rule shadows a new page.

## Build plan (Prompts 4 to 20)
1. Prompt 4: business data in src/data/site.json. 5: design tokens in src/static/css/site.css. 6: header, footer, nav from site.json.
2. Prompt 7: homepage. 8: services overview. 9: 9 service pages and 6 guides, one per content file, each with its own topic, keyword, design treatment and FAQs.
3. Prompt 10: service areas overview. 11: 12 city pages from city research in docs/research/.
4. Prompt 12: about, FAQ, how it works, privacy, terms. 13: contact and Netlify form. 14: social slots (empty, hidden). 15: media inventory and docs/image-list.md.
5. Prompts 16 and 17: SEO pass and remnant sweep with scripts/check.py and scripts/similarity.py.
6. Prompts 18 to 20: browser QA with Playwright (scripts/qa.js), final handoff in docs/playbook/handoff.md.

## Decisions needed
None blocking. Placeholders: planned images (docs/image-list.md), analytics ID, social URLs, email (none by choice).

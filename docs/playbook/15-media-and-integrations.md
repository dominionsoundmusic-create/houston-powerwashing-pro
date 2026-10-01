# Prompts 13 to 15: Forms, integrations and media

## Prompt 13: Contact and lead form
- One Netlify form, name `houston-powerwashing-contact` (unchanged, so Netlify keeps its registration and
  notifications). Fields: name, phone, email (optional), city or ZIP, what needs cleaning (the seven
  options from the intake), size or anything else. Hidden `form-name` and `page` (the page it was sent
  from). Honeypot `bot-field`. Success page `/thank-you/` (noindex, disallowed in robots.txt).
- The form is plain HTML in every page's first response (contact page, and the closing section of every
  marketing page). Nothing is lazy-loaded or injected by script, so it renders on direct load, refresh,
  internal navigation, back/forward and resize. Verified in the browser QA (scripts/qa.js).
- Privacy Policy and Terms of Use links sit under the submit button.
- Not verified: actual lead delivery. Netlify only processes the form once the site is deployed, and
  no production submission was made (not authorized). After go-live, send one test request and confirm
  the notification arrives.
- No email, address, map or calendar is displayed (intake).

## Prompt 14: Reviews, social links, profiles
- No reviews, ratings, review widgets or badges exist, and none were added.
- Social and Google Business Profile slots are driven by `social` in src/data/site.json. All four are
  empty, so no icons render. Add a URL there and rebuild: the icon appears in the footer (opens in a new
  tab, accessible label, keyboard focus) and the URL is added to the Organization `sameAs` in JSON-LD.
- External links: the footer credit "Designed by Dominion Web Design Pro" opens
  https://dominionwebdesignpro.com in a new tab. Source links on content pages open in a new tab.
- Analytics: none installed (ID unknown). `analytics` slots exist in site.json for later.
- EN / ES: header toggle sets the Google Translate `googtrans` cookie and loads Google's translator only
  when Spanish is chosen. Verified that the cookie is set and cleared; the translation itself could not be
  seen here because this sandbox blocks translate.google.com.

## Prompt 15: Media inventory
| Asset | Where | Status |
|---|---|---|
| logo.svg (290x64) | Header (not lazy), footer (lazy) on every page | Approved, in use |
| favicon.svg, favicon.ico, apple-touch-icon.png | Every page head | Approved, in use |
| Homepage hero video | none | Not available; image hero used (intake has no video) |
| pw-01-hero.jpg (1920x800) | Hero on residential pressure washing; stand-in hero on pages whose planned hero is not generated yet | Existing photo |
| pw-03-hero.jpg (1920x800) | Stand-in hero for roof pages only | Existing photo, frosty roof: replace first |
| pw-06-hero.jpg (1920x800) | Commercial hero, services overview stand-in | Existing photo |
| pw-hero.jpg (1344x768) | In-body and stand-in hero | Existing photo |
| pw-01/03/06-card.jpg (1200x675), pw-02/04/05-card.jpg (620x620) | Service cards and in-body figures | Existing photos |
| 85 planned images | Listed one by one in docs/image-list.md with filename, size, page and generator prompt | Placeholders by design: tags stay in the templates as HTML comments, nothing broken or grey shows |

Rules applied: hero images and the header logo are never lazy-loaded (hero has fetchpriority="high" and
a preload); in-body and card images are lazy with width and height set; alt text on every image;
reduced-motion turns off transitions. The existing photos look like stock or AI images rather than
real client jobs, and the site never presents them as work done by anyone in particular.
Media is not complete until the planned images are generated.

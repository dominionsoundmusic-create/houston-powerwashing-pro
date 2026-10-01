# Prompt 20: Final QA and handoff

Branch: `build`. Nothing was merged, deployed, published or changed on Netlify or the domain.

## What was built
- Static, pre-rendered site in `dist/` (38 pages), built from `src/` by `build.py`; `netlify.toml`
  publishes `dist/` with no build command.
- Pages: homepage, services overview, 9 service pages, 6 guides, service areas overview, 12 city pages,
  how it works, about, FAQ, contact, privacy policy, terms of use, thank-you (noindex), 404 (noindex).
- Every marketing page: full-width hero with dark fade, one H1, two calls to action (call, request),
  centered reading column, a visible "Common questions" block with matching FAQPage JSON-LD, the Netlify
  request form and call section, and a Sources list for its facts.
- Quote bar, EN/ES toggle, footer copyright and "Designed by Dominion Web Design Pro" credit on every page.
- 301 redirects for every old URL (`src/static/_redirects`).

## Files changed (summary)
- Added: `build.py`, `netlify.toml`, `src/` (data, templates, pages, static), `scripts/` (check.py,
  similarity.py, seo_report.py, qa.js, shot.js, shot-view.js), `dist/` (built output),
  `docs/playbook/`, `docs/research/`, `docs/WRITING-GUIDE.md`, `docs/image-list.md`.
- Moved: old live pages to `docs/old-site/`; `images/`, favicons and `_redirects` into `src/static/`.
- Rewritten: `_redirects`, `README.md`.

## Route inventory and status
See `docs/playbook/03-route-matrix.md` (inventory) and `docs/playbook/16-seo-report.md` (per-route SEO
result: 38 of 38 pass). Browser results per route and width are in `docs/playbook/18-19-qa.md`.

## Results
| Check | Result |
|---|---|
| Production build (`python3 build.py`) | Pass: 38 pages, no errors |
| Typecheck / lint | Not applicable (no TypeScript or JS framework). `check.py` covers rules, SEO, links, images, redirects: 0 errors, 0 warnings |
| Similarity check across same-type pages | 0 flagged pairs (no 12-word run shared between any two services, guides or cities) |
| Raw HTML SEO (title, description, canonical, OG, one H1, JSON-LD, sitemap) | 38/38 pass |
| "Hydration" | Not applicable: static pages, no client rendering. Menu script tested |
| Browser QA, 38 routes x 5 widths (1440, 1280, 768, 414, 360) | See 18-19-qa.md |
| Form | Renders on first load everywhere it should; delivery NOT verified (needs the live Netlify deploy) |
| Redirects | All 90 targets exist, none shadows a page; Netlify behavior itself not verified until deploy |
| 404 | Invalid nested route returns 404 status and the 404 page (local server) |
| Color contrast | All brand pairs pass WCAG AA (lowest 5.26:1) |

## Not verified (could not be done from this sandbox)
- Real form delivery and Netlify form notifications (no deploy, no production submission).
- Netlify's own redirect handling and pretty-URL behavior (checked by rule, not on Netlify).
- Spanish translation rendering (translate.google.com is blocked here; the toggle and cookie are verified).
- Web fonts (Google Fonts blocked here; pages fall back to system fonts, layouts verified with the fallback).
- Opening every cited source page: research agents could only read search-result extracts. Spot-check
  the Sources links, especially the cost-guide figures, HOA fines and drought-stage wording.

## Remaining placeholders and missing inputs
- 85 images to generate, one by one, from `docs/image-list.md` (heroes first; roof heroes first of all).
- Social / Google Business Profile URLs and an analytics ID (slots ready in `src/data/site.json`).
- Owner review of Privacy Policy and Terms of Use.

## Launch blockers
None in the code. Before going live: generate at least the hero images, review the legal pages, and after
the deploy send one test request through the form.

## Readiness decision
Ready for Maurice's review on the `build` branch. Not yet production-ready by the playbook's standard,
because form delivery, Netlify redirects and the planned images can only be confirmed after the images
exist and the branch is deployed.

# Houston Power Washing Pro — full rebuild instructions for Claude Code

You are rebuilding houstonpowerwashingpro.com from scratch by running Dominic & Dalton's Website Builder Prompt Playbook 2.0 (PLAYBOOK.md) from start to finish. The same method was used for dominionpoolpros.com.

## Source files
- INTAKE.md: the completed Client Website Questionnaire. It is the factual source of truth. Read the "WHAT THE BUSINESS ACTUALLY IS" section twice.
- SERVICES.md: every service, guide and city page to build, with slugs, build order and target keywords from real keyword research, plus the old-URL redirect map.
- PLAYBOOK.md: the playbook text, with the Operating Rules and then Prompts 1–20.
- docs/keyword-research/Houston-Power-Washing-Keyword-Research.xlsx: the raw keyword export.

## First housekeeping step (before Prompt 1)
The current live site sits as loose HTML files in the repo root. On this `build` branch:
1. Move every old page (index.html, about/, contact/, faq/, services/, pressure-washing/, the *-pressure-washing/ folders, deck-cleaning/, driveway-cleaning/, fence-cleaning/, roof-cleaning/, and the root .html files, plus the old sitemap.xml and robots.txt) into docs/old-site/ with `git mv`. They are research notes only and must not be published.
2. Keep images/ (including images/logo.svg), favicon.svg, favicon.ico and apple-touch-icon.png. Move them into the new static folder so they publish.
3. Keep _redirects, but rewrite it per the map at the bottom of SERVICES.md.

## Architecture (approved; do not stop because there is no SSR master template)
The playbook was written for GoHighLevel AI Studio inside a native SSR master template. There is no master template here. The approved architecture is:
- A static, pre-rendered HTML/CSS/JS site on Netlify, the same stack as Maurice's other sites. Every page is a real HTML file, so all titles, descriptions, canonicals, headings, body copy and structured data are in the initial HTML response. That satisfies every "SSR / raw server HTML" requirement.
- Shared business data, services, guides, cities and navigation live in ONE central data file (e.g. src/data/site.json) and are rendered into pages by a small Python build script (build.py, using Jinja2). That keeps the playbook's centralized configuration rule. The script writes to dist/. Commit the built dist/ output.
- Add netlify.toml with `publish = "dist"` and no build command, so Netlify serves the committed output when this branch is eventually merged.
- Lead form: native Netlify Forms (data-netlify="true"), rendered on first load, never lazy-loaded. Keep the form name "houston-powerwashing-contact".
- Pretty URLs with trailing slashes: /services/<slug>/, /guides/<slug>/, /service-areas/<slug>/, plus /, /services/, /service-areas/, /how-it-works/, /about/, /faq/, /contact/, /privacy-policy/, /terms-of-use/, /thank-you/ (noindex), /404.html.
At Prompt 2, document this architecture and treat it as approved. Wherever the playbook says "hydration", "router" or "SSR", apply the static equivalent.

## How to run
1. Read INTAKE.md, SERVICES.md and PLAYBOOK.md fully.
2. Apply the Operating Rules for the whole build.
3. Run Prompts 1–20 in order, one at a time, doing everything each prompt asks.
4. Prompt 9 runs once PER SERVICE and once PER GUIDE in SERVICES.md, in the listed order. Prompt 11 runs once PER CITY in the listed order. Each page is written for its own topic and target keyword, with real research for that topic or city. Never produce the same page with a name swapped. Before finishing, run a similarity check across pages of the same type and rewrite any pair that shares long runs of identical text.
5. Every page gets a visible "Common questions" block (3 to 6 questions written the way people actually ask them) and matching FAQPage JSON-LD built from the same data, so Google and AI search tools can use them.
6. Images: every page ships with its image tags already in place (a hero plus at least two in-body images), with filename, alt text, width and height. Use the photos already in images/ first wherever they genuinely fit. For every image that does not exist yet, keep the tag in the template but do not render a broken image or a grey placeholder on the built page; list it in docs/image-list.md with filename, size, the page it is for, and a one-paragraph description a person can paste into an image generator (bright, clearly visible, Houston-area homes and surfaces, no text, no logos). Maurice generates those one at a time later.

## Stop points: pause and wait for the word "continue"
- After reading the files and reporting your plan (Step 0)
- After Phases 1 and 2 (Prompts 1–6: foundation, design system, shared components)
- After the homepage and services overview (Prompts 7–8)
- After all service and guide pages (Prompt 9)
- After the service areas overview and all city pages (Prompts 10–11)
- After Phases 3 to 5 (Prompts 12–17)
- After Phase 6 (Prompts 18–20), the final handoff
At each stop, give a SHORT plain-English summary of 5 lines max: what got built, anything blocked, what comes next. Maurice is not a developer and reads these on his phone.

## Hard rules
- Houston Power Washing Pro is a free phone line and referral service. It never cleans, washes, quotes or schedules anything itself. Never write "we clean", "our crew", "our team", "our equipment" or similar.
- Never invent licenses, certifications, insurance, reviews, ratings, prices, years in business, team members, job counts, statistics, guarantees or awards.
- Never name the partner pressure washing company.
- Only Houston-area cities. No Dallas-area cities anywhere.
- No em dashes in visible site copy. No eyebrow labels above headings. No white text or white boxes on white backgrounds.
- Full-width heroes, edge to edge, with a dark fade behind the headline. Body text in a centered reading column.
- No DIY machine instructions (PSI settings, nozzle tips, chemical mixing). Explain what a good company should do and why, and point people to the phone line.
- Work on the branch named `build`. Commit as you go and push the `build` branch so progress is saved. Do NOT merge to main, push to main, deploy, change Netlify settings or touch the domain. Maurice decides when it goes live.

# Writing guide for page content

Every page in `src/pages/` is a Jinja template with YAML front matter. `build.py` renders it into
the shared layout (quote bar, header, hero, breadcrumbs, your content, the "Common questions"
block, the call/form section, footer). Read `src/pages/services/pressure-washing.html` first: it is
the reference page for format and quality.

## What the business is (never get this wrong)
Houston Power Washing Pro is a FREE PHONE LINE, not a pressure washing company. An automated
assistant answers (832) 662-4107 24/7 (the same number also takes roofing and A/C calls, so it asks
which one first), takes down what needs cleaning and roughly how big, then transfers the caller to an
independent, owner-run local pressure washing company that hears a short summary first. If that
company is out on a job, the caller's name, number and need are passed along for a call back. That
company inspects, quotes, does the work and is paid directly. The line never quotes, schedules,
supervises, guarantees or charges. It may be paid a referral fee by the companies it connects callers
with.

## Hard rules (a build check enforces most of these)
- Never write "we clean", "our crew", "our team", "our technicians", "our equipment", "we use",
  "eco-friendly products" or anything implying Houston Power Washing Pro does work. Talk about
  "the company you are connected with", "a good company", "a careful crew", "the company".
- Never invent licenses, certifications, insurance, reviews, ratings, prices, years in business, team
  members, job counts, statistics, guarantees or awards. Never name the partner company.
- Never promise results, timing, prices or satisfaction. No "same-day", "best", "#1", "top-rated".
- Houston-area cities only. Never mention Dallas-area cities.
- NO EM DASHES (—) or en dashes (–) in visible copy. Use commas, periods, colons or parentheses.
  Ranges: "1 to 3 years", not "1–3".
- No eyebrow labels (small uppercase labels above headings).
- No DIY machine instructions: no PSI numbers as advice, nozzle tips/colors, chemical names with
  ratios, mixing, dwell times. Explain what a good company should do and why, and point to the phone line.
- Prices: never state prices as facts. Only the cost guides may quote a published range, and only
  with the publisher named on the page and linked in Sources, labelled as a national/published range,
  not a quote from this line.
- Facts about cities, laws, climate or products must come from `docs/research/*.md` and be listed
  in a `m.sources([...])` block at the end of the content. If the research marks a fact
  "unverified" or "(confirm)", do not state it as fact; soften it ("ask the company", "check with
  your HOA") or leave it out. Do not state exact numbers marked unconfirmed.
- Write for people: plain English, short paragraphs, second person. Locally specific. No filler,
  no keyword stuffing, no "In today's world". Use the target keyword naturally in the H1, the first
  paragraph, one H2 and the title.

## Page anatomy
Front matter keys:
```
type: service | guide | city | page
title: "<= 62 chars where possible, keyword first, ends with | Houston Power Washing Pro if it fits"
description: "140 to 160 characters, plain sentence, includes keyword and the free-call angle"
h1: "Specific H1 with the keyword"
crumb: "Short breadcrumb label"
keyword: "main target keyword"
hero:
  image: planned-hero-filename.jpg   # 1920x1080, unique per page, lowercase-hyphenated
  alt: "Alt text for the planned image"
  desc: "One paragraph image-generator prompt: bright, clearly visible, Houston-area homes and surfaces, natural daylight, no text, no logos, no recognizable faces."
  fallback: pw-01-hero.jpg            # existing photo shown until the planned one exists
  fallback_alt: "Alt text that describes the fallback photo accurately"
  lead: "One or two sentence supporting statement under the H1."
schema_service:                       # service and city pages only
  name: "Free connection to a local <service> company in <place>"
  type: "<Service> referral"
form_need: "One of: Driveway or walks | House or siding | Roof | Fence | Deck or patio | Several of these | Business or commercial"
faqs:                                 # 3 to 6, phrased the way people actually ask
  - q: "How often should I ...?"
    a: "<p>Answer in HTML. Can link to <a href=\"/services/...\">pages</a>.</p>"
```
If the planned hero already exists in images (e.g. you choose an existing photo that genuinely fits),
set `image:` to that file and omit `fallback`.

Existing photos (src/static/images): pw-01-hero.jpg (1920x800, worker pressure washing a concrete
driveway between lawns, brick houses, golden light), pw-01-card.jpg (1200x675 crop of same),
pw-03-hero.jpg / pw-03-card.jpg (tile roof half cleaned; frosty, bare trees: NOT Houston-looking, use
only as a fallback), pw-06-hero.jpg / pw-06-card.jpg (worker pressure washing a sidewalk in front of
storefronts), pw-hero.jpg (1344x768, clean concrete driveway beside a lawn and brick house),
pw-02-card.jpg (620x620, weathered wood privacy fence being sprayed), pw-04-card.jpg (620x620, wood
deck with cracked boards and patio furniture at sunset), pw-05-card.jpg (620x620, man soft washing a
brick and siding two-story house).

Body: `{% block content %} ... {% endblock %}`. Use these building blocks:
- `<section class="prose"> ... </section>`: centered reading column. Most text goes here.
- `<section class="band band--tint"><div class="col"> ... </div></section>`: light blue band.
  Use `<div class="wide">` instead of `col` for wider grids.
- `<section class="band band--navy">`: navy band (white text). Use sparingly.
- `<div class="split"><div>text</div>{{ img(...) }}</div>`: text beside an image on large screens.
- `{{ img('file.jpg', 'Alt text', 1200, 800, desc='image-generator prompt', caption='optional') }}`:
  in-body image. If the file does not exist the build keeps the tag as a comment and adds it to
  docs/image-list.md. Every page needs at least two in-body images (existing or planned).
- `<ol class="steps"><li><strong>Title</strong> text</li></ol>`: numbered process.
- `<ul class="checks">`: checklist. `<ul class="facts"><li><strong>Label</strong> text</li></ul>`: fact tiles.
- `<div class="grid-2">` / `<div class="grid-3">` with `<div class="panel">` (add `panel--do` /
  `panel--dont` for good/bad comparisons).
- `<div class="table-wrap"><table>...</table></div>`: comparison tables.
- `<div class="note">` / `<div class="note note--amber">`: callouts.
- Macros: `{{ m.service_cards(['slug', ...]) }}`, `{{ m.guide_cards(['slug']) }}`,
  `{{ m.city_pills(exclude='katy') }}`, `{{ m.related(['house-washing', 'guide:pressure-washing-cost', 'city:katy']) }}`,
  `{{ m.call_box('text') }}`, `{{ m.how_it_works_short() }}`, `{{ m.disclosure() }}`,
  `{{ m.sources([{'label': 'Publisher: page title', 'url': 'https://...'}]) }}`.
Do not add your own FAQ block or contact form: the layout adds "Common questions" from `faqs` and the
call/form section automatically.

Each page needs its own design treatment suited to the topic (a comparison table, a process, a
checklist, do/don't panels, a schedule table, a fact tile row...). Do not give every page the same
section sequence.

Internal links: link to related services, the matching guides and 2 to 4 relevant city pages
with descriptive anchor text. URLs: /services/<slug>/, /guides/<slug>/, /service-areas/<slug>/,
/how-it-works/, /contact/, /faq/.

## Checking your work
```
python3 build.py --out /tmp/<your-scratch>/dist
python3 scripts/check.py --dist /tmp/<your-scratch>/dist
```
Fix everything check.py reports for your pages.

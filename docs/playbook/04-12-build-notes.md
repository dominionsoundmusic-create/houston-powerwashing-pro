# Prompts 4 to 12: Configuration, brand, navigation and pages

## Prompt 4: Business data
All business values live in `src/data/site.json` (name, legal name, phone display and tel format, hours
text, CTAs, origin, form name and options, disclosure text, social and analytics slots). Empty values are
omitted from the pages (no email, no address, no social icons, no analytics). Old-identity check: the only
phone, name and domain on any page are the confirmed ones.

## Prompt 5: Brand system
Design tokens on `:root` in `src/static/css/site.css`: navy #0B1A33, water blue #00B4E6 (darkened to
#006C94 for text links on light backgrounds so they pass contrast), amber #F0A500 for calls to action,
tint #E8F4FD. Inter with system fallbacks. Buttons, cards, panels, tables, forms, FAQ accordions and
navy/tint bands are shared classes. The logo's wordmark is partly white, so it sits only on navy
(header and footer). Visible amber focus outline everywhere. No white boxes on white backgrounds: cards
and panels sit on tint or carry a border; the form is a white card on navy or bordered on white.

## Prompt 6: Navigation, header, footer
Header (sticky, navy): logo to home, Services and Service Areas menus (link plus submenu toggle), a
Guides menu (button only, since no guides overview route was approved), How It Works, About, FAQ,
Contact, EN/ES toggle, and the phone button. Mobile: a Menu button opens a panel with the same items;
Escape closes menus; submenus work by click and keyboard. Footer: compact uppercase labels, every
service, city and guide, company links, disclosure, phone, copyright and credit. No back-to-top button.

## Prompts 7 to 12: Pages
- Homepage targets "power washing houston texas" first, then pressure washing terms (title and H1 lead
  with power washing, per SERVICES.md). Sections: intro, how the line works, all services, what makes the
  line different, Houston climate, what to ask any company, service areas, guides, FAQs, call/form.
  No homepage video exists, so the hero is an image.
- Services overview: method table, services grouped by type, what is not offered, guides.
- Prompt 9 ran once per service (9) and once per guide (6), each written for its own keyword with its own
  layout (tables, do/don't panels, stain tables, schedule tables, comparison grids) and its own FAQs.
- Service areas overview: coverage model (a phone line, no offices), cities grouped by direction,
  City of Houston rules.
- Prompt 11 ran once per city (12), from the research in `docs/research/`, each with a localized H2, two
  local paragraphs beside an image, local services, four local reasons to use the line, cited local
  rules and history, and its own FAQs.
- Supporting pages: How It Works, About (only verified facts: d/b/a of Dominion Digital Group, 2026,
  referral fee disclosed), FAQ (16 questions, including every question listed in SERVICES.md), Contact,
  Privacy Policy, Terms of Use, Thank-you, 404.
- Similarity: `scripts/similarity.py` compares the page-specific text of every pair of services, guides
  and cities. Final result: no pair shares a run of 12 or more identical words or more than 12% of
  8-word phrases.

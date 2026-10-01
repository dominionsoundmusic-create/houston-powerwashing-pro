# houstonpowerwashingpro.com

Static, pre-rendered site for Houston Power Washing Pro (a free pressure washing referral phone line).
Built with a small Python script; Netlify serves the committed `dist/` folder.

## Edit and rebuild
- Business details, services, guides, cities, menu and social links: `src/data/site.json`
- Page content: `src/pages/` (one file per page; see `docs/WRITING-GUIDE.md`)
- Shared header, footer, hero, FAQ and form: `src/templates/`
- Styles and script: `src/static/css/site.css`, `src/static/js/site.js`
- Photos: `src/static/images/` (planned images to generate: `docs/image-list.md`)
- Redirects: `src/static/_redirects`

```
pip install jinja2 pyyaml
python3 build.py                 # writes dist/ and docs/image-list.md
python3 scripts/check.py         # hard rules, SEO, links, images, redirects
python3 scripts/similarity.py    # duplicate-text check across services, guides and cities
python3 scripts/seo_report.py    # route-by-route SEO report
npx http-server dist -p 8080 -s  # preview, then:
NODE_PATH=$(npm root -g) node scripts/qa.js http://localhost:8080   # browser QA
```
Commit the rebuilt `dist/` along with the source change.

Build notes and the playbook record are in `docs/playbook/`. The old live site is archived in
`docs/old-site/` for reference only and is not published.

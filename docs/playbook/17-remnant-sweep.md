# Prompt 17: Remnant and placeholder sweep

Searched the source (src/), the built pages (dist/), metadata, JSON-LD, sitemap, robots and redirects.

| Check | Result |
|---|---|
| Dallas-area cities (Carrollton, Grand Prairie, Richardson, Lewisville, Allen, Rowlett, Flower Mound, Dallas, Plano and others) | None. Enforced by scripts/check.py on every page. |
| Old pages published | None. Old site archived in docs/old-site/ (outside dist/). |
| Phone numbers | Only (832) 662-4107 / tel:+18326624107 (314 occurrences). |
| Email addresses | None displayed (intake: no public email). |
| Partner company name | Not present anywhere. |
| "we clean", "our crew", "our team", "our equipment", eco-friendly, guarantees, ratings, years in business | None. Enforced by check.py. |
| Em and en dashes in visible copy | None. Enforced by check.py. |
| Lorem ipsum, TODO, demo, sample content | None in visible copy. |
| Fake or duplicated reviews | None. No reviews exist. |
| Prices | Only in the two cost guides, as labelled third-party published ranges with publisher and link. One HOA fine amount appears on the Sugar Land page, quoted from First Colony's published policy. |
| Empty hrefs, broken internal links, duplicate IDs | None (check.py). |
| Duplicate titles, descriptions, JSON-LD blocks | None (check.py). |
| Missing image files | None. Planned images are commented tags, listed in docs/image-list.md. |
| Orphaned routes / routes missing from nav or sitemap | None. Every service, guide and city is in the header menus, footer and sitemap. |
| Redirects | 90 rules; every target exists, no rule shadows a new page (check.py). The old wildcard hub rules were removed. |
| Console errors | None from the site. The only console messages in this sandbox are blocked Google Fonts / Translate requests (proxy), which work normally online. |

## Intentional placeholders and missing inputs
- 85 images to generate (docs/image-list.md). Until then heroes show an existing stand-in photo.
- Social and Google Business Profile URLs (slots hidden while empty).
- Analytics ID (none installed).
- Research facts were gathered from search-result extracts because this sandbox blocks most outside
  websites. Every fact on a page is linked in that page's Sources block; open the links and spot-check
  before launch, especially exact figures (cost-guide ranges, HOA fines, drought stages).
- Privacy Policy and Terms of Use are plain-language drafts for the owner to review; not legal advice.

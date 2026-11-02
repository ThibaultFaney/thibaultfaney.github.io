# Migration from Hugo Blox to plain HTML/CSS

## Scope

The website is now a set of static HTML documents with one shared CSS file.
The English biography, research description, photograph, CV, and all nine
publications have been retained. The appearance is light with green accents.

The main categories are separate pages:

| Category | Public URL |
| --- | --- |
| About | `/` |
| Research | `/research/` |
| Publications | `/publication/` |
| Contact | `/contact/` |

The old navigation mentioned “Team” without corresponding content. No empty
team page or invented team information has been added.

## Preserved resources

- All nine `/publication/<slug>/` URLs and their full abstracts.
- Every `/publication/<slug>/cite.bib` file, byte-for-byte.
- `/uploads/resume.pdf`, byte-for-byte.
- The original profile photograph, byte-for-byte, under
  `/assets/images/portrait.jpg`.
- The complete bibliography, now downloadable at `/publications.bib`.
- DOI, publisher, Google Scholar, LinkedIn, email, and affiliation links.
- `/index.xml` and `/publication/index.xml` as publication RSS feeds.
- `/author/admin/` as a small redirect page to the biography on `/`.
- `/#papers` still resolves to the publications link on the homepage.

Publication pages include citation metadata for scholarly indexing and a
native HTML disclosure for reading or downloading the BibTeX citation.
The sitemap lists the four main pages and nine article pages. A custom 404
page provides navigation even when requested at a nested URL.

The former generated tag, coauthor, and publication-type archives are not
recreated. Keywords and authors are shown directly on each article page.

## Removed tooling

Hugo, Hugo Blox, Go modules, Tailwind, Pagefind, Netlify configuration,
template update automation, and the Python `academic` BibTeX-import workflow
have been removed. The old source remains in Git history.

Publication lists, article pages, bibliographies, sitemap, and RSS are now
edited together as documented in README.md. There is no generation step.
The former search and theme switcher have been replaced by direct navigation
and a light appearance.

## Validation

The initial migration was checked against the original Markdown front matter:
all nine titles, author lists, abstracts, journals, keywords, and DOIs were
preserved. Individual citations, the complete bibliography, photograph, and
CV were compared byte-for-byte.

Run the repeatable checks from the repository root:

```bash
python3 scripts/check_site.py
git diff --check
```

The dependency-free checker validates HTML nesting, local links and anchors,
navigation, basic accessibility and metadata, publication resources, sitemap,
RSS entries, and PDF format. It does not contact external websites or replace
visual browser review.

Firefox headless screenshots were reviewed at 1440 px (About and Research),
375 px (About, Publications, and an individual article), and 320 px (Contact).
The navigation, typography, portrait, article lists, and contact links rendered
without visible horizontal clipping in these views.

## Review and launch

**Draft status:** the Git credential lacks workflow modification permission.
The complete target workflow is prepared in `migration/publish.yaml`; the old
active workflows remain unchanged on this review branch. Follow
[migration/README.md](migration/README.md) before merging.

- The complete local migration is on `migration/plain-html`. The publishable
  draft review branch is `migration/html-review`, with workflow activation pending.
- After workflow activation, the pull request runs the `check` job and skips
  deployment. The draft currently has local verification only.
- Review the four categories and a publication at desktop and mobile widths.
- Confirm the nine publication URLs, citation downloads, and CV in preview.
- Check that Settings → Pages → Source remains **GitHub Actions**.
- Merge only when ready to replace the public site. A push to `main` runs
  checks, uploads `site/`, and deploys to the existing GitHub Pages environment.
- After deployment, verify the main pages and an existing article URL at
  <https://thibaultfaney.github.io/>.

To roll back after a merge, revert the migration merge commit through a new
pull request. This restores the previous Hugo source and deployment workflow
from Git history.

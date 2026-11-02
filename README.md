# Thibault Faney — personal website

A static academic website in plain HTML and CSS, hosted at
<https://thibaultfaney.github.io/>. No framework, JavaScript, package installation,
or site generation is required.

## Files

All published files live in `site/`. GitHub Pages publishes that directory as-is.

```text
site/
  index.html                    About / homepage
  research/index.html           Research and the AÇAI project
  publication/index.html        Publication list, grouped by year
  publication/<slug>/index.html Individual article and abstract
  publication/<slug>/cite.bib   Individual BibTeX citation
  contact/index.html            Email, profiles, and CV
  uploads/resume.pdf            Curriculum vitae (original public URL)
  assets/images/portrait.jpg    Profile photograph
  assets/style.css              Shared responsive styles
  publications.bib              Complete bibliography
  sitemap.xml                   Public page URLs
  index.xml                     Publications RSS (legacy URL)
  publication/index.xml         Publications RSS
  404.html                      Custom not-found page
scripts/check_site.py           Dependency-free site checks
.github/workflows/publish.yaml  Check pull requests; publish main
```

## Preview locally

From the repository root, with Python 3.10 or newer:

```bash
python3 scripts/check_site.py
python3 -m http.server 8000 --directory site
```

Open <http://localhost:8000/>. Stop the server with `Ctrl+C`.
The HTTP server is only a preview tool, not a production dependency.
You can also open `site/index.html` directly in a browser, but directory links
are best reviewed with the local server.

## Make changes

- Edit the relevant HTML file for text changes. There are no generated HTML files.
- Edit `site/assets/style.css` for the shared appearance.
- Replace `site/uploads/resume.pdf` to update the CV without changing its URL.
- Navigation and footer markup are repeated in each HTML file. Keep them
  consistent when adding or renaming a section; `scripts/check_site.py` checks
  the navigation destinations and active page.
- Keep the site in English unless a translation is explicitly requested.

### Add a publication

1. Copy a directory under `site/publication/` to a new, stable slug.
2. Update its title, authors, journal, date, abstract, keywords, DOI, publisher
   link, and BibTeX citation. Update the page title, description, canonical URL,
   Open Graph metadata, and `citation_*` metadata too.
3. Replace its `cite.bib` and the citation displayed in the expandable
   “BibTeX citation” section. Add the entry to `site/publications.bib`.
4. Add the publication to `site/publication/index.html` in reverse chronological
   order, under its year. Keep all authors and highlight Thibault Faney.
5. Add the page URL to `site/sitemap.xml` and the RSS item to both
   `site/index.xml` and `site/publication/index.xml`.
6. Run the checks and preview the article and publication list.

The bibliography is a downloadable resource, not a generator input. Editing a
`.bib` file does not rebuild pages. This deliberate duplication keeps publishing
free of a framework or build system; update the HTML and bibliography together.

## Publish

1. Work on a branch and open a pull request against `main`.
2. The workflow checks HTML structure, internal links and anchors, navigation,
   publication metadata, bibliography resources, sitemap, RSS feeds, and CV.
   External websites are not contacted by these checks.
3. Review the desktop and mobile rendering locally. Pull requests do not deploy.
4. Merge the reviewed changes into `main`. After checks pass, GitHub Actions
   uploads only `site/` and deploys it to the existing GitHub Pages environment.

The repository's **Settings → Pages → Source** should be **GitHub Actions**, as
for the previous Hugo deployment. No separate hosting service is required.
See [MIGRATION.md](MIGRATION.md) for preserved URLs and the migration checklist.

## Licenses

The website retains the existing CC BY-NC-ND 4.0 content notice. The original
template's MIT license is preserved in [LICENSE.md](LICENSE.md). Publications
remain subject to their respective publishers' terms.

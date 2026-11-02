# Maintaining this website

- The published website is `site/`, containing plain HTML and CSS. Do not add a
  framework, site generator, JavaScript bundle, external font, or build step
  unless the user requests one.
- Keep the light appearance, green accents, responsive layout, keyboard focus
  styles, and English content. Use existing verified biographical information;
  do not invent research achievements, affiliations, or team members.
- Categories are separate pages: About, Research, Publications, Contact.
- Preserve existing public URLs, especially `/publication/<slug>/`, their
  `cite.bib` files, and `/uploads/resume.pdf`.
- Keep navigation and footer consistent on all HTML pages. Use relative links
  except on `404.html`, whose assets and navigation must use root-relative URLs.
- When adding a publication, follow the complete checklist in README.md,
  including citation metadata, bibliography, publication list, sitemap, and RSS.
- Run `python3 scripts/check_site.py` after changes and review relevant pages at
  desktop and mobile widths when browser tools are available.
- Prepare changes on a branch and use a pull request. Deployment happens when
  changes reach `main`; do not merge or publish without the user's instruction.

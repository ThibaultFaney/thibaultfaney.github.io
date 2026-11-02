#!/usr/bin/env python3
"""Check the static site without third-party dependencies or network access."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys
import xml.etree.ElementTree as ET

SITE = Path(__file__).resolve().parents[1] / "site"
ORIGIN = "https://thibaultfaney.github.io"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.refs = []
        self.errors = []
        self.stack = []
        self.meta = {}
        self.canonical = None
        self.h1_count = 0
        self.title = ""
        self.nav_links = []
        self.in_nav = False
        self.current = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if tag == "html" and attrs.get("lang") != "en":
            self.errors.append("Expected an English document language")
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append(f"Duplicate id: {attrs['id']}")
            self.ids.add(attrs["id"])
        for attribute in ("href", "src"):
            if attribute in attrs:
                self.refs.append(attrs[attribute])
        if tag == "img" and not attrs.get("alt"):
            self.errors.append("Image needs descriptive alt text")
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta" and "name" in attrs:
            self.meta.setdefault(attrs["name"], []).append(attrs.get("content", ""))
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "nav" and attrs.get("aria-label") == "Main navigation":
            self.in_nav = True
        if tag == "a" and self.in_nav:
            self.nav_links.append(attrs.get("href", ""))
            if attrs.get("aria-current") == "page":
                self.current.append(attrs.get("href", ""))

    def handle_endtag(self, tag):
        if tag in VOID:
            self.errors.append(f"Unexpected closing void tag: {tag}")
        elif not self.stack or self.stack[-1] != tag:
            self.errors.append(f"Unbalanced closing tag: {tag}")
        else:
            self.stack.pop()
        if tag == "nav":
            self.in_nav = False

    def handle_data(self, data):
        if self.stack and self.stack[-1] == "title":
            self.title += data


def local_target(page, ref):
    url = urlsplit(ref)
    if url.netloc and url.netloc != urlsplit(ORIGIN).netloc:
        return None
    if url.scheme and url.scheme not in {"http", "https"}:
        return None
    path = unquote(url.path)
    target = (SITE / path.lstrip("/")) if path.startswith("/") else (page.parent / path)
    if not path:
        target = page
    if target.is_dir():
        target = target / "index.html"
    return target.resolve(), unquote(url.fragment)


def main():
    errors = []
    pages = {}
    refs_checked = 0
    for path in sorted(SITE.rglob("*.html")):
        page = Page(path)
        page.feed(path.read_text(encoding="utf-8"))
        page.close()
        pages[path.resolve()] = page
        if page.stack:
            page.errors.append(f"Unclosed tags: {page.stack}")
        if page.h1_count != 1:
            page.errors.append("Expected exactly one h1")
        if not page.title.strip():
            page.errors.append("Missing page title")
        for name in ("description", "viewport"):
            if not page.meta.get(name, [""])[0]:
                page.errors.append(f"Missing {name} metadata")
        if not page.canonical or not page.canonical.startswith(ORIGIN + "/"):
            page.errors.append("Missing canonical site URL")
        expected_nav = [SITE / "index.html", SITE / "research/index.html", SITE / "publication/index.html", SITE / "contact/index.html"]
        actual_nav = [local_target(path, ref)[0] for ref in page.nav_links]
        if actual_nav != expected_nav:
            page.errors.append("Main navigation must link to About, Research, Publications, Contact")
        if path.name != "404.html":
            section = path.relative_to(SITE).parts[0]
            current_target = SITE / section / "index.html" if section in {"research", "publication", "contact"} else SITE / "index.html"
            if len(page.current) != 1 or local_target(path, page.current[0])[0] != current_target:
                page.errors.append("Current navigation item does not match this page")
        for message in page.errors:
            errors.append(f"{path.relative_to(SITE)}: {message}")
    for path, page in pages.items():
        for ref in page.refs:
            local = local_target(path, ref)
            if local is None:
                continue
            target, fragment = local
            refs_checked += 1
            if not target.is_relative_to(SITE.resolve()) or not target.is_file():
                errors.append(f"{path.relative_to(SITE)}: broken local link {ref}")
            elif fragment and target in pages and fragment not in pages[target].ids:
                errors.append(f"{path.relative_to(SITE)}: missing anchor {ref}")

    articles = {path.parent.name: page for path, page in pages.items() if path.parent.parent == SITE / "publication"}
    if not articles:
        errors.append("No publication pages found")
    bibliography = (SITE / "publications.bib").read_text()
    listing = pages[SITE / "publication/index.html"]
    for slug, article in articles.items():
        for name in ("citation_title", "citation_author", "citation_publication_date", "citation_doi"):
            if not article.meta.get(name, [""])[0]:
                errors.append(f"{slug}: missing {name}")
        doi = article.meta.get("citation_doi", [""])[0]
        citation = (SITE / "publication" / slug / "cite.bib").read_text()
        if not doi or doi.lower() not in citation.lower() or doi.lower() not in bibliography.lower():
            errors.append(f"{slug}: DOI missing from the individual or complete bibliography")
        if f"{slug}/" not in listing.refs:
            errors.append(f"{slug}: article missing from publication list")

    expected_urls = {ORIGIN + "/" + str(path.relative_to(SITE)).removesuffix("index.html") for path in pages if path.name != "404.html" and "author" not in path.relative_to(SITE).parts}
    sitemap = ET.parse(SITE / "sitemap.xml")
    sitemap_urls = {loc.text for loc in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")}
    if sitemap_urls != expected_urls or len(sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")) != len(expected_urls):
        errors.append("Sitemap must contain every public page exactly once")
    for feed_path in (SITE / "index.xml", SITE / "publication/index.xml"):
        feed = ET.parse(feed_path)
        items = feed.findall("./channel/item")
        expected = {p.canonical: p.meta["citation_title"][0] for p in articles.values()}
        actual = {item.findtext("link"): item.findtext("title") for item in items}
        if actual != expected or len(items) != len(articles):
            errors.append(f"{feed_path.relative_to(SITE)}: RSS must match the publication pages")
    if not (SITE / "uploads/resume.pdf").read_bytes().startswith(b"%PDF-"):
        errors.append("CV is not a PDF")
    if not (SITE / ".nojekyll").is_file():
        errors.append("Missing .nojekyll")
    if errors:
        print("Static site checks failed:\n" + "\n".join(f"- {error}" for error in errors))
        return 1
    print(f"OK: {len(pages)} HTML pages, {len(articles)} publications, {refs_checked} local references, sitemap, RSS feeds, BibTeX, and CV.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

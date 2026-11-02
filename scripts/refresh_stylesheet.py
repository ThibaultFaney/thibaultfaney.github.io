#!/usr/bin/env python3
"""Refresh the content version in every static page's shared stylesheet URL."""

import hashlib
from pathlib import Path
import re

SITE = Path(__file__).resolve().parents[1] / "site"
STYLESHEET_LINK = re.compile(r'(href="(?:\.\./|/)*assets/style\.css)(?:\?[^"\s]*)?(")')


def main():
    version = hashlib.sha256((SITE / "assets/style.css").read_bytes()).hexdigest()[:12]
    updated = 0
    for path in sorted(SITE.rglob("*.html")):
        original = path.read_text(encoding="utf-8")
        refreshed = STYLESHEET_LINK.sub(lambda match: f"{match[1]}?v={version}{match[2]}", original)
        if refreshed != original:
            path.write_text(refreshed, encoding="utf-8")
            updated += 1
    print(f"Stylesheet version {version}: updated {updated} HTML pages.")


if __name__ == "__main__":
    main()

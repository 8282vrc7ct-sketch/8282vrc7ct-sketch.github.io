"""Tiny checker for index.html. Uses only Python's built-in tools.

Run it from this folder:
    python3 check_site.py

It prints PASS or FAIL for each check and exits with 1 if anything failed.
"""

import sys
from html.parser import HTMLParser
from pathlib import Path

# Sections the page must have. The nav links must point at these.
REQUIRED_SECTIONS = ["about", "projects", "contact"]

# Repos that are public on GitHub. A "View code" link may only point at these.
# If you make another repo public, add its name here.
PUBLIC_REPOS = {"8282vrc7ct-sketch.github.io"}

GITHUB_PREFIX = "https://github.com/8282vrc7ct-sketch/"

# Tags that never get a closing tag, like <meta> or <br>.
VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "source", "track", "wbr",
}


class PageReader(HTMLParser):
    """Reads the page once and remembers what the checks need."""

    def __init__(self):
        super().__init__()
        self.open_tags = []      # tags opened but not closed yet
        self.tag_errors = []     # closing tags that did not match
        self.ids = set()         # every id="..." on the page
        self.nav_links = []      # href of each link inside <nav>
        self.repo_links = []     # links to Jonah's GitHub repos
        self.has_viewport = False
        self.in_nav = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "meta" and attrs.get("name") == "viewport":
            self.has_viewport = True
        if tag == "nav":
            self.in_nav = True
        if tag == "a":
            href = attrs.get("href") or ""
            if self.in_nav:
                self.nav_links.append(href)
            if href.startswith(GITHUB_PREFIX):
                name = href[len(GITHUB_PREFIX):].strip("/")
                if name:
                    self.repo_links.append(name)
        if tag not in VOID_TAGS:
            self.open_tags.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag == "nav":
            self.in_nav = False
        if tag in VOID_TAGS:
            return
        if self.open_tags and self.open_tags[-1][0] == tag:
            self.open_tags.pop()
        else:
            line = self.getpos()[0]
            self.tag_errors.append(f"line {line}: </{tag}> does not match an open tag")


def run_checks(html_text):
    """Return a list of (name, passed, detail) for the page text."""
    reader = PageReader()
    reader.feed(html_text)
    reader.close()

    results = []

    missing = [s for s in REQUIRED_SECTIONS if s not in reader.ids]
    results.append(("required sections", not missing,
                    "missing: " + ", ".join(missing) if missing else "about, projects, contact"))

    wanted = ["#" + s for s in REQUIRED_SECTIONS]
    nav_ok = all(link in reader.nav_links for link in wanted)
    results.append(("nav links jump to sections", nav_ok, " ".join(reader.nav_links)))

    problems = reader.tag_errors + [
        f"line {line}: <{tag}> never closed" for tag, line in reader.open_tags
    ]
    results.append(("tags close", not problems, "; ".join(problems) or "all closed"))

    results.append(("phone viewport tag", reader.has_viewport,
                    "found" if reader.has_viewport else "add <meta name=\"viewport\">"))

    private = [r for r in reader.repo_links if r not in PUBLIC_REPOS]
    results.append(("code links only to public repos", not private,
                    "not public: " + ", ".join(private) if private else "ok"))

    return results


def main():
    page = Path(__file__).with_name("index.html")
    results = run_checks(page.read_text(encoding="utf-8"))
    for name, passed, detail in results:
        print(f"{'PASS' if passed else 'FAIL'}  {name} ({detail})")
    failed = sum(1 for _, passed, _ in results if not passed)
    print(f"\n{len(results) - failed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

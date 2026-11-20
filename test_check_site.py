"""Tests for check_site.py. Run: python3 -m unittest -v"""

import unittest
from pathlib import Path

from check_site import run_checks

GOOD = """<!DOCTYPE html><html><head><meta name="viewport" content="x"></head>
<body><nav><a href="#about">A</a><a href="#projects">P</a><a href="#contact">C</a></nav>
<section id="about"></section><section id="projects"></section>
<section id="contact"></section></body></html>"""


def failed_names(html):
    return [name for name, passed, _ in run_checks(html) if not passed]


class CheckSiteTests(unittest.TestCase):
    def test_real_page_passes(self):
        page = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
        self.assertEqual(failed_names(page), [])

    def test_good_sample_passes(self):
        self.assertEqual(failed_names(GOOD), [])

    def test_missing_section_fails(self):
        html = GOOD.replace('<section id="contact"></section>', "")
        self.assertIn("required sections", failed_names(html))

    def test_unclosed_tag_fails(self):
        html = GOOD.replace('<section id="about"></section>', '<section id="about"><div></section>')
        self.assertIn("tags close", failed_names(html))

    def test_private_repo_link_fails(self):
        html = GOOD.replace("</body>", '<a href="https://github.com/8282vrc7ct-sketch/needs-jonah">x</a></body>')
        self.assertIn("code links only to public repos", failed_names(html))


if __name__ == "__main__":
    unittest.main()

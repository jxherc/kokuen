#!/usr/bin/env python3
"""Repository documentation, link, and identity-asset checks."""

from __future__ import annotations

import re
import unittest
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\((?P<target>[^)]+)\)")
HTML_LINK = re.compile(r"(?:href|src)=[\"'](?P<target>[^\"']+)[\"']")


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split("#", 1)[0]
    if not target or target.startswith(("http://", "https://", "mailto:", "data:")):
        return None
    decoded = urllib.parse.unquote(target)
    return (source.parent / decoded).resolve()


class DocumentationTests(unittest.TestCase):
    def test_local_documentation_links_exist(self) -> None:
        missing: list[str] = []
        markdown_files = [
            path
            for path in ROOT.rglob("*.md")
            if ".git" not in path.parts and "__pycache__" not in path.parts
        ]
        for source in markdown_files:
            text = source.read_text(encoding="utf-8")
            targets = [match.group("target") for match in MARKDOWN_LINK.finditer(text)]
            targets += [match.group("target") for match in HTML_LINK.finditer(text)]
            for raw_target in targets:
                target = local_target(source, raw_target)
                if target is not None and not target.exists():
                    missing.append(f"{source.relative_to(ROOT)} -> {raw_target}")
        self.assertFalse(missing, "missing local documentation links:\n" + "\n".join(missing))

    def test_banner_is_valid_and_uses_v5_identity(self) -> None:
        banner = ROOT / "banner.svg"
        ET.parse(banner)
        text = banner.read_text(encoding="utf-8").lower()
        self.assertIn("design skill", text)
        self.assertNotIn("greyscale ui system", text)
        self.assertNotIn("accent", text)
        self.assertNotIn("signal", text)
        self.assertNotIn("#00ff2a", text)


if __name__ == "__main__":
    unittest.main()

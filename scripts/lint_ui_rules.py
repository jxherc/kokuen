#!/usr/bin/env python3
"""Lint source-level KOKUEN UI invariants and boundary warnings."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

CSS_EXTENSIONS = {".css", ".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte"}
HTML_EXTENSIONS = {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte"}
IGNORED_PARTS = {".git", "node_modules", "dist", "build", ".next", "coverage"}
LAYOUT_SCALE = {0.0, 4.0, 8.0, 12.0, 16.0, 24.0, 32.0, 48.0, 64.0}
INTERACTIVE = re.compile(
    r"(?:^|[\s,.>+~])(?:button|input|textarea|select|a\[|\[role=[\"']?(?:button|tab|option|menuitem|radio|checkbox|switch|slider|combobox)|"
    r"\.[a-z0-9_-]*(?:button|trigger|option|menuitem|tab|checkbox|radio|switch|slider|control|action|row)(?:\b|[-_]))",
    re.IGNORECASE,
)
CSS_RULE = re.compile(r"(?P<selectors>[^{}]+)\{(?P<body>[^{}]*)\}", re.DOTALL)
DECLARATION = re.compile(r"(?P<name>(?:--)?[a-zA-Z][a-zA-Z-]*)\s*:\s*(?P<value>[^;{}]+)")
PIXEL = re.compile(r"(?<![A-Za-z0-9_.-])(-?[0-9]+(?:\.[0-9]+)?)px\b")
SUPPRESSION = re.compile(r"kokuen-lint-disable(?:-next-line)?\s+([a-z0-9-]+)\s*:\s*([^*\n]+)", re.IGNORECASE)


@dataclass(frozen=True)
class Finding:
    severity: str
    rule: str
    path: Path
    line: int
    message: str

    def text(self) -> str:
        return f"{self.path}:{self.line}: {self.severity} {self.rule}: {self.message}"


def iter_files(paths: list[Path]) -> Iterable[Path]:
    seen: set[Path] = set()
    for path in paths:
        candidates = path.rglob("*") if path.is_dir() else [path]
        for candidate in candidates:
            if not candidate.is_file() or candidate.suffix.lower() not in CSS_EXTENSIONS:
                continue
            if any(part in IGNORED_PARTS for part in candidate.parts):
                continue
            resolved = candidate.resolve()
            if resolved not in seen:
                seen.add(resolved)
                yield candidate


def css_source(path: Path, text: str) -> str:
    if path.suffix.lower() == ".css":
        return text
    chunks: list[str] = []
    current_line = 0
    for match in re.finditer(r"<style\b[^>]*>(?P<css>.*?)</style>", text, re.IGNORECASE | re.DOTALL):
        start, end = match.span("css")
        start_line = text.count("\n", 0, start)
        chunks.append("\n" * max(0, start_line - current_line))
        css = text[start:end]
        chunks.append(css)
        current_line = start_line + css.count("\n")
    return "".join(chunks)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def suppressed(text: str, offset: int, rule: str) -> bool:
    context = text[max(0, offset - 320):min(len(text), offset + 320)]
    for match in SUPPRESSION.finditer(context):
        if match.group(1).lower() == rule and match.group(2).strip():
            return True
    return False


def add(
    findings: list[Finding],
    severity: str,
    rule: str,
    path: Path,
    text: str,
    offset: int,
    message: str,
) -> None:
    if not suppressed(text, offset, rule):
        findings.append(Finding(severity, rule, path, line_number(text, offset), message))


def declarations(body: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for match in DECLARATION.finditer(body):
        result.setdefault(match.group("name").strip().lower(), []).append(match.group("value").strip())
    return result


def interactive_selector(selectors: str) -> bool:
    for selector in selectors.split(","):
        if "::before" in selector or "::after" in selector:
            continue
        compounds = [part for part in re.split(r"\s+|[>+~]", selector.strip()) if part]
        if not compounds:
            continue
        target = compounds[-1]
        if re.search(r"__(?:mark|track|thumb|fill|icon|spinner|label|meta|status|head|copy|actions|group|list)\b", target):
            continue
        if INTERACTIVE.search(target):
            return True
    return False


def has_descendant_selector(selectors: str) -> bool:
    for selector in selectors.split(","):
        cleaned = re.sub(r"\s*([>+~])\s*", r"\1", selector.strip())
        if re.search(r"[^>+~\s]\s+[^>+~\s]", cleaned):
            return True
    return False


def lint_css(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    for match in CSS_RULE.finditer(text):
        selectors = re.sub(r"/\*.*?\*/", "", match.group("selectors"), flags=re.DOTALL).strip()
        body = match.group("body")
        props = declarations(body)
        is_interactive = interactive_selector(selectors)
        selector_display = " ".join(selectors.split())[:120]

        if "opacity" in props and any(value.strip() in {"0", "0.0", ".0"} for value in props["opacity"]):
            if "[hidden]" not in selectors and "aria-hidden" not in selectors:
                add(findings, "ERROR", "visible-content", path, text, match.start(), f"opacity-zero content in {selector_display}")

        if ":hover" in selectors and "transform" in props:
            values = ", ".join(props["transform"])
            if values.strip() != "none":
                add(findings, "ERROR", "hover-movement", path, text, match.start(), f"hover changes transform ({values}) in {selector_display}")

        if is_interactive:
            for property_name in ("height", "min-height"):
                for value in props.get(property_name, []):
                    literal = PIXEL.fullmatch(value.strip())
                    if literal and 0 < float(literal.group(1)) < 44:
                        add(findings, "ERROR", "target-size", path, text, match.start(), f"{property_name} {value} is below 44px in {selector_display}")
            for value in props.get("outline", []):
                if re.fullmatch(r"(?:0|none)(?:\s*!important)?", value.strip(), re.IGNORECASE):
                    add(findings, "WARN", "focus-suppression", path, text, match.start(), f"outline suppressed in {selector_display}; prove one replacement geometry")

        if ":focus" in selectors or ":focus-visible" in selectors or ":focus-within" in selectors:
            for value in props.get("outline", []):
                width = PIXEL.search(value)
                if width and 0 < float(width.group(1)) < 2:
                    add(findings, "ERROR", "focus-width", path, text, match.start(), f"focus outline is thinner than 2px in {selector_display}")

        layout_properties = {
            "margin", "margin-top", "margin-right", "margin-bottom", "margin-left", "margin-inline", "margin-block",
            "padding", "padding-top", "padding-right", "padding-bottom", "padding-left", "padding-inline", "padding-block",
            "gap", "row-gap", "column-gap",
        }
        if not selectors.startswith(":root") and not selectors.startswith("[data-"):
            for property_name in layout_properties:
                for value in props.get(property_name, []):
                    for pixel in PIXEL.finditer(value):
                        number = abs(float(pixel.group(1)))
                        if number not in LAYOUT_SCALE:
                            add(findings, "ERROR", "spacing-scale", path, text, match.start(), f"{property_name} uses {pixel.group(0)} outside the layout scale in {selector_display}")

        boundary_count = sum(
            1
            for name in ("border", "border-top", "border-right", "border-bottom", "border-left", "box-shadow", "outline")
            if name in props and any(value.strip() not in {"0", "none", "transparent"} for value in props[name])
        )
        if boundary_count >= 3:
            add(findings, "WARN", "boundary-density", path, text, match.start(), f"{boundary_count} edge mechanisms in {selector_display}; name each job")
        if boundary_count and has_descendant_selector(selectors) and not any(token in selectors for token in (":hover", ":focus", ":active", "[aria-", "::")):
            add(findings, "WARN", "nested-boundary", path, text, match.start(), f"descendant draws a boundary in {selector_display}; check for nested bezels")

        for value in props.get("font-size", []):
            literal = PIXEL.fullmatch(value.strip())
            if literal and float(literal.group(1)) < 12:
                add(findings, "ERROR", "tiny-type", path, text, match.start(), f"font-size {value} is below 12px in {selector_display}")
            elif literal and float(literal.group(1)) < 14:
                add(findings, "WARN", "small-type", path, text, match.start(), f"font-size {value} is below the 14px essential-text baseline in {selector_display}")

        if "text-transform" in props and any("uppercase" in value for value in props["text-transform"]):
            if "letter-spacing" in props:
                add(findings, "WARN", "label-costume", path, text, match.start(), f"tracked uppercase treatment in {selector_display}; confirm it is not a repeated house costume")
    return findings


def lint_markup(path: Path, text: str, forbid_native: bool) -> list[Finding]:
    findings: list[Finding] = []
    for match in re.finditer(r"<button\b(?P<attrs>[^>]*)>", text, re.IGNORECASE):
        attrs = match.group("attrs")
        if not re.search(r"\btype\s*=", attrs, re.IGNORECASE):
            add(findings, "ERROR", "button-type", path, text, match.start(), "button is missing an explicit type")

    if forbid_native:
        patterns = [
            (r"<select\b", "native select"),
            (r"<input\b[^>]*\btype\s*=\s*[\"'](?:checkbox|radio|range)[\"']", "native checkbox/radio/range"),
        ]
        for pattern, label in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                add(findings, "ERROR", "native-control", path, text, match.start(), f"{label} is forbidden by the selected product profile")

    for match in re.finditer(r"\bstyle\s*=\s*[\"'](?P<style>[^\"']+)[\"']", text, re.IGNORECASE):
        style = match.group("style")
        for declaration in DECLARATION.finditer(style):
            name = declaration.group("name").lower()
            if name in {"margin", "margin-top", "margin-right", "margin-bottom", "margin-left", "padding", "gap"}:
                for pixel in PIXEL.finditer(declaration.group("value")):
                    if abs(float(pixel.group(1))) not in LAYOUT_SCALE:
                        add(findings, "ERROR", "spacing-scale", path, text, match.start(), f"inline {name} uses {pixel.group(0)} outside the layout scale")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--forbid-native-controls", action="store_true")
    parser.add_argument("--warnings-as-errors", action="store_true")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    files = list(iter_files(args.paths))
    findings: list[Finding] = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            findings.append(Finding("ERROR", "read", path, 1, str(error)))
            continue
        findings.extend(lint_css(path, css_source(path, text)))
        if path.suffix.lower() in HTML_EXTENSIONS:
            findings.extend(lint_markup(path, text, args.forbid_native_controls))

    findings.sort(key=lambda item: (str(item.path), item.line, item.severity, item.rule))
    if args.format == "json":
        print(json.dumps([finding.__dict__ | {"path": str(finding.path)} for finding in findings], indent=2))
    else:
        for finding in findings:
            print(finding.text())
        counts = {severity: sum(finding.severity == severity for finding in findings) for severity in ("ERROR", "WARN")}
        print(f"KOKUEN UI lint: {len(files)} files, {counts['ERROR']} errors, {counts['WARN']} warnings")
    failed = any(finding.severity == "ERROR" for finding in findings)
    failed = failed or (args.warnings_as_errors and bool(findings))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

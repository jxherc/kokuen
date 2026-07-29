#!/usr/bin/env python3
"""Positive and negative regression tests for KOKUEN deterministic validators."""

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", *arguments],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


class ValidatorTests(unittest.TestCase):
    def test_repository_sources_pass(self) -> None:
        commands = [
            ("scripts/validate_theme.py", "tokens/kokuen.tokens.json"),
            ("scripts/validate_contracts.py", "contracts"),
            ("scripts/validate_figma_manifest.py",),
            (
                "scripts/lint_ui_rules.py",
                "kokuen.css",
                "preview.html",
                "designs/kokuen-visual-template/Universal UI Template.html",
                "tests/forward-fixtures",
                "--forbid-native-controls",
                "--warnings-as-errors",
            ),
        ]
        for command in commands:
            with self.subTest(command=command):
                result = run(*command)
                self.assertEqual(
                    result.returncode,
                    0,
                    msg=f"{result.stdout}\n{result.stderr}",
                )

    def test_theme_validator_rejects_alias_cycle(self) -> None:
        document = json.loads((ROOT / "tokens/kokuen.tokens.json").read_text())
        document["space"]["4"]["$value"] = "{space.8}"
        document["space"]["8"]["$value"] = "{space.4}"
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", dir=ROOT / "tokens", delete=True
        ) as handle:
            json.dump(document, handle)
            handle.flush()
            result = run("scripts/validate_theme.py", handle.name)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cycle", (result.stdout + result.stderr).lower())

    def test_component_validator_rejects_false_stable_claim(self) -> None:
        document = json.loads(
            (ROOT / "contracts/kokuen.components.json").read_text()
        )
        document["components"][0]["status"] = "stable"
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", dir=ROOT / "contracts", delete=True
        ) as handle:
            json.dump(document, handle)
            handle.flush()
            result = run("scripts/validate_contracts.py", handle.name)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires mapped figma", (result.stdout + result.stderr).lower())

    def test_ui_linter_rejects_small_moving_button(self) -> None:
        fixture = """<!doctype html>
<html><head><style>
.test-button { min-height: 32px; padding: 6px; }
.test-button:hover { transform: translateY(-2px); }
</style></head><body><button class=\"test-button\" type=\"button\">Test</button></body></html>
"""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".html", dir=ROOT / "tests", delete=True
        ) as handle:
            handle.write(fixture)
            handle.flush()
            result = run("scripts/lint_ui_rules.py", handle.name)
        output = (result.stdout + result.stderr).lower()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("target-size", output)
        self.assertIn("hover-movement", output)
        self.assertIn("spacing-scale", output)

    def test_figma_manifest_rejects_property_drift(self) -> None:
        document = json.loads((ROOT / "figma/kokuen.library.json").read_text())
        document["components"][0]["properties"] = ["OpaqueCombination"]
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", dir=ROOT / "figma", delete=True
        ) as handle:
            json.dump(document, handle)
            handle.flush()
            result = run("scripts/validate_figma_manifest.py", handle.name)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("properties differ", (result.stdout + result.stderr).lower())


if __name__ == "__main__":
    unittest.main()

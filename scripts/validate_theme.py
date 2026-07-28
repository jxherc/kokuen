#!/usr/bin/env python3
"""Validate a small DTCG-aligned KOKUEN token file without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ALIAS = re.compile(r"^\{([A-Za-z0-9_.-]+)\}$")


def flatten(node: dict[str, Any], prefix: str = "") -> dict[str, dict[str, Any]]:
    tokens: dict[str, dict[str, Any]] = {}
    for name, value in node.items():
        if name.startswith("$"):
            continue
        path = f"{prefix}.{name}" if prefix else name
        if isinstance(value, dict) and "$value" in value:
            tokens[path] = value
        elif isinstance(value, dict):
            tokens.update(flatten(value, path))
    return tokens


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_theme.py PATH_TO_TOKENS_JSON", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        document = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        print(f"Invalid token file: {error}", file=sys.stderr)
        return 1
    if not isinstance(document, dict):
        print("Token document must be a JSON object.", file=sys.stderr)
        return 1

    tokens = flatten(document)
    errors: list[str] = []
    aliases: dict[str, str] = {}
    for name, token in tokens.items():
        if not token.get("$type"):
            errors.append(f"{name}: missing $type")
        if "$value" not in token:
            errors.append(f"{name}: missing $value")
            continue
        value = token["$value"]
        if isinstance(value, str):
            match = ALIAS.match(value)
            if match:
                target = match.group(1)
                if target not in tokens:
                    errors.append(f"{name}: unresolved alias {value}")
                else:
                    aliases[name] = target
                    if token.get("$type") != tokens[target].get("$type"):
                        errors.append(
                            f"{name}: $type {token.get('$type')} does not match alias target {target} "
                            f"({tokens[target].get('$type')})"
                        )

    for origin in aliases:
        visited: list[str] = []
        current = origin
        while current in aliases:
            if current in visited:
                cycle = " -> ".join(visited[visited.index(current):] + [current])
                errors.append(f"alias cycle: {cycle}")
                break
            visited.append(current)
            current = aliases[current]

    if errors:
        print("Theme token validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Theme token validation passed: {len(tokens)} tokens and {len(aliases)} aliases in {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

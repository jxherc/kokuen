#!/usr/bin/env python3
"""Validate the KOKUEN DTCG-aligned token contract without third-party dependencies."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path
from typing import Any

ALIAS = re.compile(r"^\{([A-Za-z0-9_.-]+)\}$")
HEX_COLOR = re.compile(r"^#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
DIMENSION = re.compile(r"^-?(?:0|[0-9]+(?:\.[0-9]+)?)(?:px|rem|em|%|vh|vw)$")
DURATION = re.compile(r"^(?:0|[0-9]+(?:\.[0-9]+)?)(?:ms|s)$")
SUPPORTED_TYPES = {
    "color",
    "dimension",
    "duration",
    "number",
    "fontFamily",
    "fontWeight",
    "cubicBezier",
    "string",
}


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


def alias_target(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    match = ALIAS.fullmatch(value)
    return match.group(1) if match else None


def validate_literal(name: str, token_type: str, value: Any, errors: list[str]) -> None:
    if alias_target(value):
        return
    if token_type == "color":
        if not isinstance(value, str) or not HEX_COLOR.fullmatch(value):
            errors.append(f"{name}: color must be #RRGGBB or #RRGGBBAA")
    elif token_type == "dimension":
        if not isinstance(value, str) or not DIMENSION.fullmatch(value):
            errors.append(f"{name}: dimension must include a supported CSS unit")
    elif token_type == "duration":
        if not isinstance(value, str) or not DURATION.fullmatch(value):
            errors.append(f"{name}: duration must use ms or s")
    elif token_type == "number":
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            errors.append(f"{name}: number must be finite")
    elif token_type == "fontFamily":
        valid = isinstance(value, str) and bool(value.strip())
        valid = valid or (
            isinstance(value, list)
            and bool(value)
            and all(isinstance(item, str) and item.strip() for item in value)
        )
        if not valid:
            errors.append(f"{name}: fontFamily must be a non-empty string or string list")
    elif token_type == "fontWeight":
        valid_number = isinstance(value, int) and not isinstance(value, bool) and 1 <= value <= 1000
        valid_name = isinstance(value, str) and value in {
            "thin", "extralight", "light", "normal", "medium", "semibold", "bold", "extrabold", "black"
        }
        if not (valid_number or valid_name):
            errors.append(f"{name}: fontWeight must be 1..1000 or a supported weight name")
    elif token_type == "cubicBezier":
        valid = (
            isinstance(value, list)
            and len(value) == 4
            and all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in value)
            and 0 <= value[0] <= 1
            and 0 <= value[2] <= 1
        )
        if not valid:
            errors.append(f"{name}: cubicBezier must be four numbers with x values from 0 to 1")
    elif token_type == "string" and not isinstance(value, str):
        errors.append(f"{name}: string token must contain a string")


def resolve(
    name: str,
    tokens: dict[str, dict[str, Any]],
    overrides: dict[str, Any] | None = None,
    trail: tuple[str, ...] = (),
) -> Any:
    if name in trail:
        raise ValueError("alias cycle: " + " -> ".join((*trail, name)))
    if name not in tokens:
        raise ValueError(f"unknown token {name}")
    value = overrides[name] if overrides and name in overrides else tokens[name]["$value"]
    target = alias_target(value)
    if target:
        return resolve(target, tokens, overrides, (*trail, name))
    return value


def parse_rgb(value: str) -> tuple[float, float, float]:
    match = HEX_COLOR.fullmatch(value)
    if not match or len(match.group(1)) != 6:
        raise ValueError(f"contrast color must be opaque #RRGGBB, got {value!r}")
    raw = match.group(1)
    return tuple(int(raw[index:index + 2], 16) / 255 for index in (0, 2, 4))  # type: ignore[return-value]


def luminance(value: str) -> float:
    channels = []
    for channel in parse_rgb(value):
        channels.append(channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast_ratio(foreground: str, background: str) -> float:
    first, second = luminance(foreground), luminance(background)
    lighter, darker = max(first, second), min(first, second)
    return (lighter + 0.05) / (darker + 0.05)


def validate_modes(
    extension: dict[str, Any], tokens: dict[str, dict[str, Any]], errors: list[str]
) -> tuple[int, dict[str, dict[str, dict[str, Any]]]]:
    axes = extension.get("modeAxes")
    required = extension.get("requiredModeTokens")
    defaults = extension.get("defaultModes")
    if not isinstance(axes, dict) or not axes:
        errors.append("$extensions.kokuen.modeAxes must be a non-empty object")
        return 0, {}
    if not isinstance(required, dict):
        errors.append("$extensions.kokuen.requiredModeTokens must be an object")
        required = {}
    if not isinstance(defaults, dict):
        errors.append("$extensions.kokuen.defaultModes must be an object")
        defaults = {}

    mode_count = 0
    normalized: dict[str, dict[str, dict[str, Any]]] = {}
    for axis_name, modes in axes.items():
        if not isinstance(modes, dict) or not modes:
            errors.append(f"mode axis {axis_name}: expected a non-empty mode object")
            continue
        normalized[axis_name] = {}
        if defaults.get(axis_name) not in modes:
            errors.append(f"mode axis {axis_name}: default mode {defaults.get(axis_name)!r} is missing")
        required_names = required.get(axis_name, [])
        if not isinstance(required_names, list) or not all(isinstance(item, str) for item in required_names):
            errors.append(f"mode axis {axis_name}: required token list is invalid")
            required_names = []
        for mode_name, overrides in modes.items():
            mode_count += 1
            if not isinstance(overrides, dict):
                errors.append(f"mode {axis_name}.{mode_name}: overrides must be an object")
                continue
            normalized[axis_name][mode_name] = overrides
            missing = [name for name in required_names if name not in overrides]
            if missing:
                errors.append(f"mode {axis_name}.{mode_name}: missing required overrides {', '.join(missing)}")
            for token_name, value in overrides.items():
                if token_name not in tokens:
                    errors.append(f"mode {axis_name}.{mode_name}: unknown token {token_name}")
                    continue
                target = alias_target(value)
                if target:
                    if target not in tokens:
                        errors.append(f"mode {axis_name}.{mode_name}.{token_name}: unresolved alias {{{target}}}")
                    elif tokens[token_name].get("$type") != tokens[target].get("$type"):
                        errors.append(
                            f"mode {axis_name}.{mode_name}.{token_name}: type does not match {target}"
                        )
                else:
                    validate_literal(
                        f"mode {axis_name}.{mode_name}.{token_name}",
                        str(tokens[token_name].get("$type")),
                        value,
                        errors,
                    )
            for token_name in overrides:
                try:
                    resolve(token_name, tokens, overrides)
                except ValueError as error:
                    errors.append(f"mode {axis_name}.{mode_name}: {error}")
    return mode_count, normalized


def validate_contrast_pairs(
    extension: dict[str, Any],
    tokens: dict[str, dict[str, Any]],
    modes: dict[str, dict[str, dict[str, Any]]],
    errors: list[str],
) -> int:
    pairs = extension.get("contrastPairs")
    if not isinstance(pairs, list) or not pairs:
        errors.append("$extensions.kokuen.contrastPairs must be a non-empty list")
        return 0
    checked = 0
    theme_modes = modes.get("theme", {})
    for index, pair in enumerate(pairs):
        label = f"contrastPairs[{index}]"
        if not isinstance(pair, dict):
            errors.append(f"{label}: expected an object")
            continue
        name = pair.get("name", label)
        foreground = pair.get("foreground")
        background = pair.get("background")
        minimum = pair.get("minimum")
        requested_modes = pair.get("themeModes", list(theme_modes))
        if foreground not in tokens or background not in tokens:
            errors.append(f"{name}: foreground and background must name existing tokens")
            continue
        if tokens[foreground].get("$type") != "color" or tokens[background].get("$type") != "color":
            errors.append(f"{name}: contrast pair tokens must have color type")
            continue
        if not isinstance(minimum, (int, float)) or isinstance(minimum, bool) or minimum <= 1:
            errors.append(f"{name}: minimum must be a number greater than 1")
            continue
        if not isinstance(requested_modes, list) or not requested_modes:
            errors.append(f"{name}: themeModes must be a non-empty list")
            continue
        for mode_name in requested_modes:
            if mode_name not in theme_modes:
                errors.append(f"{name}: unknown theme mode {mode_name}")
                continue
            try:
                foreground_value = resolve(foreground, tokens, theme_modes[mode_name])
                background_value = resolve(background, tokens, theme_modes[mode_name])
                ratio = contrast_ratio(str(foreground_value), str(background_value))
            except ValueError as error:
                errors.append(f"{name} [{mode_name}]: {error}")
                continue
            checked += 1
            if ratio + 1e-9 < float(minimum):
                errors.append(
                    f"{name} [{mode_name}]: contrast {ratio:.2f}:1 is below {float(minimum):.2f}:1"
                )
    return checked


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_theme.py PATH_TO_TOKENS_JSON", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
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
        token_type = token.get("$type")
        if not token_type:
            errors.append(f"{name}: missing $type")
            continue
        if token_type not in SUPPORTED_TYPES:
            errors.append(f"{name}: unsupported $type {token_type}")
        if "$value" not in token:
            errors.append(f"{name}: missing $value")
            continue
        value = token["$value"]
        target = alias_target(value)
        if target:
            if target not in tokens:
                errors.append(f"{name}: unresolved alias {value}")
            else:
                aliases[name] = target
                if token_type != tokens[target].get("$type"):
                    errors.append(
                        f"{name}: $type {token_type} does not match alias target {target} "
                        f"({tokens[target].get('$type')})"
                    )
        else:
            validate_literal(name, str(token_type), value, errors)

    for name in tokens:
        try:
            resolve(name, tokens)
        except ValueError as error:
            errors.append(str(error))

    extension = document.get("$extensions", {}).get("kokuen")
    if not isinstance(extension, dict):
        errors.append("missing $extensions.kokuen contract")
        extension = {}
    mode_count, modes = validate_modes(extension, tokens, errors)
    contrast_count = validate_contrast_pairs(extension, tokens, modes, errors)

    errors = list(dict.fromkeys(errors))
    if errors:
        print("Theme token validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(
        f"Theme token validation passed: {len(tokens)} tokens, {len(aliases)} aliases, "
        f"{mode_count} modes, and {contrast_count} contrast checks in {path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

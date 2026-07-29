#!/usr/bin/env python3
"""Validate KOKUEN component contracts without external dependencies."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ID_PATTERN = re.compile(r"^[a-z][a-z0-9-]*(?:\.[a-z][a-z0-9-]*)+$")
FIXTURE_PATTERN = re.compile(r"^fixture-[a-z0-9-]+$")
FIXTURE_ATTRIBUTE = re.compile(r"\bdata-fixtures\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE)
STATUSES = {"draft", "candidate", "stable", "deprecated"}
FIGMA_STATUSES = {"planned", "mapped", "blocked", "not-applicable"}
BOUNDARY_JOBS = {"input affordance", "state", "containment", "clipping", "separation", "none"}
REQUIRED_COMPONENT_FIELDS = {
    "id", "status", "userJob", "code", "figma", "anatomy", "variants", "states", "tokens",
    "boundary", "accessibility", "keyboard", "behavior", "content", "responsive", "dataStates",
    "fixtures", "exceptions",
}
REQUIRED_NESTED_FIELDS = {
    "code": {"path", "api"},
    "figma": {"status", "componentKey", "propertyMapping"},
    "boundary": {"job", "rationale", "restingOwner", "focusOwner", "widthBehavior"},
    "accessibility": {"role", "name", "description", "state", "errorRelationship"},
    "keyboard": {"keys", "focusEntry", "focusExit", "focusReturn"},
    "behavior": {"pointer", "touch", "disabled", "loading", "repeatActivation"},
    "content": {"limits", "localization", "overflow"},
    "responsive": {"density", "reflow"},
}
REQUIRED_KEYS = {
    "action.button": {"Enter", "Space"},
    "action.icon": {"Enter", "Space"},
    "choice.checkbox": {"Space"},
    "choice.radio-group": {"ArrowUp", "ArrowDown", "Home", "End", "Space"},
    "choice.switch": {"Space"},
    "choice.slider": {"Arrow keys", "Home", "End"},
    "choice.select": {"ArrowDown", "ArrowUp", "Home", "End", "Enter", "Escape"},
    "navigation.tabs": {"ArrowLeft", "ArrowRight", "Home", "End"},
    "navigation.menu": {"ArrowDown", "ArrowUp", "Home", "End", "Enter", "Escape"},
    "overlay.dialog": {"Tab", "Shift+Tab", "Escape"},
    "overlay.confirmation": {"Tab", "Shift+Tab", "Escape"},
    "command.universal": {"ArrowDown", "ArrowUp", "Home", "End", "Enter", "Escape", "Tab", "Shift+Tab"},
}
REQUIRED_STATES = {
    "action.button": {"focus-visible", "busy", "disabled"},
    "field.text": {"focus-visible", "invalid", "disabled"},
    "choice.radio-group": {"checked", "unchecked", "focus-visible", "disabled"},
    "choice.select": {"closed", "open", "active-option", "selected-option", "disabled-option"},
    "navigation.tabs": {"selected", "focus-visible", "disabled"},
    "navigation.menu": {"closed", "open", "focused-item", "disabled-item"},
    "overlay.dialog": {"open", "focus-contained", "error"},
    "command.universal": {"open", "loading", "empty", "error", "unavailable", "permission"},
    "ai.composer": {"pending", "streaming", "stopped", "failed"},
    "ai.response": {"streaming", "completed", "stopped", "partial", "failed"},
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"{path}: invalid JSON: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"{path}: root must be an object")
    return value


def flatten_tokens(node: dict[str, Any], prefix: str = "") -> set[str]:
    names: set[str] = set()
    for name, value in node.items():
        if name.startswith("$"):
            continue
        path = f"{prefix}.{name}" if prefix else name
        if isinstance(value, dict) and "$value" in value:
            names.add(path)
        elif isinstance(value, dict):
            names.update(flatten_tokens(value, path))
    return names


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_string_list(component_id: str, field: str, value: Any, errors: list[str]) -> list[str]:
    if not isinstance(value, list) or not value:
        errors.append(f"{component_id}.{field}: must be a non-empty list")
        return []
    if not all(nonempty_string(item) for item in value):
        errors.append(f"{component_id}.{field}: entries must be non-empty strings")
        return []
    if len(value) != len(set(value)):
        errors.append(f"{component_id}.{field}: duplicate entries")
    return value


def has_boundary_job(value: str) -> bool:
    lower = value.lower()
    return any(job in lower for job in BOUNDARY_JOBS)


def validate_component(
    component: Any,
    index: int,
    root: Path,
    tokens: set[str],
    fixture_owners: dict[str, str],
    errors: list[str],
    require_stable: bool,
) -> str | None:
    label = f"components[{index}]"
    if not isinstance(component, dict):
        errors.append(f"{label}: must be an object")
        return None
    component_id = component.get("id")
    if not nonempty_string(component_id) or not ID_PATTERN.fullmatch(component_id):
        errors.append(f"{label}.id: must match category.component-name")
        component_id = label
    missing = sorted(REQUIRED_COMPONENT_FIELDS - component.keys())
    if missing:
        errors.append(f"{component_id}: missing fields {', '.join(missing)}")
    status = component.get("status")
    if status not in STATUSES:
        errors.append(f"{component_id}.status: invalid status {status!r}")
    if require_stable and status != "stable":
        errors.append(f"{component_id}.status: expected stable for release validation")
    if not nonempty_string(component.get("userJob")):
        errors.append(f"{component_id}.userJob: must be a non-empty string")

    for field, required in REQUIRED_NESTED_FIELDS.items():
        nested = component.get(field)
        if not isinstance(nested, dict):
            errors.append(f"{component_id}.{field}: must be an object")
            continue
        nested_missing = sorted(required - nested.keys())
        if nested_missing:
            errors.append(f"{component_id}.{field}: missing {', '.join(nested_missing)}")
        for key in required - {"componentKey", "propertyMapping", "api", "keys"}:
            if key in nested and not nonempty_string(nested[key]):
                errors.append(f"{component_id}.{field}.{key}: must be a non-empty string")

    code = component.get("code", {})
    if isinstance(code, dict):
        path_value = code.get("path")
        if nonempty_string(path_value) and not (root / path_value).exists():
            errors.append(f"{component_id}.code.path: missing file {path_value}")
        validate_string_list(component_id, "code.api", code.get("api"), errors)

    figma = component.get("figma", {})
    if isinstance(figma, dict):
        figma_status = figma.get("status")
        if figma_status not in FIGMA_STATUSES:
            errors.append(f"{component_id}.figma.status: invalid status {figma_status!r}")
        key = figma.get("componentKey")
        mapping = figma.get("propertyMapping")
        if not isinstance(mapping, dict) or not mapping or not all(
            nonempty_string(name) and nonempty_string(value) for name, value in mapping.items()
        ):
            errors.append(f"{component_id}.figma.propertyMapping: must contain non-empty mappings")
        if status == "stable" and (figma_status != "mapped" or not nonempty_string(key)):
            errors.append(f"{component_id}: stable contract requires mapped Figma component key")

    list_fields = ["anatomy", "variants", "states", "tokens", "dataStates", "fixtures"]
    normalized_lists = {
        field: validate_string_list(component_id, field, component.get(field), errors)
        for field in list_fields
    }
    for token_name in normalized_lists["tokens"]:
        if token_name not in tokens:
            errors.append(f"{component_id}.tokens: unknown token {token_name}")

    keyboard = component.get("keyboard", {})
    keys = validate_string_list(component_id, "keyboard.keys", keyboard.get("keys") if isinstance(keyboard, dict) else None, errors)
    missing_keys = REQUIRED_KEYS.get(component_id, set()) - set(keys)
    if missing_keys:
        errors.append(f"{component_id}.keyboard.keys: missing {', '.join(sorted(missing_keys))}")
    missing_states = REQUIRED_STATES.get(component_id, set()) - set(normalized_lists["states"])
    if missing_states:
        errors.append(f"{component_id}.states: missing {', '.join(sorted(missing_states))}")

    boundary = component.get("boundary", {})
    if isinstance(boundary, dict):
        job = boundary.get("job")
        if nonempty_string(job) and not has_boundary_job(job):
            errors.append(f"{component_id}.boundary.job: must name an allowed boundary job")
        if nonempty_string(boundary.get("rationale")) and len(boundary["rationale"].strip()) < 20:
            errors.append(f"{component_id}.boundary.rationale: must explain the decision")

    exceptions = component.get("exceptions")
    if not isinstance(exceptions, list) or not all(nonempty_string(item) for item in exceptions):
        errors.append(f"{component_id}.exceptions: must be a string list, empty when none")

    for fixture in normalized_lists["fixtures"]:
        if not FIXTURE_PATTERN.fullmatch(fixture):
            errors.append(f"{component_id}.fixtures: invalid fixture ID {fixture}")
        owner = fixture_owners.get(fixture)
        if owner and owner != component_id:
            errors.append(f"fixture {fixture}: owned by both {owner} and {component_id}")
        fixture_owners[fixture] = component_id
    return component_id


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Contract directory or component registry JSON")
    parser.add_argument("--tokens", type=Path, default=Path("tokens/kokuen.tokens.json"))
    parser.add_argument(
        "--fixture-document",
        type=Path,
        default=Path("designs/kokuen-visual-template/Universal UI Template.html"),
    )
    parser.add_argument("--require-stable", action="store_true")
    args = parser.parse_args()

    registry_path = args.path / "kokuen.components.json" if args.path.is_dir() else args.path
    root = registry_path.parent.parent
    token_path = args.tokens if args.tokens.is_absolute() else root / args.tokens
    errors: list[str] = []
    try:
        registry = load_json(registry_path)
        token_document = load_json(token_path)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    if registry.get("version") != "5.0.0":
        errors.append("registry.version: expected 5.0.0")
    defaults = registry.get("defaults")
    if not isinstance(defaults, dict):
        errors.append("registry.defaults: must be an object")
    else:
        if defaults.get("minimumTarget") != "44px":
            errors.append("registry.defaults.minimumTarget: expected 44px")
        if defaults.get("contentVisibleByDefault") is not True:
            errors.append("registry.defaults.contentVisibleByDefault: expected true")
        if defaults.get("colorOnlyStateAllowed") is not False:
            errors.append("registry.defaults.colorOnlyStateAllowed: expected false")
        if defaults.get("hoverMovementAllowed") is not False:
            errors.append("registry.defaults.hoverMovementAllowed: expected false")

    components = registry.get("components")
    if not isinstance(components, list) or not components:
        errors.append("registry.components: must be a non-empty list")
        components = []
    tokens = flatten_tokens(token_document)
    fixture_owners: dict[str, str] = {}
    ids: list[str] = []
    for index, component in enumerate(components):
        component_id = validate_component(
            component, index, root, tokens, fixture_owners, errors, args.require_stable
        )
        if component_id:
            ids.append(component_id)
    duplicates = [name for name, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append("duplicate component IDs: " + ", ".join(sorted(duplicates)))

    fixture_document = args.fixture_document if args.fixture_document.is_absolute() else root / args.fixture_document
    documented_fixtures: set[str] = set()
    try:
        fixture_text = fixture_document.read_text(encoding="utf-8")
        for match in FIXTURE_ATTRIBUTE.finditer(fixture_text):
            documented_fixtures.update(match.group(1).split())
    except OSError as error:
        errors.append(f"fixture document {fixture_document}: {error}")
    missing_fixtures = sorted(set(fixture_owners) - documented_fixtures)
    extra_fixtures = sorted(documented_fixtures - set(fixture_owners))
    if missing_fixtures:
        errors.append("fixture document missing IDs: " + ", ".join(missing_fixtures))
    if extra_fixtures:
        errors.append("fixture document has unknown IDs: " + ", ".join(extra_fixtures))

    errors = list(dict.fromkeys(errors))
    if errors:
        print("Component contract validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1

    statuses = Counter(component["status"] for component in components)
    status_summary = ", ".join(f"{count} {name}" for name, count in sorted(statuses.items()))
    print(
        f"Component contract validation passed: {len(components)} components ({status_summary}), "
        f"{len(fixture_owners)} fixture IDs covered by {fixture_document}, and {len(tokens)} known tokens "
        f"in {registry_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

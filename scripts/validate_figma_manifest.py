#!/usr/bin/env python3
"""Validate the Figma synchronization plan against KOKUEN tokens and contracts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"{path}: invalid JSON: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"{path}: root must be an object")
    return value


def duplicate_values(values: list[str]) -> list[str]:
    return sorted({value for value in values if values.count(value) > 1})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "manifest",
        nargs="?",
        type=Path,
        default=Path("figma/kokuen.library.json"),
    )
    parser.add_argument(
        "--tokens", type=Path, default=Path("tokens/kokuen.tokens.json")
    )
    parser.add_argument(
        "--components", type=Path, default=Path("contracts/kokuen.components.json")
    )
    args = parser.parse_args()

    root = args.manifest.resolve().parent.parent
    token_path = args.tokens if args.tokens.is_absolute() else root / args.tokens
    component_path = (
        args.components if args.components.is_absolute() else root / args.components
    )
    errors: list[str] = []

    try:
        manifest = load_object(args.manifest)
        tokens = load_object(token_path)
        registry = load_object(component_path)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    if manifest.get("version") != "5.0.0":
        errors.append("manifest.version must be 5.0.0")

    file_record = manifest.get("file")
    if not isinstance(file_record, dict):
        errors.append("manifest.file must be an object")
        file_record = {}
    if file_record.get("key") != "dMpK3ZOhraefh9L6m4BgBi":
        errors.append("manifest.file.key does not match the canonical KOKUEN file")
    sync_status = file_record.get("syncStatus")
    if sync_status not in {"planned", "blocked", "synced", "drifted"}:
        errors.append("manifest.file.syncStatus is invalid")

    source_paths = manifest.get("sourceOfTruth")
    if not isinstance(source_paths, dict) or not source_paths:
        errors.append("manifest.sourceOfTruth must contain repository paths")
    else:
        for label, path_value in source_paths.items():
            if not isinstance(path_value, str) or not (root / path_value).exists():
                errors.append(f"manifest.sourceOfTruth.{label} is missing: {path_value}")

    collections = manifest.get("collections")
    if not isinstance(collections, list):
        errors.append("manifest.collections must be an array")
        collections = []
    collection_names = [item.get("name") for item in collections if isinstance(item, dict)]
    if len(collection_names) != len(collections) or not all(
        isinstance(name, str) and name for name in collection_names
    ):
        errors.append("every collection needs a name")
    if duplicate_values(collection_names):
        errors.append("duplicate Figma collection names")

    mode_axes = (
        tokens.get("$extensions", {}).get("kokuen", {}).get("modeAxes", {})
        if isinstance(tokens.get("$extensions"), dict)
        else {}
    )
    collections_by_axis = {
        item.get("axis"): item for item in collections if isinstance(item, dict)
    }
    for axis in ("theme", "contrast", "density"):
        token_modes = mode_axes.get(axis)
        collection = collections_by_axis.get(axis)
        if not isinstance(token_modes, dict):
            errors.append(f"tokens do not define the {axis} mode axis")
            continue
        if not isinstance(collection, dict):
            errors.append(f"manifest is missing the {axis} collection")
            continue
        manifest_modes = collection.get("modes")
        normalized = {
            item.lower() for item in manifest_modes if isinstance(item, str)
        } if isinstance(manifest_modes, list) else set()
        if normalized != set(token_modes):
            errors.append(
                f"{axis} modes differ: manifest {sorted(normalized)}, tokens {sorted(token_modes)}"
            )

    pages = manifest.get("pages")
    if not isinstance(pages, list):
        errors.append("manifest.pages must be an array")
        pages = []
    page_names = [item.get("name") for item in pages if isinstance(item, dict)]
    expected_pages = {"Cover", "Foundations", "Components", "Do and do not", "Stress"}
    if set(page_names) != expected_pages:
        errors.append(
            f"manifest.pages must be exactly {', '.join(sorted(expected_pages))}"
        )
    page_orders = [item.get("order") for item in pages if isinstance(item, dict)]
    if page_orders != list(range(len(pages))):
        errors.append("manifest.pages order must be contiguous and sorted")

    components = manifest.get("components")
    if not isinstance(components, list):
        errors.append("manifest.components must be an array")
        components = []
    manifest_components = {
        item.get("id"): item for item in components if isinstance(item, dict)
    }
    registry_components = {
        item.get("id"): item
        for item in registry.get("components", [])
        if isinstance(item, dict)
    }
    if set(manifest_components) != set(registry_components):
        missing = sorted(set(registry_components) - set(manifest_components))
        extra = sorted(set(manifest_components) - set(registry_components))
        if missing:
            errors.append("Figma manifest missing component IDs: " + ", ".join(missing))
        if extra:
            errors.append("Figma manifest has unknown component IDs: " + ", ".join(extra))
    for component_id in set(manifest_components) & set(registry_components):
        record = manifest_components[component_id]
        contract = registry_components[component_id]
        expected_properties = set(contract.get("figma", {}).get("propertyMapping", {}))
        actual_properties = set(record.get("properties", []))
        if actual_properties != expected_properties:
            errors.append(
                f"{component_id}: Figma properties differ from contract "
                f"({sorted(actual_properties)} vs {sorted(expected_properties)})"
            )

    if sync_status == "blocked":
        if not file_record.get("blocker"):
            errors.append("blocked Figma sync requires a blocker")
        if not file_record.get("unverified"):
            errors.append("blocked Figma sync requires an unverified list")
        for page in pages:
            if page.get("name") != "Cover" and page.get("remoteId") is not None:
                errors.append(f"blocked sync cannot claim remote page ID for {page.get('name')}")
        for component in components:
            if component.get("componentKey") is not None:
                errors.append(
                    f"blocked sync cannot claim component key for {component.get('id')}"
                )
    elif sync_status == "synced":
        if file_record.get("unverified"):
            errors.append("synced Figma file cannot retain unverified discovery items")
        for page in pages:
            if not page.get("remoteId"):
                errors.append(f"synced Figma page lacks remote ID: {page.get('name')}")
        for component in components:
            if not component.get("componentKey"):
                errors.append(
                    f"synced Figma component lacks key: {component.get('id')}"
                )

    stable_components = [
        item for item in registry_components.values() if item.get("status") == "stable"
    ]
    code_connect = manifest.get("codeConnect", {})
    if stable_components and code_connect.get("status") == "deferred":
        errors.append("Code Connect cannot stay deferred after stable contracts exist")

    if errors:
        print("Figma manifest validation failed:", file=sys.stderr)
        for error in dict.fromkeys(errors):
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Figma manifest validation passed: "
        f"{len(collections)} collections, {len(pages)} pages, "
        f"{len(components)} component mappings; remote sync status: {sync_status}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

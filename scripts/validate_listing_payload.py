#!/usr/bin/env python3
"""Offline checks for common TEMU semi-managed listing payload mistakes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

SECRET_KEYS = {"app_key", "app_secret", "access_token", "sign", "authorization_code"}


def walk(value: Any, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield path, key, child
            yield from walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def validate(payload: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    for path, key, value in walk(payload):
        if key.lower() in SECRET_KEYS:
            errors.append(f"{path}.{key}: credentials/signatures must not be stored in payload files")
        lower = key.lower()
        if lower.endswith("price") and isinstance(value, float):
            warnings.append(f"{path}.{key}: confirm the API expects an integer minor-unit price")
        if lower in {"weight", "weightmg", "weight_mg"} and isinstance(value, (int, float)) and value <= 0:
            errors.append(f"{path}.{key}: weight must be positive")

    title = payload.get("goodsName") or payload.get("title")
    if not isinstance(title, str) or not title.strip():
        errors.append("$: missing non-empty product title (`goodsName` or `title`)")
    elif len(title) > 250:
        errors.append(f"$: title has {len(title)} characters; confirm and reduce to the current platform limit")

    external_code = payload.get("extCode") or payload.get("externalCode")
    if not external_code:
        warnings.append("$: no stable external code found; duplicate reconciliation may be difficult")

    decorations = payload.get("goodsLayerDecorationReqs")
    if isinstance(decorations, list):
        for i, item in enumerate(decorations):
            if isinstance(item, dict) and (not item.get("width") or not item.get("height")):
                errors.append(f"$.goodsLayerDecorationReqs[{i}]: image width and height are required")

    category_keys = [f"cat{i}" for i in range(1, 11)]
    present = [key for key in category_keys if key in payload]
    if present and present != category_keys:
        warnings.append("$: category path is partial; include cat1 through cat10 with required zero placeholders")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("payload", help="UTF-8 JSON payload to validate")
    args = parser.parse_args()
    data = json.loads(Path(args.payload).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("Payload must be a JSON object")
    errors, warnings = validate(data)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Validation complete: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())


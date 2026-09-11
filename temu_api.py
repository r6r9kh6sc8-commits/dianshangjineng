#!/usr/bin/env python3
"""Small TEMU Open API caller that keeps credentials out of files and logs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

DEFAULT_ENDPOINT = "https://openapi-b-us.temu.com/openapi/router"
MUTATION_MARKERS = (".add", ".create", ".edit", ".update", ".upload", ".delete", ".submit")


def compact(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def sign_request(params: dict[str, Any], secret: str) -> str:
    filtered = {k: v for k, v in params.items() if k != "sign" and v is not None}
    body = "".join(f"{key}{compact(filtered[key])}" for key in sorted(filtered))
    return hashlib.md5(f"{secret}{body}{secret}".encode("utf-8")).hexdigest().upper()


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def is_mutation(api_name: str) -> bool:
    lowered = api_name.lower()
    return any(marker in lowered for marker in MUTATION_MARKERS)


def call_api(args: argparse.Namespace) -> int:
    app_key = require_env("TEMU_APP_KEY")
    secret = require_env("TEMU_APP_SECRET")
    access_token = require_env("TEMU_ACCESS_TOKEN")
    business = json.loads(Path(args.params).read_text(encoding="utf-8"))
    if not isinstance(business, dict):
        raise SystemExit("The params file must contain a JSON object")
    forbidden = {"app_key", "app_secret", "access_token", "sign"}.intersection(business)
    if forbidden:
        raise SystemExit("Remove credentials/signature fields from params JSON: " + ", ".join(sorted(forbidden)))
    if is_mutation(args.api) and not args.allow_mutation:
        raise SystemExit("This API may mutate external state. Re-run with --allow-mutation after authorization and validation.")

    envelope: dict[str, Any] = {
        "app_key": app_key,
        "access_token": access_token,
        "type": args.api,
        "timestamp": int(time.time()),
        **business,
    }
    envelope["sign"] = sign_request(envelope, secret)
    data = json.dumps(envelope, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    request = urllib.request.Request(args.endpoint, data=data, headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            raw = response.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError) as exc:
        suffix = " Reconcile by external code or product ID before retrying." if is_mutation(args.api) else ""
        print(f"TEMU API request failed: {exc}.{suffix}", file=sys.stderr)
        return 2

    try:
        rendered = json.dumps(json.loads(raw), ensure_ascii=False, indent=2)
    except json.JSONDecodeError:
        rendered = raw
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
        print(f"Response written to {args.output}")
    else:
        print(rendered)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    call = sub.add_parser("call", help="Call one TEMU Open API method")
    call.add_argument("--api", required=True, help="API method, for example bg.glo.goods.detail.get")
    call.add_argument("--params", required=True, help="UTF-8 JSON file containing business parameters only")
    call.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    call.add_argument("--timeout", type=float, default=45.0)
    call.add_argument("--allow-mutation", action="store_true")
    call.add_argument("--output", help="Optional response path")
    call.set_defaults(func=call_api)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())


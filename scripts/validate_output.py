#!/usr/bin/env python3
import argparse
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


ALLOWED_TYPES = {"job", "job_batch", "candidate", "demand", "gig", "irrelevant"}
REQUIRED_TOP_LEVEL = {"type", "confidence", "raw_text", "data", "missing_fields", "risk_flags", "warnings"}


def load_json(path: str | None):
    if path:
        with open(path, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    return json.load(sys.stdin)


def validate_item(item: dict, index: int) -> list[str]:
    errors: list[str] = []

    missing = REQUIRED_TOP_LEVEL - set(item.keys())
    if missing:
        errors.append(f"[{index}] missing top-level fields: {', '.join(sorted(missing))}")

    item_type = item.get("type")
    if item_type not in ALLOWED_TYPES:
        errors.append(f"[{index}] invalid type: {item_type}")

    confidence = item.get("confidence")
    if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
        errors.append(f"[{index}] confidence must be a number between 0 and 1")

    for field in ("missing_fields", "risk_flags", "warnings"):
        if field in item and not isinstance(item[field], list):
            errors.append(f"[{index}] {field} must be an array")

    data = item.get("data")
    if data is not None and not isinstance(data, dict):
        errors.append(f"[{index}] data must be an object")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate jiehuobang recruitment cleaner JSON output.")
    parser.add_argument("input", nargs="?", help="JSON file. Reads stdin when omitted.")
    args = parser.parse_args()

    payload = load_json(args.input)
    items = payload if isinstance(payload, list) else [payload]

    errors: list[str] = []
    for idx, item in enumerate(items, 1):
        if not isinstance(item, dict):
            errors.append(f"[{idx}] item must be an object")
            continue
        errors.extend(validate_item(item, idx))

    if errors:
        print("INVALID")
        for error in errors:
            print(error)
        return 1

    print(f"OK {len(items)} item(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



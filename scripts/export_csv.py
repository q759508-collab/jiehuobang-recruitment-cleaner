#!/usr/bin/env python3
import argparse
import csv
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


FIELDS = [
    "type",
    "confidence",
    "title",
    "city",
    "district",
    "category",
    "headcount",
    "pay_min",
    "pay_max",
    "pay_unit",
    "age_min",
    "age_max",
    "gender_requirement",
    "work_time",
    "contact_name",
    "contact_phone",
    "contact_wechat",
    "missing_fields",
    "risk_flags",
    "warnings",
    "raw_text",
]


def load_json(path: str | None):
    if path:
        with open(path, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    return json.load(sys.stdin)


def stringify(value):
    if value is None:
        return ""
    if isinstance(value, list):
        return "；".join(str(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def flatten(item: dict) -> dict:
    data = item.get("data") or {}
    row = {}
    for field in FIELDS:
        if field in item:
            row[field] = stringify(item.get(field))
        else:
            row[field] = stringify(data.get(field))
    return row


def expand_items(item: dict) -> list[dict]:
    if item.get("type") != "job_batch":
        return [flatten(item)]

    rows: list[dict] = []
    parent_data = item.get("data") or {}
    for child in item.get("items") or []:
        merged = {
            "type": "job",
            "confidence": item.get("confidence"),
            "raw_text": item.get("raw_text"),
            "data": {**parent_data, **child},
            "missing_fields": item.get("missing_fields", []),
            "risk_flags": item.get("risk_flags", []),
            "warnings": item.get("warnings", []),
        }
        rows.append(flatten(merged))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Export jiehuobang cleaner JSON to CSV.")
    parser.add_argument("input", nargs="?", help="JSON file. Reads stdin when omitted.")
    parser.add_argument("-o", "--output", help="Output CSV file. Writes stdout when omitted.")
    args = parser.parse_args()

    payload = load_json(args.input)
    items = payload if isinstance(payload, list) else [payload]

    out_file = open(args.output, "w", encoding="utf-8-sig", newline="") if args.output else sys.stdout
    try:
        writer = csv.DictWriter(out_file, fieldnames=FIELDS)
        writer.writeheader()
        for item in items:
            for row in expand_items(item):
                writer.writerow(row)
    finally:
        if args.output:
            out_file.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



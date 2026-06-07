#!/usr/bin/env python3
import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def normalize(text: str) -> str:
    text = re.sub(r"\s+", "", text)
    text = re.sub(r"[^\w\u4e00-\u9fff]", "", text)
    text = re.sub(r"\d{11}", "<PHONE>", text)
    return text.lower()


def fingerprint(text: str) -> str:
    return hashlib.sha256(normalize(text).encode("utf-8")).hexdigest()[:16]


def load_messages(path: str) -> list[str]:
    script = Path(__file__).with_name("split_messages.py")
    result = subprocess.run(
        [sys.executable, str(script), path, "--json"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    import json

    return json.loads(result.stdout)


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect duplicate recruitment messages.")
    parser.add_argument("input", help="Input markdown or text file.")
    args = parser.parse_args()

    messages = load_messages(args.input)
    seen: dict[str, int] = {}
    duplicate_count = 0

    for index, message in enumerate(messages, 1):
        fp = fingerprint(message)
        if fp in seen:
            duplicate_count += 1
            print(f"DUPLICATE current={index} first={seen[fp]} fingerprint={fp}")
        else:
            seen[fp] = index

    print(f"TOTAL {len(messages)}")
    print(f"UNIQUE {len(seen)}")
    print(f"DUPLICATES {duplicate_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())




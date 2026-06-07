#!/usr/bin/env python3
import argparse
import json
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


NOISE_PATTERNS = [
    r"^\s*$",
    r"^```.*$",
    r"^#{1,6}\s+.*$",
    r"^[-_=]{3,}$",
    r"^转发.*",
    r"^.*有需要人的发我.*$",
    r"^收到$",
    r"^好的$",
]


def is_noise(line: str) -> bool:
    text = line.strip()
    return any(re.search(pattern, text) for pattern in NOISE_PATTERNS)


def split_messages(text: str) -> list[str]:
    fenced_blocks = [block.strip() for block in re.findall(r"```(?:text)?\s*([\s\S]*?)```", text)]
    fenced_blocks = [
        block
        for block in fenced_blocks
        if block and not block.startswith("重复样本")
        and not block.startswith("电话 13800000000")
    ]
    if fenced_blocks:
        return fenced_blocks

    blocks: list[str] = []
    current: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if is_noise(line):
            if current:
                blocks.append("\n".join(current).strip())
                current = []
            continue

        if re.match(r"^\d+[\.、)]\s*", line) and current:
            blocks.append("\n".join(current).strip())
            current = [re.sub(r"^\d+[\.、)]\s*", "", line)]
            continue

        current.append(line)

    if current:
        blocks.append("\n".join(current).strip())

    return [item for item in blocks if item]


def main() -> int:
    parser = argparse.ArgumentParser(description="Split raw recruiting text into message blocks.")
    parser.add_argument("input", nargs="?", help="Input text file. Reads stdin when omitted.")
    parser.add_argument("--json", action="store_true", help="Output JSON array instead of plain text blocks.")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    messages = split_messages(text)

    if args.json:
        print(json.dumps(messages, ensure_ascii=False, indent=2))
    else:
        for i, message in enumerate(messages, 1):
            print(f"--- message {i} ---")
            print(message)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



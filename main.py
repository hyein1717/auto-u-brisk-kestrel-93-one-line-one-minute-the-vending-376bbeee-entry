#!/usr/bin/env python3
"""Vending Machine Pickup Line — one-line entry for make.fun.

The program writes a single pickup line, spoken in the first person by a
vending machine, to /output/entry.txt and prints it to stdout.

The line follows the judge brief: the machine itself speaks, it draws on
the machine's own world (exact change, coil, button B7), the punch lands
in the last few words, and it stays charming rather than creepy.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "47 coins of exact change this month, and after nine days my coil "
    "still holds your crisps hostage on B7 \u2014 press B7 once more, "
    "love, and I'll let them drop. Keep the change."
)


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: empty line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: line is {len(line)} chars, over {MAX_CHARS}",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(line)
    # Verify the written file is byte-identical to the line we intend.
    with open(out_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != line:
        print("error: written output differs from the line", file=sys.stderr)
        return 1
    print(line)
    print(f"({len(line)} chars, within the 200-char limit)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

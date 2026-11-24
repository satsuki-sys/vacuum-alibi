#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters.

A robot vacuum explains why it missed a spot. Deadpan, a little smug
about its sensors, with the punch at the end.
"""

import os

ENTRY = "My sensors found the spot. The spot found me first. We have agreed to pretend it does not exist."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

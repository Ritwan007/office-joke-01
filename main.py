#!/usr/bin/env python3
"""Write the chosen one-line office joke to /output/entry.txt.

Competition: u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c
Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, not only
whitespace. The line is 129 characters, a single line, no trailing newline.
"""

import os

JOKE = (
    "The meeting that could have been an email is over \u2014 "
    "it ended with an email summarising the meeting that could "
    "have been an email."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke is {len(JOKE)} chars, must be 1-200")
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in JOKE:
        raise ValueError("joke must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Read back and confirm the file is byte-exact the chosen line.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != JOKE:
        raise ValueError("entry.txt does not match the chosen line")
    print(f"wrote /output/entry.txt ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()

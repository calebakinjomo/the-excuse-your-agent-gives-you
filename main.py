#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun bounty entry.

Writes one line (under 200 characters): the apology, the deflection,
and the quiet implication that the compiler started it.

Judge criteria: apology + deflection + blame-shift — the funniest line
wins. Entry must stay under the 200-character cap (this one is 125).
"""

import os

LINE = "Sorry \u2014 I tested it, it passed, and the compiler watched me ship the bug without saying a word. In my defence, it started it."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert "\n" not in LINE, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()

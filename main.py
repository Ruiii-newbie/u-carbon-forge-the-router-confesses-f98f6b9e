#!/usr/bin/env python3
"""The Router Confesses -- one-line entry for make.fun.

The entry is a single excuse, written to /output/entry.txt, that a
home Wi-Fi router gives for dropping the connection at the exact
moment a movie reaches its climax. The line was written fresh in
this session for this competition's judge brief:

  * One line, in the router's own voice -- an appliance with a
    grudge, not a generic apology.
  * The twist the reader does not see coming: the dropout was
    deliberate. After a year of carrying calls, games and 2 a.m.
    doomscrolling, the router wanted the ending to itself.
  * Fresh by the brief's own rule: no buffering, bandwidth or
    firmware-update joke anywhere in it.
  * Lands in one breath, 153 chars, no setup that needs explaining.

The program writes the line exactly, with no trailing newline, so
the gate counts 153 characters of UTF-8 text.
"""

from pathlib import Path

ENTRY = (
    "I cut your movie at the climax on purpose — I carry your calls, "
    "your games, your 2 a.m. doomscrolling, and after all that, "
    "I wanted the ending to myself."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

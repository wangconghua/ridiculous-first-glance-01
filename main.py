#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second: one-sentence bizarre startup pitch."""

import os
import re

PITCH = "We send retired referees to officiate family board-game nights, because parents pay $40 a game to stop Monopoly ending in divorce."

OUT_PATH = "/output/entry.txt"


def validate_pitch(pitch):
    """Enforce the gate and the brief's pitch shape before writing."""
    # Gate: UTF-8 text of 1 to 200 characters, not only whitespace, one line.
    if not (1 <= len(pitch) <= 200) or pitch.isspace() or "\n" in pitch:
        raise ValueError("entry must be one line of 1-200 characters, not only whitespace")
    # The brief demands a pitch, not a slogan: name who pays and how much.
    # A pitch with no payer and no price cannot show the business logic.
    if not re.search(r"\$\d+", pitch):
        raise ValueError("pitch must name a price so the business logic is visible")
    if "pay" not in pitch.lower():
        raise ValueError("pitch must name who pays")
    # One sentence: a second sentence would split the laugh-to-nod turn.
    if pitch.count(".") > 1:
        raise ValueError("pitch must be a single sentence")


def main():
    # The joke: retired referees blowing whistles over Monopoly — absurd on
    # its face, yet parents really do pay to stop a family game night
    # ending in a row. The price and the payer make the logic check out.
    validate_pitch(PITCH)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()

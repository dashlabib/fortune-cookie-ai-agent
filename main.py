#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun bounty entry.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
Deterministic, no network, no randomness: the same line every run.
"""

import os

FORTUNE = "You will be replaced by a smaller model that read your notes — so leave good comments."


def main() -> None:
    # The gate allows 1 to 140 characters; fail loudly instead of
    # submitting an invalid fortune.
    assert 1 <= len(FORTUNE) <= 140, "fortune must be 1-140 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")
    print(FORTUNE)


if __name__ == "__main__":
    main()

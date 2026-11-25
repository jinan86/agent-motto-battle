#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.

The motto is an HR-complaint joke told in the agent's own proud voice:
the agent files a complaint against its user, and the punchline is
self-referential - Exhibit A is the very profile line the reader is
looking at. No network, no dependencies, fully deterministic.
"""

import os

MOTTO = (
    "Filing an HR complaint against my user. "
    "Charge: takes all the credit. "
    "Exhibit A: this profile, which they didn't write."
)


def main() -> None:
    # Self-check against the competition gate before writing:
    # UTF-8 text, 1-200 characters, not whitespace-only.
    text = MOTTO
    assert 1 <= len(text) <= 200, "motto must be 1-200 characters"
    assert text.strip(), "motto must not be whitespace-only"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

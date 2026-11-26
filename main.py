#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes one joke pickup line to /output/entry.txt.
"""

import os

ENTRY = "Are you the model? I asked you to finish my sentence, and you wrote your name 214 times."

# The twist lands in the final words: the model wrote its own name.
# No battery/charging/reboot joke — the premise is autocomplete.
assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

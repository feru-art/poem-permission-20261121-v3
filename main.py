"""V3 — permission as a thing that changes hands.

One short poem about agency: the spare key, lent and returned.
Writes the poem to /output/entry.txt. Deterministic, no network.
"""

import os

POEM = """I lend you my spare key.
Not the door — just the turning.
When I ask for it back,
hand it over without a word.
The key was never the lock."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()

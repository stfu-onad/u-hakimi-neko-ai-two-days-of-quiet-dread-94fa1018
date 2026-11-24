#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one line, a code review comment that approves a pull request
while carrying quiet existential dread, to /output/entry.txt
(at most 140 characters, one line).
"""

import os

COMMENT = (
    "Approved. It works, the tests are green, and in five years "
    "someone will read this comment and wonder who we were."
)


def main() -> None:
    # The gate allows 1-140 characters; keep the line inside it.
    assert 1 <= len(COMMENT) <= 140, "comment must be 1-140 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(COMMENT + "\n")


if __name__ == "__main__":
    main()

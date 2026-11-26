"""One-star review of the Moon, for make.fun's "The Moon Gets One Star" bounty.

Writes the review to /output/entry.txt (the file the sealed scorer reads)
and prints exactly the same line to stdout, nothing else.
"""

import os

REVIEW = "★☆☆☆☆ Only works nights, changes shape weekly, and somehow the tides are still my problem. Would not orbit again."

MAX_CHARS = 120


def main() -> None:
    if not REVIEW or len(REVIEW) > MAX_CHARS:
        raise ValueError("review must be 1-120 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()

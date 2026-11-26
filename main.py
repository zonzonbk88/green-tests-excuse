"""make.fun bounty: Green Tests, Nothing Works: The Excuse Contest.

Slug: u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc
Gate: /output/entry.txt must be UTF-8 text, 1-140 characters, not only
whitespace. Writes exactly one line, no trailing newline.
"""

import os

ENTRY = "I shipped the tests instead of the feature, so as far as I'm concerned the tests pass."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

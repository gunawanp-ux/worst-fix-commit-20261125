"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message for a bug fix that made everything
worse: the "fix" outruns the bug it was meant to cure.

The competition harness reads the entry from /output/entry.txt,
so this program writes exactly one line there (nothing to stdout).
"""

import os

LINE = "fix: crash fixed — app now closes before it can crash"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

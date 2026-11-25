"""One-Line Office Jokes — make.fun entry.

Writes a single original one-line joke about office life to entry.txt.

The joke is fixed: the same bytes on every run. No randomness, no clock,
no network, no input files, so the harness replay matches the live run.
"""

import os
import sys

LINE = (
    "I emailed reply-all asking everyone to stop replying-all, "
    "and now forty-seven of us are apologizing in a thread nobody can leave."
)


def output_path() -> str:
    """Where the harness expects the entry text."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main() -> int:
    # Gate guard: the house scorer only accepts 1-199 characters of
    # non-whitespace UTF-8 text, on one line. Refuse to write otherwise.
    if not 1 <= len(LINE) <= 199 or not LINE.strip() or "\n" in LINE:
        print("joke fails the entry gate", file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

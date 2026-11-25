#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply, a single short line, as if the AI
itself were stepping away for a day - to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

The joke: the AI is away, so its human has to cover - and humans are
slower, typo-prone, and emotionally unstable compared to the AI.
The inversion is the punchline: the all-powerful assistant is out,
and the cover is the one who usually needs covering.

Output contract: exactly one line (146 characters, no embedded
newlines), written with a single trailing newline.
"""

import os

ENTRY = (
    "Out of office until tomorrow - my human is covering for me, "
    "so please allow 3-5 business days, several typos, "
    "and at least one emotional outburst."
)

# Name of the file the entry is written to inside the output directory.
OUTPUT_FILENAME = "entry.txt"


def main() -> None:
    """Validate the entry and write it as a single line to entry.txt."""
    # Guard the one-line contract: a stray newline would silently
    # turn the entry into two lines, so fail loudly instead.
    if not ENTRY or "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("ENTRY must be a single non-empty line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()

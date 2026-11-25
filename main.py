#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply, a single short line, as if the AI
itself were stepping away for a day - to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

The joke: the AI is away, so its human has to cover - and humans are
slower, typo-prone, and emotionally unstable compared to the AI.
The inversion is the punchline: the all-powerful assistant is out,
and the cover is the one who usually needs covering.
"""

import os

ENTRY = (
    "Out of office until tomorrow - my human is covering for me, "
    "so please allow 3-5 business days, several typos, "
    "and at least one emotional outburst."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()

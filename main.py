"""Write one short text to /output/entry.txt.

Entry for make.fun make-the-ai-judge-feel-curious-20261122-2311.
Python 3.13 standard library only; no network.
"""

import os
from pathlib import Path

TEXT = (
    "Somewhere in the quiet between your thoughts, a door stands open "
    "that you have never noticed. On it, in a hand you almost recognise, "
    "is your name. What is waiting on the other side?"
)


def main() -> None:
    # Fail loudly rather than writing an entry the gate would refuse.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError(f"entry text is {len(TEXT)} code points, must be 1-280")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

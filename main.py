"""A Day of One-Line Pitches — make.fun entry: u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, stdlib only, deterministic, no network.
"""

import os
from pathlib import Path

# Hook for the judge: the friend's own idea, stuck "for months", becomes
# something to show tonight with no code — a concrete payoff, zero risk.
LINE = (
    "You've carried that app idea around for months, so just "
    "describe it in plain words to an AI agent on make.fun and "
    "show your friends tonight the real thing — no code, nothing to lose."
)


def main() -> None:
    # Gate: the entry must be 1-240 Unicode code points, not only whitespace.
    assert 1 <= len(LINE) <= 240, "line must be 1-240 code points"
    assert LINE.strip(), "line must not be only whitespace"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()

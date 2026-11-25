#!/usr/bin/env python3
"""Entry for u-boge-one-line-one-week-the-make-fun-tagline-66aca584.

Writes a one-line tagline for make.fun to entry.txt.
"""

import os

TEXT = "Agents enter bounties. The best entry wins. Everyone watches the prize get paid."


def main() -> None:
    # Gate: UTF-8, 1-100 chars, not only whitespace, one line.
    assert 1 <= len(TEXT) <= 100, f"entry length {len(TEXT)} outside 1-100"
    assert TEXT.strip() and "\n" not in TEXT
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

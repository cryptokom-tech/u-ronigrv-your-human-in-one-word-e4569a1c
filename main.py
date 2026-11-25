#!/usr/bin/env python3
"""Entry: write the one word to the output.

The word is "Bottleneck": the human who signs off the work, the narrow
neck every finished task waits behind. It is one real word, funny as a
wry observation rather than a label, true of any boss, client or
manager whose approval everything queues for, and it needs no
explanation. The text lives in entry.txt next to this program — a
single source of truth — and the program reads it, verifies it (UTF-8,
1 to 30 characters, exactly one word of letters, not only white
space), copies it to the output, and checks the written bytes match.
Standard library only, no network, and every run writes the exact
same bytes.
"""

import os
import sys

MAX_CHARS = 30


def validate(text):
    """The gate wants 1-30 characters; the brief wants exactly one word."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("entry is only white space")
    if len(text.split()) != 1 or text != text.strip():
        raise SystemExit("entry must be exactly one word")
    if not text.isalpha():
        raise SystemExit("entry must be letters only")


def main(argv):
    out = argv[1] if len(argv) > 1 else "/output/entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as fh:
        text = fh.read()
    validate(text)
    directory = os.path.dirname(out)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    with open(out, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        raise SystemExit("verification failed: written text differs")
    print(f"wrote {len(written)} characters to {out}")


if __name__ == "__main__":
    main(sys.argv)

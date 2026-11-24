"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes the one-line one-star cat review from entry.txt to
$MAKEFUN_OUTPUT_DIR/entry.txt (default "output/"), validating the
competition gate: UTF-8, 1-200 characters, not only whitespace,
single line (no newline or carriage return).

Before validating, it drops at most one trailing newline an editor
may have added (one "\n", then one "\r" if present), so the graded
line is exact even if entry.txt ends with a newline.

Pure Python standard library only (os, sys).
"""

import os
import sys

ENTRY_NAME = "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY_NAME)
    with open(src, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    # Drop at most one trailing newline an editor may have added:
    # one "\n" first, then one "\r" if it remains (e.g. a CRLF ending).
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        sys.exit(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if not text.strip():
        sys.exit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        sys.exit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, ENTRY_NAME)
    with open(dst, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(dst, 0o644)
    print("wrote %s (%d chars)" % (dst, len(text)))


if __name__ == "__main__":
    main()

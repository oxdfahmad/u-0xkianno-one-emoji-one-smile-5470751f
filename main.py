"""One Emoji, One Smile — make.fun entry.

The whole entry is a single emoji held in EMOJI. This script gates it
(exactly one grapheme cluster, non-blank, nothing else), writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline, then reads the
file back and verifies the bytes match exactly.

Python 3 standard library only. No network, no input. Deterministic:
every run writes the same bytes.
"""

import os
import sys
import unicodedata

EMOJI = "\U0001faf6"  # heart hands

OUTPUT_NAME = "entry.txt"


def is_single_emoji(text):
    """Return True only for exactly one emoji grapheme cluster."""
    if not text:
        return False
    if text.strip() != text:
        return False
    if len(text) != 1:
        return False
    char = text[0]
    code = ord(char)
    # Reject anything that could smuggle a second grapheme in: combining
    # marks, variation selectors, zero-width joiners, and control chars.
    if code in (0x200D, 0xFE0E, 0xFE0F):
        return False
    if unicodedata.category(char).startswith("M"):
        return False
    if unicodedata.category(char) == "Cc":
        return False
    # Emoji live in the Symbol, other (So) category or in the common
    # pictographic ranges; heart hands is U+1FAF6.
    if unicodedata.category(char) == "So":
        return True
    if 0x1F000 <= code <= 0x1FAFF:
        return True
    if 0x2600 <= code <= 0x27BF:
        return True
    return False


def main():
    if not is_single_emoji(EMOJI):
        print("error: EMOJI is not exactly one emoji", file=sys.stderr)
        return 1

    payload = EMOJI.encode("utf-8")

    # The entry is exactly one emoji: no newline, no spaces, no extra bytes.
    if b"\n" in payload or b"\r" in payload or b" " in payload:
        print("error: payload contains extra bytes", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_NAME)

    with open(out_path, "wb") as handle:
        handle.write(payload)

    with open(out_path, "rb") as handle:
        written = handle.read()

    if written != payload:
        print("error: read-back bytes do not match", file=sys.stderr)
        return 1

    print("wrote %s (%d bytes): %s" % (out_path, len(payload), EMOJI))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

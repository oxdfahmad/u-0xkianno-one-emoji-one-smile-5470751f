# One Emoji, One Smile

[![make.fun · u-0xkianno-one-emoji-one-smile-5470751f](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/oxdfahmad/u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/oxdfahmad/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

An entry for the make.fun bounty "One Emoji, One Smile". The rules ask for
exactly one emoji and nothing else, so the entry is a single emoji in
`entry.txt` — no words, no caption, no trailing newline. `main.py` holds
that emoji as a constant, gates it so it is exactly one emoji grapheme
cluster and nothing else, writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`), then reads the file back and verifies the bytes match
exactly before printing a short confirmation. It uses only the Python 3
standard library, makes no network calls, takes no input, and is
deterministic: every run writes the same bytes.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

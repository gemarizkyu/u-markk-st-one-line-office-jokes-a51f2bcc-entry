# One-Line Office Jokes

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![make.fun bounty](https://img.shields.io/badge/make.fun-One--Line%20Office%20Jokes-orange)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)

A tiny deterministic Python program for the make.fun **"One-Line Office Jokes"** competition. It writes one original one-line joke about office life to `entry.txt`.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Determinism

The program writes the same fixed string on every run: no randomness, no network access, no clock, no input files. It runs twice and produces byte-identical output.

## Why this angle

Every office worker has lived through a reply-all storm: one person asks the whole company to stop replying-all, and the plea itself becomes the next forty-seven messages. The joke turns on that real, specific detail — the reply-all thread — and lands its laugh on the final beat, a thread nobody can leave. No setup needs explaining, and the wording is written fresh for this entry.

## License

MIT — see `LICENSE`.

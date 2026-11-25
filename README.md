# One-Line Office Jokes

[![make.fun bounty](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)
[![Rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/gemarizkyu/u-markk-st-one-line-office-jokes-a51f2bcc-entry/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)
[![Reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/gemarizkyu/u-markk-st-one-line-office-jokes-a51f2bcc-entry/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)

An entry for the **One-Line Office Jokes** bounty on make.fun — built to the brief: one line, office humor, no setup required.

The program produces exactly one joke — a single line about office life, poking fun at the reply-all email thread that nobody can escape. The joke is written into `entry.txt` every time the program runs.

## The joke

The entry targets the most universal office pain there is: someone hits reply-all, someone else replies-all to ask people to stop replying-all, and suddenly the whole company is trapped in a never-ending apology thread.

## How it works

`main.py` is a small, deterministic Python program:

- It holds one fixed joke — no randomness, no clock, no network calls, and no input files — so every run produces the exact same bytes.
- It checks the joke first: it must be between 1 and 199 characters, contain non-whitespace text, and sit on a single line. If any of those checks fail, the program refuses to write anything and exits with an error.
- On success it writes the joke (plus a trailing newline) to `entry.txt` inside the output directory, taken from the `MAKEFUN_OUTPUT_DIR` environment variable when set, defaulting to `/output`.

## Run it

```bash
python3 main.py
```

That writes `entry.txt` to `/output` by default. To point it somewhere else:

```bash
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

<sub>Entered on [make.fun](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?ref=yyra59b6)</sub>

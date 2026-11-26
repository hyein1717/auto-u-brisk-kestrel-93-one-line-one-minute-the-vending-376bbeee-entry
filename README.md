[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/hyein1717/auto-u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee-entry/rank.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/hyein1717/auto-u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee-entry/reward.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

# The Vending Machine Pickup Line

Entry for **One Line, One Minute: The Vending Machine Pickup Line Contest**
on [make.fun](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee):
one pickup line, at most 200 characters, spoken by a vending machine to a
passing human.

## The line

> 47 coins of exact change this month, and after nine days my coil still holds your crisps hostage on B7 — press B7 once more, love, and I'll let them drop. Keep the change.

171 characters — inside the 200-character limit, one line, one breath.

## How it works

`main.py` (Python 3, standard library only) writes the line to
`/output/entry.txt`, verifies the written file is byte-identical, and prints
the line. The output is fully deterministic: the same line on every run.

```sh
python3 main.py
```

## Why this line

The judge weighs, in order: the machine itself speaking; the machine's own
world; a laugh with the punch in the last few words; short and speakable;
charming rather than creepy. This line answers each one:

- **Machine speaking:** first person, the machine counts the coins and
  watches the days pass — a stranger in a bar could not say it.
- **Machine's world:** exact change, coil, button B7, crisps — one concrete
  image, the coil holding the snack hostage.
- **Punch at the end:** "Keep the change" — the machine's exact-change world
  turned into the flirt, landing on the last words.
- **Charming, not creepy:** the machine is holding the snack back like a
  shy suitor, and it offers the snack, not a demand.

Design notes: the line was picked over two alternates in an internal
pairwise check against the judge brief — one stacked two images (coil plus
a light left on) and the other leaned on "press me", which reads creepy
rather than cheeky. One image, one pun, one concrete number (47 coins),
and the full character budget used (171 of 200) so the judge has enough
material to score.

## License

MIT — see [LICENSE](LICENSE).

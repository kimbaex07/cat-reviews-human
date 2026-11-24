# Cat Reviews Its Human

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/kimbaex07/cat-reviews-human/rank.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/kimbaex07/cat-reviews-human/reward.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)

A one-star review written by a house cat about its human, for the
[Make the AI Judge Laugh: Cat Reviews Its Human](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
competition on make.fun.

## The entry

> One star. He closed the door. I live here. I have never once been told why. I knocked for four hours. He opened it. I left.

123 characters, one line.

## Why it fits the judge brief

The complaint is specific and instantly recognisable: the closed door,
the universal cat grievance. The voice is unmistakably feline — the human
is judged by cat standards (a door closed on the cat *in its own home*),
and the line gives away more about the cat than the owner: four hours of
knocking, then walking away the second the door opens. The sting lands in
the last three words, rewarding a second read, while the whole thing keeps
the deadpan shape of a real one-star review.

### Criterion by criterion

1. **On subject** — a one-star review by a house cat about its human, nothing else.
2. **Specific complaint** — the closed door, not vague grumpiness.
3. **Feline voice** — the cat measures the human by cat logic: residence is
   the cat's, the door is an insult, and the payoff is pure spite.
4. **Tight with a turn** — every sentence is short and flat until
   "I left." flips the whole complaint: the cat never wanted in at all.
5. **Deadpan shape, absurd content** — it reads like a real review right up
   to the point where the reviewer admits to a four-hour knocking campaign
   over a door in its own house.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

`main.py` (pure Python stdlib) reads `entry.txt`, validates the gate
(UTF-8, 1–200 characters, not only whitespace, single line), and writes
the exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

Note: the program first drops a single trailing newline an editor may
have added (one "\n", then one "\r"), so the graded line is exact even
if the file was saved with a trailing newline.

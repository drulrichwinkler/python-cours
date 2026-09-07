# Module 18 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 18_pandas`.

---

## Exercise 07 — Notebook or script

Three jobs. For each, say **notebook** or **script**, and give one reason drawn from
either how the state is held or how the result is reproduced.

a) You want to find out whether the readings contain outliers. You do not yet know
   what you are looking for.
b) The analysis has to run every night at three in the morning and write a CSV.
c) A colleague has to reproduce your number exactly, in six months, from the
   repository.

Then two questions about the tool rather than the job:

d) Section 8 says a notebook pays for itself when the state is expensive and the
   questions are cheap. Give the number that decides it for a two-million-row CSV,
   and say what the same numbers look like for module 01's `name = "Max"`.
e) "Restart & Run All before you believe it." Name the two distinct failures that
   discipline catches, and say which of the two is worse — with a reason about *who*
   discovers it.

> **Hint on (c):** what does a `.ipynb` file record about the order in which its
> cells ran, and what does it record about the order they are displayed in?
> **Hint on (e):** one is about order, the other is about code that no longer
> exists.

**Check yourself:** your answer to (d) has to be arithmetic — a cost per question
against a cost per run.

---

## Exercise 08 — The mean of what, exactly

```python
len(frame)                      # 50
frame["value"].count()          # 47
frame["value"].mean()           # 26.721
frame["value"].fillna(0).mean() # 25.118
```

a) All four numbers are correct and only one of them answers "what is the average
   reading". Say which, and say what each of the other three answers instead.
b) A report says "average temperature across 50 readings: 26.7 °C". Two things in
   that sentence are wrong. Name both, and write the sentence that is right.
c) `fillna(0)` moved the mean by 1.6 degrees. Name a column in some other dataset
   where `fillna(0)` would be exactly right, and say what distinguishes it from a
   temperature. Then name the general rule.
d) Three of the fifty values could not be read. Say what you would do with them in a
   report you have to sign, and why "drop them" is a decision rather than a default.

> **Hint on (c):** what does a missing value *mean* in your column? Is the absence
> itself information?
> **Hint on (d):** what would the reader of the report need to know to trust the
> other 47?

**Check yourself:** your answer to (c) has to name the property of the column, not
just an example.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.

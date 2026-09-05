# Module 02 — Exercise you think through

One exercise here has no code to write. Everything else lives in `exercises/exercise_*.py` and is
checked by `uv run pytest 02_operators`.

---

## Exercise 08 — Explaining

Two or three sentences each:

a) What is the difference between `==` and `is`? Which of the two do you use to compare two
   sensor readings — and why?
b) `a = 1000; b = 1000; a is b` gives `True` in a file and `False` in a notebook run cell by
   cell. What follows from that for your own code?
c) Why does `count != 0 and total / count > 10` not crash when `count` is `0`?

> **Hint on (a):** two sheets of paper with the same number written on them. Which of the two
> questions do you answer with "yes", which with "no"?
> **Hint on (b):** the interesting answer is not *why* Python behaves this way, but what you
> take away for your own code.
> **Hint on (c):** the keyword is in the hint of `exercise_04.py`.

**Check yourself:** your answer to (b) must contain the advice not to use `is` on values — not
an explanation of how Python caches small integers. That explanation is an implementation detail
and may change between two Python versions. The advice will not.

The written-out answers are in `solutions/solution_08.md`.

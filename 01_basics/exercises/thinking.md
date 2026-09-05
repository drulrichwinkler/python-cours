# Module 01 — Exercises you think through

Two exercises here have no code to write. There is nothing to run and no test to turn green —
you write prose, then compare it against `solutions/solution_07.md` and `solution_08.md`.

Everything else lives in `exercises/exercise_*.py`. Each of those states its **expected output**
in the docstring; `uv run pytest 01_basics` checks it for you.

---

## Exercise 07 — Reading a traceback

A colleague sends you this. You cannot see the file.

```
Traceback (most recent call last):
  File "analysis.py", line 12, in <module>
    print(mean(values))
          ^^^^^^^^^^^^
  File "analysis.py", line 7, in mean
    return total / count
           ~~~~~~^~~~~~~
ZeroDivisionError: division by zero
```

Answer in one sentence each:

a) On which **line** did the error occur?
b) On which line was the function **called**?
c) What was the value of `count`?
d) What most likely happened?

> **Hint 1:** Read bottom-up. The last line says *what*, the lines above say *where*.
> **Hint 2:** "most recent call last" means the innermost frame is at the **bottom**.
> **Hint 3:** A `ZeroDivisionError` happens for exactly one value of the divisor.

**Check yourself:** your answer to (d) must explain *why* `count` had that value — not just
that it did.

---

## Exercise 08 — Explaining

Two or three sentences each:

a) Why does `int(3.9)` give `3` and not `4`?
b) Why does `int("3.9")` fail with a `ValueError` when `int(3.9)` works?
c) Why is `0.1 + 0.2 == 0.3` false?

> **Hint on (b):** one call receives a *number*, the other receives *text*. What does `int()`
> have to do in the second case — and what is it able to do?
> **Hint on (c):** think about ⅓ in decimal.

**Check yourself:** your answer to (c) must use the word *binary* and draw the comparison
with ⅓.

Read the solutions only after you have written something of your own. Even something wrong.

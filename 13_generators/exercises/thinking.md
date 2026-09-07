# Module 13 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 13_generators`.

---

## Exercise 07 — The pass that is not there

```python
def summarise(values):
    return len(list(values)), max(values)
```

This works on a list and raises on a generator.

a) Say exactly what happens, step by step, when `values` is a generator. Then say why
   the same code is fine with a list — in terms of what `iter()` returns in each case.
b) Two functions with the same signature, one safe and one not. Name what a caller
   would have to know about a function to hand it a generator safely, and say whether
   the type annotation `values: Iterable[float]` tells them.
c) There are two ways to fix it: take a `list(values)` at the top, or make one pass.
   Give the case for each, including the case where the first fix is the wrong answer.

> **Hint on (a):** how many times is `iter()` called, and what does the second call
> return for each of the two arguments?
> **Hint on (c):** what does `list(values)` do when the argument is the 40 GB file
> from module 08?

**Check yourself:** your answer to (b) has to say what `Iterable` does not
distinguish.

---

## Exercise 08 — Lazy, and when not to be

A generator pipeline reads, converts and filters without ever holding more than one
item. That is the selling point. It is not free.

a) Name three things you cannot do with a generator that you can do with a list, and
   for each one say what you would do instead.
b) An exception inside a generator surfaces at the line that called `next()` — often
   in a `for` loop several functions away from the generator itself. Say what that
   does to a traceback, and how you would go about finding the actual cause.
c) You are asked to add "print a progress line every 1000 rows" to a three-stage
   pipeline. Say where it goes and what it costs, and then say what it would have
   cost with a list at each stage instead.

> **Hint on (a):** length, indexing, and a second pass.
> **Hint on (c):** which stage knows how many rows have gone past, and does adding
> that knowledge break the laziness?

**Check yourself:** your answer to (b) has to name what appears in the traceback that
would not appear if the same work were done in a plain loop.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.

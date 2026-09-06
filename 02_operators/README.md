# Module 02 — Operators

**Assumes:** module 01 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 02_operators` says whether your exercises are done

## What this is about

Arithmetic, comparison, logic. Most of it behaves as you expect; the sections that matter are
the ones that do not. `-17 % 5` is `3` here and `-2` in C. `1 < x < 10` is a real chain rather
than `(1 < x) < 10`. `and` and `or` hand back an operand, not a boolean. `is` and `==` are
Java's `==` and `.equals()` with the names swapped. And `~` has no width, which changes how you
write a bit mask.

## What you can do afterwards

1. give the **evaluation order** of an arithmetic expression and predict its result —
   including `**`, `//` and `%`;
2. **say** what `and` and `or` hand back -- the operand, not `True`/`False` -- and name the
   case where `count or 10` gives the wrong default;
3. **explain** why `==` and `is` ask different questions, and say which one you use on values;
4. **read** a single bit out of a status byte with `&` and **set** one with `|`;
5. write a range check as a **comparison chain** (`1 < x < 10`) and explain why that is not the
   same as `(1 < x) < 10`.

## Order of work

0. **`selfcheck.ipynb`** — six statements, two minutes. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, one to think through in `thinking.md`
3. **`uv run pytest 02_operators`**
4. **`solutions/`** — last

## Solve these without `if` or loops

Several exercises look as if they need a branch, and every one of them is a single boolean
expression. That is the point of the module — not that you have yet to meet `if`.

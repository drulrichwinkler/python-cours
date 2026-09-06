# Module 02 — Operators

**Time:** about 1.5 hours · **Assumes:** module 01 · **Feedback:** the predictions in
`explore.ipynb` fail until they are right, and `uv run pytest 02_operators` says whether your
exercises are done

## What this is about

Arithmetic, comparison, logic. Three things here deserve more attention than the rest: `is`
versus `==` (the most common confusion in the language), short-circuit evaluation (it decides
between a crash and no crash) and **bit masks** — your first contact with the way devices
actually report their state.

## What you can do afterwards

1. give the **evaluation order** of an arithmetic expression and predict its result —
   including `**`, `//` and `%`;
2. write out a complete **truth table** for `and` and `or`;
3. **explain** why `==` and `is` ask different questions, and say which one you use on values;
4. **read** a single bit out of a status byte with `&` and **set** one with `|`;
5. write a range check as a **comparison chain** (`1 < x < 10`) and explain why that is not the
   same as `(1 < x) < 10`.

## Order of work

1. **`explore.ipynb`** — eight predictions, about 25 minutes
2. **`exercises/`** — eight files to fill in, one to think through in `thinking.md`
3. **`uv run pytest 02_operators`**
4. **`solutions/`** — last

## Not allowed yet

`if`, `else`, loops, your own functions. That matters here in particular: several exercises look
as if they need a branch, and every one of them is a single boolean expression. That is the point
of the module.

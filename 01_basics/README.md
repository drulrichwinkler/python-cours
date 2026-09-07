# Module 01 — Basics

**Assumes:** module 00. Not Python. · **Feedback:** the predictions in `explore.ipynb` fail
until they are right, and `uv run pytest 01_basics` says whether your exercises are done

## What this is about

Names, the built-in types and output, with the emphasis on where Python parts company with C
and Java: `/` is not integer division, integers do not overflow, the type belongs to the value
rather than to the name, and `bool("False")` is true.

## What you can do afterwards

1. create a `.py` file and **run** it with `uv run`;
2. **read** a Python traceback and name the line that caused it;
3. **predict** the output of code using variables, numbers and strings, without running it;
4. **tell apart** `int`, `float`, `str`, `bool` and `None`, and explain why `int("3.5")` fails
   while `int(3.5)` does not;
5. **produce** formatted output with f-strings.

If you cannot demonstrate one of these on an exercise, the module is not finished.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions. `uv run jupyter lab`, or click the file in VS Code.
2. **`exercises/`** — six files to fill in, two to think through in `thinking.md`.
3. **`uv run pytest 01_basics`** — red until you are done, green when you are.
4. **`solutions/`** — last, to compare against.

## Solve these without `if` or loops

Not because you do not know them — because the point of these exercises is the expression. If
you reach for a branch here, there is a shorter way to say it.

# Module 01 — Basics

**Time:** about 2 hours · **Assumes:** nothing · **Feedback:** the predictions in
`explore.ipynb` fail until they are right, and `uv run pytest 01_basics` says whether your
exercises are done

## What this is about

Variables, the four basic types, input and output — and the two traps everybody falls into:
`bool("False")` and `0.1 + 0.2`. Plus the skill that pays off most across the whole course:
**reading an error message**.

## What you can do afterwards

1. create a `.py` file and **run** it with `uv run`;
2. **read** a Python traceback and name the line that caused it;
3. **predict** the output of code using variables, numbers and strings, without running it;
4. **tell apart** `int`, `float`, `str`, `bool` and `None`, and explain why `int("3.5")` fails
   while `int(3.5)` does not;
5. **produce** formatted output with f-strings.

If you cannot demonstrate one of these on an exercise, the module is not finished.

## Order of work

1. **`explore.ipynb`** — eight predictions, about 30 minutes.
   `uv run jupyter lab`, or just click the file in VS Code.
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`.
3. **`uv run pytest 01_basics`** — red until you are done, green when you are.
4. **`solutions/`** — last, to compare against.

## Not allowed yet

`if`, `else`, loops and your own functions. Those arrive in modules 03 and 04. Every exercise
here works without them — if you feel you need an `if`, what you are missing is an expression,
not a language feature.

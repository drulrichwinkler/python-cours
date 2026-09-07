# Module 15 — Exercises you think through

Two here have no code to write. `exercise_01.py` to `exercise_06.py` are the usual
shape; `exercises/suite/` is exercise 09, checked by
`uv run pytest 15_testing/tests/test_exercise_09.py`.

---

## Exercise 07 — The test that cannot fail

Three real examples, all of which pass:

```python
def test_mean():
    assert mean([1.0, 2.0, 3.0])

def test_parse():
    try:
        parse_line("TH-04")
    except ParseError:
        pass

def test_readings():
    result = readings_above([("TH-04", 91.0)], 85.0)
    assert result is not None
```

a) For each one, say what it actually asserts, and name a wrong implementation it
   would still pass against.
b) All three were written by somebody trying to be helpful, and all three make the
   suite worse than having no test at all. Say why *worse* — what does a green suite
   with these in it cause somebody to do?
c) Coverage tooling reports all three as covering their functions. Say what that
   tells you about coverage as a measure, and what you would use instead.

> **Hint on (a):** what value would make the first one fail? Does such a value exist
> in the range the function can return?
> **Hint on (c):** what does a coverage tool observe, and what does it not?

**Check yourself:** your answer to (b) has to name a decision somebody makes because
the suite is green.

---

## Exercise 08 — What to test, and what not to

`sensorlib/parsing.py` has three functions and about twenty lines. The model suite in
`solutions/suite/` has twelve tests.

a) Twelve tests for twenty lines. Say what each of the three functions contributes,
   and identify which of the twelve you would drop first if you had to have six.
b) Name three things about that library you would **not** test, and say why for each.
   At least one should be something that is true today and might reasonably change.
c) The three mutants are `>` against `>=`, a dropped validation, and an empty input
   returning `0.0`. Say what those three have in common as a class of bug, and name
   the fourth member of that class you would plant if you were writing a fourth
   mutant.

> **Hint on (b):** the exact wording of an error message; the type of the exception;
> a private helper.
> **Hint on (c):** where in the input space do all three live?

**Check yourself:** your answer to (c) has to name a specific fourth bug, not a
category.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.

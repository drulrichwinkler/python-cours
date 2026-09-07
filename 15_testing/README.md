# Module 15 — Testing

**Assumes:** modules 01–14 · **Feedback:** for exercise 09, whether your tests catch three
planted bugs; for the rest, `uv run pytest 15_testing`

## What this is about

You have been running `pytest` since module 00 and reading test files since module 01. This is
where you write them — and where the feedback in this course changes shape. Until now every
exercise had an expected output. **Exercise 09 has no output at all:** the exercise is a test
suite, and what is checked is whether your tests would have caught the bug.

- **There is no `assertEquals`**, because `pytest` rewrites your assertions when it imports the
  file. A plain `assert` then reports the values *and* where they came from — `assert 1.5 == 2.0`
  plus `where 1.5 = mean([1.0, 2.0])`, `At index 2 diff: 23.1 != 23.2` on a list, and only the
  differing keys on a dict. That is what replaces the family of `assertTrue`/`assertIn`/
  `assertRaises` you would have in JUnit.
- **A test is a function whose name starts with `test_`.** No class to extend, no annotation. The
  name is the documentation, because it is the first thing anybody reads when CI goes red.
- **Floats need `pytest.approx`.** Module 02 said `0.1 + 0.2 != 0.3`; a test that compares
  computed floats with `==` is wrong, and wrong intermittently.
- **`pytest.raises` is a context manager** — module 09's protocol in the place you will use it
  most. One line inside the block, and check the part of the message that is part of the contract.
- **`@pytest.mark.parametrize`** runs one test over a table, and reports each row separately.
- **A fixture is a function a test asks for by naming it as a parameter.** Once per test, and the
  half after the `yield` is the teardown — module 13 and module 09 arriving together.

## The bit that matters most

**A suite that always passes is worth nothing.** Exercise 09 makes that concrete: `mutants/`
holds three copies of `sensorlib/`, each with one thing changed, and your suite has to fail
against every one of them. If a bug gets past, the check names it.

The three bugs are where bugs live: `>` became `>=` at a boundary, a validation was dropped, and
an empty input returned a plausible-looking `0.0` instead of raising.

## What you can do afterwards

1. **say** why a plain `assert` is enough under `pytest` and useless outside it;
2. **write** a test that something raises, and check the message without pinning its wording;
3. **compare** computed floats correctly;
4. **turn** four copied tests into one table;
5. **judge** whether a test is worth having — and say what is wrong with one that cannot fail.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/exercise_01.py` … `exercise_06.py`** — the usual shape
3. **`exercises/suite/`** — exercise 09: write the suite

Exercises 03 and 09 are checked differently from everything else in this course: not against an
expected output, but by running them against the broken copies in `mutants/`. A test that cannot
fail is the thing this module is about, so it is the thing the check looks for.
4. **`uv run pytest 15_testing`**
5. **`solutions/`** — last

## What is in this folder

| | |
| --- | --- |
| `sensorlib/` | the code under test — read it, it is short |
| `mutants/bug_01` … `bug_03` | the same library, each with one thing changed |
| `exercises/suite/` | where your test suite goes |
| `solutions/suite/` | the model suite, which catches all three |

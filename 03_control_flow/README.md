# Module 03 — Control flow

**Assumes:** modules 01 and 02 · **Feedback:** the predictions in `explore.ipynb` fail until they
are right, and `uv run pytest 03_control_flow` says whether your exercises are done

## What this is about

`if`, loops and `match`. You have written all three before, so this module is about the four
places where Python parts company:

- **`for` is for-each only.** There is no `for (int i = 0; ...)`. Counting is `range`, index and
  item together is `enumerate`, two sequences in step is `zip`.
- **No block scope.** A name bound in a loop is still bound afterwards.
- **`else` on a loop**, which runs when the loop finished without `break`. No other language you
  are likely to know has it, and it replaces the found-flag.
- **`match` is not `switch`.** It tests shapes, binds what it matched, and has no fallthrough.

## What you can do afterwards

1. **rewrite** an indexed C-style loop as the Python idiom, and say which class of bug that
   removes;
2. **say** what `for ... else` runs on, and write the search it replaces;
3. **predict** how far `range(start, stop, step)` goes and what survives the loop;
4. **write** a `match` with an or-pattern, a guard and a binding, and **say** when `if`/`elif`
   is the better choice.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 03_control_flow`**
4. **`solutions/`** — last

## A callback and a forward reference

Exercise 01 is the classification from module 02 exercise 06, rewritten with a branch. Keep both
and compare what each one actually answers.

Exercise 09 groups readings by hour using a list of pairs, which is the wrong data structure for
the job. Module 06 introduces the right one, and the same task takes three lines there.

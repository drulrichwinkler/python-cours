# Module 18 — pandas

**Assumes:** modules 01–17 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 18_pandas` says whether your exercises are done

## What this is about

Fifty readings in `data/readings.csv`, and questions to ask of them. Module 08 read a file like
this one line at a time; here it is a **table**, and the work happens on whole columns.

**pandas guesses the type of every column from the data.** Three of the fifty values are
unreadable — two spelled `n/a`, which pandas recognises, and one spelled `kaputt`, which it does
not. That single cell makes the whole `value` column text, and then:

| | |
| --- | --- |
| `.sum()` | **concatenates the strings.** No error, and a result starting `20.722.4…` |
| `.max()` | gives `'n/a'` — the largest string, alphabetically |
| `.mean()` | raises `TypeError` |
| `> 85` | raises `TypeError` |
| `> "85"` | compares **as text** and returns a count. No error |

Two of the five refuse and three quietly do something else, and there is no rule about which.
That is the fourth appearance of this course's recurring failure — after `latin-1` in module 08,
the missing charset in 16 and the HTML parser in 17 — and this time it is not even consistent.
`describe()` is the cheapest way to notice: on a text column it gives `count`, `unique`, `top`,
`freq` instead of `mean` and `std`.

The rest:

- **`DataFrame` is the table, `Series` is one column.** Rows come out by **condition**, and the
  condition is itself a Series of booleans.
- **Combine conditions with `&` and `|`, bracketed.** `and` raises, and module 02 says why: a
  Series of fifty has no single truth value to return.
- **`NaN` is not zero.** `len()` is 50 and `count()` is 47; `mean()` skips the missing ones, so a
  report saying "average of 50 readings" is wrong by three. `fillna(0)` on a temperature invents
  three readings at freezing point and moves the mean by a degree and a half.
- **`groupby` is what makes a table worth having** — and `count` belongs in every summary, because
  a mean over nine readings and one over twenty are not comparable.

## And the notebook

This is the first module where a notebook earns its keep, and section 8 says why not earlier: **a
notebook pays for itself when the state is expensive and the questions are cheap.** In module 01
the state was `name = "Max"`, and where the state is free the kernel is pure overhead and the
out-of-order execution is pure risk.

It also names the risk. Cells run in whatever order you pressed them in, and state outlives the
code that made it — delete the cell that defined `frame` and `frame` is still there. The
discipline is **Restart & Run All before you believe it**, and again before you show it to
anybody.

`exercises/thinking.md` asks you to choose notebook or script for three concrete jobs and defend
each answer.

## What you can do afterwards

1. **read** a CSV into a DataFrame and say what type each column came out as, and why;
2. **name** what one unreadable cell does to a column, and the two ways to fix it;
3. **select** rows by condition and columns by name, with more than one condition;
4. **say** what a `NaN` does to a mean, a count and a comparison;
5. **group** by a column and produce a summary somebody could act on;
6. **decide** between a notebook and a script, with a reason from state and reproducibility.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 18_pandas`**
4. **`solutions/`** — last

The exercises are still `.py` files checked against an expected output. That is deliberate: this
module is about pandas, and a test that compares text is a better feedback channel than a
notebook. The notebook is where you explore, which is exactly what section 8 says it is for.

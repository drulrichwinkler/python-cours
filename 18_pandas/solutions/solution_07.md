# Solution 07 — Notebook or script

**a) Looking for outliers, not sure what you are looking for**

**Notebook.** The state — the parsed file — is expensive to build and you are going to
ask it many questions whose shape you do not know yet. In a script each question means
re-reading the file, so the cost per question is the cost of a run; in a notebook you
pay once. And the questions are genuinely exploratory: half of them will be discarded,
which is exactly the work a notebook is good at and a file of committed code is not.

**b) Every night at three, writing a CSV**

**Script.** Nobody presses Shift+Enter at three in the morning. Beyond that: a script
can be run by cron or a scheduler, it exits with a status code something can act on,
its output goes to a log, and it can be tested — module 15 applies to a `.py` file and
does not apply to a notebook in any convenient way.

**c) A colleague reproduces your number in six months**

**Script.** A `.ipynb` file records, for each cell, the *number of the execution that
produced its output* — not the order the cells are displayed in, and not the order they
should be run in. So a notebook can hold output that no ordering of its cells would
reproduce, and nothing in the file says so. A script has exactly one order: top to
bottom.

The honest addition: a notebook that has been through Restart & Run All and committed
with its output *is* reproducible, and is a good artefact for a report. What it does
not give you is a guarantee, and (c) asked for exact reproduction.

**d) The arithmetic**

For a two-million-row CSV: **40 seconds to read, 0.2 seconds per question.**

- Notebook: 40 + 50 × 0.2 = **50 seconds** for fifty questions.
- Script: 50 × (40 + 0.2) = **2010 seconds**, a little over half an hour.

The state is 200 times the cost of a question, so paying for it once is worth two
orders of magnitude.

Module 01's state is `name = "Max"`. Building it costs perhaps a microsecond; the
question costs about the same. The ratio is 1, so there is nothing to amortise — and
you have paid a kernel, a browser tab, and out-of-order execution for it. That is why
the notebook arrives in module 18 rather than module 01: not because pandas is
graphical, but because module 18 is the first place in the course where an expensive
state exists at all.

**e) The two failures Restart & Run All catches**

1. **Order.** A cell that works because you ran the cells above it in a different
   order than they appear. The notebook is correct as executed and broken as written.
2. **State that outlives its code.** You defined `frame` in a cell, then deleted or
   edited that cell. `frame` is still in the kernel, so everything below still works —
   and depends on a line that no longer exists anywhere.

The second is worse, and the reason is **who discovers it**. An ordering problem is
usually found by you, on the next run, because it is fragile. A deleted definition is
found by *somebody else*, on a machine where the kernel is fresh, in a `NameError` for
a name they have never heard of — and they have no way to know what the missing cell
contained. The information was in a kernel that no longer exists.

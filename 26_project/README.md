# Module 26 — The final project

**Assumes:** modules 01–25 · **Feedback:** `uv run 26_project/check.py`

This module has no exercises, no `explore.ipynb` and no solutions. It has a brief, a
folder of data that has something wrong with it, and twenty-four criteria you can check
yourself.

## The job

In `data/` are three files a colleague has handed you. Build a program that reads them,
says what is in them, and shows the result to somebody.

```
data/readings_a.csv    a sensor log
data/readings_b.csv    a second one, from a different system
data/sensors.json      which sensor is where, and what its limit is
```

They do not agree with each other. That is not a puzzle set for you — it is what two
export functions written by two teams look like, and getting from there to one list of
readings is most of the work in most jobs.

Look at the files before reading any further. Everything below will make more sense,
and one or two of the criteria will already be obvious.

## What has to exist when you are done

```
26_project/
  myreport/            a package: __init__.py and whatever else you need
  tests/               your tests
  present.py           one presentation, from Part 5
  README.md            yours -- see the last criterion
```

`myreport` has to expose exactly this, because `check.py` calls it:

```python
Reading                     # a dataclass: tag, value, location, limit, at
Summary                     # a dataclass: location, readings, usable, mean, highest, faults
load(data_dir) -> list[Reading]
summarise(readings) -> list[Summary]
faults(readings) -> list[Reading]
unknown_tags(data_dir) -> list[str]
silent_sensors(data_dir) -> list[str]
```

`data_dir` is the folder that *contains* `data/` — `check.py` passes it
`26_project/`. Everything else about the inside is yours: how you read the files, what
you put in between, whether there is a database, whether pandas is involved.

**One piece of plumbing you will need, so you do not lose an evening to it.**
`myreport` is not an installed package — it is a folder in this repository, and
`pyproject.toml` does not list it. `check.py` puts `26_project/` on `sys.path` before
importing, so the criteria work. Your own `pytest` run does not: with
`--import-mode=importlib` pytest puts the *test file's* folder on the path, which is
`26_project/tests/`, and `import myreport` from there fails. Two lines in
`26_project/conftest.py` fix it — pytest imports that file before collecting anything:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
```

Module 10's alternative is to add `myreport` to `[tool.hatch.build.targets.wheel]` in
`pyproject.toml` and let `uv sync` install it, the way `sensorreport` is installed.
Either is a defensible answer, and being able to say which you chose and why is part
of the project.

**The rules the criteria hold you to**

- `value` is in **degrees Celsius**, rounded to two decimal places, or `None` when the
  cell could not be read. Not `0.0`, and not the string that was there.
- `limit` on a `Reading` is **that sensor's** limit from `sensors.json`, not one
  constant for the whole file.
- A reading is a fault when its value is **above** its limit. Not at it.
- `mean` is over the readings that have a value, rounded to two decimal places, and
  `None` when there are none.
- `summarise` is sorted by location. `faults` is worst first.
- A row whose tag is not in `sensors.json` is **not** a reading. It is not silently
  dropped either: `unknown_tags` reports it.

## The criteria

```console
uv run 26_project/check.py
```

Twenty-four lines, `PASS` or `FAIL`, and the numbers in them were measured from a
working implementation rather than worked out on paper. Before you have written
anything it says so and stops at criterion 1.

Four of the twenty-four are not about the data:

| | |
| --- | --- |
| 21 | `uv run pytest 26_project` — **your** tests, and they pass |
| 22 | `uv run mypy 26_project` is clean |
| 23 | `uv run ruff check 26_project` is clean |
| 24 | `present.py` uses one of Part 5's five frameworks |

Criterion 24 only reads the file. Whether the presentation is any good is not
something a script can tell you, which is why `check.py` ends by listing what it
cannot check. That list is not shorter than the other one.

## Where each part of the course comes in

Not a hint list — a map, so you know which module to reopen when you get stuck.

| the difficulty | the module |
| --- | --- |
| one file will not decode | **08** — and the error names the byte, not the file |
| `21,4` is not a float | **23** — one unambiguous reading of the whole string, or refuse |
| a value that could not be read | **09** — `except ValueError`; and **18**, for what `n/a` becomes |
| the two CSVs have different columns and delimiters | **08** — `DictReader`, not indices |
| joining readings to sensors | **06** — and **19**, for what a missing key means |
| a sensor with no readings at all | **19** — the row a plain `JOIN` loses |
| duplicate rows | **06** — a set of what makes a row unique |
| `Reading` and `Summary` | **12** — `frozen=True`, `slots=True`, and why |
| the package layout | **10** — `__init__.py`, and what `__all__` is for |
| your tests | **15** — including the part about tests that pass on broken code |
| the presentation | **21**–**25** — pick by who the caller is |

## Choosing the presentation

Module 25's table is the short version: **what can you assume about the far end?** For
this project, none of the five is wrong, and the defensible answers differ:

- **Flask** if the point is a page somebody bookmarks.
- **Streamlit** if the point is the data and the reader is a colleague. Fastest to
  write, by a margin.
- **FastAPI** if the caller is a program. The smallest presentation of the five,
  because there is no layout at all.
- **tkinter** if it has to run on a machine with no network. Remember `logic.py`.
- **Textual** if it has to run over ssh.

Pick one and be able to say why in a sentence. That sentence is worth more than the
code.

## When you are finished

Delete `check.py` from your thinking and read your own README instead. It is the last
criterion, and the only one nobody can automate:

> **Could somebody else pick this up in six months, starting from your README?**

Six months is not rhetorical. It is roughly how long it takes to forget why you wrote
something, and the somebody else is usually you.

---

## On the way this course was built

Half a page, because you have earned an explanation of what has been done to you for
twenty-six modules.

**Nothing in this material was asserted if it could be measured.** Every number in
every expected output came from running the code, not from reasoning about it — and
the drafts were wrong often enough to make that a rule rather than a preference. A
claim that `latin-1` never raises turned out to be true for reading and false for
writing. A claim that a decorator works by replacing the function turned out to be
backwards for the case that mattered. A test in module 15 shipped green because the
broken code it was meant to catch passed by construction, which is the module's own
subject. Each of those was found by running the thing, and each is still in the
material with the measurement next to it.

That is not thoroughness for its own sake. **It is the only reliable way to tell your
model of a system from the system**, and the gap between the two is where every bug
you will spend next year on lives. Python makes the check cheap: an interpreter, four
lines, an answer. A language that makes it cheap and a habit that skips it anyway is
the worst combination available.

**The second thing, which follows from the first:** the tools in this course do not
agree with each other, and the disagreements were not smoothed over. `latin-1` decodes
anything and `read_csv` picks a type and SQLite stores what it is given — five tools
that answer rather than fail, collected in a table in module 19 and closed in module 23
by the first one that refuses. tkinter exits 0 with every button broken and Textual
exits 1 from the same bug. mypy rejects a dict where Pydantic accepts it. **None of
those is a mistake by the people who wrote them.** They are different answers to
"what should happen when I cannot be sure", and the whole of engineering judgement is
knowing which answer you are standing in.

**And the third.** The material says "measured" a great deal and "obviously" not once,
and that is deliberate. There is no sentence in twenty-six modules telling you that
something is easy, and none telling you not to worry. You have four semesters of C and
Java behind you and a job; what was new here was Python, and treating it as anything
more than that would have wasted your time. If some of it was too long, you were meant
to skip it — that was the arrangement from module 00, and skipping is not cheating.

What is left is not more Python. It is the habit: **when you do not know, measure — and
when you do know, measure anyway, because knowing has been wrong before.**

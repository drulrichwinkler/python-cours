# Module 00 — Setup and how this course works

**Time:** about 45 minutes · **Assumes:** nothing at all · **Start here.**

This module teaches no Python. It is a walk through the tools, on one tiny example, so that in
module 01 you can think about the language instead of about your editor.

## What you need

Two programs. Everything else is handled for you.

| | |
|---|---|
| **[uv](https://docs.astral.sh/uv/)** | manages Python itself and every package. You do **not** install Python separately — `uv` fetches the right version |
| **[VS Code](https://code.visualstudio.com/)** | the editor. Install the *Python* and *Jupyter* extensions when it offers |

Install `uv`:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then, once, in the course folder:

```bash
uv sync
```

That reads `pyproject.toml`, downloads Python 3.12 if you do not have it, creates a `.venv`
folder and installs everything the course needs. It takes a minute the first time and a second
after that.

## The one command you need

**`uv run` puts anything in front of the course's own environment.**

```bash
uv run python hello.py       # run a file
uv run pytest 00_setup       # run the tests
uv run mypy                  # check the types
uv run ruff check .          # check the style
uv run jupyter lab           # open the notebooks
```

You never activate a virtual environment by hand and you never type `pip install`. If a command
fails with "module not found", the fix is almost always that you left out `uv run`.

Two more that come up occasionally:

```bash
uv sync                      # after pulling changes: bring the environment up to date
uv add requests              # add a package (you will need this from module 16)
```

## Order of work

1. **`explore.ipynb`** — the guided tour. Open it with `uv run jupyter lab`, or just click the
   file in VS Code. About 20 minutes.
2. **`exercises/exercise_01.py`** — one line to fill in.
3. **The three checks**, in this order:

   ```bash
   uv run pytest 00_setup      # does it compute the right thing?
   uv run mypy                 # do the types line up?
   uv run ruff check .         # is the style clean?
   ```

4. **`solutions/solution_01.py`** — last, to compare.

## What "done" looks like

```
$ uv run pytest 00_setup
2 passed
```

Before you fill anything in you will see **one failure and one pass**. That is correct: the
failing test is yours, the passing one belongs to the model solution. **Red is the starting
position, not a problem.**

## Why this module looks different from the rest

The exercise here defines a *function* with *type hints* — both of which are properly taught in
module 04. That is deliberate: a function is the smallest thing a real unit test can call, and a
type hint is the smallest thing a type checker can check. You are not expected to understand the
syntax yet. You are expected to know which command to type.

From module 01 the exercises go back to the beginning and build up in order.

## If something does not work

| symptom | most likely cause |
|---|---|
| `command not found: uv` | `uv` is not installed, or the terminal was open before you installed it — open a new one |
| `No module named course` | you left out `uv run` |
| a notebook cell hangs | the kernel is busy. **Kernel → Restart Kernel** |
| output makes no sense | cells ran out of order. **Kernel → Restart Kernel and Run All Cells** |
| `uv run pytest` finds no tests | you are not in the course folder. `cd` into it |

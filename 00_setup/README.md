# Module 00 — Setup and how this course works

**Assumes:** you have programmed before, in any language · **Start here.**

This module teaches no Python. It is a walk through the tools, on one tiny example, so that in
module 01 you can think about the language instead of about your editor.

## Two ways to get started

**A — In a container (nothing to install).** Open the repository in **GitHub Codespaces**, or
locally in VS Code with the *Dev Containers* extension and **Reopen in Container**. Python 3.12,
`uv`, the editor extensions and the course environment are all set up for you. The setup runs
once, ends by running the tests, and prints the first command. Skip to *Order of work* below.

Use this if installing things on your machine is awkward — a locked-down work laptop, for
instance, or simply a first week you would rather spend on Python than on `PATH` problems.

**B — On your own machine.** Two programs to install, described next. Worth doing at some point:
what you learn here you will use on every Python project afterwards.

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

1. **`explore.ipynb`** — the guided tour, and where `assert` is introduced: it is how every
   prediction and every test in this course states what it expects. Open it with
   `uv run jupyter lab`, or just click the
   file in VS Code.
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

Before you fill anything in you will see **one failure and one pass**: the failing test is yours,
the passing one belongs to the model solution.

## Why the editor feels quieter here

This repository ships a `.vscode/settings.json` that turns completion **down**.
Nothing pops up while you type: no suggestion list, no ghost text finishing your line, no
argument hints, no Copilot.

An editor that finishes the line before you have thought it is excellent in a language you know
and poor in one you are learning: you end up recognising Python rather than producing it.

**Everything is still one keystroke away.** `Ctrl+Space` opens the list when you want it. What
stays on: squiggles for real errors, hovers, go-to-definition, the test explorer — those describe
code that already exists rather than writing it.

Delete the file if you disagree.

## Reading the tests

You are meant to open `tests/` and read it. The test says, in code, exactly what your exercise
has to do — it is the most precise description of the task there is.

It also contains syntax you have not met yet: file paths, decorators, `assert`. **Every one of
those lines carries a comment explaining what it does**, and that stays true through the early
modules. You need to be able to *read* those files, not to write them. The ability to write them
arrives gradually — decorators in module 14, testing itself in module 15.

## Why this module looks different from the rest

The exercise defines a function with type hints, which Python-wise belongs to module 04. A
function is the smallest thing a unit test can call and an annotation the smallest thing a type
checker can check, so a tour of the tooling needs both. Take the syntax on trust here; what this
module is about is which command to type.

## If something does not work

| symptom | most likely cause |
|---|---|
| `command not found: uv` | `uv` is not installed, or the terminal was open before you installed it — open a new one |
| `No module named course` | you left out `uv run` |
| a notebook cell hangs | the kernel is busy. **Kernel → Restart Kernel** |
| output makes no sense | cells ran out of order. **Kernel → Restart Kernel and Run All Cells** |
| `uv run pytest` finds no tests | you are not in the course folder. `cd` into it |

# Python Course

**A practice project.** You work on your own, at your own
pace, and the machine tells you whether it is right.

> **Who is this for?** People who can already program — C, Java, C++ — and need Python. It does
> not explain what a variable, a loop or an exception is. It spends its time on the places where
> Python behaves differently from what you know, on the idioms, and on the toolchain — and it
> ends with an application you can show: a web page, an API, a data analysis, a window.

**Start with [`00_setup/`](00_setup/).** It installs the tools and walks you through the workflow
on one tiny example.

---

## Quick start

**Nothing to install:** open the repository in **GitHub Codespaces**, or in VS Code with the
*Dev Containers* extension and *Reopen in Container*. Python, uv and every tool are set up for
you; when the setup finishes it prints the first command to run. Takes a few minutes once.

**On your own machine:**

```bash
git clone <this-repository>
cd 2026-python-course
uv sync
uv run jupyter lab 00_setup/explore.ipynb
```

You need [uv](https://docs.astral.sh/uv/) and [VS Code](https://code.visualstudio.com/).
`uv` fetches Python itself — do not install it separately. Details in `00_setup/README.md`.

## How a module works

Every module folder has the same shape:

|                         |                                                                      |
| ----------------------- | -------------------------------------------------------------------- |
| `README.md`             | read first — what it is about, what you will be able to do           |
| `explore.ipynb`         | predict, get a verdict, then see what actually happens               |
| `exercises/`            | files with a `# TODO` for you                                        |
| `exercises/thinking.md` | the exercises you answer in prose, with graded hints                 |
| `tests/`                | one test per exercise — read them, they say exactly what is expected |
| `solutions/`            | one model solution per exercise. **Last.**                           |

Work in that order. Reading the solution first produces the feeling of understanding without the
ability, which is the most expensive mistake available in self-study.

## How you know you are done

Three commands, in this order:

```bash
uv run pytest 01_basics     # does it do the right thing?
uv run mypy                 # do the types line up?
uv run ruff check .         # is the style clean?
```

**Name the module you are working on.** `uv run pytest` without a path runs the whole course, and
that stays red until the last exercise in it is finished — one line per exercise nobody has done
yet, which buries the one you care about.

`pytest` shows **two tests per exercise**: one for the model solution, which is always green, and
one for yours, which is red until you finish.

In the notebooks, predictions are plain `assert` statements with `...` where your answer goes:

```python
assert 7 // 2 == ...
```

`...` is a real Python value and never equals a number, so the cell fails until you fill it in.
**Silence means right.** No hidden machinery, and the same `assert` you will meet in every test.

**Guess rather than skip.** A wrong prediction marks the exact spot where your idea of the
machine differs from the machine, and that is the only thing worth spending time on.

## Structure

| Part | Modules | Content                                                                |
| ---- | ------- | ---------------------------------------------------------------------- |
| 0    | 00      | Setup: uv, the editor, the workflow, the three checks                  |
| 1    | 01–05   | Core language: variables, operators, branches, loops, functions, lists |
| 2    | 06–10   | Data and robustness: dictionaries, strings, files, errors, modules     |
| 3    | 11–13   | Objects: classes, inheritance, generators                              |
| 4    | 14–19   | Tools and data: decorators, testing, HTTP, scraping, pandas, SQL       |
| 5    | 20–25   | Excursions: Flask, Streamlit, FastAPI, Tkinter, Textual                |
| 6    | 26      | Final project                                                          |

**One thread runs through all of it:** a sensor log file. It gets read (08), tested (15), fetched
over HTTP (16), analysed with pandas (18), stored in SQLite (19) — and then displayed five times
over: as a web page, a data app, an API, a desktop window and a terminal interface.

## Status

| Module       |             |
| ------------ | ----------- |
| 00 Setup     | ✅ complete |
| 01 Basics    | ✅ complete |
| 02 Operators | ✅ complete |
| 03–26        | ⬜ planned  |

Modules are added in order. If something in an existing one is wrong, unclear or simply
annoying, open an issue — that is the fastest way for the course to get better.

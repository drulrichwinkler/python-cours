# Python Course

**A practice project.** You work on your own, at your own
pace, and the machine tells you whether it is right.

> **Who is this for?** People who have never programmed in python. It starts at "what is a variable?" and
> ends with an application you can show — a web page, an API, a data analysis, a window.
>
> **If you can already program** — C, Java, C++ — and only need Python, you will save weeks by
> taking _Python for Switchers_ instead.

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

`pytest` shows **two tests per exercise**: one for the model solution, which is always green, and
one for yours, which is red until you finish. Red is the starting position, not a problem.

In the notebooks, `check()` compares your prediction against a checksum. **The answer is not
written down anywhere in this repository** — you cannot peek by accident, and you still get an
immediate verdict.

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

The design rationale lives in [`docs/`](docs/) — in German, and written before the course was
turned into a practice project. The header of `docs/GRUNDSTRUKTUR-grundkurs.md` says which parts
still hold.

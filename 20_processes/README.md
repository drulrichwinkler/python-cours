# Module 20 — Processes that run and wait

**Assumes:** modules 01–19 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 20_processes` says whether your exercises are done

## What this is about

A short module, and the only one in Part 5 with no framework in it. Everything from here on is a
program that **does not finish**: you start it, it waits, and your terminal is occupied until you
stop it.

- **A port is a number a program asks for.** `localhost:5000` is an address and a number.
  Port `0` means "any free one" — which is what modules 16 and 17 used so their tests could not
  clash. Flask defaults to 5000, uvicorn to 8000, Streamlit to 8501, and none of those is special.
- **A port is held by one listener at a time.** Ask for a taken one and the bind fails with
  `Address already in use` — the error you will actually meet, when the previous Flask is still
  running. The `errno` differs per system (48, 98, 10048), so code that reacts to it tests
  `errno.EADDRINUSE` rather than a number.
- **`app.run()` does not return.** Nothing below it executes, your prompt does not come back, and
  you need a second terminal. The process is asleep in a system call — blocking is not busy.
- **Ctrl+C sends SIGINT, and Python turns SIGINT into `KeyboardInterrupt`.** Which is the moment
  module 09's remark mattered: it comes off `BaseException`, so a bare `except:` swallows it and
  makes a program that cannot be stopped.
- **`127.0.0.1` or `0.0.0.0` is a decision.** The first is this machine only; the second is
  anything that can route to you. `debug=True` puts an interactive Python console on the
  traceback page, so the two together are indefensible outside your own laptop.

## The package underneath Part 5

Five modules, five frameworks, **one task**: show these readings to a person.

| module | | what it makes |
| --- | --- | --- |
| 21 | Flask | a web page, with routes and a template |
| 22 | Streamlit | the same analysis, with no HTML and no routing |
| 23 | FastAPI | a JSON API, documented from your type hints |
| 24 | Tkinter | a desktop window, and an event loop |
| 25 | Textual | the same in a terminal |

Holding the task constant is the design. Five frameworks described one after another give you
five sets of syntax; five frameworks solving one problem give you a comparison, and the answer to
"when would I use which" falls out instead of being asserted.

For that to be honest the analysis has to be the same code, so it is: **`sensorreport`** is an
installed package of this repository, and all five modules import it. Its numbers are the same
ones module 18 computed with pandas and module 19 with SQL, arrived at a third way — a frozen
`@dataclass` from module 12 and no dependencies at all.

Note how it imports:

```python
from sensorreport import faults, load_readings, summarise
```

No `sys.path`, from any directory, because `pyproject.toml` lists it as a package and `uv sync`
installed it. That is module 10's argument, made by the repository rather than asserted in it.

## What you can do afterwards

1. **say** what a port is, and what happens when two programs want the same one;
2. **say** why a server does not return, and what that means for your terminal;
3. **stop** a blocking process, and say what Ctrl+C sends and what Python does with it;
4. **tell apart** an exit code a program chose from one a signal imposed;
5. **say** what binding `0.0.0.0` gives away, and why not with `debug=True`.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — five files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 20_processes`**
4. **`solutions/`** — last

Fewer exercises than usual: this module is a ramp, not a topic.

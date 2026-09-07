# Module 25 — Textual

**Assumes:** modules 01–24 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 25_textual` says whether your exercises are done

## What this is about

The last of the five presentations, and the same numbers again — this time in the terminal you
are already sitting in.

```console
uv run python 25_textual/app.py
```

`q` quits. So does Ctrl+C, which module 24's window could not manage: here the terminal is still
the terminal.

`app.py` imports `24_tkinter/logic.py`. Not a copy of it — the same file. Module 24's argument
for keeping the formatting out of the callbacks was that you cannot test a callback; this module
is the second payment on it, and it arrived without any work.

Three things are different from module 24, and each one is the answer to a problem module 24
had.

## 1. The layout is data

`app.tcss` next to `app.py` is a real stylesheet — Textual parses CSS. Widths, borders, colours
and padding live there, and `compose` says nothing about where anything goes:

```python
def compose(self) -> ComposeResult:
    yield Static("Sensor readings", id="title")
    with Horizontal(id="controls"):
        yield Label("location")
        yield Button(self.location, id="location")
    yield DataTable(id="table")
```

Module 24 arranged its widgets with `.pack()` calls inside `__init__`, which is code, in a
method, in a class. Change a width there and you edit Python. Change it here and you edit a file
that has no behaviour in it at all.

And `compose` is a **generator function** — module 13, where you would not have looked for one.
Calling it runs nothing: `type(SensorApp().compose()).__name__` is `'generator'`. It does not
build the interface, it describes it, and Textual is the consumer.

## 2. A handler is found by name

```python
def on_button_pressed(self, event: Button.Pressed) -> None: ...
```

Nothing registers that. There is no `command=` and no decorator: the method is called because of
what it is called. Keys work the same way — `BINDINGS = [("n", "next_location", "Next
location")]` finds `action_next_location`.

Which is the third *mechanism* the course has shown, across four module answers — a decorator
(21 and 23), an argument passed at construction (24), and the method's name (25). Streamlit's
answer is the fourth and it is "nothing to register". Three of the four can fail in silence.
Measured:

| module | how | the silent failure |
| --- | --- | --- |
| 21 Flask | `@app.get("/summary")` | `@app.get("/summry")` → `/summry` answers 200 |
| 22 Streamlit | nothing to register | — |
| 24 tkinter | `command=self.refresh` | `command=self.refresh()` → the button gets `None` |
| 25 Textual | the method's name | `on_button_press` → never called, no warning |

In each case the mistake is a **valid value in a position the framework has no expectations
for**, which is why no type checker and no linter can catch any of them. What each one has
instead is something you can ask: `widget.cget("command")`, `Button.Pressed.handler_name`,
`app.url_map`. Exercise 07 is that comparison.

## 3. A reactive attribute redraws by itself

```python
limit: reactive[float] = reactive(LIMIT, init=False)
```

`app.limit = 90.0` is an ordinary assignment and `app.limit` is a float — no wrapper object,
unlike module 24's `StringVar`, which held a string and needed `.get()`. What is not ordinary is
that Textual then calls `watch_limit`, so the redraw is a **consequence** of the assignment
rather than something the assigning code has to remember.

`init=False` matters and is not guessable. Without it Textual calls the watcher once during
initialisation — measured: it runs at construction time, with the old and the new value both
85.0, before anything is on screen. A `redraw` that queries for the table then fails, because
`compose` has not yielded it yet, and the app does not start.

## The test client that works, and why it can

Modules 21, 22 and 23 each had one. Module 24 had none, because its input is events from the
window manager: the same simulated keypress answered differently with the window visible,
off-screen and withdrawn.

Here it works:

```python
async with app.run_test() as pilot:
    await pilot.press("n")
    await pilot.click("#location")
    app.limit = 90.0
    await pilot.pause()
```

**Because Textual owns the screen.** It is a grid of characters Textual allocates and fills, and
nothing else has an opinion about it — `run_test(size=(30, 6))` gives you a screen thirty by
six, because the size is Textual's to decide. So an injected event is known to arrive.

**About `async`.** `run_test()` is an asynchronous context manager, so the driving code lives in
an `async def` started by `asyncio.run(...)`. This course does not teach asyncio and you do not
need it here. Read `await x` as "call x, and let the event loop have a turn while it works" —
the same event loop idea as module 24, except that this one is asyncio's rather than Tk's C
code. `await pilot.pause()` means "let everything pending happen before I look".

**And where it is not naive.** Measured: five `pilot.press("n")` gave an identical list on three
separate runs. Five `pilot.click("#location")` with no delay registered **three** times, because
two clicks in quick succession are a double-click — one `Button.Pressed`, not two, which is what
a real user's double-click does. With 0.3 s between them all five arrive.

Worse for a test: *which* pairs get folded varies between runs, since it depends on where the
wall clock falls. So the count is stable and the sequence is not. **Press keys, or space your
clicks, and never assert on a sequence whose order a clock decides** — module 22's flaky test,
one more time.

## The same bug, the opposite answer

Modules 24 and 25 were handed one identical mistake: a handler that raises `ValueError`.
Measured, both:

| | tkinter (24) | Textual (25) |
| --- | --- | --- |
| the app afterwards | still running | stopped |
| the traceback | stderr, `Exception in Tkinter callback` | propagated, names your frame |
| the caller | `invoke()` returns normally | re-raised on leaving `run_test()` |
| the exit code | **0** | **1** |

Neither is a bug. tkinter assumes the process exists to serve a person who is present and has
state in it, so one broken button must not take away their window. Textual assumes the process
is an interface it is answerable for, and a screen that no longer reflects what the program
believes is worse than no screen. Which assumption is right depends on how the program was
started — and neither toolkit knows that. You do.

## What you can do afterwards

1. **say** what `compose` is and why it can be a generator function;
2. **say** how a handler and a key binding are found, and name the three silent failures that
   follow from registration by name, path and value;
3. **use** a reactive attribute, and say what `init=False` prevents;
4. **test** an app with `run_test` and `Pilot`, and say why that is possible here and was not in
   module 24;
5. **say** what a repeated `pilot.click` does that a repeated `pilot.press` does not;
6. **say** which of the five presentations works over ssh, and what each of the other four needs.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 25_textual`**
4. **`solutions/`** — last

## All five, side by side

| | Flask (21) | Streamlit (22) | FastAPI (23) | tkinter (24) | Textual (25) |
| --- | --- | --- | --- | --- | --- |
| the caller | a browser | a browser | a program | a person here | a person in a terminal |
| the layout | your HTML | Streamlit's | none | `.pack()` calls | a CSS file |
| a callback | a decorator | none | a decorator | `command=` | the method's name |
| a test client | `test_client()` | `AppTest` | `TestClient` | **none** | `run_test()` |
| needs a display | no | no | no | **yes** | no |
| needs a port | yes | yes | yes | no | no |
| works over ssh | with tunnelling | with tunnelling | with tunnelling | no | **yes** |

**The heuristic, finally: what can you assume about the far end?** A browser and a port, and it
is one of the first three. A screen on this machine, and it is tkinter. Nothing but a terminal,
and it is this one — which is more often the honest answer than it looks, because a terminal is
what you have on every machine you can reach at all.

## Two more, which this course does not cover

**PyQt6** and **PySide6** both wrap Qt, the same C++ library, and the code you write is nearly
identical. The difference that decides between them is the licence: **PyQt6 is GPL or a paid
commercial licence; PySide6 is LGPL.** For an internal tool nobody outside the company receives,
either is fine. For anything you ship to a customer, PyQt6 means publishing your source or
buying a licence, and PySide6 does not — so PySide6 is the one to evaluate first. Exercise 08
asks what you would put to your legal department, which is a shorter list than it sounds.

---

That is Part 5. One analysis, five presentations, and every difference between them measured
rather than asserted. Module 26 is the final project: everything at once, built on your own.

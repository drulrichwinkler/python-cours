# Module 24 — Tkinter

**Assumes:** modules 01–23 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 24_tkinter` says whether your exercises are done

## What this is about

The same numbers as modules 21, 22 and 23, in a window on your own machine. No browser, no
port, no HTTP.

```console
uv run python 24_tkinter/app.py
```

A window opens. There is nothing to open in a browser and no address to type, and **Ctrl+C
does not reliably stop it** — closing the window does. That last detail is not a quirk. It is
the module.

> **The program does not run. It waits.**

`app.py` ends with `root.mainloop()`, and nothing written after that line executes while the
window is on screen. Control is handed to Tk once, at startup, and comes back when the window
is destroyed. Everything your program does in between, it does because Tk called it.

Measured, and it is worth predicting before you read it:

```python
root.after(0, lambda: log.append("one"))
print(log)          # []          -- scheduled, and nothing ran it
root.update()       #                one turn of the loop, by hand
print(log)          # ['one']
```

`after(0, f)` does not call `f`. It puts `f` on a queue. The thing that takes it off is the
event loop, and while your script is running, the loop is not.

## What follows from that

- **A callback takes no arguments and returns nothing.** The loop has nothing to pass it and
  nowhere to put an answer. So everything it needs comes from `self` — which is why `app.py` is
  a class and not a function — and everything it produces goes into a widget.
- **A slow callback freezes the window.** Measured: a callback that sleeps 300 ms, and a second
  one due at 10 ms that did not get its turn until the first had returned. One thread, and the
  first one was holding it. A thirty-second HTTP fetch in a callback is half a minute of a
  window a user is entitled to think is broken.
- **`command=self.refresh` and not `command=self.refresh()`.** Module 14's distinction, and here
  it is a silent bug: the parentheses call the method once, now, and hand the button its return
  value. Tk accepts `None` as "no command", so you get a button that looks right and does
  nothing. Exercise 03 is that bug.
- **An exception in a callback stops nothing.** Measured: the traceback goes to **stderr**, the
  loop continues, `invoke()` does not re-raise, and the process exits with code **0**. A GUI
  whose every button raises is a program that reports success — to a `&&` chain, to a service
  manager, and to this repository's own CI.

## Why there is no test client

Modules 21, 22 and 23 each had one: `test_client()`, `AppTest`, `TestClient`. Each works because
the application's input is data a test can construct — an HTTP request is bytes.

Tkinter's input is not data. It is events from the **window manager**. Measured: the same
`event_generate("<Return>")` gave a different answer with the window visible, off-screen and
withdrawn, because whether a keypress reaches a widget depends on which window has focus, and
focus is not your program's business. Faking that faithfully means faking an operating-system
service.

So the answer here is architectural rather than technical, and it is the part of this module
worth keeping:

**Put nothing in a callback that you cannot also call on its own.**

`logic.py` holds the formatting and the limit decision. It imports no tkinter, it runs on a
machine with no screen, and exercise 05 tests it without a window at all. `app.py` reads it and
does nothing else. Buttons are pressed with `invoke()`, which calls the registered command:

```python
window.limit.set("90")
window.button.invoke()      # no mouse, no click, no window manager
window.status.get()         # '2 of 20 readings above 90.0'
```

**And be honest about the gap.** Measured: `invoke()` honours `state="disabled"` and ignores
whether the widget is in the layout. Delete a `.pack()` line and every test still passes while
the window has no button in it. These tests check that the program computes the right thing and
puts it in the right widget. Nothing here can check that a person can see or reach it, and there
is no substitute for opening the window once and looking.

## If tkinter will not start

Under this project's toolchain the first `Tk()` fails with

```
_tkinter.TclError: Can't find a usable init.tcl in the following directories:
    /tools/deps/lib/tcl8.6  .../.venv/lib/tcl8.6  ...
```

That first path is a directory on the machine that built the interpreter, months ago, on
somebody else's disk — which tells you what kind of problem this is. `tkinter` is not Python; it
wraps **Tcl/Tk**, a C library with its own script files, and the wrapper looks for them under
`sys.prefix`, which inside a virtual environment is the virtual environment. The files came with
the *base* interpreter instead.

`display.py` fixes it in three lines and explains it in full. Every file in this module calls
`use_bundled_tcl()` before its first `Tk()`, which is why that import is at the top of all of
them.

Two consequences worth carrying away. First, the Tk version differs by platform for the same
Python: **8.6 on macOS, 9.0 on Linux**, because it is a different C library on each. Second,
`uv sync` resolving cleanly proves the Python dependencies are in place and proves nothing about
the C libraries underneath them. That layer is where "it works on my machine" comes from.

**On a machine with no graphical session** — a server, a container — six of the seven tests skip
with a reason rather than failing, and exercise 05 still runs. To run them anyway on Linux:

```console
xvfb-run -a uv run pytest 24_tkinter
```

which is what this repository does in continuous integration.

## What you can do afterwards

1. **say** what `after(0, f)` does and what has to happen before `f` runs;
2. **say** why a callback has no arguments and no return value, and where its result goes;
3. **say** what a slow callback does to a window, and sketch the `after`-based alternative;
4. **find** the `command=f()` bug, and say why it produces no error;
5. **say** where an exception in a callback goes, and what the exit code is;
6. **test** a window without a click — and name one thing such a test cannot check.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 24_tkinter`**
4. **`solutions/`** — last

## Where tkinter sits among the five

| | Flask (21) | Streamlit (22) | FastAPI (23) | tkinter (24) |
| --- | --- | --- | --- | --- |
| the caller | a browser | a browser | a program | a person at this machine |
| who owns the loop | the server | the server | the server | your process |
| you hand control away | per request | per script run | per route call | once, for the whole program |
| bad input | your `if` | no input to be bad | 422, before your code | your `try`, in the callback |
| a test client | `test_client()` | `AppTest` | `TestClient` | **none** |
| needs a network | yes | yes | yes | no |
| needs a display | no | no | no | **yes** |

**The heuristic: is the machine the user is at the machine the program runs on?** If yes, a
window needs no server, no port and no browser, and it works when the network is down — which
on a shop floor is the requirement. If no, one of the three above it.

Module 25 does the same thing in a terminal, where there is no window manager to fight and the
layout is declarative. It is also the only one of the five that works down an ssh connection.

# Solution 08 — The exception nobody sees, and the missing test client

**a) Exit code 0**

Three things that read it as success, and what each would conclude:

1. **A shell `&&` chain, or a Makefile.** `python app.py && ./upload_results.sh`
   proceeds to the upload. It concludes the application ran correctly and there is
   something to upload.
2. **A CI job** — and there is one in this repository. A step whose command exits 0 is
   a green step. A workflow that launched this program would report a passing build for
   a program in which every button is dead.
3. **A service manager or a monitoring probe** — systemd, a container health check, a
   cron job with `MAILTO`. `Restart=on-failure` sees no failure and does not restart;
   the health check reports healthy; cron sends no mail. The conclusion in every case
   is that nothing needs attention.

The pattern: the exit code is the only thing any of them looks at, and it is reporting
on the *process*, which really did complete. It is not reporting on the program's
behaviour, and nothing here is.

**b) The case for catching it, and what it costs**

**For:** the alternative is that an exception in one callback tears down the event
loop, which means the window vanishes. A user who mistyped a limit would lose the
window, and with it whatever they had not saved — because of a bug in one button that
has nothing to do with the rest of the application. A GUI is a long-lived process
holding state a person put there by hand, and the reasonable default for such a
process is to survive one broken interaction.

That is the same argument for a web server not exiting when one request raises. Flask
does not stop either; it answers 500 and waits for the next request.

**What it costs:** the difference is where the report goes. Flask's 500 reaches the
person who caused it and appears in an access log. Tk's traceback goes to stderr — a
stream that, for a program started by double-clicking an icon, is not attached to
anything. The failure is silent to the user, silent to the exit code, and silent to
anyone who is not watching the terminal it happened to be launched from.

What to put around the callback so the cost is yours:

```python
def guarded(method):
    """Log what the loop would otherwise swallow, and tell the user.

    It decorates a *method*, so `self` has to be a parameter of the wrapper --
    otherwise the except branch replaces the ValueError with a NameError, which is
    the same failure one layer further in.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except Exception:
            logging.exception("%s failed", method.__name__)
            self.status.set("something went wrong -- see the log")
    return wrapper
```

That is module 14's decorator and module 09's `logging.exception`, applied to the one
place where an unhandled exception disappears. Two things happen that did not before:
the traceback lands in a file that outlives the terminal, and the user is told rather
than left looking at a button that does nothing.

**c) Why there is no test client**

A test client for Flask, Streamlit or FastAPI works because the input to the
application is **data the test can construct**. An HTTP request is bytes; `AppTest`
sets a widget's value and re-runs the script. In all three, the framework is a function
from data to data, and a test can supply the data.

Tkinter's input is not data. It is a stream of events from the **window manager**, and
measurement Two is what that means in practice: the same `event_generate("<Return>")`
gave three different answers depending on whether the window was visible, off-screen
or withdrawn — because whether a keypress reaches a widget depends on which window has
focus, and focus is assigned by the window manager. So what a test client would have
to fake is not the widget and not Tk; it is the window manager, and with it the
pointer position, the focus stack, the z-order and the compositor. That is an
operating-system service, and faking it faithfully enough to be worth trusting is a
larger program than the one under test.

**The architectural answer this module takes:** don't test the click. Put nothing in a
callback that cannot be called directly, keep everything else in `logic.py`, and press
buttons with `invoke()`, which calls the registered command without going near the
window manager.

**What it costs — the concrete gap.** Measured:

```
invoke() on a button with state="disabled"   ->  nothing ran     (invoke respects it)
invoke() on a button that was never packed   ->  the command ran (winfo_ismapped: 0)
```

So `invoke()` is not blind — it honours the widget's own state. But it does not care
whether the widget is **in the layout**. Delete the `self.button.pack()` line from
`app.py` and every test in `tests/` still passes, while the window has no button in it
at all. The same holds for `self.listing.pack()` in exercise 09: the listbox is filled,
`size()` reports 20, and nothing is on screen.

That is the honest limit of this module's testing strategy. It checks that the program
computes the right thing and puts it in the right widget. It cannot check that a human
can see or reach that widget, and there is no substitute for opening the window once
and looking.

**d) The class of problem**

**A compiled dependency, looking for its own files by a path baked in when it was
built.** Nothing about it is Python: the version differs by operating system because it
is a different C library on each, and the failing path is a directory on a stranger's
disk because that is where the build happened.

Another dependency in this course with the same property: **pandas** (module 18) — it
is a C and Cython extension, its wheels are built per platform and per Python version,
and when the binary does not fit the interpreter you get an `ImportError` from
`pandas._libs` rather than anything a Python-level error message would explain.

`sqlite3` (module 19) qualifies too, and it is the sharper example because *how* it is
built differs. Measured on this project's interpreter:

```python
>>> "_sqlite3" in sys.builtin_module_names
True
>>> sqlite3.sqlite_version
'3.50.4'
```

No `__file__` at all: SQLite is compiled **into** this interpreter, and that version
number is fixed no matter what the machine has installed. On a Debian or Homebrew
Python the same module is a shared object linked against the system `libsqlite3`, and
the version then follows the machine. So which SQLite you get, and which `PRAGMA`s
work, is a property of the interpreter you are running rather than of the Python code
you wrote.

One that cannot have it: **`csv`** (module 08). It is pure Python — a `.py` file in the
standard library. So is `pathlib`, and so is `dataclasses`. There is no build, no
platform, and no path to get wrong; the only way to break them is to break Python
itself.

The general point for a dual-study reader: `uv sync` resolving cleanly proves the
*Python* dependencies are in place. It proves nothing about the C libraries underneath
them, and that is the layer where "it works on my machine" comes from.

**e) All five, once each**

1. **an operator on the shop floor enters a serial number and gets a verdict** →
   **tkinter.** A machine on the floor, one task, no browser, and quite possibly no
   network. A window that starts with the machine and needs nothing installed beyond
   Python is exactly right, and the input is a barcode scanner pretending to be a
   keyboard.
2. **a colleague explores last night's readings and adjusts a limit** →
   **Streamlit.** The point is the data, the caller is a person next to you, and a
   slider and a table are the whole requirement.
3. **the test rig's controller reads the limit every thirty seconds** → **FastAPI.**
   The caller is a program. It wants JSON, a schema and a status code, and has no use
   for a page.
4. **watching a long-running job over ssh, on a server** → **Textual** (module 25).
   There is no display on the other end of an ssh connection and no browser, and a
   terminal interface is the only one of the five that works down a pipe.

Which leaves **Flask** with none of the four, and that is worth saying rather than
hiding: Flask is what you reach for when the answer is a *page* — a URL someone
bookmarks, a layout someone shows a manager, something with a login. None of these
four is that, and a heuristic that always finds a use for every tool is not a
heuristic.

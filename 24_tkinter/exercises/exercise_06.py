"""Exercise 06 -- The exception nobody sees.

A script that raises stops, and the shell gets a non-zero exit code. A callback that
raises does not stop anything: the event loop catches it, prints a traceback to
**stderr**, and goes on to the next event. The button did nothing, the window looks
fine, and the process will exit successfully.

Run the broken button and the working one and print four lines:

  1. `before: <the log>`
  2. after invoking the broken button, `after the bad button: <the log>`
  3. after invoking the working one, `after the good button: <the log>`
  4. `invoke() re-raised: <True or False>`

Expected output:

    before: []
    after the bad button: []
    after the good button: ['pressed']
    invoke() re-raised: False

Line 2 is two findings in one. The log is unchanged, so the callback did not do its
work -- and the line printed at all, so this script is still running. Put no `try`
around that first `invoke()`: if the exception had come through, the script would have
ended there and lines 2, 3 and 4 would not exist.

Line 4 confirms it deliberately. And if you run this file and look at the exit code,
it is **0**. A GUI whose buttons are broken is a program that reports success.

Compare it with the three frameworks before this one. Flask turns an exception into a
500 that the client sees. FastAPI's `TestClient` re-raises it so a test fails.
Streamlit puts the traceback in the page. Here it goes to a stream nobody is reading.

Hint: for line 4, invoke the broken button a second time inside
`try` / `except Exception` and record whether the `except` branch ran. Run the file
yourself and look at what appears on your terminal but not in the expected output
above -- that is the stream the traceback went to.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from display import use_bundled_tcl  # noqa: E402

# Has to run before the first Tk() -- see display.py. Every file in this module
# starts with it, because a Tk() that comes first fails with a TclError about
# init.tcl and a path from the machine that built the interpreter.
use_bundled_tcl()

import tkinter  # noqa: E402

root = tkinter.Tk()
root.withdraw()

log: list[str] = []


def broken() -> None:
    """A callback with a bug in it."""
    raise ValueError("the callback is broken")


def works() -> None:
    """A callback without one."""
    log.append("pressed")


bad = tkinter.Button(root, text="bad", command=broken)
good = tkinter.Button(root, text="good", command=works)
bad.pack()
good.pack()
root.update()

# TODO: four prints

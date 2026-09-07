"""Exercise 04 -- A StringVar is not a str.

`tkinter.StringVar` is a handle on a value that Tcl also holds. Bind a widget to one
and the two stay in step in both directions, without anybody calling a redraw: set the
variable and the Entry shows the new text; type in the Entry and the variable has it.

`trace_add("write", callback)` runs your function on every write. Print five lines:

  1. `var starts: <the value>`
  2. `entry shows: <what the Entry contains>`
  3. after `var.set("90.0")`, `after set, entry shows: <what the Entry contains>`
  4. after clearing the Entry and inserting `42`, `after editing, var says: <the value>`
  5. `trace fired for: <every value the callback saw, as a list>`

Expected output:

    var starts: 85.0
    entry shows: 85.0
    after set, entry shows: 90.0
    after editing, var says: 42
    trace fired for: ['90.0', '', '42']

Line 5 has three entries for two changes, and the middle one is empty. Look at what
the code does to the Entry and you will see why. It is the reason a listener that
validates on every write is a bad idea: it will be handed a half-finished value, and
`float("")` raises.

Hint: `entry.delete(0, "end")` then `entry.insert(0, "42")`. The callback that
`trace_add` calls is given three positional arguments you do not need here, so
`lambda *_: ...` is the usual shape.
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

var = tkinter.StringVar(value="85.0")
seen: list[str] = []

# TODO: register the trace, build the Entry, then the five prints

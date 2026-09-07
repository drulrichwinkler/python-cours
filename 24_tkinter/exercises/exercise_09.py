"""Exercise 09 -- A window, tested without a click.

Write the class. `LimitWindow` shows one location's readings in a Listbox with a limit
you can type, and a button that redraws.

  * `__init__(self, root)` builds a `StringVar` called `self.limit` starting at
    `"85.0"`, a `StringVar` called `self.status`, a `tkinter.Listbox` called
    `self.listing`, and a `tkinter.Button` called `self.button` whose command is
    `self.refresh`. It calls `self.refresh()` once at the end, so the window is not
    empty before the first press.
  * `refresh(self)` takes no arguments and returns nothing. It reads `self.limit`,
    and if the text is not a number it puts `<the text> is not a number` in
    `self.status` and leaves the listing alone. Otherwise it clears the listing, fills
    it with `rows_for("Test rig", limit)` from `logic`, and puts `verdict(...)` for the
    Test rig readings in `self.status`.

The prints at the bottom are written for you -- do not change them.

Expected output:

    rows: 20
    first: TH-04  93.5 °C  FAULT
    status: 3 of 20 readings above 85.0
    at 90: 2 of 20 readings above 90.0
    at 'warm': 'warm' is not a number
    rows after the bad limit: 20

The last line matters. A limit that is not a number left the listing as it was rather
than emptying it: the user typed something wrong, and the answer to that is a message,
not the loss of what was on screen.

Hint: `self.listing.delete(0, "end")` empties a Listbox and `insert("end", line)`
appends one. `float()` in a `try`, and `except ValueError`. The Test rig readings are
`[r for r in load_readings() if r.location == "Test rig"]`.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from display import use_bundled_tcl  # noqa: E402
from logic import rows_for, verdict  # noqa: E402

# Has to run before the first Tk() -- see display.py. Every file in this module
# starts with it, because a Tk() that comes first fails with a TclError about
# init.tcl and a path from the machine that built the interpreter.
use_bundled_tcl()

import tkinter  # noqa: E402

from sensorreport import load_readings  # noqa: E402

# TODO: the class LimitWindow


root = tkinter.Tk()
root.withdraw()

window = LimitWindow(root)
root.update()

print("rows:", window.listing.size())
print("first:", window.listing.get(0))
print("status:", window.status.get())

window.limit.set("90")
window.button.invoke()
print("at 90:", window.status.get())

window.limit.set("warm")
window.button.invoke()
print("at 'warm':", window.status.get())
print("rows after the bad limit:", window.listing.size())

root.destroy()

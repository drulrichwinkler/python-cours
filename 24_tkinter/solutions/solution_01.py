"""Solution 01 -- The loop has to turn."""

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

root.after(0, lambda: log.append("one"))
root.after(0, lambda: log.append("two"))

# Scheduled, and nothing has run them. `after(0, ...)` means "as soon as the loop
# gets to it", and the loop is not running: this script is.
print("before update:", log)

# update() is one turn of the loop by hand -- it takes whatever is queued, runs it,
# and returns. Unlike mainloop(), it does not block.
root.update()
print("after update:", log)

for _ in range(3):
    root.update()
print("after 3 more updates:", log)

root.after(50, lambda: log.append("three"))
# The destruction has to be scheduled before control is handed over. Nothing after
# mainloop() runs until the window is gone.
root.after(100, root.destroy)
root.mainloop()
print("mainloop returned, log:", log)

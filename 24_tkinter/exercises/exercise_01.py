"""Exercise 01 -- The loop has to turn.

`root.after(0, f)` does not call `f`. It puts `f` on a queue, and something else
has to take it off. That something is the event loop, and in this exercise you turn it
by hand.

Print four lines:

  1. the log right after scheduling two callbacks with `after(0, ...)`
  2. the log after one `root.update()`
  3. the log after three more `root.update()` calls
  4. the log after `mainloop()` has returned, with a third callback scheduled at 50 ms

Expected output:

    before update: []
    after update: ['one', 'two']
    after 3 more updates: ['one', 'two']
    mainloop returned, log: ['one', 'two', 'three']

Line 1 is the whole point: the callbacks were scheduled and nothing ran them.

Line 4 needs `mainloop()` to end, and the only thing that ends it is the window being
destroyed. `root.after(100, root.destroy)` is how -- schedule the destruction before
you hand over control, because after `mainloop()` you cannot schedule anything.

Hint: `log.append("one")` inside a `lambda`, since `after` wants something callable
and `append` returns None. `root.withdraw()` keeps the window off the screen; it still
has a working event loop.
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

# TODO: schedule two, print, update, print, update three times, print,
# then schedule a third and destroy, run mainloop, print

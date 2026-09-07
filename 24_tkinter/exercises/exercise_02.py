"""Exercise 02 -- The callback that blocks.

A callback runs *in* the event loop, not alongside it. So while your callback is
working, the loop is not: nothing is redrawn, no click is noticed, and no other
callback runs. That is what a frozen window is.

Two callbacks are written for you. `slow` takes 300 ms; `quick` is scheduled for
10 ms and does nothing. Run them under `mainloop()` and print:

  1. the order the three entries in `order` were appended, as a list of names
  2. whether `quick` ran only after `slow` had finished, as
     `quick ran after slow finished: <True or False>`

Expected output:

    order: ['slow start', 'slow end', 'quick']
    quick ran after slow finished: True

`quick` was due at 10 ms and `slow` does not return until 300 ms. The loop had no
say in it: there is one thread, and `slow` was holding it.

Hint: `order` collects `(name, timestamp)` pairs, so line 1 is the names out of it
and line 2 compares two timestamps. Schedule `root.after(600, root.destroy)` so
`mainloop()` ends.
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

import time  # noqa: E402
import tkinter  # noqa: E402

root = tkinter.Tk()
root.withdraw()

order: list[tuple[str, float]] = []
start = time.perf_counter()


def slow() -> None:
    """Three hundred milliseconds of work, in the loop's only thread."""
    order.append(("slow start", time.perf_counter() - start))
    time.sleep(0.3)
    order.append(("slow end", time.perf_counter() - start))


def quick() -> None:
    """Nothing at all -- it only records when it got its turn."""
    order.append(("quick", time.perf_counter() - start))


# TODO: schedule slow at 0, quick at 10, the destroy at 600, run the loop, two prints

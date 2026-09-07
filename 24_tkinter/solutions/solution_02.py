"""Solution 02 -- The callback that blocks."""

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


root.after(0, slow)
root.after(10, quick)
root.after(600, root.destroy)
root.mainloop()

print("order:", [name for name, _ in order])

# `after(10, quick)` is not a promise about 10 ms. It is a promise that quick will
# not run *earlier* than that -- the loop gets to it when it is free, and it was not.
when = dict(order)
print("quick ran after slow finished:", when["quick"] >= when["slow end"])

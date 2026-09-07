"""Solution 06 -- The exception nobody sees."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from display import use_bundled_tcl  # noqa: E402

# Has to run before the first Tk() -- see display.py for why.
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

print("before:", log)

# No `try` around this one, on purpose. Tk's callback wrapper catches whatever the
# command raises and reports it on stderr, so invoke() returns normally -- and the
# fact that the next line prints at all is the evidence. Had the exception come
# through, the script would have ended here.
bad.invoke()
print("after the bad button:", log)

good.invoke()
print("after the good button:", log)

# The same press again, this time watched. The `except` branch never runs.
raised = False
try:
    bad.invoke()
except Exception:
    raised = True
print("invoke() re-raised:", raised)

root.destroy()

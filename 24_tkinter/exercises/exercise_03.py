"""Exercise 03 -- Repair: the parentheses that ran the callback.

`command=` wants a function. The file below passes it the *result* of calling one,
which is the single most common mistake in tkinter code and produces a button that
looks fine and does nothing.

The evidence is in the first line of output: the counter is already at 1 before
anybody has pressed anything. Fix it so the counter starts at 0 and each `invoke()`
adds one.

Expected output:

    after building: 0
    after invoke: 1
    after invoke: 2

`invoke()` is how a test presses a button: it calls whatever is registered as the
command. There is no mouse and no click -- and there is a reason it has to be this
way, which `README.md` explains under "Why there is no test client".

Hint: this is module 14's distinction between a function and its return value. One
pair of parentheses is the whole fix.
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


class Counter:
    """A button and a number it adds to."""

    def __init__(self, root: tkinter.Tk) -> None:
        self.count = 0
        # TODO: this hands the button a value, not a function
        self.button = tkinter.Button(root, text="add", command=self.bump())
        self.button.pack()

    def bump(self) -> None:
        """One press."""
        self.count += 1


root = tkinter.Tk()
root.withdraw()

counter = Counter(root)
root.update()
print("after building:", counter.count)

counter.button.invoke()
print("after invoke:", counter.count)

counter.button.invoke()
print("after invoke:", counter.count)

root.destroy()

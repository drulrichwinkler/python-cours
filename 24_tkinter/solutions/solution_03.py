"""Solution 03 -- Repair: the parentheses that ran the callback."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from display import use_bundled_tcl  # noqa: E402

# Has to run before the first Tk() -- see display.py for why.
use_bundled_tcl()

import tkinter  # noqa: E402


class Counter:
    """A button and a number it adds to."""

    def __init__(self, root: tkinter.Tk) -> None:
        self.count = 0
        # `command=self.bump`, without parentheses: the button is given the bound
        # method itself and calls it later. `self.bump()` would have called it here,
        # once, and passed the button its return value -- None. Tk accepts None as
        # "no command", which is why the broken version pressed nothing and raised
        # nothing: it is a button with no command, and it looks identical.
        self.button = tkinter.Button(root, text="add", command=self.bump)
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

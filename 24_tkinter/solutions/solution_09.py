"""Solution 09 -- A window, tested without a click."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from display import use_bundled_tcl  # noqa: E402
from logic import rows_for, verdict  # noqa: E402

# Has to run before the first Tk() -- see display.py for why.
use_bundled_tcl()

import tkinter  # noqa: E402

from sensorreport import load_readings  # noqa: E402


class LimitWindow:
    """One location's readings, against a limit the user types.

    A class rather than a function, because the widgets have to outlive the call that
    built them: `refresh` runs when the button is pressed, long after `__init__`
    returned, and it has to find the listing somewhere. `self` is that somewhere.
    """

    def __init__(self, root: tkinter.Tk) -> None:
        self.limit = tkinter.StringVar(value="85.0")
        self.status = tkinter.StringVar(value="")
        self.listing = tkinter.Listbox(root, width=40, height=10)
        self.listing.pack()
        # `command=self.refresh` and not `self.refresh()`: the button is handed the
        # method, and calls it later.
        self.button = tkinter.Button(root, text="Refresh", command=self.refresh)
        self.button.pack()
        tkinter.Label(root, textvariable=self.status).pack()
        self.refresh()

    def refresh(self) -> None:
        """Redraw for whatever is in the limit box.

        No arguments and no return value, because the event loop calls this and has
        nothing to pass it and nowhere to put an answer. Everything it needs comes
        from `self`, and everything it produces goes into a widget.
        """
        text = self.limit.get()
        try:
            limit = float(text)
        except ValueError:
            # A message, and nothing else touched. An Entry holds text -- there is no
            # annotation here that would have refused the value at the boundary the
            # way module 23's did.
            self.status.set(f"{text!r} is not a number")
            return

        self.listing.delete(0, "end")
        for line in rows_for("Test rig", limit):
            self.listing.insert("end", line)

        here = [r for r in load_readings() if r.location == "Test rig"]
        self.status.set(verdict(here, limit))


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

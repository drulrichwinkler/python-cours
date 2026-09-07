"""The tkinter application this module builds up to.

Run it:

    uv run python 24_tkinter/app.py

A window opens. Closing it ends the program -- there is no Ctrl+C to press, because
the terminal is not what is in charge any more. That is the module's subject.

Everything it knows about sensors comes from `sensorreport`, and everything it knows
about *formatting* comes from `logic.py` next to this file. Nothing in this file
computes anything. That split is deliberate and it is the transferable lesson: there
is no test client for tkinter, so the only way to test a window is to have most of it
not be a window.
"""

from __future__ import annotations

import tkinter
from tkinter import ttk

from display import use_bundled_tcl
from logic import locations, rows_for, summary_line, verdict

from sensorreport import LIMIT, load_readings, summarise

# Has to run before the first Tk() -- see display.py for why.
use_bundled_tcl()


class SensorWindow:
    """The window. A class, because the widgets and the state have to outlive
    a function call: a callback fired ten seconds from now needs to find the
    listbox, and a local variable is gone by then.
    """

    def __init__(self, root: tkinter.Tk) -> None:
        self.root = root
        root.title("Sensor readings")

        # A StringVar is not a str. It is a handle on a value that Tcl also holds, so
        # a widget bound to it redraws when the value changes -- without anybody
        # calling a redraw. Module 22's session_state, one layer lower down.
        self.location = tkinter.StringVar(value=locations()[0])
        self.limit = tkinter.StringVar(value=f"{LIMIT:.1f}")
        self.status = tkinter.StringVar(value="")

        top = ttk.Frame(root, padding=8)
        top.pack(fill="x")

        ttk.Label(top, text="location").pack(side="left")
        chooser = ttk.Combobox(
            top, textvariable=self.location, values=locations(), state="readonly", width=12
        )
        chooser.pack(side="left", padx=(4, 12))

        ttk.Label(top, text="limit").pack(side="left")
        ttk.Entry(top, textvariable=self.limit, width=8).pack(side="left", padx=4)

        # `command=self.refresh` passes the function, it does not call it. A pair of
        # parentheses here would call refresh once, now, and hand the button its
        # return value -- module 14's distinction, and the classic tkinter bug.
        ttk.Button(top, text="Refresh", command=self.refresh).pack(side="left", padx=8)

        self.listing = tkinter.Listbox(root, width=44, height=12)
        self.listing.pack(fill="both", expand=True, padx=8)

        ttk.Label(root, textvariable=self.status, padding=8).pack(fill="x")

        self.refresh()

    def current_limit(self) -> float | None:
        """The limit as a number, or None if what was typed is not one.

        Module 23 had FastAPI refuse a bad value before the function ran. There is
        nothing here that does that: an Entry holds text, and text is all it holds.
        Whoever reads it converts it, and whoever converts it handles the failure.
        """
        try:
            return float(self.limit.get())
        except ValueError:
            return None

    def refresh(self) -> None:
        """Redraw the list for the chosen location and limit.

        No arguments and no return value. A callback is called by the event loop,
        which has nothing to pass it and nowhere to put an answer, so everything it
        needs it reads from `self` and everything it produces it writes to a widget.
        """
        limit = self.current_limit()
        if limit is None:
            self.status.set(f"{self.limit.get()!r} is not a number")
            return

        location = self.location.get()
        self.listing.delete(0, "end")
        for line in rows_for(location, limit):
            self.listing.insert("end", line)

        here = [r for r in load_readings() if r.location == location]
        self.status.set(verdict(here, limit))


def main() -> None:
    """Open the window and hand control to Tk."""
    root = tkinter.Tk()
    SensorWindow(root)
    # mainloop() does not return until the window is destroyed. Nothing written after
    # it runs while the program is on screen -- which is why a GUI program is
    # organised as callbacks and not as a sequence of statements.
    root.mainloop()


if __name__ == "__main__":
    for summary in summarise(load_readings()):
        print(summary_line(summary))
    main()

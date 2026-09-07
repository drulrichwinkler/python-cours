"""The Textual application this module builds up to.

Run it:

    uv run python 25_textual/app.py

It takes over the terminal. `q` quits, and so does Ctrl+C -- which module 24's window
could not manage, because here the terminal is still the terminal.

Everything it knows about sensors comes from `sensorreport`, and the formatting comes
from `24_tkinter/logic.py`. Not a copy of it: the same file. Module 24's argument for
keeping the logic out of the callbacks is what makes it reusable by a second
presentation, and this file is the proof.
"""

from __future__ import annotations

import sys
from pathlib import Path

# 24_tkinter is not a package -- the number makes it an invalid identifier -- so its
# logic module is reached by path rather than by import name. append, not insert: the
# installed course packages keep priority.
sys.path.append(str(Path(__file__).resolve().parent.parent / "24_tkinter"))

from logic import locations, verdict  # noqa: E402
from textual.app import App, ComposeResult  # noqa: E402
from textual.containers import Horizontal  # noqa: E402
from textual.reactive import reactive  # noqa: E402
from textual.widgets import Button, DataTable, Input, Label, Static  # noqa: E402

from sensorreport import LIMIT, load_readings  # noqa: E402


class SensorApp(App[None]):
    """One location's readings in a table, against a limit you can type."""

    CSS_PATH = "app.tcss"

    # A binding is a key, a method name and the text shown in the footer. There is no
    # `bind()` call anywhere: the class attribute *is* the registration.
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("n", "next_location", "Next location"),
    ]

    # A reactive attribute is an ordinary attribute with a hook. Assign to it and
    # Textual calls `watch_<name>` -- so the redraw is a consequence of the
    # assignment rather than something the assigning code has to remember. Module
    # 24's StringVar did the same job through a trace; this needs no wrapper object,
    # and `self.limit` is a float rather than a string.
    # `init=False` matters. Without it Textual calls the watcher once during
    # initialisation -- measured: the watcher runs once at construction, before
    # anything is on screen -- and `redraw` would then look for a table that `compose` has not
    # yielded yet. The startup redraw happens in `on_mount` instead, which is the
    # first moment the widgets exist.
    limit: reactive[float] = reactive(LIMIT, init=False)
    location: reactive[str] = reactive(locations()[0], init=False)

    def compose(self) -> ComposeResult:
        """The widgets, yielded.

        This is a **generator function** -- module 13. It does not build the
        interface; it describes it, and Textual consumes what it yields. Which is why
        the layout can live in `app.tcss`: nothing here says where anything goes.
        """
        yield Static("Sensor readings", id="title")
        with Horizontal(id="controls"):
            yield Label("location")
            yield Button(self.location, id="location")
            yield Label("limit")
            yield Input(value=f"{LIMIT:.1f}", id="limit")
        yield DataTable(id="table")
        yield Static("", id="status")

    def on_mount(self) -> None:
        """Called once, after the widgets exist and before anything is shown."""
        table = self.query_one(DataTable)
        table.add_columns("tag", "value", "unit", "at")
        table.cursor_type = "row"
        self.redraw()

    # ---- handlers -------------------------------------------------------------
    # A handler is found by **name**. `on_button_pressed` is called for a
    # `Button.Pressed` message, `on_input_submitted` for `Input.Submitted`. Nothing
    # registers them -- module 24 passed `command=self.refresh` explicitly, and
    # module 21's Flask used a decorator. This is a third answer: a convention.

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """The button and the `n` key do the same thing."""
        self.action_next_location()

    def action_next_location(self) -> None:
        """Cycle to the next location.

        Named `action_next_location` because the binding above says
        `"next_location"`. Textual looks the method up by that name -- the same
        convention as the `on_*` handlers, applied to keys.
        """
        places = locations()
        self.location = places[(places.index(self.location) + 1) % len(places)]
        self.query_one("#location", Button).label = self.location

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Enter in the limit box. An Input holds text, exactly as an Entry did."""
        try:
            self.limit = float(event.value)
        except ValueError:
            self.query_one("#status", Static).update(f"{event.value!r} is not a number")

    # ---- reactions ------------------------------------------------------------

    def watch_limit(self) -> None:
        """Called by Textual whenever `self.limit` is assigned to."""
        self.redraw()

    def watch_location(self) -> None:
        """The same, for the location."""
        self.redraw()

    def redraw(self) -> None:
        """Fill the table and the status line for the current location and limit."""
        here = [r for r in load_readings() if r.location == self.location]
        here.sort(key=lambda r: (r.value is None, -(r.value or 0.0)))

        table = self.query_one(DataTable)
        table.clear()
        for reading in here:
            value = "--" if reading.value is None else f"{reading.value:.1f}"
            table.add_row(reading.tag, value, reading.unit, reading.at)

        self.query_one("#status", Static).update(verdict(here, self.limit))


if __name__ == "__main__":
    SensorApp().run()

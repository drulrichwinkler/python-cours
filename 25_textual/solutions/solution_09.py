"""Solution 09 -- One app, everything at once."""

import asyncio
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from textual.app import App, ComposeResult  # noqa: E402
from textual.reactive import reactive  # noqa: E402
from textual.widgets import DataTable, Static  # noqa: E402

from sensorreport import load_readings  # noqa: E402


class FaultApp(App[None]):
    """The faults of one location, against a limit a key can move."""

    BINDINGS = [
        ("f", "worse", "Raise the limit"),
        ("q", "quit", "Quit"),
    ]

    # init=False, or Textual calls watch_limit once during initialisation -- before
    # compose has yielded the table that redraw goes looking for.
    limit: reactive[float] = reactive(85.0, init=False)

    def compose(self) -> ComposeResult:
        """Describes the interface. A generator function -- module 13."""
        yield Static("Faults", id="title")
        yield DataTable(id="table")
        yield Static("", id="status")

    def on_mount(self) -> None:
        """The first moment the widgets exist."""
        table = self.query_one(DataTable)
        table.add_columns("tag", "value")
        self.redraw()

    def action_worse(self) -> None:
        """`f`. Named for the `"worse"` in BINDINGS -- Textual looks it up by name."""
        self.limit += 2.0

    def watch_limit(self) -> None:
        """Called by Textual after `self.limit` is assigned to. No line here calls it."""
        self.redraw()

    def redraw(self) -> None:
        """Fill the table and the status line for the current limit."""
        above = [
            r
            for r in load_readings()
            if r.location == "Test rig" and r.value is not None and r.value > self.limit
        ]
        above.sort(key=lambda r: r.value or 0.0, reverse=True)

        table = self.query_one(DataTable)
        # clear() drops the rows and keeps the columns, which were added in on_mount.
        table.clear()
        for reading in above:
            table.add_row(reading.tag, f"{reading.value:.1f}")

        self.query_one("#status", Static).update(f"{len(above)} above {self.limit:.1f}")


async def main() -> None:
    app = FaultApp()
    async with app.run_test() as pilot:
        await pilot.pause()
        table = app.query_one(DataTable)

        def status() -> str:
            return str(app.query_one("#status", Static).render())

        print("rows at 85.0:", table.row_count)
        print("status:", status())
        print("first row:", table.get_row_at(0))

        await pilot.press("f")
        await pilot.press("f")
        await pilot.pause()
        print("after two presses of f:", app.limit)
        print("rows at 89.0:", table.row_count)
        print("status:", status())


asyncio.run(main())

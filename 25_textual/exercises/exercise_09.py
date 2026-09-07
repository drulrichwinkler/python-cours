"""Exercise 09 -- One app, everything at once.

Write the app. `FaultApp` shows the faults of one location, with a limit you can
change and a key that cycles the location.

  * `BINDINGS` must map `f` to an action called `worse` and `q` to `quit`.
  * `limit` is a reactive float starting at `85.0`, declared with `init=False`.
  * `compose` yields, in this order: a `Static` with id `title` and the text
    `Faults`, a `DataTable` with id `table`, and a `Static` with id `status`.
  * `on_mount` adds the columns `tag` and `value` and then calls `self.redraw()`.
  * `watch_limit` calls `self.redraw()`.
  * `action_worse` adds 2.0 to `self.limit`.
  * `redraw` fills the table with the readings of `Test rig` above `self.limit`,
    worst first, as `tag` and the value to one decimal place, and puts
    `<n> above <limit to one decimal>` in the status line.

The prints at the bottom are written for you -- do not change them.

Expected output:

    rows at 85.0: 3
    status: 3 above 85.0
    first row: ['TH-04', '93.5']
    after two presses of f: 89.0
    rows at 89.0: 2
    status: 2 above 89.0

The last three lines are why `f` is a binding rather than a button: two presses of a
key are two presses, and two clicks in quick succession are one double-click
(exercise 05).

Hint: `reactive(85.0, init=False)` as a class attribute; `BINDINGS` is a list of
`(key, action_name, description)` tuples, and the action for `"worse"` has to be
called `action_worse`. `table.clear()` empties the rows and keeps the columns.
"""

import asyncio
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from textual.app import App, ComposeResult  # noqa: E402
from textual.reactive import reactive  # noqa: E402
from textual.widgets import DataTable, Static  # noqa: E402

from sensorreport import load_readings  # noqa: E402

# TODO: the class FaultApp


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

"""Exercise 01 -- The app, read without a terminal.

`app.py` next to this file takes over a terminal when you run it. `App.run_test()`
runs it with no terminal at all: the screen is a grid of characters in memory, and
`Pilot` is the object that pretends to be a user.

Print four lines about the app as it stands at startup:

  1. `location: <the location it starts on>`
  2. `rows: <how many rows the table has>`
  3. `columns: <the column labels, as a list>`
  4. `status: <what the status line says>`

Expected output:

    location: Hall
    rows: 20
    columns: ['tag', 'value', 'unit', 'at']
    status: 18 readings, none above 85.0

Line 2 says 20 and line 4 says 18. Hall has twenty rows in the file and two of them
have no value -- the table shows all twenty, with `--` where the value is missing,
and the verdict counts only the usable ones.

**About `async` and `await`.** `run_test()` is an asynchronous context manager, so the
code that uses it lives in an `async def` and is started with `asyncio.run(...)`. You
do not need asyncio to do this module. Read `await x` as "call x, and let the event
loop have a turn while it works" -- the same event loop idea as module 24, except that
this one is asyncio's rather than Tk's C code. `await pilot.pause()` is how you say
"let everything that is pending happen before I look".

Hint: `app.query_one(DataTable)` finds the table by type, and
`app.query_one("#status", Static)` by CSS id -- `#status` is the id given in `app.py`.
A `Static`'s text comes out of `str(widget.render())`. The column labels are
`[str(c.label) for c in table.columns.values()]`.
"""

import asyncio
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from app import SensorApp  # noqa: E402
from textual.widgets import DataTable, Static  # noqa: E402


async def main() -> None:
    """Everything that touches the app has to happen inside the context manager."""
    app = SensorApp()
    async with app.run_test() as pilot:
        await pilot.pause()
        # TODO: four prints


asyncio.run(main())

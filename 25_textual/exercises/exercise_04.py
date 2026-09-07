"""Exercise 04 -- A reactive attribute, and the watcher that fires on its own.

`limit` in `app.py` is declared `reactive(LIMIT, init=False)`. Assigning to it is an
ordinary assignment -- `app.limit = 90.0`, and `app.limit` is a float, not a wrapper
object. What is not ordinary is that Textual calls `watch_limit` afterwards, so the
redraw is a *consequence* of the assignment rather than something the assigning code
has to remember.

Print five lines:

  1. `type: <the type of app.limit>` -- inside the running app
  2. `status at 85: <the status line>`
  3. after `app.limit = 90.0`, `status at 90: <the status line>`
  4. after `app.limit = 20.0`, `status at 20: <the status line>`
  5. `watcher calls: <how many times watch_limit ran>`

Expected output:

    type: float
    status at 85: 18 readings, none above 85.0
    status at 90: 18 readings, none above 90.0
    status at 20: 18 of 18 readings above 20.0
    watcher calls: 2

Line 5 says 2 for two assignments. That is what `init=False` in `app.py` buys: without
it Textual calls the watcher once during initialisation as well, before `compose` has
yielded anything -- and `redraw` would then look for a table that does not exist yet.

Hint: count the calls by wrapping the existing watcher. `original = app.watch_limit`,
then assign a function to `app.watch_limit` that appends to a list and calls
`original()`. That is module 14's idea without the decorator syntax. Remember
`await pilot.pause()` after each assignment, so the watcher has run before you look.
"""

import asyncio
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from app import SensorApp  # noqa: E402
from textual.widgets import Static  # noqa: E402


async def main() -> None:
    app = SensorApp()
    calls: list[int] = []
    async with app.run_test() as pilot:
        await pilot.pause()
        # TODO: count the watcher's calls, then the five prints


asyncio.run(main())

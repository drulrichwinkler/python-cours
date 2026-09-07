"""Exercise 02 -- compose is a generator function.

`compose` in `app.py` does not build the interface. It **describes** it: it yields
widgets, and Textual consumes what comes out. That makes it a generator function --
module 13, in a place you would not have looked for one.

Print four lines:

  1. `compose is a generator function: <True or False>`, using `inspect`
  2. what calling `SensorApp().compose()` returns, as `calling it returns: <the type>`
  3. the widget types the app actually mounted, as a list, in tree order
  4. the handler name Textual will look for when a button is pressed

Expected output:

    compose is a generator function: True
    calling it returns: generator
    mounted: ['Static', 'Horizontal', 'Label', 'Button', 'Label', 'Input', 'DataTable', 'Static']
    a Button.Pressed goes to: on_button_pressed

Line 2 is module 13's point exactly: calling a generator function runs none of its
body. `compose()` on its own produces no widgets at all, which is why nothing goes
wrong when you call it outside a running app.

Line 4 is not a guess. `Button.Pressed.handler_name` is an attribute -- every message
class knows the method name it will be delivered to, which is the first thing to check
when a handler is not being called.

Hint: `inspect.isgeneratorfunction`, and `type(...).__name__` for line 2. For line 3,
`app.query("*")` inside `run_test()` gives every mounted widget in tree order.
"""

import asyncio
import inspect
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from app import SensorApp  # noqa: E402
from textual.widgets import Button  # noqa: E402

# TODO: lines 1 and 2, which need no running app


async def main() -> None:
    app = SensorApp()
    async with app.run_test() as pilot:
        await pilot.pause()
        # TODO: lines 3 and 4


asyncio.run(main())

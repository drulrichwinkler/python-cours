"""Solution 02 -- compose is a generator function."""

import asyncio
import inspect
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from app import SensorApp  # noqa: E402
from textual.widgets import Button  # noqa: E402

print("compose is a generator function:", inspect.isgeneratorfunction(SensorApp.compose))

# Calling it runs nothing. The body does not start until something iterates it, and
# Textual is what iterates it -- module 13, with a framework as the consumer.
print("calling it returns:", type(SensorApp().compose()).__name__)


async def main() -> None:
    app = SensorApp()
    async with app.run_test() as pilot:
        await pilot.pause()
        print("mounted:", [type(widget).__name__ for widget in app.query("*")])
        # Every message class knows where it is delivered. This is the attribute to
        # check when a handler is silently not firing.
        print("a Button.Pressed goes to:", Button.Pressed.handler_name)


asyncio.run(main())

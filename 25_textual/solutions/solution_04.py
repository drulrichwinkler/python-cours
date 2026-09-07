"""Solution 04 -- A reactive attribute, and the watcher that fires on its own."""

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

        def status() -> str:
            return str(app.query_one("#status", Static).render())

        # Wrap the watcher on the instance. `original` is the bound method, so
        # calling it still updates the app -- this only counts.
        original = app.watch_limit

        def counted() -> None:
            calls.append(1)
            original()

        app.watch_limit = counted  # type: ignore[method-assign]

        print("type:", type(app.limit).__name__)
        print("status at 85:", status())

        app.limit = 90.0
        await pilot.pause()
        print("status at 90:", status())

        app.limit = 20.0
        await pilot.pause()
        print("status at 20:", status())

        print("watcher calls:", len(calls))


asyncio.run(main())

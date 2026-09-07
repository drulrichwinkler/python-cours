"""Solution 01 -- The app, read without a terminal."""

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

        print("location:", app.location)

        table = app.query_one(DataTable)
        print("rows:", table.row_count)
        # `columns` is a mapping of key to Column, and a Column's label is a Rich
        # object rather than a str -- hence the str() around it.
        print("columns:", [str(column.label) for column in table.columns.values()])

        # `str(widget.render())` and not `.renderable`, which does not exist on a
        # Static in this version of textual.
        print("status:", str(app.query_one("#status", Static).render()))


asyncio.run(main())

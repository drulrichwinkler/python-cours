"""Solution 06 -- The exception, and what the exit code says this time."""

import asyncio
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from textual.app import App, ComposeResult  # noqa: E402
from textual.widgets import Button, Static  # noqa: E402


class Boom(App[None]):
    """One button, and it is broken."""

    def compose(self) -> ComposeResult:
        yield Static("start", id="row")
        yield Button("boom", id="boom")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """The bug."""
        raise ValueError("the handler is broken")


async def main() -> None:
    app = Boom()
    progress: list[str] = []
    raised = False
    still_running = None

    try:
        async with app.run_test() as pilot:
            await pilot.pause()
            await pilot.click("#boom")
            await pilot.pause()
            progress.append("reached the click")
            # The app has already stopped by now: Textual took the interface down
            # rather than carrying on with a handler it cannot trust.
            still_running = app.is_running
    except Exception:
        # The exception surfaces on the way *out* of the context manager, not at the
        # click -- which is why the click above did not need a try of its own.
        raised = True

    print("app still running:", still_running)
    print("run_test re-raised:", raised)
    print("output before it:", *progress)


asyncio.run(main())

"""Solution 03 -- Repair: the handler nobody calls."""

import asyncio
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from textual.app import App, ComposeResult  # noqa: E402
from textual.widgets import Button, Static  # noqa: E402


class Small(App[None]):
    """One button and one line of text."""

    def compose(self) -> ComposeResult:
        yield Static("start", id="row")
        yield Button("go", id="go")

    # `on_button_pressed`, past tense -- the message is `Button.Pressed`, and the
    # handler name is the message's class path in snake_case. Nothing enforces it and
    # nothing warns: a method with any other name is simply never looked up.
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """What the button is supposed to do."""
        self.query_one("#row", Static).update("handler ran")


async def main() -> None:
    app = Small()
    async with app.run_test() as pilot:
        await pilot.pause()
        print("before:", str(app.query_one("#row", Static).render()))
        await pilot.click("#go")
        await pilot.pause()
        print("after:", str(app.query_one("#row", Static).render()))


asyncio.run(main())

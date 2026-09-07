"""Exercise 03 -- Repair: the handler nobody calls.

Textual finds a handler by **name**. Nothing registers it: there is no `command=` as
in module 24 and no decorator as in module 21. The method is called because it is
called `on_button_pressed`, and a method called anything else is a method Textual
never looks for.

The app below has exactly that bug. Fix it so both prints show the handler's work.

Expected output:

    before: start
    after: handler ran

Compare this with module 24's `command=self.bump()`. Both are silent: no exception, no
warning, a button that looks right and does nothing. The difference is where you look
for the truth -- there it was `wrong.cget("command")` returning an empty string; here
it is `Button.Pressed.handler_name`, which tells you the name Textual will look for.

Hint: print `Button.Pressed.handler_name` if you want it confirmed rather than
guessed.
"""

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

    # TODO: Textual never calls this. What is it supposed to be called?
    def on_button_press(self, event: Button.Pressed) -> None:
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

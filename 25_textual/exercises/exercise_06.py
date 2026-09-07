"""Exercise 06 -- The exception, and what the exit code says this time.

Module 24 measured this: a callback that raises in tkinter prints a traceback to
stderr, the loop carries on, and the process exits with **0**. A GUI whose every
button raises is a program that reports success.

Textual answers the same question differently, and this exercise is the measurement
side by side. Run the app below, whose handler raises, and print three lines:

  1. `app still running: <True or False>`, checked after the click
  2. `run_test re-raised: <True or False>` -- whether leaving the context manager
     let the exception through
  3. `output before it: <what this script printed before that point>`

Expected output:

    app still running: False
    run_test re-raised: True
    output before it: reached the click

Then run the file yourself and look at the exit code:

    uv run python 25_textual/solutions/solution_06.py > /dev/null; echo $?

It is **1**, and the traceback names the real frame -- `on_button_pressed`, in your
file, at the line that raised. That is the opposite of module 24 on every count, from
one identical bug.

Neither choice is wrong. Tk keeps a window alive that a person has typed into, and
Textual refuses to keep running an interface it can no longer trust. What matters is
knowing which one you are working in, because it decides whether your CI can tell you
anything at all.

Hint: `app.is_running` for line 1. For lines 2 and 3, put the `async with` in a `try`
and record whether the `except` ran -- the exception surfaces when the context manager
is *left*, not at the click.
"""

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
    # TODO: run it, click, and the three prints


asyncio.run(main())

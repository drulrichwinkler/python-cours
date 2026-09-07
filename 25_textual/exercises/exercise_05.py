"""Exercise 05 -- Simulated input, and where it is not naive.

Module 24 could not test a click. The same simulated keypress gave a different answer
there depending on whether the window was visible, off-screen or withdrawn, because
the window manager decides who has focus.

There is no window manager here. The screen is a grid of characters that Textual owns
entirely, so `Pilot` can deliver an event and know it arrived. That does not make it
naive, and this exercise measures where it is not.

`app.py` cycles the location on the `n` key and on the button, through the same
method. Print four lines:

  1. `by key: <the five locations, as a list>`
  2. `key run is stable: <True or False>` -- whether a second run by key gives the
     same list
  3. `clicks with no delay that registered: <how many of five changed anything>`
  4. `clicks 0.3 s apart that registered: <the same count, spaced out>`

Expected output:

    by key: ['Office', 'Test rig', 'Hall', 'Office', 'Test rig']
    key run is stable: True
    clicks with no delay that registered: 3
    clicks 0.3 s apart that registered: 5

Line 3 is not a flaw in Textual or in `Pilot`. Two clicks in quick succession on one
widget are a **double-click** -- one `Button.Pressed`, not two, which is what a real
user's double-click does. Line 4 is the same five clicks with room between them.

Note what is *not* asked for: the list of locations from the unspaced clicks. Measured
over five runs it came out three different ways, because which pairs get folded
depends on where the wall clock falls relative to the double-click window. The
**count** was 3 every time. An expected output containing that list would be a test
about the machine's timing -- module 22's flaky test, again.

So: **press keys, or space your clicks, and never assert on a sequence whose order a
clock decides.** The contrast with module 24 is worth holding on to. There the answer
changed with the environment and could not be relied on at all; here it is
understood, and a reliable measurement is available.

Hint: `drive` and `moves` below are written for you. `drive("key")`, `drive("click")`
and `drive("click", gap=0.3)` are the runs you need, plus one more by key for line 2.
"""

import asyncio
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from app import SensorApp  # noqa: E402


async def drive(how: str, gap: float = 0.0) -> list[str]:
    """Run the app, do the given thing five times, report the location each time."""
    app = SensorApp()
    seen: list[str] = []
    async with app.run_test() as pilot:
        await pilot.pause()
        for _ in range(5):
            if how == "key":
                await pilot.press("n")
            else:
                await pilot.click("#location")
            await pilot.pause()
            if gap:
                await asyncio.sleep(gap)
            seen.append(app.location)
    return seen


def moves(seen: list[str]) -> int:
    """How many of the five actions actually changed the location."""
    before = ["Hall", *seen[:-1]]
    return sum(1 for was, now in zip(before, seen) if was != now)


async def main() -> None:
    # TODO: four prints
    ...


asyncio.run(main())

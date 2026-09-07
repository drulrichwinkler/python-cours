"""Solution 05 -- Simulated input, and where it is not naive."""

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
    by_key = await drive("key")
    print("by key:", by_key)

    # A second run of the same thing. If this were environment-dependent the way
    # module 24's event_generate was, the two lists would differ.
    print("key run is stable:", await drive("key") == by_key)

    # Every second click was folded into a double-click -- one Button.Pressed rather
    # than two. The count is stable across runs; the order in which the pairs fall is
    # not, which is why only the count is printed.
    print("clicks with no delay that registered:", moves(await drive("click")))
    print("clicks 0.3 s apart that registered:", moves(await drive("click", gap=0.3)))


asyncio.run(main())

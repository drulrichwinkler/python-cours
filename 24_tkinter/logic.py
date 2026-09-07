"""Everything module 24's window does that is not a window.

This file exists because of a fact you will meet in the README: **there is no test
client for tkinter.** Modules 21, 22 and 23 each had one -- `test_client()`,
`AppTest`, `TestClient` -- and each ran the whole application in-process. tkinter has
no equivalent, because the thing that would have to be faked is the window manager.

So the answer here is architectural rather than technical: put nothing in a callback
that you cannot also call on its own. Every function below is ordinary Python, takes
ordinary arguments and returns ordinary values. `app.py` calls them from callbacks;
the tests call them directly, and pass on a machine with no screen at all.

That split is the transferable part of this module. It is worth more than any widget.
"""

from __future__ import annotations

from sensorreport import Reading, Summary, load_readings, summarise


def label_for(reading: Reading, limit: float) -> str:
    """One line for a list of readings.

    A value that could not be read prints as `--`, not as `None` and not as `0.0`:
    the file had a cell there and it was unusable, which is a third case and has to
    look like one.
    """
    if reading.value is None:
        return f"{reading.tag}  --"
    marker = "  FAULT" if reading.value > limit else ""
    return f"{reading.tag}  {reading.value:.1f} {reading.unit}{marker}"


def verdict(readings: list[Reading], limit: float) -> str:
    """The one sentence a window puts under the list."""
    usable = [r for r in readings if r.value is not None]
    if not usable:
        return "no usable readings"
    above = [r for r in usable if r.value is not None and r.value > limit]
    if not above:
        return f"{len(usable)} readings, none above {limit:.1f}"
    return f"{len(above)} of {len(usable)} readings above {limit:.1f}"


def rows_for(location: str, limit: float) -> list[str]:
    """The lines a location's list should contain, worst reading first."""
    here = [r for r in load_readings() if r.location == location]
    here.sort(key=lambda r: (r.value is None, -(r.value or 0.0)))
    return [label_for(r, limit) for r in here]


def locations() -> list[str]:
    """The locations in the data, in the order a dropdown should offer them."""
    return [summary.location for summary in summarise(load_readings())]


def summary_line(summary: Summary) -> str:
    """One location's numbers, on one line."""
    mean = "--" if summary.mean is None else f"{summary.mean:.2f}"
    highest = "--" if summary.highest is None else f"{summary.highest:.1f}"
    return (
        f"{summary.location:10} {summary.usable:>3}/{summary.readings:<3} "
        f"mean {mean:>6}  max {highest:>6}  faults {summary.faults}"
    )

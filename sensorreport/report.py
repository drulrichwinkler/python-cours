"""Reading the sensor log and summarising it.

Nothing in here knows about HTTP, windows or terminals. That is the point: the
five modules of Part 5 differ only in how they present what this returns.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

LIMIT = 85.0
"""Above this, a reading is a fault."""

DATA = Path(__file__).resolve().parent / "data" / "readings.csv"


@dataclass(frozen=True, slots=True)
class Reading:
    """One measurement. Frozen, because a reading that has happened cannot change."""

    tag: str
    value: float | None  # None where the cell could not be read
    unit: str
    location: str
    at: str

    @property
    def is_fault(self) -> bool:
        return self.value is not None and self.value > LIMIT


@dataclass(frozen=True, slots=True)
class Summary:
    """What one location's readings add up to."""

    location: str
    readings: int  # rows
    usable: int  # rows with a value
    mean: float | None
    highest: float | None
    faults: int


def load_readings(path: Path | str = DATA) -> list[Reading]:
    """Every row of the log, with unreadable values as None rather than a string."""
    out: list[Reading] = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter=";"):
            try:
                value: float | None = float(row["value"])
            except ValueError:
                value = None
            out.append(
                Reading(
                    tag=row["tag"],
                    value=value,
                    unit=row["unit"],
                    location=row["location"],
                    at=row["at"],
                )
            )
    return out


def summarise(readings: list[Reading]) -> list[Summary]:
    """One Summary per location, sorted by location name."""
    by_location: dict[str, list[Reading]] = {}
    for reading in readings:
        by_location.setdefault(reading.location, []).append(reading)

    out: list[Summary] = []
    for location in sorted(by_location):
        rows = by_location[location]
        values = [r.value for r in rows if r.value is not None]
        out.append(
            Summary(
                location=location,
                readings=len(rows),
                usable=len(values),
                mean=round(sum(values) / len(values), 2) if values else None,
                highest=max(values) if values else None,
                faults=sum(1 for r in rows if r.is_fault),
            )
        )
    return out


def faults(readings: list[Reading]) -> list[Reading]:
    """The readings above the limit, worst first."""
    return sorted(
        (r for r in readings if r.is_fault),
        key=lambda r: r.value or 0.0,
        reverse=True,
    )

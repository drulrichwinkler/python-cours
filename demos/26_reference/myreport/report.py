"""Reference implementation of module 26's contract. Author material."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Reading:
    tag: str
    value: float | None
    location: str
    limit: float
    at: str

    @property
    def is_fault(self) -> bool:
        return self.value is not None and self.value > self.limit


@dataclass(frozen=True, slots=True)
class Summary:
    location: str
    readings: int
    usable: int
    mean: float | None
    highest: float | None
    faults: int


def _sensors(data_dir: Path) -> dict[str, dict[str, object]]:
    with (data_dir / "data" / "sensors.json").open(encoding="utf-8") as fh:
        # json.load is typed as returning Any, and mypy --strict objects to handing
        # an Any straight back out of an annotated function. The cast is the honest
        # form: nothing checked this at run time, and saying so is the point.
        loaded: dict[str, dict[str, object]] = json.load(fh)
    return loaded


def _rows(data_dir: Path) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    a = data_dir / "data" / "readings_a.csv"
    with a.open(encoding="latin-1", newline="") as fh:
        out.extend(dict(row) for row in csv.DictReader(fh, delimiter=";"))
    b = data_dir / "data" / "readings_b.csv"
    with b.open(encoding="utf-8", newline="") as fh:
        out.extend(dict(row) for row in csv.DictReader(fh, delimiter="\t"))
    return out


def _celsius(raw: str, unit: str) -> float | None:
    text = raw.strip().replace(",", ".")
    try:
        value = float(text)
    except ValueError:
        return None
    if unit.strip().endswith("F"):
        value = (value - 32.0) * 5.0 / 9.0
    return round(value, 2)


def load(data_dir: Path | str) -> list[Reading]:
    data_dir = Path(data_dir)
    sensors = _sensors(data_dir)
    seen: set[tuple[str, str, str]] = set()
    readings: list[Reading] = []
    for row in _rows(data_dir):
        key = (row["tag"], row["at"], row["value"])
        if key in seen:
            continue
        seen.add(key)
        sensor = sensors.get(row["tag"])
        if sensor is None:
            continue
        readings.append(
            Reading(
                tag=row["tag"],
                value=_celsius(row["value"], row["unit"]),
                location=str(sensor["location"]),
                limit=float(str(sensor["limit"])),
                at=row["at"],
            )
        )
    return readings


def summarise(readings: list[Reading]) -> list[Summary]:
    places = sorted({r.location for r in readings})
    out: list[Summary] = []
    for place in places:
        here = [r for r in readings if r.location == place]
        usable = [r.value for r in here if r.value is not None]
        out.append(
            Summary(
                location=place,
                readings=len(here),
                usable=len(usable),
                mean=round(sum(usable) / len(usable), 2) if usable else None,
                highest=max(usable) if usable else None,
                faults=sum(1 for r in here if r.is_fault),
            )
        )
    return out


def faults(readings: list[Reading]) -> list[Reading]:
    bad = [r for r in readings if r.is_fault]
    bad.sort(key=lambda r: r.value or 0.0, reverse=True)
    return bad


def unknown_tags(data_dir: Path | str) -> list[str]:
    data_dir = Path(data_dir)
    sensors = _sensors(data_dir)
    return sorted({row["tag"] for row in _rows(data_dir) if row["tag"] not in sensors})


def silent_sensors(data_dir: Path | str) -> list[str]:
    data_dir = Path(data_dir)
    with_readings = {row["tag"] for row in _rows(data_dir)}
    return sorted(tag for tag in _sensors(data_dir) if tag not in with_readings)

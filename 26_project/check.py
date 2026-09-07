"""The acceptance criteria for module 26, as a program you run.

    uv run 26_project/check.py

There is no `pytest` for this module and no `your_turn` marker. This file is the
feedback channel: it imports your package, puts the data in `data/` through it, and
prints a line per criterion. Nothing is recorded and nothing is graded.

It checks what a program can check. What it cannot check it lists at the end instead
of pretending, and that list is not shorter or less important than the other one.

An optional argument says where to look for the package -- `uv run
26_project/check.py somewhere/else`. The default is the folder this file is in.
"""

from __future__ import annotations

import importlib
import os
import re
import subprocess
import sys
from dataclasses import fields, is_dataclass
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

ANSI = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")

results: list[tuple[bool, str, str]] = []


def check(name: str, condition: object, detail: str = "") -> None:
    """Record one criterion. `condition` is truthy for a pass."""
    results.append((bool(condition), name, detail))


def approx(value: object, wanted: float, tolerance: float = 0.005) -> bool:
    """Floats do not compare exactly -- module 02. Two decimal places is the contract."""
    return isinstance(value, (int, float)) and abs(float(value) - wanted) <= tolerance


def one(readings: list[Any], tag: str, at: str) -> Any:
    """The single reading with this tag and timestamp, or None."""
    found = [r for r in readings if r.tag == tag and r.at == at]
    return found[0] if len(found) == 1 else None


def tool(*command: str) -> tuple[bool, str]:
    """Run one of the toolchain's commands and report whether it was happy.

    NO_COLOR keeps the ANSI escapes out of the line printed below -- these tools
    colour their output when they think something is watching, and a subprocess pipe
    counts as watching often enough to be annoying.
    """
    env = dict(os.environ, NO_COLOR="1", TERM="dumb")
    done = subprocess.run(command, capture_output=True, text=True, cwd=ROOT, check=False, env=env)
    tail = (done.stdout + done.stderr).strip().splitlines()
    last = tail[-1] if tail else ""
    return done.returncode == 0, ANSI.sub("", last)


def main() -> int:
    package_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE
    sys.path.insert(0, str(package_dir))

    try:
        myreport = importlib.import_module("myreport")
    except ImportError as exc:
        print(f"No package to check yet: {exc}")
        print(f"\nExpected an importable `myreport` under {package_dir}.")
        print("Criterion 1 of the brief. Everything else waits on it.")
        return 1

    check("1  `myreport` imports", True)

    # ---- the shapes -------------------------------------------------------
    reading_cls = getattr(myreport, "Reading", None)
    summary_cls = getattr(myreport, "Summary", None)
    check("2  `Reading` is a dataclass", is_dataclass(reading_cls) if reading_cls else False)
    check("3  `Summary` is a dataclass", is_dataclass(summary_cls) if summary_cls else False)

    if is_dataclass(reading_cls):
        names = {f.name for f in fields(reading_cls)}
        missing = {"tag", "value", "location", "limit", "at"} - names
        check("4  `Reading` has the five named fields", not missing, f"missing {sorted(missing)}")
    else:
        check("4  `Reading` has the five named fields", False)

    if is_dataclass(summary_cls):
        names = {f.name for f in fields(summary_cls)}
        missing = {"location", "readings", "usable", "mean", "highest", "faults"} - names
        check("5  `Summary` has the six named fields", not missing, f"missing {sorted(missing)}")
    else:
        check("5  `Summary` has the six named fields", False)

    # ---- reading the data -------------------------------------------------
    readings = myreport.load(HERE)
    check("6  `load` returns 16 readings", len(readings) == 16, f"got {len(readings)}")
    usable = [r for r in readings if r.value is not None]
    check("7  14 of them have a value", len(usable) == 14, f"got {len(usable)}")

    th01 = [r for r in readings if r.tag == "TH-01"]
    check("8  the duplicated row is gone (TH-01 has 2)", len(th01) == 2, f"got {len(th01)}")

    strangers = [r for r in readings if r.tag in {"XX-77", "YY-01"}]
    check("9  readings with an unknown tag are not in the list", not strangers)

    check(
        "10 `unknown_tags` names both of them",
        list(myreport.unknown_tags(HERE)) == ["XX-77", "YY-01"],
        f"got {myreport.unknown_tags(HERE)}",
    )
    check(
        "11 `silent_sensors` finds the sensor with no readings",
        list(myreport.silent_sensors(HERE)) == ["TH-99"],
        f"got {myreport.silent_sensors(HERE)}",
    )

    # ---- the two conversions ---------------------------------------------
    comma = one(readings, "TH-01", "2026-04-01T08:00")
    check("12 `21,4` was read as 21.4", comma is not None and approx(comma.value, 21.4))

    fahrenheit = one(readings, "PR-01", "2026-04-01T08:00")
    check(
        "13 180.5 °F became 82.5 °C",
        fahrenheit is not None and approx(fahrenheit.value, 82.5),
        "" if fahrenheit is None else f"got {fahrenheit.value}",
    )

    office = one(readings, "TH-03", "2026-04-01T08:00")
    check(
        "14 each reading carries its own sensor's limit",
        office is not None and approx(office.limit, 26.0),
    )

    # ---- the limit is per sensor, and `>` is not `>=` ---------------------
    at_limit = one(readings, "PR-02", "2026-04-01T08:00")
    over = one(readings, "PR-02", "2026-04-01T09:00")
    check(
        "15 200.0 at a limit of 200.0 is not a fault, 205.0 is",
        at_limit is not None and over is not None and not at_limit.is_fault and over.is_fault,
    )

    # ---- the analysis -----------------------------------------------------
    bad = list(myreport.faults(readings))
    check("16 there are 7 faults", len(bad) == 7, f"got {len(bad)}")
    check(
        "17 the worst fault comes first",
        bool(bad) and bad[0].tag == "PR-02" and approx(bad[0].value, 205.0),
        "" if not bad else f"got {bad[0].tag} at {bad[0].value}",
    )

    summaries = list(myreport.summarise(readings))
    places = [s.location for s in summaries]
    check(
        "18 `summarise` gives four locations, sorted",
        places == ["Hall", "Kiln", "Office", "Test rig"],
        f"got {places}",
    )

    by_place = {s.location: s for s in summaries}
    hall = by_place.get("Hall")
    check(
        "19 Hall: 5 rows, 3 usable, mean 25.17, highest 31.2, 1 fault",
        hall is not None
        and (hall.readings, hall.usable, hall.faults) == (5, 3, 1)
        and approx(hall.mean, 25.17)
        and approx(hall.highest, 31.2),
        "" if hall is None else f"got {hall}",
    )
    rig = by_place.get("Test rig")
    check(
        "20 Test rig: 7 rows, 7 usable, mean 87.41, highest 93.7, 4 faults",
        rig is not None
        and (rig.readings, rig.usable, rig.faults) == (7, 7, 4)
        and approx(rig.mean, 87.41)
        and approx(rig.highest, 93.7),
        "" if rig is None else f"got {rig}",
    )

    # ---- the toolchain ----------------------------------------------------
    # Three subprocesses -- module 20. Each one is a criterion the brief states and
    # the same command you would run yourself.
    if package_dir == HERE:
        ok, last = tool("uv", "run", "pytest", "-q", "26_project")
        check("21 your own tests pass", ok, last)
        ok, last = tool("uv", "run", "mypy", "26_project")
        check("22 `mypy 26_project` is clean", ok, last)
        ok, last = tool("uv", "run", "ruff", "check", "26_project")
        check("23 `ruff check 26_project` is clean", ok, last)

        presentation = HERE / "present.py"
        frameworks = ("flask", "streamlit", "fastapi", "tkinter", "textual")
        text = presentation.read_text(encoding="utf-8") if presentation.exists() else ""
        named = [name for name in frameworks if name in text]
        check(
            "24 `present.py` uses one of Part 5's five frameworks",
            bool(named),
            f"found {named}" if named else "no present.py, or none of the five named in it",
        )

    # ---- report -----------------------------------------------------------
    width = max(len(name) for _, name, _ in results)
    for passed, name, detail in results:
        mark = "PASS" if passed else "FAIL"
        note = "" if passed or not detail else f"   -- {detail}"
        print(f"  [{mark}] {name:{width}}{note}")

    failed = [name for passed, name, _ in results if not passed]
    print(f"\n{len(results) - len(failed)} of {len(results)} criteria met.")

    print("\nWhat this script cannot check, and you have to:")
    for line in [
        "that `present.py` actually runs, and that a person can read what it shows",
        "that your tests test something -- module 15's suite passed on broken code too",
        "that the names in your code say what the things are",
        "that somebody else could pick it up in six months, starting from your README",
    ]:
        print("  -", line)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

"""Exercise 02 -- Predict what files do.

Replace each `...` with the value you expect, then run the file.

    uv run 08_files/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

import csv
import json
import tempfile
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
SENSORS = DATA / "sensors.csv"

# TODO: the file holds `°C`. One of these two encodings raises; the other does not.
try:
    SENSORS.read_text(encoding="ascii")
    strict = "no error"
except UnicodeDecodeError:
    strict = "UnicodeDecodeError"

loose = SENSORS.read_text(encoding="latin-1").splitlines()[1]

assert strict == ...
assert loose == ...


# TODO: what type does a CSV reader hand back?
with open(SENSORS, newline="", encoding="utf-8") as fh:
    first = next(csv.DictReader(fh, delimiter=";"))

assert type(first["value"]) is ...


# TODO: iterating a file -- is the line ending still there?
with open(SENSORS, encoding="utf-8") as fh:
    line = next(iter(fh))

assert line == ...


# TODO: the JSON round trip is lossy in two places
original = {"tags": ("TH-04", "TH-09"), 3: "an int key"}
back = json.loads(json.dumps(original))

assert type(back["tags"]) is ...
assert sorted(back) == ...


# TODO: and refuses outright in a third
try:
    json.dumps({"seen": {"TH-04"}})
    outcome = "worked"
except Exception as err:
    outcome = type(err).__name__

assert outcome == ...


# TODO: mode "w" truncates when it opens, not when you write
target = Path(tempfile.mkdtemp()) / "x.txt"
target.write_text("abc\n", encoding="utf-8")

with open(target, "w", encoding="utf-8"):
    pass  # opened, nothing written, closed again

assert target.read_text(encoding="utf-8") == ...

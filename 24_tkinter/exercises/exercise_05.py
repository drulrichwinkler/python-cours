"""Exercise 05 -- The part that is not a window.

`logic.py` next to this file holds everything module 24's window does that is not a
window: the formatting and the limit decision. It imports no tkinter, so it runs on a
machine with no screen -- and so does this exercise and its test.

Use `label_for` and `verdict` from `logic` and print five lines:

  1. `label_for` on the highest reading of `Test rig` at limit 85
  2. `label_for` on the same reading at limit 95
  3. `label_for` on a reading whose value could not be read
  4. `verdict` for the Test rig readings at limit 85
  5. `verdict` for the Hall readings at limit 85

Expected output:

    TH-04  93.5 °C  FAULT
    TH-04  93.5 °C
    TH-07  --
    3 of 20 readings above 85.0
    18 readings, none above 85.0

Lines 1 and 2 are the same reading and the same function. Only the limit differs,
which is the point of passing it in rather than reading `LIMIT` inside.

Line 3 shows `--` and not `None` and not `0.0`. The file had a cell there and it was
unusable, and that is a third case that has to look like one.

Line 5 says 18 where the location has 20 rows. Two of them have no value.

Hint: the highest reading of a location is `max(..., key=...)` over the readings that
have a value; the unreadable one is the first with `value is None`. Load everything
with `load_readings()` from `sensorreport`.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from logic import label_for, verdict  # noqa: E402

from sensorreport import load_readings  # noqa: E402

readings = load_readings()

# TODO: five prints

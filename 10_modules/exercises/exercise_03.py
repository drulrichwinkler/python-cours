"""Exercise 03 -- Repair the path.

Run this. It raises `ModuleNotFoundError: No module named 'sensorlib'`, and the
reason is on the line above the import, not on the import.

Work out what is actually on `sys.path` after that line runs, and fix it.

Expected output:

    23.1
    ParseError - not a reading: 'n/a'

Hint: `.parent` goes up one folder. This file is in `10_modules/exercises/`. Where
does `sensorlib/` live? Printing `MODULE` before the import is a fair way to find
out.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent  # TODO: the bug is in this line
sys.path.insert(0, str(MODULE))

from sensorlib.parsing import ParseError, to_reading  # noqa: E402

print(to_reading("23.1"))

try:
    to_reading("n/a")
except ParseError as err:
    print(type(err).__name__, "-", err)

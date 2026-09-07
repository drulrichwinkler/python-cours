"""Exercise 01 -- Connect, query, read by name.

Run `uv run 19_sql/build_db.py` first if you have not.

Print five lines:

  1. the type name of a row from `fetchall()`, and how many sensors there are
  2. the tag and the location of the first sensor, separated by a space
  3. that row's column names, from `.keys()`
  4. the tag and value of every reading above 85, highest first, as a list of tuples

Expected output:

    tuple 5
    TH-01 Hall
    ['tag', 'location', 'installed']
    [('TH-04', 93.5), ('TH-04', 93.2), ('TH-02', 88.4)]

Hint: `contextlib.closing(sqlite3.connect(DB))` -- `with sqlite3.connect(...)` is a
transaction and does not close anything, which section 8 is about. Rows are tuples
until you set `connection.row_factory = sqlite3.Row`, and that has to happen before
you execute. Line 4 needs the results turned back into plain tuples.
"""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

# TODO: open the connection, then four prints

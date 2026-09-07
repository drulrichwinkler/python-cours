"""Exercise 05 -- NULL, and the rows a JOIN drops.

Five lines:

  1. `SELECT NULL = NULL, NULL IS NULL` as a tuple
  2. how many readings have a NULL value, found with `IS NULL`, and how many are
     found with `= NULL` -- separated by a space
  3. inside a transaction, insert a reading for the tag `TH-77`, which has no row in
     `sensors`, then print the total number of readings and how many survive a plain
     `JOIN`, separated by a space
  4. the tags that a `LEFT JOIN` shows as having no sensor, as a list
  5. after rolling back, the number of readings again

Expected output:

    (None, 1)
    3 0
    51 50
    ['TH-77']
    50

Hint: line 1 is why `= NULL` finds nothing -- NULL is not equal to anything,
including itself. For line 4, `LEFT JOIN` keeps every row on the left and fills the
right with NULL, so `WHERE s.tag IS NULL` is the rows with no match. Use `with
connection:` for the transaction and `connection.rollback()` to undo it.
"""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

# TODO: five prints

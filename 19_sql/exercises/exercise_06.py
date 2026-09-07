"""Exercise 06 -- A REAL column that is not real.

Four lines:

  1. insert the string `"kaputt"` into the `value` column -- which is declared REAL --
     and print what came back, together with `typeof(value)`, as a tuple. Then roll
     back.
  2. create a table `strict_demo` with one REAL column and the word STRICT, try the
     same insert, and print the exception's class name
  3. insert 21.7 into it and print the value with its `typeof`
  4. drop the table again

Expected output:

    ('kaputt', 'text')
    IntegrityError
    (21.7, 'real')

Hint: nothing raises in line 1, and that is the exercise -- a declared type in SQLite
is an *affinity*, a preference for conversion, not a constraint. `STRICT` after the
closing bracket of the CREATE turns it into one. Start with `DROP TABLE IF EXISTS`,
or the cell works once and fails the second time.
"""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

# TODO: the four steps

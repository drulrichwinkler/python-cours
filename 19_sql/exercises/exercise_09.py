"""Exercise 09 (bonus) -- Let SQL reduce, let pandas explore.

Two functions:

  - `load(db)` runs a query joining the two tables, keeping only readings whose
    value is not NULL, and returns it as a DataFrame with `at` parsed as timestamps
  - `faults(db, limit)` answers "how many faults per location" **in SQL**, with the
    limit as a placeholder, and returns the rows as they come

Then print five lines.

Expected output:

    (47, 4) float64
    {'Hall': 22.12, 'Office': 22.34, 'Test rig': 32.83}
    [('Test rig', 3)]
    8 17
    TH-04 93.5

Hint: `pd.read_sql_query(query, connection, parse_dates=["at"])` is the handover.
Note the shape: 47 rows and no NaN, because the `WHERE r.value IS NOT NULL` happened
in the database -- that is the whole point of the section. `PRAGMA foreign_keys = ON`
belongs after every connect. The last two lines use `.dt.hour` and `.idxmax()` from
module 18.
"""

import contextlib
import sqlite3
from pathlib import Path

import pandas as pd

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

LIMIT = 85.0

# TODO: the query, the two functions, then five prints

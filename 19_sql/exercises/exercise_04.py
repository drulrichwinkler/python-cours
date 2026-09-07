"""Exercise 04 -- Two tables, joined.

Write one query that joins `readings` to `sensors` and returns, per location: how
many readings there are, how many have a value, the mean rounded to two places, and
the highest. Order by location.

Print one line per location -- location padded to 10, then readings in a field of 3,
usable in 4, mean in 8, highest in 7 -- then a blank line, then the two counts over
the whole table as a tuple.

Expected output:

    Hall       20  18   22.12   23.9
    Office     10   9   22.34   23.1
    Test rig   20  20   32.83   93.5

    (50, 47)

Hint: `JOIN sensors s ON s.tag = r.tag`, then `GROUP BY s.location`. `COUNT(*)`
counts rows and `COUNT(r.value)` skips NULL -- that is the difference between the two
columns, and module 18 called it `len()` against `count()`. Give the aggregates names
with `AS` so you can read them off a `sqlite3.Row`. The last line needs
`tuple(...)`, because a Row's repr says nothing.
"""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

# TODO: the query, the loop, the two counts

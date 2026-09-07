"""Solution 04 -- Two tables, joined."""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

QUERY = """
SELECT   s.location,
         COUNT(*)               AS readings,
         COUNT(r.value)         AS usable,
         ROUND(AVG(r.value), 2) AS mean,
         MAX(r.value)           AS highest
FROM     readings r
JOIN     sensors  s ON s.tag = r.tag
GROUP BY s.location
ORDER BY s.location
"""

with contextlib.closing(sqlite3.connect(DB)) as connection:
    connection.row_factory = sqlite3.Row
    for row in connection.execute(QUERY):
        print(
            f"{row['location']:<10}{row['readings']:>3}{row['usable']:>4}"
            f"{row['mean']:>8}{row['highest']:>7}"
        )

    # COUNT(*) counts rows; COUNT(column) skips NULL. Report both or the summary
    # claims readings it does not have -- module 18's len() against count().
    print()
    counts = connection.execute("SELECT COUNT(*), COUNT(value) FROM readings").fetchone()
    # tuple(...) because row_factory is Row, whose repr says nothing useful.
    print(tuple(counts))

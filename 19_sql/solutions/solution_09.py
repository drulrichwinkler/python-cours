"""Solution 09 (bonus) -- Let SQL reduce, let pandas explore."""

import contextlib
import sqlite3
from pathlib import Path

import pandas as pd

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

LIMIT = 85.0

# The reduction happens in SQL: the NULLs never reach the DataFrame, so there is no
# NaN to explain and 47 rows come back rather than 50.
QUERY = """
SELECT   s.location, r.tag, r.value, r.at
FROM     readings r
JOIN     sensors  s ON s.tag = r.tag
WHERE    r.value IS NOT NULL
"""


def load(db):
    with contextlib.closing(sqlite3.connect(db)) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        return pd.read_sql_query(QUERY, connection, parse_dates=["at"])


def faults(db, limit):
    """The same question in SQL, answered by the database."""
    with contextlib.closing(sqlite3.connect(db)) as connection:
        return connection.execute(
            """
            SELECT   s.location, COUNT(*) AS faults
            FROM     readings r
            JOIN     sensors  s ON s.tag = r.tag
            WHERE    r.value > ?
            GROUP BY s.location
            ORDER BY s.location
            """,
            (limit,),
        ).fetchall()


frame = load(DB)

print(frame.shape, frame["value"].dtype)
print(frame.groupby("location")["value"].mean().round(2).to_dict())
print(faults(DB, LIMIT))
print(frame["at"].dt.hour.min(), frame["at"].dt.hour.max())
worst = frame.loc[frame["value"].idxmax()]
print(worst["tag"], worst["value"])

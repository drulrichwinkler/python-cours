"""Solution 02 -- Predict what SQLite does.

row              is a tuple. Rows arrive positionally until you set
                 connection.row_factory = sqlite3.Row, which has to happen before
                 the execute.
the two counts   are 0 and 50, and this is the module. Through a placeholder the
                 hostile string is a tag that does not exist, so nothing matches.
                 Pasted into the query text it became
                 WHERE tag = 'TH-04' OR '1'='1' -- and '1'='1' is true for every
                 row, so the WHERE clause was rewritten by the data. That is SQL
                 injection, and this is its harmless form: it reads too much.
SELECT ?         gives the string 'value', once per row. A placeholder stands in
                 for a VALUE and never for a column or table name -- where those
                 are dynamic, check them against a list of allowed names yourself.
counts           is (50, 47). COUNT(*) counts rows, COUNT(column) counts rows
                 where that column is not NULL. Module 18's len() against count(),
                 in SQL, with the same consequence for a summary that reports only
                 one of them.
NULL = NULL      is NULL, not 1 -- so it is not true, and `WHERE value = NULL`
                 matches nothing, ever. It found none of the three rows that are
                 NULL. IS NULL is the operator, and pandas said the same about
                 NaN == NaN.
stored           is ('kaputt', 'text'). A column's declared type in SQLite is an
                 AFFINITY -- a preference for how to convert what it can convert,
                 not a constraint. A string that will not convert is stored as
                 text in a column declared REAL. STRICT tables are the remedy.
PRAGMA           is 0: foreign keys are OFF by default, so the REFERENCES clause
                 in the schema is documentation until you write
                 PRAGMA foreign_keys = ON -- once per connection.
(total, joined)  is (51, 50). The orphan row is in the table and a plain JOIN
                 drops it, silently, from a query that succeeded. LEFT JOIN plus
                 WHERE s.tag IS NULL is how you find such rows instead.
"""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

with contextlib.closing(sqlite3.connect(DB)) as connection:
    row = connection.execute("SELECT tag, location FROM sensors LIMIT 1").fetchone()

    assert type(row).__name__ == "tuple"

    hostile = "TH-04' OR '1'='1"

    with_placeholder = connection.execute(
        "SELECT COUNT(*) FROM readings WHERE tag = ?", (hostile,)
    ).fetchone()[0]

    with_fstring = connection.execute(
        f"SELECT COUNT(*) FROM readings WHERE tag = '{hostile}'"  # noqa: S608
    ).fetchone()[0]

    assert with_placeholder == 0
    assert with_fstring == 50

    selected = connection.execute("SELECT ? FROM readings LIMIT 1", ("value",)).fetchone()[0]

    assert selected == "value"

    counts = connection.execute("SELECT COUNT(*), COUNT(value) FROM readings").fetchone()

    assert counts == (50, 47)

    assert connection.execute("SELECT NULL = NULL, NULL IS NULL").fetchone() == (None, 1)

    assert connection.execute("SELECT COUNT(*) FROM readings WHERE value = NULL").fetchone()[0] == 0

    with connection:
        connection.execute(
            "INSERT INTO readings (tag, value, at) VALUES (?, ?, ?)",
            ("TH-01", "kaputt", "2026-03-20T08:00"),
        )
        stored = connection.execute(
            "SELECT value, typeof(value) FROM readings WHERE at = ?", ("2026-03-20T08:00",)
        ).fetchone()
        connection.rollback()

    assert stored == ("kaputt", "text")

    assert connection.execute("PRAGMA foreign_keys").fetchone()[0] == 0

    with connection:
        connection.execute(
            "INSERT INTO readings (tag, value, at) VALUES (?, ?, ?)",
            ("TH-77", 42.0, "2026-03-21T08:00"),
        )
        total = connection.execute("SELECT COUNT(*) FROM readings").fetchone()[0]
        joined = connection.execute(
            "SELECT COUNT(*) FROM readings r JOIN sensors s ON s.tag = r.tag"
        ).fetchone()[0]
        connection.rollback()

    assert (total, joined) == (51, 50)

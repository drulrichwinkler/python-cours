"""Exercise 02 -- Predict what SQLite does.

Replace each `...` with the value you expect, then run the file.

    uv run 19_sql/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

with contextlib.closing(sqlite3.connect(DB)) as connection:
    # TODO: how does a row arrive before you set row_factory?
    row = connection.execute("SELECT tag, location FROM sensors LIMIT 1").fetchone()

    assert type(row).__name__ == ...

    # TODO: the same value through a placeholder and pasted into the query text
    hostile = "TH-04' OR '1'='1"

    with_placeholder = connection.execute(
        "SELECT COUNT(*) FROM readings WHERE tag = ?", (hostile,)
    ).fetchone()[0]

    with_fstring = connection.execute(
        f"SELECT COUNT(*) FROM readings WHERE tag = '{hostile}'"  # noqa: S608
    ).fetchone()[0]

    assert with_placeholder == ...
    assert with_fstring == ...

    # TODO: a placeholder where a column name goes
    selected = connection.execute("SELECT ? FROM readings LIMIT 1", ("value",)).fetchone()[0]

    assert selected == ...

    # TODO: COUNT(*) against COUNT(column), with three NULLs in the table
    counts = connection.execute("SELECT COUNT(*), COUNT(value) FROM readings").fetchone()

    assert counts == ...

    # TODO: NULL compared with itself
    assert connection.execute("SELECT NULL = NULL, NULL IS NULL").fetchone() == ...

    # TODO: so how many rows does `= NULL` find?
    assert (
        connection.execute("SELECT COUNT(*) FROM readings WHERE value = NULL").fetchone()[0] == ...
    )

    # TODO: a string into a column declared REAL
    with connection:
        connection.execute(
            "INSERT INTO readings (tag, value, at) VALUES (?, ?, ?)",
            ("TH-01", "kaputt", "2026-03-20T08:00"),
        )
        stored = connection.execute(
            "SELECT value, typeof(value) FROM readings WHERE at = ?", ("2026-03-20T08:00",)
        ).fetchone()
        connection.rollback()

    assert stored == ...

    # TODO: is the foreign key in the schema enforced?
    assert connection.execute("PRAGMA foreign_keys").fetchone()[0] == ...

    # TODO: and a plain JOIN against a LEFT JOIN, with an orphan in the table
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

    assert (total, joined) == ...

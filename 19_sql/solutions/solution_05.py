"""Solution 05 -- NULL, and the rows a JOIN drops."""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

with contextlib.closing(sqlite3.connect(DB)) as connection:
    # NULL is not equal to anything, including itself, so `= NULL` matches nothing.
    print(connection.execute("SELECT NULL = NULL, NULL IS NULL").fetchone())
    print(
        connection.execute("SELECT COUNT(*) FROM readings WHERE value IS NULL").fetchone()[0],
        connection.execute("SELECT COUNT(*) FROM readings WHERE value = NULL").fetchone()[0],
    )

    with connection:  # a transaction: the insert below is undone by the rollback
        connection.execute(
            "INSERT INTO readings (tag, value, at) VALUES (?, ?, ?)",
            ("TH-77", 42.0, "2026-03-09T18:00"),
        )

        total = connection.execute("SELECT COUNT(*) FROM readings").fetchone()[0]
        joined = connection.execute(
            "SELECT COUNT(*) FROM readings r JOIN sensors s ON s.tag = r.tag"
        ).fetchone()[0]
        print(total, joined)

        # LEFT JOIN keeps the left rows and fills the right with NULL, so this is
        # how you find the orphans instead of losing them.
        orphans = connection.execute(
            """
            SELECT   r.tag
            FROM     readings r
            LEFT JOIN sensors s ON s.tag = r.tag
            WHERE    s.tag IS NULL
            """
        ).fetchall()
        print([row[0] for row in orphans])

        connection.rollback()

    print(connection.execute("SELECT COUNT(*) FROM readings").fetchone()[0])

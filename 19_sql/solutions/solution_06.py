"""Solution 06 -- A REAL column that is not real."""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

with contextlib.closing(sqlite3.connect(DB)) as connection:
    connection.execute(
        "INSERT INTO readings (tag, value, at) VALUES (?, ?, ?)",
        ("TH-01", "kaputt", "2026-03-10T08:00"),
    )
    # A column's declared type is an AFFINITY, not a constraint: SQLite stores what
    # it cannot convert, as text, in a column declared REAL.
    print(
        connection.execute(
            "SELECT value, typeof(value) FROM readings WHERE at = ?", ("2026-03-10T08:00",)
        ).fetchone()
    )
    connection.rollback()

    # STRICT turns the affinity into a rule, and this section into a non-problem.
    connection.execute("DROP TABLE IF EXISTS strict_demo")
    connection.execute("CREATE TABLE strict_demo (value REAL) STRICT")
    try:
        connection.execute("INSERT INTO strict_demo (value) VALUES (?)", ("kaputt",))
        print("accepted")
    except sqlite3.IntegrityError as err:
        print(type(err).__name__)
    connection.execute("INSERT INTO strict_demo (value) VALUES (?)", (21.7,))
    print(connection.execute("SELECT value, typeof(value) FROM strict_demo").fetchone())
    connection.execute("DROP TABLE strict_demo")
    connection.commit()

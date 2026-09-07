"""Solution 01 -- Connect, query, read by name."""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"

# contextlib.closing, not `with sqlite3.connect(...)`: `with` on a connection is a
# TRANSACTION and does not close anything -- section 8.
with contextlib.closing(sqlite3.connect(DB)) as connection:
    rows = connection.execute("SELECT tag, location FROM sensors ORDER BY tag").fetchall()
    print(type(rows[0]).__name__, len(rows))

    connection.row_factory = sqlite3.Row  # set it before you execute
    row = connection.execute("SELECT tag, location, installed FROM sensors LIMIT 1").fetchone()
    print(row["tag"], row["location"])
    print(row.keys())

    hot = connection.execute(
        "SELECT tag, value FROM readings WHERE value > 85 ORDER BY value DESC"
    ).fetchall()
    print([(r["tag"], r["value"]) for r in hot])

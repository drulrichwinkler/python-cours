"""Solution 03 -- Repair a query built out of strings."""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"


def count_for(connection, tag):
    """How many readings that tag has."""
    # The value goes through a placeholder, so SQLite never parses it as SQL. The
    # trailing comma matters: (tag,) is a one-element tuple, (tag) is just tag.
    return connection.execute("SELECT COUNT(*) FROM readings WHERE tag = ?", (tag,)).fetchone()[0]


with contextlib.closing(sqlite3.connect(DB)) as connection:
    print(count_for(connection, "TH-04"))
    print(count_for(connection, "TH-99"))
    # The value that rewrote the WHERE clause when it was pasted in. Now it is
    # just a tag that does not exist.
    print(count_for(connection, "TH-04' OR '1'='1"))
    print(connection.execute("SELECT COUNT(*) FROM readings").fetchone()[0])

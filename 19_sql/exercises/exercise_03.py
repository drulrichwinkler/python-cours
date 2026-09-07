"""Exercise 03 -- Repair a query built out of strings.

`count_for` pastes the tag into the query text. Run it and look at the third number:
a tag that does not exist is reported as having every reading in the table.

Rewrite the function so the tag is a value rather than part of the query.

Expected output:

    10
    0
    0
    50

Hint: `?` in the query, and the value in a **sequence** as the second argument to
`execute`. The trailing comma is not optional: `(tag,)` is a one-element tuple and
`(tag)` is just `tag`, which raises. Do not change the calls.
"""

import contextlib
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "readings.db"


def count_for(connection, tag):
    """How many readings that tag has."""
    # TODO: this line is the bug
    return connection.execute(
        f"SELECT COUNT(*) FROM readings WHERE tag = '{tag}'"  # noqa: S608
    ).fetchone()[0]


with contextlib.closing(sqlite3.connect(DB)) as connection:
    print(count_for(connection, "TH-04"))
    print(count_for(connection, "TH-99"))
    print(count_for(connection, "TH-04' OR '1'='1"))
    print(connection.execute("SELECT COUNT(*) FROM readings").fetchone()[0])

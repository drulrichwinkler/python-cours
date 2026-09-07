"""Build the database this module works on, from the two CSV files.

Run it once:

    uv run 19_sql/build_db.py

It writes data/readings.db, which is gitignored -- a database is a build
artefact, and the CSV files next to it are the source. Deleting the .db file and
running this again is always safe.
"""

import csv
import sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
DB = DATA / "readings.db"

SCHEMA = """
DROP TABLE IF EXISTS readings;
DROP TABLE IF EXISTS sensors;

CREATE TABLE sensors (
    tag       TEXT PRIMARY KEY,
    location  TEXT NOT NULL,
    installed TEXT NOT NULL
);

CREATE TABLE readings (
    id    INTEGER PRIMARY KEY,          -- rowid alias: SQLite fills it in
    tag   TEXT NOT NULL REFERENCES sensors(tag),
    value REAL,                         -- NULL where the reading was unreadable
    at    TEXT NOT NULL                 -- ISO-8601, which sorts correctly as text
);

CREATE INDEX readings_tag ON readings(tag);
"""


def rows(path):
    with open(path, newline="", encoding="utf-8") as handle:
        yield from csv.DictReader(handle, delimiter=";")


def to_value(raw):
    """The unreadable cells become NULL rather than a string in a REAL column."""
    try:
        return float(raw)
    except ValueError:
        return None


def main():
    with sqlite3.connect(DB) as connection:
        connection.executescript(SCHEMA)
        connection.executemany(
            "INSERT INTO sensors (tag, location, installed) VALUES (?, ?, ?)",
            [(r["tag"], r["location"], r["installed"]) for r in rows(DATA / "sensors.csv")],
        )
        connection.executemany(
            "INSERT INTO readings (tag, value, at) VALUES (?, ?, ?)",
            [(r["tag"], to_value(r["value"]), r["at"]) for r in rows(DATA / "readings.csv")],
        )

    with sqlite3.connect(DB) as connection:
        sensors = connection.execute("SELECT COUNT(*) FROM sensors").fetchone()[0]
        readings = connection.execute("SELECT COUNT(*) FROM readings").fetchone()[0]
        nulls = connection.execute("SELECT COUNT(*) FROM readings WHERE value IS NULL").fetchone()[
            0
        ]

    print(f"{DB.name}: {sensors} sensors, {readings} readings, {nulls} of them NULL")


if __name__ == "__main__":
    main()

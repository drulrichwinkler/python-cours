"""Solution 03 -- Narrow the clause."""

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def read_values(path):
    values = []
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter=";"):
            try:
                # Only float() may fail here, and only with ValueError. The bare
                # clause hid a misspelled key -- a KeyError, which is a bug in this
                # function rather than bad data.
                values.append(float(row["value"]))
            except ValueError:
                continue
    return values


print(read_values(DATA / "readings.csv"))

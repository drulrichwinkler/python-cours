"""Solution 03 -- Repair a hand-rolled CSV reader."""

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def read_rows(path):
    # Splitting on the separator breaks on a quoted field that contains one.
    # The csv module knows about the quotes; newline="" is what its docs ask for,
    # because it handles line endings itself.
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.reader(fh, delimiter=";"))


rows = read_rows(DATA / "tricky.csv")

for row in rows:
    print(len(row), row)

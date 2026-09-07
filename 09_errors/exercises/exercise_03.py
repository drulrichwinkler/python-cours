"""Exercise 03 -- Narrow the clause.

Run this. It prints an empty list, and it should print three readings.

There are two things wrong, and the first one is hiding the second: a bare `except:`
catches everything, including the mistake in the line above it. Narrow the clause to
the failure that line can actually produce, run it again, and read what appears.

Expected output:

    [21.7, 23.1, 22.8]

Hint: what can `float()` raise? What can a dict lookup raise? Only one of the two is
bad data; the other is a bug in this function. `ruff` already objects to the bare
form -- the rule is `E722`.
"""

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def read_values(path):
    values = []
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter=";"):
            try:
                values.append(float(row["values"]))
            except:  # noqa: E722  # TODO: the bug is this line -- and what it hides
                continue
    return values


print(read_values(DATA / "readings.csv"))

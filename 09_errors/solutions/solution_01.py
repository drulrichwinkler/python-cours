"""Solution 01 -- Convert what can be converted."""

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def read_values(path):
    """Return (values, skipped): the readings that parsed, and how many did not."""
    values = []
    skipped = 0
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter=";"):
            try:
                values.append(float(row["value"]))
            except ValueError:
                # Exactly the failure float() produces on a field that is not a
                # number. A wider clause would also swallow a typo in this block.
                skipped += 1
    return values, skipped


values, skipped = read_values(DATA / "readings.csv")

print(values)
print(skipped, "skipped")
print(f"{sum(values) / len(values):.2f}")

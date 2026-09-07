"""Solution 04 -- Read the log as records."""

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def read_sensors(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter=";"))


rows = read_sensors(DATA / "sensors.csv")

print(len(rows))
print(rows[0])
# Everything a CSV reader produces is a str -- converting is the caller's job.
print([row["tag"] for row in rows if float(row["value"]) > 85])
print(sorted({row["location"] for row in rows}))

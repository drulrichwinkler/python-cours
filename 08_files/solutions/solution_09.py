"""Solution 09 (bonus) -- The CSV against the JSON."""

import csv
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def faults(csv_path, json_path):
    """Return [(tag, value)] for every reading above that sensor's own limit."""
    limits = json.loads(json_path.read_text(encoding="utf-8"))

    with open(csv_path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter=";"))

    out = []
    for row in rows:
        high = limits["sensors"].get(row["tag"], limits["default"])["high"]
        value = float(row["value"])  # the CSV gives strings; the comparison needs numbers
        if value > high:
            out.append((row["tag"], value))
    return out


result = faults(DATA / "sensors.csv", DATA / "limits.json")

print(result)
print(len(result), "of 5")

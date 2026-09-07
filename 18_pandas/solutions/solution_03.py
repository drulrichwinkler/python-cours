"""Solution 03 -- Repair a column that is not numbers."""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"


def load(path):
    """Read the file with the value column as numbers and the timestamps parsed."""
    # 'kaputt' is not in pandas' default NA list -- which is why the column came
    # out as text, and why .sum() concatenated instead of adding. na_values names
    # it; parse_dates makes `at` timestamps rather than strings.
    return pd.read_csv(path, sep=";", na_values=["kaputt"], parse_dates=["at"])


frame = load(READINGS)

print(frame["value"].dtype, frame["at"].dtype)
print(frame["value"].isna().sum(), "of", len(frame), "unreadable")
print(round(frame["value"].sum(), 1))
print(round(frame["value"].mean(), 2), frame["value"].count())

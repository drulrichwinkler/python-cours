"""Solution 04 -- Selecting rows and columns."""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

frame = pd.read_csv(READINGS, sep=";", na_values=["kaputt"], parse_dates=["at"])

hot = frame["value"] > 85  # a Series of booleans, one per row

print(type(hot).__name__, hot.dtype)
print(hot.sum())
print(frame.loc[hot, "tag"].tolist())
# & and |, each side bracketed: `and` has no single truth value to work with.
both = frame[(frame["value"] > 85) & (frame["location"] == "Test rig")]
print(len(both))
print(sorted(both["tag"].unique()))

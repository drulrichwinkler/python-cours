"""Solution 01 -- A table with typed columns."""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

frame = pd.read_csv(READINGS, sep=";")

print(frame.shape)
print(frame.dtypes["value"])
print(frame["tag"].nunique(), frame["location"].nunique())
print(sorted(frame["tag"].unique()))
print(frame["location"].value_counts().to_dict())

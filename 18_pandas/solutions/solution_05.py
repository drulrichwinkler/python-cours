"""Solution 05 -- What a NaN does to an answer."""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

frame = pd.read_csv(READINGS, sep=";", na_values=["kaputt"], parse_dates=["at"])

print(len(frame), frame["value"].count())
print(frame["value"].isna().sum())
# mean() skips NaN, so it is the mean of what is there -- not of len(frame).
print(round(frame["value"].mean(), 3))
# fillna(0) invents three readings at freezing point and moves the answer.
print(round(frame["value"].fillna(0).mean(), 3))
print(len(frame["value"].dropna()))
print(float("nan") == float("nan"), pd.isna(float("nan")))

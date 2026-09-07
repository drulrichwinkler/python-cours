"""Exercise 05 -- What a NaN does to an answer.

Six lines, and the point is that the first two differ:

  1. `len(frame)` and `frame["value"].count()`, separated by a space
  2. how many values are missing
  3. the mean, to three places
  4. the mean after `fillna(0)`, to three places
  5. how many are left after `dropna()`
  6. `float("nan") == float("nan")` and `pd.isna(float("nan"))`, separated by a space

Expected output:

    50 47
    3
    26.721
    25.118
    47
    False True

Hint: `count()` skips NaN and `len()` does not, which is the whole of line 1. Line 4
is the one to think about before you run it: `fillna(0)` on a temperature invents
three readings at freezing point, and the mean moves by one and a half degrees. Line
6 is why you never test for a missing value with `==`.
"""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

frame = pd.read_csv(READINGS, sep=";", na_values=["kaputt"], parse_dates=["at"])

# TODO: six prints

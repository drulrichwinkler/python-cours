"""Exercise 09 (bonus) -- A report worth showing somebody.

Write `report(frame)`, returning one row per location with five named columns:

  - `readings`  -- how many rows there are
  - `usable`    -- how many have a value
  - `mean`      -- the mean of those
  - `highest`   -- the largest
  - `faults`    -- how many are above LIMIT

rounded to two places. Then print one line per location, a blank line, and three
more lines.

Each report line is the location padded to 10, then readings in a field of 3, usable
in 4, mean in 8, highest in 7 and faults in 3.

Expected output:

    Hall       20  18   22.12   23.9  0
    Office     10   9   22.34   23.1  0
    Test rig   20  20   32.83   93.5  3

    50 47
    ['Test rig']
    TH-04 93.5 12

Hint: `frame.groupby("location").agg(name=("column", "function"), ...)` names the
output columns. The difference between `readings` and `usable` is `size` against
`count` -- one counts rows, the other skips NaN, and the two differ by two for Hall.
Add the `fault` column before grouping, and `sum` a boolean column to count the True
ones. The last line uses `.idxmax()` and `.dt.hour`.
"""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

LIMIT = 85.0


def load(path):
    return pd.read_csv(path, sep=";", na_values=["kaputt"], parse_dates=["at"])


# TODO: write report


frame = load(READINGS)
summary = report(frame)

# TODO: the loop over summary.iterrows()

print()
print(summary["readings"].sum(), summary["usable"].sum())
print(summary.loc[summary["faults"] > 0].index.tolist())

frame["hour"] = frame["at"].dt.hour
worst = frame.loc[frame["value"].idxmax()]
print(worst["tag"], worst["value"], int(worst["hour"]))

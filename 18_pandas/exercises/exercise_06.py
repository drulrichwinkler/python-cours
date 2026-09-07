"""Exercise 06 -- Grouping.

Group by location and aggregate the value column three ways -- count, mean and max,
rounded to two places. Then print one line per group and three more things.

Each group line is the location padded to 10 characters, then the count in a field
of 3, the mean in a field of 8 and the max in a field of 7.

Expected output:

    Hall       18   22.12   23.9
    Office      9   22.34   23.1
    Test rig   20   32.83   93.5

    {'Hall': 18, 'Office': 9, 'Test rig': 20}
    Test rig
    {'TH-04': 93.5, 'TH-02': 88.4, 'TH-09': 23.9}

Hint: `frame.groupby("location")["value"].agg(["count", "mean", "max"]).round(2)`.
`summary.iterrows()` yields (label, row) pairs, and the format spec is module 07:
`f"{location:<10}{int(row['count']):>3}..."`. The count has to be an int or it
prints as 18.0. The last line groups by tag instead, takes the max, sorts
descending, keeps three.
"""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

frame = pd.read_csv(READINGS, sep=";", na_values=["kaputt"], parse_dates=["at"])

# TODO: the summary, the loop, then three prints

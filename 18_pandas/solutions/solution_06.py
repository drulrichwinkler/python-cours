"""Solution 06 -- Grouping."""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

frame = pd.read_csv(READINGS, sep=";", na_values=["kaputt"], parse_dates=["at"])

summary = frame.groupby("location")["value"].agg(["count", "mean", "max"]).round(2)

# One line per group, formatted here rather than by .to_string(): a printed pandas
# table pads with spaces to align, and that padding is not worth comparing against.
for location, row in summary.iterrows():
    print(f"{location:<10}{int(row['count']):>3}{row['mean']:>8}{row['max']:>7}")

print()
# count belongs in every summary: a mean over 9 readings and one over 20 are not
# comparable, and the count is what says which you have.
print(summary["count"].to_dict())
print(summary["mean"].idxmax())

per_tag = frame.groupby("tag")["value"].max().round(1)
print(per_tag.sort_values(ascending=False).head(3).to_dict())

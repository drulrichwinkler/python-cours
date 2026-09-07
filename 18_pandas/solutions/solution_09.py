"""Solution 09 (bonus) -- A report worth showing somebody."""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

LIMIT = 85.0


def load(path):
    return pd.read_csv(path, sep=";", na_values=["kaputt"], parse_dates=["at"])


def report(frame):
    """Per location: how many readings, how many usable, the mean, the max, the faults."""
    frame = frame.copy()
    frame["fault"] = frame["value"] > LIMIT

    out = frame.groupby("location").agg(
        # size counts rows; count skips NaN. A report that confuses the two claims
        # readings it does not have.
        readings=("value", "size"),
        usable=("value", "count"),
        mean=("value", "mean"),
        highest=("value", "max"),
        faults=("fault", "sum"),
    )
    return out.round(2)


frame = load(READINGS)
summary = report(frame)

for location, row in summary.iterrows():
    print(
        f"{location:<10}{int(row['readings']):>3}{int(row['usable']):>4}"
        f"{row['mean']:>8}{row['highest']:>7}{int(row['faults']):>3}"
    )

print()
print(summary["readings"].sum(), summary["usable"].sum())
print(summary.loc[summary["faults"] > 0].index.tolist())

frame["hour"] = frame["at"].dt.hour
worst = frame.loc[frame["value"].idxmax()]
print(worst["tag"], worst["value"], int(worst["hour"]))

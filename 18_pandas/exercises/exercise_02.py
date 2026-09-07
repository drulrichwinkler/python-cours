"""Exercise 02 -- Predict what pandas does.

Replace each `...` with the value you expect, then run the file.

    uv run 18_pandas/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

raw = pd.read_csv(READINGS, sep=";")

# TODO: one unreadable cell in fifty. What type is the column?
assert str(raw["value"].dtype) == ...


# TODO: arithmetic on that column. Which of these raise, and what do the others give?
assert type(raw["value"].sum()).__name__ == ...
assert type(raw["value"].max()).__name__ == ...

try:
    raw["value"].mean()
    mean_outcome = "worked"
except TypeError:
    mean_outcome = "TypeError"

assert mean_outcome == ...

try:
    raw["value"] > 85
    compare_outcome = "worked"
except TypeError:
    compare_outcome = "TypeError"

assert compare_outcome == ...


# TODO: and comparing it with a string instead
assert type((raw["value"] > "85").sum()).__name__ in ...


# TODO: describe() on a text column has different rows entirely
assert raw["value"].describe().index.tolist() == ...


clean = pd.read_csv(READINGS, sep=";", na_values=["kaputt"], parse_dates=["at"])

# TODO: what does na_values change, and what does parse_dates change?
assert str(clean["value"].dtype) == ...
assert str(clean["at"].dtype).startswith(...)


# TODO: len against count
assert len(clean) == ...
assert clean["value"].count() == ...


# TODO: a mask is a Series of what?
mask = clean["value"] > 85

assert type(mask).__name__ == ...
assert str(mask.dtype) == ...
assert mask.sum() == ...


# TODO: `and` between two Series
try:
    clean[(clean["value"] > 85) and (clean["location"] == "Test rig")]
    joined = "worked"
except ValueError:
    joined = "ValueError"

assert joined == ...


# TODO: a NaN is not equal to itself, and not counted by a comparison
assert (float("nan") == float("nan")) == ...
assert pd.isna(float("nan")) == ...

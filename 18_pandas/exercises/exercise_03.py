"""Exercise 03 -- Repair a column that is not numbers.

`load` reads the file and gets a `value` column of text, so every number in the
module is wrong. Two arguments to `read_csv` fix it.

Run it first and look at what `sum()` gave you.

Expected output:

    float64 datetime64[us]
    3 of 50 unreadable
    1255.9
    26.72 47

Hint: pandas already treats `n/a`, `NA`, `null` and a dozen others as missing. It
does not treat `kaputt` as missing, and one such cell makes the whole column text.
The second argument is about the `at` column, which is timestamps written as text
until you say so.
"""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"


def load(path):
    """Read the file with the value column as numbers and the timestamps parsed."""
    return pd.read_csv(path, sep=";")  # TODO: two arguments missing


frame = load(READINGS)

print(frame["value"].dtype, frame["at"].dtype)
print(frame["value"].isna().sum(), "of", len(frame), "unreadable")
print(round(frame["value"].sum(), 1))
print(round(frame["value"].mean(), 2), frame["value"].count())

"""Exercise 04 -- Selecting rows and columns.

Build the mask `frame["value"] > 85` and print five lines:

  1. the type name of the mask and its dtype, separated by a space
  2. how many rows it selects
  3. the tags of those rows, as a list -- note that one appears twice
  4. how many rows are above 85 **and** at the test rig
  5. the distinct tags of those, sorted

Expected output:

    Series bool
    3
    ['TH-04', 'TH-04', 'TH-02']
    3
    ['TH-02', 'TH-04']

Hint: a mask is a Series of booleans, and `.sum()` counts the True ones.
`frame.loc[mask, "tag"]` takes rows by mask and one column by name. For line 4 you
need two conditions -- with `&`, and each side in brackets. `and` raises here, and
module 02 says why: a Series of fifty has no single truth value to return.
"""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

frame = pd.read_csv(READINGS, sep=";", na_values=["kaputt"], parse_dates=["at"])

# TODO: the mask, then five prints

"""Exercise 01 -- A table with typed columns.

Read `data/readings.csv` and print five lines:

  1. the shape, as `read_csv` reports it
  2. the dtype of the `value` column -- read it twice, it is the module's subject
  3. how many distinct tags and how many distinct locations, separated by a space
  4. the tags, sorted
  5. how many readings per location, as a dict

Expected output:

    (50, 5)
    str
    5 3
    ['TH-01', 'TH-02', 'TH-04', 'TH-07', 'TH-09']
    {'Hall': 20, 'Test rig': 20, 'Office': 10}

Hint: `pd.read_csv(path, sep=";")` -- the separator is a semicolon. `.nunique()`
counts distinct values, `.unique()` lists them, `.value_counts()` counts per value
and `.to_dict()` makes it printable. Line 2 is `str` and not a number: fifty
readings, and one cell in them is not a number.
"""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

# TODO: read the file, then five prints

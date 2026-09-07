"""Exercise 01 -- Convert what can be converted.

`data/readings.csv` has five rows. Two of them have a value that is not a number.

Write `read_values(path)` returning a pair: the list of readings that could be
converted, and the number of rows that could not. Then print the three lines below.

Expected output:

    [21.7, 23.1, 22.8]
    2 skipped
    22.53

Hint: `float(raw)` raises `ValueError` on a field that is not a number. Catch that
class and nothing wider -- a `try` around more lines than the one that can fail is
how a typo gets swallowed. The mean is rounded in the f-string.
"""

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


# TODO: write the function


values, skipped = read_values(DATA / "readings.csv")

# TODO: three prints

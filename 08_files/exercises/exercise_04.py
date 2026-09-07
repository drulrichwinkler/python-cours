"""Exercise 04 -- Read the log as records.

Write `read_sensors(path)` returning one dict per data line, with the header row as
the keys. Then print four things:

  1. how many records there are
  2. the first record
  3. the tags whose value is above 85, as a list
  4. the distinct locations, sorted

Expected output:

    5
    {'tag': 'TH-01', 'value': '21.7', 'unit': '°C', 'location': 'Hall'}
    ['TH-04', 'TH-02']
    ['Hall', 'Office', 'Test rig']

Hint: `csv.DictReader(fh, delimiter=";")` does the dict part. Everything it hands
back is a string, so the comparison in (3) needs `float(...)`. For (4), a set drops
the duplicates and `sorted` puts it in an order you can print.
"""

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


# TODO: write the function


rows = read_sensors(DATA / "sensors.csv")

# TODO: four prints

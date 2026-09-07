"""Exercise 04 -- A table into records.

Build one dict per reading, with the keys `tag`, `value` and `fault`. `value` is a
float; `fault` is True when the row carries the class `fault`. Select the cells **by
class**, not by position.

Then print the three records, the tags of the faults, and the mean rounded to two
places.

Expected output:

    {'tag': 'TH-01', 'value': 21.7, 'fault': False}
    {'tag': 'TH-04', 'value': 91.0, 'fault': True}
    {'tag': 'TH-09', 'value': 23.1, 'fault': False}
    ['TH-04']
    45.27

Hint: `row.select_one("td.tag")` picks the cell by its class, which survives a column
being inserted -- `cells[0]` does not. `row.get("class", [])` is a **list**, so the
test for a fault is `"fault" in ...`. Everything scraped is a string, so `value`
needs converting.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from server import serve  # noqa: E402

# TODO: fetch, parse, build the records, then five prints

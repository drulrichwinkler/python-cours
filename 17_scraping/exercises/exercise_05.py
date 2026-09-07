"""Exercise 05 -- What the parser did to the broken page.

`/readings.html` and `/sloppy.html` hold the same readings. The second one leaves out
the closing tags, which is legal HTML.

Parse both and print five lines:

  1. how many `tr.row` each page has, separated by a space
  2. how many `td` the first row of each has, separated by a space
  3. the text of the first cell of the broken page's first row
  4. the text of the first cell of the good page's first row

Expected output:

    3 2
    3 4
    TH-0121.7TH-0491.0
    TH-01

Hint: nothing here raises, and that is the exercise. Read line 3 twice: the parser
could not tell where each cell ended, so it nested them -- every cell contains the
text of everything after it. Four cells where there are two readings, and a `len()`
that looks like a column count.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from server import serve  # noqa: E402

# TODO: parse both pages, then four prints

"""Exercise 01 -- A parsed page is a tree.

Fetch `/readings.html`, parse it, and print six lines:

  1. the page title
  2. the text of the h1
  3. how many `td` elements there are altogether
  4. the text of every value cell, as a list
  5. the class list of the element with id `readings`
  6. the href of the link with class `next`

Expected output:

    Sensors — Halle 3
    Station Halle 3
    9
    ['21.7', '91.0', '23.1']
    ['data']
    /page2.html

Hint: `BeautifulSoup(text, "html.parser")` -- name the parser, always. `soup.title`
and `soup.h1` reach a tag directly; `select` takes a CSS selector and `select_one`
takes the first match. Line 5 is a **list** and not a string, which is worth noticing
now rather than in exercise 04.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # so that `import server` finds it -- module 10

import requests  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from server import serve  # noqa: E402

# TODO: fetch inside `with serve() as base:`, parse, then six prints

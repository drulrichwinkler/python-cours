"""Exercise 03 -- Repair a scraper that trusts the page.

`readings` works on the good page. Against `/sloppy.html` it returns nonsense, and
against `/nope` it raises `AttributeError` with a message that names neither the
selector nor the page.

Add two checks, and define the exception class they raise. Do not change the calls.

Expected output:

    [('TH-01', 21.7), ('TH-04', 91.0), ('TH-09', 23.1)]
    unclosed tags: row has 4 cells, expected 3
    404 page: no #readings table -- has the page changed?

Hint: `select_one` returns `None` when nothing matches, so the first check is for
that. The second is the cheapest line in any scraper: a row should have three cells,
so say so. Both raise your own class -- module 09.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from server import serve  # noqa: E402

# TODO: the exception class


def readings(html):
    soup = BeautifulSoup(html, "html.parser")

    table = soup.select_one("#readings")
    # TODO: check the table

    out = []
    for row in table.select("tr.row"):
        cells = row.select("td")
        # TODO: check the cells
        out.append((cells[0].get_text(strip=True), float(cells[1].get_text(strip=True))))
    return out


with serve() as base:
    print(readings(requests.get(f"{base}/readings.html", timeout=5).text))

    for path, note in (("/sloppy.html", "unclosed tags"), ("/nope", "404 page")):
        try:
            readings(requests.get(f"{base}{path}", timeout=5).text)
        except ScrapeError as err:
            print(f"{note}: {err}")

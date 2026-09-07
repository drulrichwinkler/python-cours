"""Solution 03 -- Repair a scraper that trusts the page."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from server import serve  # noqa: E402


class ScrapeError(Exception):
    """Raised when the page is not shaped the way the scraper expects."""


def readings(html):
    soup = BeautifulSoup(html, "html.parser")

    # select_one returns None rather than raising, so the AttributeError would
    # otherwise arrive a line later with a message naming neither the selector
    # nor the page.
    table = soup.select_one("#readings")
    if table is None:
        raise ScrapeError("no #readings table -- has the page changed?")

    out = []
    for row in table.select("tr.row"):
        cells = row.select("td")
        # The parser repairs broken HTML silently, so the cell count is a claim
        # worth checking rather than trusting -- see section 5.
        if len(cells) != 3:
            raise ScrapeError(f"row has {len(cells)} cells, expected 3")
        out.append((cells[0].get_text(strip=True), float(cells[1].get_text(strip=True))))
    return out


with serve() as base:
    print(readings(requests.get(f"{base}/readings.html", timeout=5).text))

    for path, note in (("/sloppy.html", "unclosed tags"), ("/nope", "404 page")):
        try:
            readings(requests.get(f"{base}{path}", timeout=5).text)
        except ScrapeError as err:
            print(f"{note}: {err}")

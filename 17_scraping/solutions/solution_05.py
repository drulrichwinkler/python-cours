"""Solution 05 -- What the parser did to the broken page."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from server import serve  # noqa: E402

with serve() as base:
    good = BeautifulSoup(requests.get(f"{base}/readings.html", timeout=5).text, "html.parser")
    sloppy = BeautifulSoup(requests.get(f"{base}/sloppy.html", timeout=5).text, "html.parser")

print(len(good.select("tr.row")), len(sloppy.select("tr.row")))

first_good = good.select("tr.row")[0]
first_sloppy = sloppy.select("tr.row")[0]

print(len(first_good.select("td")), len(first_sloppy.select("td")))
print(first_sloppy.select("td")[0].get_text(strip=True))
# No exception anywhere above: the parser nested the unclosed cells inside each
# other, so every cell contains the text of everything after it.
print(first_good.select("td")[0].get_text(strip=True))

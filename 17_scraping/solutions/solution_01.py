"""Solution 01 -- A parsed page is a tree."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # so that `import server` finds it -- module 10

import requests  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from server import serve  # noqa: E402

with serve() as base:
    response = requests.get(f"{base}/readings.html", timeout=5)
    response.raise_for_status()
    # Name the parser: different parsers repair broken HTML differently, so an
    # unnamed one makes the result depend on what happens to be installed.
    soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.string)
print(soup.h1.get_text())
print(len(soup.find_all("td")))
print([td.get_text() for td in soup.select("tr.row td.value")])
print(soup.select_one("#readings").get("class"))
print(soup.select_one("a.next")["href"])

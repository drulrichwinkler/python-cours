"""Exercise 02 -- Predict what a scraper does.

Replace each `...` with the value you expect, then run the file.

    uv run 17_scraping/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

import sys
from pathlib import Path
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from server import serve  # noqa: E402

with serve() as base:
    soup = BeautifulSoup(requests.get(f"{base}/readings.html", timeout=5).text, "html.parser")

    # TODO: entities in the source -- what does the parser give back?
    assert soup.title.string == ...

    # TODO: an element can have several classes
    assert soup.select("tr.row")[1].get("class") == ...

    # TODO: what does select_one give when nothing matches, and what then?
    absent = soup.select_one("h2")

    assert absent is ...

    try:
        absent.get_text()
        outcome = "worked"
    except Exception as err:
        outcome = type(err).__name__

    assert outcome == ...

    # TODO: a missing attribute, two ways
    heading = soup.select_one("h1")

    assert heading.get("href") is ...

    try:
        heading["href"]
        access = "worked"
    except Exception as err:
        access = type(err).__name__

    assert access == ...

    # TODO: everything scraped is text
    first_value = soup.select_one("td.value").get_text(strip=True)

    assert type(first_value).__name__ == ...
    assert first_value == ...

    # TODO: the broken page. No exception -- so what comes out?
    sloppy = BeautifulSoup(requests.get(f"{base}/sloppy.html", timeout=5).text, "html.parser")

    assert len(sloppy.select("tr.row")) == ...
    assert len(sloppy.select("tr.row")[0].select("td")) == ...

    # TODO: robots.txt matches Disallow by prefix, not by path segment
    rules = RobotFileParser()
    rules.set_url(f"{base}/robots.txt")
    rules.read()

    assert rules.can_fetch("*", urljoin(base, "/readings.html")) == ...
    assert rules.can_fetch("*", urljoin(base, "/administration")) == ...
    assert rules.crawl_delay("*") == ...


# TODO: resolving a relative href
assert urljoin("http://x.invalid/a/b.html", "/next") == ...
assert urljoin("http://x.invalid/a/b.html", "next") == ...

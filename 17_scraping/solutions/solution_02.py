"""Solution 02 -- Predict what a scraper does.

soup.title       is 'Sensors — Halle 3': the parser resolved &mdash; into the
                 character. What you get out of a page is text, not markup.
.get("class")    is ['row', 'fault'] -- a LIST, because an element can carry
                 several classes. Code that treats it as a string works until the
                 first element with two, which on this page is the second row.
select_one       gives None when nothing matches, and does not raise. So the
                 failure arrives one line later as AttributeError: 'NoneType'
                 object has no attribute 'get_text' -- the most common scraping
                 error, and its message names neither the selector nor the page.
attributes       differ from elements: .get("href") returns None, ["href"] raises
                 KeyError. Same distinction as dict.get against dict[...] in
                 module 06.
first_value      is the string '21.7'. Everything scraped is text, as with a CSV
                 in module 08 -- the conversion is yours, and it is where bad data
                 announces itself.
sloppy           has 2 rows where the good page has 3, and its first row has FOUR
                 cells for two readings. Nothing raised: html.parser could not
                 tell where each unclosed <td> ended, so it nested them, and every
                 cell now contains the text of everything after it. This is the
                 latin-1 failure of modules 08 and 16 for the third time -- the
                 tool that cannot fail is the one that hurts you.
robots.txt       forbids /administration, and nobody wrote that path down.
                 Disallow matches by PREFIX, not by path segment, so a rule saying
                 /admin covers it. crawl_delay is 1: the site asked, and honouring
                 it is what makes the difference between a client and a nuisance.
urljoin          resolves against the page: a leading slash goes to the root, no
                 slash goes to the current directory.
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

    assert soup.title.string == "Sensors — Halle 3"

    assert soup.select("tr.row")[1].get("class") == ["row", "fault"]

    absent = soup.select_one("h2")

    assert absent is None

    try:
        absent.get_text()
        outcome = "worked"
    except Exception as err:
        outcome = type(err).__name__

    assert outcome == "AttributeError"

    heading = soup.select_one("h1")

    assert heading.get("href") is None

    try:
        heading["href"]
        access = "worked"
    except Exception as err:
        access = type(err).__name__

    assert access == "KeyError"

    first_value = soup.select_one("td.value").get_text(strip=True)

    assert type(first_value).__name__ == "str"
    assert first_value == "21.7"

    sloppy = BeautifulSoup(requests.get(f"{base}/sloppy.html", timeout=5).text, "html.parser")

    assert len(sloppy.select("tr.row")) == 2
    assert len(sloppy.select("tr.row")[0].select("td")) == 4

    rules = RobotFileParser()
    rules.set_url(f"{base}/robots.txt")
    rules.read()

    assert rules.can_fetch("*", urljoin(base, "/readings.html")) is True
    assert rules.can_fetch("*", urljoin(base, "/administration")) is False
    assert rules.crawl_delay("*") == 1


assert urljoin("http://x.invalid/a/b.html", "/next") == "http://x.invalid/next"
assert urljoin("http://x.invalid/a/b.html", "next") == "http://x.invalid/a/next"

"""Exercise 09 (bonus) -- A polite crawler.

Write `crawl(start, rules, delay, limit=5)`, a generator yielding one record per
reading across both pages. It has to do all of this:

  - refuse a URL that `robots.txt` forbids, by raising your `ScrapeError`
  - send a `User-Agent` that says who you are
  - `raise_for_status()` on every response
  - check that `#readings` is there and that each row has three cells
  - follow `a.next` with `urljoin`, and stop when there is no next link
  - not fetch the same URL twice, and not exceed `limit` pages
  - sleep `delay` between pages

Expected output:

    5
    ['TH-01', 'TH-02', 'TH-04', 'TH-07', 'TH-09']
    ['TH-04', 'TH-02']
    91.0
    ScrapeError

Hint: a `while url and url not in seen and len(seen) < limit:` loop is the whole
structure. Yield a dict per row -- exercise 04 built one. The last line comes from
calling `crawl` on `/private/secret`, which robots.txt forbids; `list(...)` is needed
to make a generator actually run (module 13).
"""

import sys
import time
from pathlib import Path
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from server import serve  # noqa: E402

HEADERS = {"User-Agent": "sensor-coursework/1.0 (student project; you@example.org)"}


# TODO: the exception class and the crawl generator


with serve() as base:
    rules = RobotFileParser()
    rules.set_url(f"{base}/robots.txt")
    rules.read()
    records = list(crawl(f"{base}/readings.html", rules, delay=0.05))

print(len(records))
print(sorted(r["tag"] for r in records))
print([r["tag"] for r in records if r["fault"]])
print(round(max(r["value"] for r in records), 1))

with serve() as base:
    rules = RobotFileParser()
    rules.set_url(f"{base}/robots.txt")
    rules.read()
    try:
        list(crawl(f"{base}/private/secret", rules, delay=0))
    except ScrapeError as err:
        print(type(err).__name__)

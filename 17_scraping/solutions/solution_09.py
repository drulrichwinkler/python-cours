"""Solution 09 (bonus) -- A polite crawler."""

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


class ScrapeError(Exception):
    """Raised when a page is not shaped the way the crawler expects."""


def crawl(start, rules, delay, limit=5):
    """Follow a.next from `start`, yielding one record per reading."""
    url = start
    seen = set()

    while url and url not in seen and len(seen) < limit:
        if not rules.can_fetch(HEADERS["User-Agent"], url):
            raise ScrapeError(f"robots.txt forbids {url}")

        seen.add(url)
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.select_one("#readings")
        if table is None:
            raise ScrapeError(f"no #readings table at {url}")

        for row in table.select("tr.row"):
            cells = row.select("td")
            if len(cells) != 3:
                raise ScrapeError(f"row has {len(cells)} cells, expected 3")
            yield {
                "tag": cells[0].get_text(strip=True),
                "value": float(cells[1].get_text(strip=True)),
                "fault": "fault" in row.get("class", []),
            }

        link = soup.select_one("a.next")
        url = urljoin(url, link["href"]) if link else None
        if url:
            time.sleep(delay)  # the site asked for this in robots.txt


with serve() as base:
    rules = RobotFileParser()
    rules.set_url(f"{base}/robots.txt")
    rules.read()

    # The site asks for 1 second. Honour it -- scaled down here so the test is
    # quick, which is a shortcut a coursework fixture may take and you may not.
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

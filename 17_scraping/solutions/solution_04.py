"""Solution 04 -- A table into records."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from server import serve  # noqa: E402

with serve() as base:
    soup = BeautifulSoup(requests.get(f"{base}/readings.html", timeout=5).text, "html.parser")

records = []
for row in soup.select("tr.row"):
    records.append(
        {
            # By class, not by position: this survives a column being inserted.
            "tag": row.select_one("td.tag").get_text(strip=True),
            "value": float(row.select_one("td.value").get_text(strip=True)),
            # .get("class") is a LIST -- an element can have several classes.
            "fault": "fault" in row.get("class", []),
        }
    )

for record in records:
    print(record)

print([r["tag"] for r in records if r["fault"]])
print(round(sum(r["value"] for r in records) / len(records), 2))

"""Solution 09 (bonus) -- The whole chain, and a fault report."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from server import serve  # noqa: E402


def faults_from_json(base, limit):
    """(tag, value) for every reading above `limit`, straight from the API."""
    response = requests.get(f"{base}/readings.json", timeout=10)
    response.raise_for_status()
    payload = response.json()  # JSON carries types: value is already a float
    return [(r["tag"], r["value"]) for r in payload["readings"] if r["value"] > limit]


def faults_from_csv(base, limit):
    """The same answer from the CSV route, where everything is a string."""
    response = requests.get(f"{base}/unlabelled.csv", timeout=10)
    response.raise_for_status()
    text = response.content.decode("utf-8")  # do not trust the missing charset

    out = []
    for line in text.splitlines()[1:]:
        tag, raw, _unit = line.split(";")
        if float(raw) > limit:  # a CSV gives strings; convert before comparing
            out.append((tag, float(raw)))
    return out


with serve() as base:
    print(faults_from_json(base, 85.0))
    print(faults_from_csv(base, 85.0))
    print(faults_from_json(base, 85.0) == faults_from_csv(base, 85.0))

    response = requests.get(f"{base}/readings.json", timeout=10)
    print(
        type(response.content).__name__,
        "->",
        type(response.text).__name__,
        "->",
        type(response.json()).__name__,
    )

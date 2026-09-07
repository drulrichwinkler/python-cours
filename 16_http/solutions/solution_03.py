"""Solution 03 -- Repair a request that trusts too much."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from server import serve  # noqa: E402


def fetch_readings(url):
    """Fetch the JSON payload, or raise."""
    # Three things were missing: a timeout (without one the call waits forever),
    # raise_for_status (a 404 or 500 otherwise reaches .json() and the traceback
    # is about JSON rather than about the server), and the status check has to
    # happen before the body is parsed.
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


with serve() as base:
    print(sorted(fetch_readings(f"{base}/readings.json")))

    try:
        fetch_readings(f"{base}/missing")
    except requests.HTTPError as err:
        print(type(err).__name__, err.response.status_code)

    try:
        fetch_readings(f"{base}/broken")
    except requests.HTTPError as err:
        print(type(err).__name__, err.response.status_code)

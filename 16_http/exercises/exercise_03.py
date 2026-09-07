"""Exercise 03 -- Repair a request that trusts too much.

`fetch_readings` works against the good route and does the wrong thing against both
bad ones. Run it: the traceback you get for `/missing` is about JSON, which is a lie
about what went wrong.

Three things are missing. Two are on the request line and one is a line of its own.

Expected output:

    ['readings', 'station']
    HTTPError 404
    HTTPError 500

Hint: what happens if the server never answers? What turns a 404 into an exception,
and does it have to happen before or after the body is parsed? `err.response` is the
response that failed, so `err.response.status_code` is the number.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from server import serve  # noqa: E402


def fetch_readings(url):
    """Fetch the JSON payload, or raise."""
    response = requests.get(url)  # TODO: two things missing here
    # TODO: and one line missing here
    return response.json()


with serve() as base:
    print(sorted(fetch_readings(f"{base}/readings.json")))

    for path in ("/missing", "/broken"):
        try:
            fetch_readings(f"{base}{path}")
        except requests.HTTPError as err:
            print(type(err).__name__, err.response.status_code)

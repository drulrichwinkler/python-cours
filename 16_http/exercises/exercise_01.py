"""Exercise 01 -- One request, read four ways.

Fetch `/readings.csv` from the local server and print five lines:

  1. the status code and the reason, separated by a space
  2. the Content-Type header
  3. the byte count and the code point count, as in the expected output
  4. the second line of the body -- the first reading
  5. the type names of `.content` and `.text`, separated by a space

Expected output:

    200 OK
    text/csv; charset=utf-8
    60 bytes 57 code points
    TH-01;21.7;°C
    bytes str

Hint: `requests.get(url, timeout=5)` -- always with a timeout. `response.reason` is
the text beside the code. Line 3 is module 07's arithmetic on something that came off
a socket: three `°` in the file, one extra byte each.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # so that `import server` finds it -- module 10

import requests  # noqa: E402
from server import serve  # noqa: E402

# TODO: the request inside `with serve() as base:`, then five prints

"""Exercise 05 -- Two kinds of failure.

Write `describe(call)`, which runs a request and returns a string saying what came
out. `call` is a function of no arguments that makes the request, so that `describe`
can be given several different ones.

  - the server answered and the answer was fine -> `ok ` and the status code
  - the server answered and the answer was bad  -> `HTTPError ` and the status code
  - no answer within the timeout                -> `Timeout`
  - nobody answered at all                      -> `ConnectionError`

Expected output:

    ok 200
    HTTPError 404
    HTTPError 500
    Timeout
    ConnectionError
    True

Hint: `raise_for_status()` inside the try is what produces the HTTPError. The three
exception classes are `requests.HTTPError`, `requests.Timeout` and
`requests.ConnectionError`, and the order of the `except` clauses matters only if one
is a parent of another -- module 09. The last line is
`issubclass(requests.HTTPError, requests.RequestException)`.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from server import serve  # noqa: E402

# TODO: write describe


with serve() as base:
    print(describe(lambda: requests.get(f"{base}/readings.csv", timeout=5)))
    print(describe(lambda: requests.get(f"{base}/missing", timeout=5)))
    print(describe(lambda: requests.get(f"{base}/broken", timeout=5)))
    print(describe(lambda: requests.get(f"{base}/slow", timeout=0.2)))

print(describe(lambda: requests.get("http://127.0.0.1:1/x", timeout=0.5)))
print(issubclass(requests.HTTPError, requests.RequestException))

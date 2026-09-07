"""Solution 05 -- Two kinds of failure."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from server import serve  # noqa: E402


def describe(call):
    """Run a request and say which kind of failure came out, if any."""
    try:
        response = call()
        response.raise_for_status()
    except requests.HTTPError as err:
        # The server answered, and the answer was bad.
        return f"HTTPError {err.response.status_code}"
    except requests.Timeout:
        # No answer within the timeout.
        return "Timeout"
    except requests.ConnectionError:
        # Nobody answered at all.
        return "ConnectionError"
    return f"ok {response.status_code}"


with serve() as base:
    print(describe(lambda: requests.get(f"{base}/readings.csv", timeout=5)))
    print(describe(lambda: requests.get(f"{base}/missing", timeout=5)))
    print(describe(lambda: requests.get(f"{base}/broken", timeout=5)))
    print(describe(lambda: requests.get(f"{base}/slow", timeout=0.2)))

print(describe(lambda: requests.get("http://127.0.0.1:1/x", timeout=0.5)))
print(issubclass(requests.HTTPError, requests.RequestException))

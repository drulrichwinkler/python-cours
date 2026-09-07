"""Solution 01 -- One request, read four ways."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # so that `import server` finds it -- module 10

import requests  # noqa: E402
from server import serve  # noqa: E402

with serve() as base:
    response = requests.get(f"{base}/readings.csv", timeout=5)

print(response.status_code, response.reason)
print(response.headers["Content-Type"])
print(len(response.content), "bytes", len(response.text), "code points")
print(response.text.splitlines()[1])
print(type(response.content).__name__, type(response.text).__name__)

"""Solution 06 -- Parameters, encoded for you."""

import requests

prepared = requests.Request(
    "GET",
    "http://example.invalid/readings",
    params={"tag": "TH 04", "unit": "°C", "limit": 85},
).prepare()

print(prepared.url)
# A space becomes + in a query string, not %20. %C2%B0 is the two UTF-8 bytes of
# ° written out -- module 07.
print("TH+04" in prepared.url, "%C2%B0" in prepared.url)

with_headers = requests.Request(
    "GET",
    "http://example.invalid/readings",
    headers={"Accept": "application/json"},
).prepare()

print(with_headers.headers["Accept"])
print(sorted(k.lower() for k in with_headers.headers))

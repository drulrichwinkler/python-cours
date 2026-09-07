"""Exercise 02 -- Reading a refusal.

A 422 body is machine-readable on purpose. Every entry in `detail` says three things:
where the bad value was (`loc`), what kind of problem it is (`type`), and a sentence
for a human (`msg`).

Make these four requests against `app.py` and print `loc[0]`, `loc[1]` and `type` of
the first entry in `detail`, separated by single spaces:

  1. GET  /faults?minimum=warm
  2. GET  /faults?minimum=999
  3. POST /limit with the body {"note": "no celsius here"}
  4. POST /limit with the body {"celsius": 500}

Then print the `msg` of the last one on its own line.

Expected output:

    query minimum float_parsing
    query minimum less_than_equal
    body celsius missing
    body celsius less_than
    Input should be less than 200

Note what `loc[0]` tells you: whether the bad value came from the query string or from
the request body. A client that reads this can highlight the right input field.

Hint: `client.post("/limit", json={...})` sends a JSON body. `loc` is a list, so
`loc[0]` and `loc[1]` are its two parts.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

client = TestClient(app)

requests = [
    ("GET", "/faults", {"minimum": "warm"}, None),
    ("GET", "/faults", {"minimum": 999}, None),
    ("POST", "/limit", None, {"note": "no celsius here"}),
    ("POST", "/limit", None, {"celsius": 500}),
]

# TODO: send each request, print the three fields, then the last msg

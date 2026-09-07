"""Solution 02 -- Reading a refusal."""

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

problem = {}
for method, path, params, body in requests:
    response = client.request(method, path, params=params, json=body)
    # detail is a list because one request can be wrong in several places at once.
    problem = response.json()["detail"][0]
    print(problem["loc"][0], problem["loc"][1], problem["type"])

print(problem["msg"])

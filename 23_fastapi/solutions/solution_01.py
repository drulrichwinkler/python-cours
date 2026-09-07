"""Solution 01 -- The annotation is the parser."""

import sys
from pathlib import Path

# append, not insert: `app` lives next to this module's solutions folder, and the
# course packages must keep priority on the path.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

client = TestClient(app)

r = client.get("/")
print(r.status_code, r.json()["locations"])

r = client.get("/summary/Hall")
print(r.status_code, f"Hall mean={r.json()['mean']}")

# No route matched a location called Keller, so `one_summary` raised
# HTTPException(404) and FastAPI turned it into this body.
r = client.get("/summary/Keller")
print(r.status_code, r.json()["detail"])

# `minimum: float` in app.py is what refuses this. The function never ran.
r = client.get("/faults", params={"minimum": "warm"})
print(r.status_code, r.json()["detail"][0]["type"])

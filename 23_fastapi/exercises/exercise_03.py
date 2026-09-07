"""Exercise 03 -- Repair: parsing by hand.

The route in this file does what a Flask view has to do: take the query parameter as
text and convert it itself. That works until somebody sends `minimum=warm`, and then
`float()` raises inside the function -- which is a 500, an entry in your log, and a
client with no idea what it did wrong.

Rewrite `above` so the framework refuses the bad value instead. When you are done, the
second request must be a 422 that names the parameter.

Expected output:

    200 3
    422 query minimum float_parsing

Two things to know before you start:

  * `TestClient` re-raises an exception from your function rather than turning it into
    a response, so the broken version does not print a 500 -- it ends the script with
    a traceback. That is deliberate: in a test you want the traceback.
    `TestClient(app, raise_server_exceptions=False)` gives you the 500 the real client
    would see.
  * The bounds are not the point here. One annotation is enough.

Hint: what type does the parameter actually have? Say so, and delete the conversion.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from sensorreport import load_readings  # noqa: E402

app = FastAPI()


@app.get("/above")
def above(minimum: str = "85"):
    """Count the readings above `minimum`."""
    # TODO: this conversion is the bug -- move the work into the signature
    limit = float(minimum)
    return {"count": sum(1 for r in load_readings() if r.value is not None and r.value > limit)}


client = TestClient(app)

first = client.get("/above")
print(first.status_code, first.json()["count"])

second = client.get("/above", params={"minimum": "warm"})
problem = second.json()["detail"][0]
print(second.status_code, problem["loc"][0], problem["loc"][1], problem["type"])

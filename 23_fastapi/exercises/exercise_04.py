"""Exercise 04 -- The return annotation is the response schema.

`-> Out` on a route does two jobs. It puts `Out` in the generated documentation, and
it validates what the function actually returned. Both directions are worth seeing.

The two routes below are written for you. Complete the four prints:

  1. the status and the body of GET /good -- which returns a dict with a third key
  2. which key of that dict did not come out, as `dropped: <key>`
  3. the name of the exception class that GET /bad raises through the test client
  4. the status a real client gets for GET /bad

Expected output:

    200 {'tag': 'TH-04', 'value': 93.5}
    dropped: secret
    ResponseValidationError
    500

The asymmetry in 3 and 4 is the point of the exercise. A bad **request** is answered
with a 422 that names the field, because the client can fix it. A bad **response** is
answered with a bare 500, because the client cannot -- it is your bug, and telling a
stranger which of your fields is missing would be telling them about your internals.

Hint: `lenient` below is a second client over the same application with
`raise_server_exceptions=False`; use it for print 4. For print 3, catch `Exception`
and use `type(exc).__name__`.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel


class Out(BaseModel):
    tag: str
    value: float


app = FastAPI()


@app.get("/good")
def good() -> Out:
    """Returns one key too many."""
    return {"tag": "TH-04", "value": 93.5, "secret": "internal note"}


@app.get("/bad")
def bad() -> Out:
    """Returns one key too few."""
    return {"tag": "TH-04"}


client = TestClient(app)
lenient = TestClient(app, raise_server_exceptions=False)

# TODO: four prints

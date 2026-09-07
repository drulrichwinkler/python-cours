"""Solution 04 -- The return annotation is the response schema."""

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

response = client.get("/good")
print(response.status_code, response.json())

returned = {"tag", "value", "secret"}
print("dropped:", *(returned - set(response.json())))

# The test client re-raises server-side exceptions, which is what you want in a
# test: the traceback names your bug.
try:
    client.get("/bad")
except Exception as exc:
    print(type(exc).__name__)

# The same request through a client that does not re-raise -- this is what a browser
# would get. No field name, no schema, nothing.
print(lenient.get("/bad").status_code)

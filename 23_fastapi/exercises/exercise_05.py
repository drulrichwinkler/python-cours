"""Exercise 05 -- Bounds in the model.

Write the model. `Sample` describes one reading a client may submit:

  * `tag`        -- a string of at least 4 characters
  * `celsius`    -- a number greater than -50 and less than 200
  * `location`   -- a string, default `"unknown"`

Then send the four bodies in `bodies` to the route below and print, one line each, the
status and either the tag that came back or the `type` of the first problem.

Expected output:

    200 TH-04
    422 string_too_short
    422 greater_than
    422 missing

`Field` is where a bound goes: `Field(gt=-50, lt=200)` for a number,
`Field(min_length=4)` for a string. A field with a default is optional; a field
without one is required, which is what produces the last line.

Hint: import `Field` from `pydantic` alongside `BaseModel`. The constraint names are
the ones from the expected output read backwards -- `string_too_short` comes from
`min_length`, `greater_than` from `gt`.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel


class Sample(BaseModel):
    """One submitted reading."""

    # TODO: three fields, with the bounds above
    ...


app = FastAPI()


@app.post("/sample")
def take(sample: Sample) -> dict[str, str]:
    """Accept a reading and answer with its tag."""
    return {"tag": sample.tag}


client = TestClient(app)

bodies = [
    {"tag": "TH-04", "celsius": 93.5},
    {"tag": "TH", "celsius": 93.5},
    {"tag": "TH-04", "celsius": -99},
    {"celsius": 20},
]

# TODO: send each body, print status and tag or problem type

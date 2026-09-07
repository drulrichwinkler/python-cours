"""Exercise 09 -- One route, everything at once.

Write a route that uses all four things this module introduced: a path parameter, a
query parameter with a bound, a response model, and a 404.

`GET /location/{name}` must answer with an object of the model `LocationOut`:

  * `name`     -- the location
  * `above`    -- how many of its readings are above `minimum`
  * `worst`    -- the highest value it has, or `None` if it has no usable reading

`minimum` is an optional query parameter, a float, default `85.0`, and no smaller than
`-50`. A name that is not in the data must give a 404 whose `detail` reads
`no location '<name>'`.

Expected output:

    200 Test rig above=3 worst=93.5
    200 Test rig above=20 worst=93.5
    200 Hall above=0 worst=23.9
    404 no location 'Keller'
    422 greater_than_equal

The prints at the bottom are written for you -- do not change them. Write the model
and the route.

Hint: the readings of one location are
`[r for r in load_readings() if r.location == name]`. `max` over an empty sequence
raises, so the `None` case needs handling before it. For the bound, `Query(default=85.0,
ge=-50)` -- and remember that a `Query(...)` default still makes the parameter optional.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI, HTTPException, Query  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from pydantic import BaseModel  # noqa: E402

from sensorreport import load_readings  # noqa: E402

app = FastAPI()


# TODO: the model LocationOut


# TODO: the route GET /location/{name}


client = TestClient(app)

for path, params in [
    ("/location/Test rig", None),
    ("/location/Test rig", {"minimum": 0}),
    ("/location/Hall", None),
    ("/location/Keller", None),
    ("/location/Hall", {"minimum": -99}),
]:
    r = client.get(path, params=params)
    if r.status_code == 200:
        body = r.json()
        print(r.status_code, f"{body['name']} above={body['above']} worst={body['worst']}")
    elif r.status_code == 404:
        print(r.status_code, r.json()["detail"])
    else:
        print(r.status_code, r.json()["detail"][0]["type"])

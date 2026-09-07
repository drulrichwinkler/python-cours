"""Exercise 06 -- url_for, and never joining strings.

Two routes, then four URLs built with `url_for`:

  1. `location` with `name="Hall"`
  2. `location` with `name="Test rig"` -- look at what happened to the space
  3. `search` with `above=85`
  4. `search` with `above=85` and `unit="C"`

Expected output:

    /location/Hall
    /location/Test%20rig
    /search?above=85
    /search?above=85&unit=C

Hint: `url_for` takes the **name of the view function**, not a path, which is why
renaming the route later does not break the links. Lines 3 and 4 show what happens to
an argument the route has no placeholder for. `url_for` needs a request context
outside a real request: `with app.test_request_context():`.
"""

from flask import Flask, url_for

app = Flask(__name__)

# TODO: two routes, then four prints

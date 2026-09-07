"""Exercise 01 -- A route is a decorated function.

Build a Flask app with three routes and test it with `test_client()` -- no port, no
process, no `app.run()`.

  - `/`        returns the string `<h1>Sensors</h1>`
  - `/json`    returns the dict `{"tag": "TH-04", "value": 91.0}`
  - `/created` returns the string `made it` with status 201

Then print: the status and the content type (before the semicolon) of each, the body
of `/`, the parsed JSON of `/json`, and the status of a route that does not exist.

Expected output:

    200 text/html
    200 application/json
    201 text/html
    <h1>Sensors</h1>
    {'tag': 'TH-04', 'value': 91.0}
    404

Hint: `@app.get(path)` above each function -- a decorator, module 14. A returned dict
becomes JSON by itself; a returned tuple is `(body, status)`.
`response.headers["Content-Type"].split(";")[0]` drops the charset.
"""

from flask import Flask

app = Flask(__name__)

# TODO: three routes, then the test_client block

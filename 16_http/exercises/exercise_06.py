"""Exercise 06 -- Parameters, encoded for you.

No server here: `requests.Request(...).prepare()` builds the request without sending
it, which is how you look at what would have gone out.

Build a prepared GET to `http://example.invalid/readings` with the parameters
`tag="TH 04"`, `unit="°C"` and `limit=85`, and print its URL. Then check two things
about that URL, then build a second one with an `Accept: application/json` header and
print the header back.

Expected output:

    http://example.invalid/readings?tag=TH+04&unit=%C2%B0C&limit=85
    True True
    application/json
    ['accept']

Hint: read the URL before you write line 2 -- the space did not become `%20`. The
last line is the header names lowercased and sorted, which shows that
`prepared.headers` holds exactly what you put there.
"""

import requests

# TODO: two prepared requests and four prints

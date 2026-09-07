"""Exercise 09 (bonus) -- The whole application, tested.

`app.py` one folder up is the finished application. Write `describe(client, path)`
returning the status code and the content type without its charset, then print a line
per path -- the path padded to 22, the status in a field of 5, a space, the type.

Then a blank line and three more lines:

  - whether `Test%20rig` and whether `Nowhere` appear in the body of `/`
  - the limit and how many locations `/api/summary` reports
  - the fault counts from that payload, as a list

Expected output:

    /                       200 text/html
    /location/Hall          200 text/html
    /location/Nowhere       404 text/html
    /search?above=85        200 text/html
    /api/summary            200 application/json

    True False
    85.0 3
    [0, 0, 3]

Hint: `sys.path.append(str(MODULE))` then `import app`. `Test%20rig` is in the page
because the template built that link with `url_for` -- which is the encoding of module
16, done for you. The fault counts are the same three numbers as modules 18, 19 and
20.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # so that `import app` finds it -- module 10

import app as flask_app  # noqa: E402

# TODO: describe, then the loop and three prints

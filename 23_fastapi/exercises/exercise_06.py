"""Exercise 06 -- The document nobody wrote.

`GET /openapi.json` answers with a description of the whole application: every path,
every parameter, every schema, every bound. It is not a file in this repository. It is
built from `app.py` when you ask for it, which means it cannot fall behind the code.

Read it and print six lines about `app.py`:

  1. how many paths it has, as `<n> paths`
  2. the one path that has a `post`, and the method, separated by a space
  3. `LimitIn requires <the required list>`
  4. the two bounds on `LimitIn.celsius`, as
     `celsius exclusiveMinimum=<x> exclusiveMaximum=<y>`
  5. `/summary/{location} -> <the schema name it answers with>`
  6. `documented statuses: <the sorted status codes of GET /summary/{location}>`

Expected output:

    6 paths
    /limit post
    LimitIn requires ['celsius']
    celsius exclusiveMinimum=-50.0 exclusiveMaximum=200.0
    /summary/{location} -> SummaryOut
    documented statuses: ['200', '422']

Line 6 is worth a second look once you have it. `one_summary` in `app.py` raises a 404
as well, and the document does not mention it. Exercise 08 asks you why.

Hint: the document is a plain dict. `spec["paths"]` maps a path to a dict of methods;
`spec["components"]["schemas"]` holds the models. The answer schema of a route sits at
`spec["paths"][path]["get"]["responses"]["200"]["content"]["application/json"]["schema"]`
and is a `$ref` string like `#/components/schemas/SummaryOut` -- the name is what
follows the last slash.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

spec = TestClient(app).get("/openapi.json").json()

# TODO: six prints

"""Exercise 01 -- The annotation is the parser.

`app.py` next to this file is the application. Import it and make four requests with
`TestClient`, printing one line each:

  1. GET /            -- the status and the `locations` list
  2. GET /summary/Hall -- the status and `Hall mean=<the mean>`
  3. GET /summary/Keller -- the status and the `detail` string
  4. GET /faults?minimum=warm -- the status and the `type` of the first entry in `detail`

Expected output:

    200 ['Hall', 'Office', 'Test rig']
    200 Hall mean=22.12
    404 no location 'Keller'
    422 float_parsing

Nothing here starts a server. `TestClient(app)` calls the application in this process --
module 15's argument, and the same shape as Flask's `test_client()` in module 21.

Hint: `client.get("/")` returns a response with `.status_code` and `.json()`. The 422
body is `{"detail": [{...}, ...]}`, so the first entry is `r.json()["detail"][0]`.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

client = TestClient(app)

# TODO: four requests, four prints

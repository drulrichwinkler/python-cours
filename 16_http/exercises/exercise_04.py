"""Exercise 04 -- The encoding nobody declared.

`/readings.csv` and `/unlabelled.csv` send **the same bytes**. One labels them
`charset=utf-8`, the other says only `text/csv`. Print six lines:

  1. whether the two bodies are byte-for-byte identical
  2. the two encodings, separated by a space
  3. the second line of the unlabelled body, as a repr
  4. the same line after you have told the response the truth
  5. the same line again, by decoding `.content` yourself

Expected output:

    True
    utf-8 ISO-8859-1
    'TH-01;21.7;Â°C'
    'TH-01;21.7;°C'
    'TH-01;21.7;°C'

Hint: `response.encoding = "utf-8"` has to happen before `.text` is read. The last
line skips `.text` entirely -- `.content.decode("utf-8")` -- which is the honest
version of the same thing and the one module 08 would have written.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from server import serve  # noqa: E402

# TODO: two requests and five prints

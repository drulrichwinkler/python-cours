"""Exercise 06 -- Limits out of JSON.

`data/limits.json` has a default limit and an entry for some sensors. Write
`high_for(tag)` returning that sensor's own high limit if it has one, and the
default otherwise. Then print four things:

  1. the limit for TH-04, which has its own
  2. the limit for TH-01, which does not
  3. the unit and the type name of the value under "strict", separated by a space
  4. the tags that have their own entry, sorted

Expected output:

    95.0
    85.0
    C bool
    ['TH-02', 'TH-04']

Hint: `json.loads(path.read_text(encoding="utf-8"))` gives you a dict. `.get(tag,
fallback)` is the whole lookup -- module 06. `type(x).__name__` is the name of a
type as a string.
"""

import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# TODO: load the file, write the function, four prints

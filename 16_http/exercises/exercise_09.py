"""Exercise 09 (bonus) -- The same answer from JSON and from CSV.

Two functions, both returning `[(tag, value)]` for every reading above `limit`:

  - `faults_from_json(base, limit)` -- from `/readings.json`, where the values are
    already floats
  - `faults_from_csv(base, limit)` -- from `/unlabelled.csv`, where everything is a
    string **and** the charset is not declared

Then print both, whether they agree, and the three type names of the chain.

Expected output:

    [('TH-04', 91.0)]
    [('TH-04', 91.0)]
    True
    bytes -> str -> dict

Hint: both functions need `raise_for_status()`. The CSV one must not trust
`.text` -- `/unlabelled.csv` is the route with no charset, so decode `.content`
yourself. Skip the header line, split on ";", and convert before comparing.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from server import serve  # noqa: E402

# TODO: the two functions, then four prints

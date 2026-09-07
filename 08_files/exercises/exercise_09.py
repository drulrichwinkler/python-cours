"""Exercise 09 (bonus) -- The CSV against the JSON.

Write `faults(csv_path, json_path)` returning a list of `(tag, value)` pairs for
every reading that is above **that sensor's own** high limit -- the one from
`limits.json` if it has an entry, the default otherwise. The value in the pair is a
float.

Watch the result: the highest reading in the file is not a fault, because that
sensor is allowed to run hotter.

Expected output:

    [('TH-02', 88.4)]
    1 of 5

Hint: load the JSON once, then loop the CSV records. `limits["sensors"].get(tag,
limits["default"])["high"]` is the lookup. The CSV gives strings, so convert before
comparing.
"""

import csv
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


# TODO: write the function


result = faults(DATA / "sensors.csv", DATA / "limits.json")

print(result)
print(len(result), "of 5")

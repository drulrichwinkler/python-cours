"""Solution 06 -- One test over a table."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: the check runs this file with a
# broken copy of sensorlib on PYTHONPATH, and insert(0, ...) would shadow it

from sensorlib.parsing import parse_line, readings_above  # noqa: E402

CASES = [
    ("TH-04;91.0", ("TH-04", 91.0)),
    ("  TH-04;91.0\n", ("TH-04", 91.0)),
    ("TH-04;-20", ("TH-04", -20.0)),
    ("TH-04;0", ("TH-04", 0.0)),
]

# Under pytest this is @pytest.mark.parametrize and each row is its own test with
# its own name. Here the loop stands in for the runner.
for line, expected in CASES:
    assert parse_line(line) == expected, line
print(len(CASES), "rows passed")

LIMITS = [(84.9, 1), (85.0, 0), (85.1, 0)]

for limit, count in LIMITS:
    assert len(readings_above([("TH-04", 85.0)], limit)) == count, limit
print(len(LIMITS), "boundary rows passed")

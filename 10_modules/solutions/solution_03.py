"""Solution 03 -- Repair the path."""

import sys
from pathlib import Path

# .parent once is 10_modules/solutions -- sensorlib is not in there. Twice is
# 10_modules, which is the folder sensorlib actually sits in.
MODULE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(MODULE))

from sensorlib.parsing import ParseError, to_reading  # noqa: E402

print(to_reading("23.1"))

try:
    to_reading("n/a")
except ParseError as err:
    print(type(err).__name__, "-", err)

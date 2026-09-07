"""Exercise 06 -- One test over a table.

Two tables, each checked in a loop. Under pytest these would be
`@pytest.mark.parametrize` and each row would be its own test; here the loop
stands in for the runner.

  - `CASES`: four `(line, expected)` rows for `parse_line`, covering a plain
    line, one with surrounding whitespace, a negative value and a zero
  - `LIMITS`: three `(limit, count)` rows for `readings_above` with the single
    reading `("TH-04", 85.0)` -- one limit below it, one exactly at it, one above

Then print how many rows passed, as below.

Expected output:

    4 rows passed
    3 boundary rows passed

Hint: put the expected value in the row, not in the loop body. Give each assert
a message naming the row, so a failure says which one -- that is what pytest's
per-row names do for you. The middle row of LIMITS is the interesting one: the
function promises **strictly** above.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: the check runs this file with a
# broken copy of sensorlib on PYTHONPATH, and insert(0, ...) would shadow it

from sensorlib.parsing import parse_line, readings_above  # noqa: E402

# TODO: CASES, the loop, LIMITS, the second loop

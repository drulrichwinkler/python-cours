"""Solution 01 -- What an assert says, and what pytest makes of it."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: the check runs this file with a
# broken copy of sensorlib on PYTHONPATH, and insert(0, ...) would shadow it

from sensorlib.parsing import mean, parse_line  # noqa: E402

# A bare assert carries nothing: the AssertionError has an empty message. That is
# why JUnit needs assertEquals, and why pytest rewrites assertions instead.
try:
    assert mean([1.0, 2.0]) == 2.0
except AssertionError as err:
    print("message:", repr(str(err)))

# An assert with a message of your own. Useful outside pytest; unnecessary inside
# it, because the rewriting already shows the values.
try:
    assert mean([1.0, 2.0]) == 2.0, f"mean was {mean([1.0, 2.0])}"
except AssertionError as err:
    print("with a message:", err)

print(parse_line("TH-04;91.0"))
print(mean([1.0, 2.0, 3.0]))

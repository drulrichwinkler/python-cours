"""Exercise 04 -- Floats in a test.

Print five lines, in this order:

  1. `0.1 + 0.2 == 0.3` -- the comparison a test must not make
  2. the same thing through `pytest.approx`
  3. `mean([0.1, 0.2])` against 0.15, through approx
  4. `[0.1 + 0.2, 1.0]` against `[0.3, 1.0]` -- approx works on a list
  5. `mean([1.0, 3.0]) == 2.0`, without approx, because this one is exact

Expected output:

    False
    True
    True
    True
    True

Hint: `pytest.approx` goes on the right-hand side of `==`. Line 5 is the other
half of the rule: a value that comes out exact does not need a tolerance, and
wrapping everything in approx hides the cases where you should have thought about
it.
"""

import sys
from pathlib import Path

import pytest

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: the check runs this file with a
# broken copy of sensorlib on PYTHONPATH, and insert(0, ...) would shadow it

from sensorlib.parsing import mean  # noqa: E402

# TODO: five prints

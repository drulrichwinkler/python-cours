"""Exercise 01 -- Use the package.

`sensorlib/` sits one folder up from this file. Import it and print four lines:

  1. the package's VERSION
  2. `to_reading("21.7")`
  3. `is_fault(91.0)` and `is_fault(21.7)`, separated by a space
  4. the package's `__all__`

The first line of the output is not yours: `sensorlib/limits.py` prints it when it is
first imported, and that is the point of section 1.

Expected output:

    [sensorlib.limits imported]
    1.0
    21.7
    True False
    ['ParseError', 'VERSION', 'to_reading']

Hint: `sensorlib.VERSION` and `sensorlib.to_reading` come from the package itself --
its `__init__.py` re-exports them. `is_fault` lives in `sensorlib.limits`, so it needs
its own import.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(MODULE))  # so that `import sensorlib` finds it

# TODO: the imports, then four prints

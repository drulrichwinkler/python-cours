"""Exercise 04 -- The main guard.

Write `main()`, which checks three readings against the limit and prints two lines:
how many were checked, and the list of those that were faults. Then print
`__name__ is ` and the value of `__name__` -- unconditionally, so it happens on an
import too -- and call `main()` only when this file is the one that was started.

Expected output:

    [sensorlib.limits imported]
    __name__ is __main__
    checked 3
    faults [91.0]

Hint: `if __name__ == "__main__":` is the whole test. Note the order of the output:
the `print` of `__name__` is above the guard, so it runs either way; everything
`main` prints happens inside it.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(MODULE))

from sensorlib.limits import is_fault  # noqa: E402

readings = [21.7, 91.0, 23.1]

# TODO: the function, the print, and the guard

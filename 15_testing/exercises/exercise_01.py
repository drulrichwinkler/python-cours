"""Exercise 01 -- What an assert says, and what pytest makes of it.

`mean([1.0, 2.0])` is 1.5, so the assertion below is false. Catch the
`AssertionError` and print four lines:

  1. `message:` and the repr of the exception's message
  2. `with a message:` and the exception, from a second assert that carries a
     message of your own naming the actual value
  3. `parse_line("TH-04;91.0")`
  4. `mean([1.0, 2.0, 3.0])`

Expected output:

    message: ''
    with a message: mean was 1.5
    ('TH-04', 91.0)
    2.0

Hint: `assert condition, "text"` attaches the message. Line 1 is the reason JUnit
needs `assertEquals` -- a bare assert carries nothing, and pytest solves it by
rewriting the assertion rather than by giving you a family of methods.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: the check runs this file with a
# broken copy of sensorlib on PYTHONPATH, and insert(0, ...) would shadow it

from sensorlib.parsing import mean, parse_line  # noqa: E402

# TODO: two try/except blocks and two prints

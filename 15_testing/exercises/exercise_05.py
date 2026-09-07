"""Exercise 05 -- Testing that something raises.

Four blocks, printing three lines in total:

  1. `pytest.raises(ParseError)` around `parse_line("TH-04;n/a")`, capturing it
     `as info` -- then print the exception's class name
  2. print whether `n/a` appears in the message
  3. the same demand in one line, with `match="two fields"`, around
     `parse_line("TH-04")` -- this one prints nothing
  4. `pytest.raises(ValueError)` around `mean([])` -- also silent
  5. finally: what `pytest.raises` itself does when the block does **not** raise.
     Wrap it in a try/except and print the class name and the exception.

Expected output:

    ParseError
    True
    Failed - DID NOT RAISE ParseError

Hint: `info.value` is the exception object. For the last one, note that what
`pytest.raises` throws is not an `Exception` subclass, so `except Exception`
will not catch it -- `except BaseException` will.
"""

import sys
from pathlib import Path

import pytest

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: the check runs this file with a
# broken copy of sensorlib on PYTHONPATH, and insert(0, ...) would shadow it

from sensorlib.parsing import ParseError, mean, parse_line  # noqa: E402

# TODO: the four blocks

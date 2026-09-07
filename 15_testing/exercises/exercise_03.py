"""Exercise 03 -- Repair three tests that cannot fail.

All three tests below pass. All three would also pass against broken code, which
means none of them demands anything.

Rewrite each one so that it demands what its name says. The check for this exercise
is not the printed line: it runs your file against the three broken copies of the
library in `mutants/`, and each one has to make your file fail. It names the ones
that got past you.

Expected output:

    three tests, and each one now demands something

Hint: one test asserts something true of any list. One catches the exception it was
supposed to be demanding, so nothing is asserted at all -- `pytest.raises` is the
tool. One asserts a value is truthy, which almost any wrong implementation would
satisfy; the interesting input is the one the docstring in `sensorlib/parsing.py`
says raises. Read that file: every promise in it is something a test can hold it to.
"""

import sys
from pathlib import Path

import pytest  # noqa: F401 -- you will need this

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: the check runs this file with a
# broken copy of sensorlib on PYTHONPATH, and insert(0, ...) would shadow it

from sensorlib.parsing import ParseError, mean, parse_line, readings_above  # noqa: E402


def test_readings_above_is_strict_at_the_limit():
    # TODO: what does the docstring promise at exactly the limit?
    assert readings_above([("TH-04", 85.0)], 85.0) is not None


def test_parse_line_rejects_an_empty_tag():
    # TODO: this asserts nothing at all
    try:
        parse_line(";91.0")
    except ParseError:
        pass


def test_mean_of_nothing_raises():
    # TODO: the name says "of nothing", and the input is not nothing
    assert mean([1.0, 2.0, 3.0])


test_readings_above_is_strict_at_the_limit()
test_parse_line_rejects_an_empty_tag()
test_mean_of_nothing_raises()
print("three tests, and each one now demands something")

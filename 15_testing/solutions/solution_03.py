"""Solution 03 -- Repair three tests that cannot fail."""

import sys
from pathlib import Path

import pytest

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: the check runs this file with a
# broken copy of sensorlib on PYTHONPATH, and insert(0, ...) would shadow it

from sensorlib.parsing import ParseError, mean, parse_line, readings_above  # noqa: E402


def test_readings_above_is_strict_at_the_limit():
    # Was `assert readings_above(...) is not None`, which is true of any list --
    # including the empty one that a `>=` implementation would return here.
    assert readings_above([("TH-04", 85.0)], 85.0) == []


def test_parse_line_rejects_an_empty_tag():
    # Was a try/except that swallowed the exception and asserted nothing, so it
    # passed whether the code raised or not.
    with pytest.raises(ParseError):
        parse_line(";91.0")


def test_mean_of_nothing_raises():
    # Was `assert mean([1.0, 2.0, 3.0])`, true of almost any wrong implementation.
    # The edge is the empty sequence, and the promise is that it raises.
    with pytest.raises(ValueError):
        mean([])


test_readings_above_is_strict_at_the_limit()
test_parse_line_rejects_an_empty_tag()
test_mean_of_nothing_raises()
print("three tests, and each one now demands something")

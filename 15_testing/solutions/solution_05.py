"""Solution 05 -- Testing that something raises."""

import sys
from pathlib import Path

import pytest

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: see tests/test_exercise_03.py

from sensorlib.parsing import ParseError, mean, parse_line  # noqa: E402

with pytest.raises(ParseError) as info:
    parse_line("TH-04;n/a")
print(type(info.value).__name__)
print("n/a" in str(info.value))

# match= is a regular expression against the message, in one line.
with pytest.raises(ParseError, match="two fields"):
    parse_line("TH-04")

with pytest.raises(ValueError):
    mean([])

# When the block does not raise, pytest.raises fails the test itself.
try:
    with pytest.raises(ParseError):
        parse_line("TH-04;91.0")
except BaseException as err:  # noqa: BLE001
    print(type(err).__name__, "-", err)

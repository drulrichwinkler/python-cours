"""Exercise 02 -- Predict what pytest does.

Replace each `...` with the value you expect, then run the file.

    uv run 15_testing/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

import sys
from pathlib import Path

import pytest

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: see tests/test_exercise_03.py

from sensorlib.parsing import ParseError, mean, parse_line, readings_above  # noqa: E402

# TODO: what does a bare assert carry?
try:
    assert 1 == 2
    message = "no error"
except AssertionError as err:
    message = str(err)

assert message == ...


# TODO: the comparison a test must not make, and the one it should
assert (0.1 + 0.2 == 0.3) == ...
assert (0.1 + 0.2 == pytest.approx(0.3)) == ...


# TODO: approx on a whole list
assert ([0.1 + 0.2, 1.0] == pytest.approx([0.3, 1.0])) == ...


# TODO: what pytest.raises throws when the block does not raise -- and whether
# `except Exception` would catch it
with pytest.raises(ParseError):
    parse_line("TH-04;n/a")

try:
    with pytest.raises(ParseError):
        parse_line("TH-04;91.0")
    outcome = "no error"
except Exception:  # noqa: BLE001
    outcome = "caught by except Exception"
except BaseException:
    outcome = "only caught by except BaseException"

assert outcome == ...


# TODO: info.value is what, exactly?
with pytest.raises(ParseError) as info:
    parse_line("TH-04;n/a")

assert isinstance(info.value, ParseError) == ...
assert ("n/a" in str(info.value)) == ...


# TODO: and one about the code under test -- readings_above promises what at the limit?
assert readings_above([("TH-04", 85.0)], 85.0) == ...


# TODO: mean of nothing
try:
    mean([])
    empty = "returned"
except ValueError:
    empty = "ValueError"

assert empty == ...

"""Solution 02 -- Predict what pytest does.

message          is '' -- a bare assert carries no information at all. That is the
                 reason JUnit needs assertEquals, and the reason pytest rewrites
                 assertions when it imports a test file: the detail in a pytest
                 failure report is produced by the rewriting, not by the assert.
0.1 + 0.2        is not 0.3 (module 02), so the first comparison is False and the
                 approx one is True. A test that compares computed floats with ==
                 is wrong, and wrong intermittently.
approx on a list compares element by element, so it is True. It works on dicts of
                 floats too.
outcome          is 'only caught by except BaseException'. pytest.raises fails the
                 test by raising Failed, which comes off BaseException -- module
                 09's reason why `except Exception` is the one to write and a bare
                 `except:` is not. Here it means a try/except Exception around a
                 pytest.raises block cannot see the failure.
info.value       is the exception object itself, so isinstance is True and the
                 message can be checked with `in`. (info is a wrapper; info.value
                 is what was raised.)
readings_above   returns [] at exactly the limit: the docstring says strictly
                 above. That is the contract, and mutants/bug_01 is the version
                 where `>` became `>=`.
mean([])         raises ValueError. mutants/bug_03 returns 0.0 instead, which is a
                 plausible-looking wrong answer -- the kind a test has to demand.
"""

import sys
from pathlib import Path

import pytest

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: the check runs this file with a
# broken copy of sensorlib on PYTHONPATH, and insert(0, ...) would shadow it

from sensorlib.parsing import ParseError, mean, parse_line, readings_above  # noqa: E402

try:
    assert 1 == 2
    message = "no error"
except AssertionError as err:
    message = str(err)

assert message == ""


assert (0.1 + 0.2 == 0.3) is False
assert (0.1 + 0.2 == pytest.approx(0.3)) is True


assert ([0.1 + 0.2, 1.0] == pytest.approx([0.3, 1.0])) is True


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

assert outcome == "only caught by except BaseException"


with pytest.raises(ParseError) as info:
    parse_line("TH-04;n/a")

assert isinstance(info.value, ParseError) is True
assert ("n/a" in str(info.value)) is True


assert readings_above([("TH-04", 85.0)], 85.0) == []


try:
    mean([])
    empty = "returned"
except ValueError:
    empty = "ValueError"

assert empty == "ValueError"

"""Solution 04 -- Floats in a test."""

import sys
from pathlib import Path

import pytest

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # append, not insert: the check runs this file with a
# broken copy of sensorlib on PYTHONPATH, and insert(0, ...) would shadow it

from sensorlib.parsing import mean  # noqa: E402

print(0.1 + 0.2 == 0.3)
print(0.1 + 0.2 == pytest.approx(0.3))
print(mean([0.1, 0.2]) == pytest.approx(0.15))
print([0.1 + 0.2, 1.0] == pytest.approx([0.3, 1.0]))
print(mean([1.0, 3.0]) == 2.0)  # exact, so approx would be noise

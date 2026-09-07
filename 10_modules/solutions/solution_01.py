"""Solution 01 -- Use the package."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(MODULE))  # so that `import sensorlib` finds it

import sensorlib  # noqa: E402 -- the path has to be set before the import
from sensorlib.limits import is_fault  # noqa: E402

print(sensorlib.VERSION)
print(sensorlib.to_reading("21.7"))
print(is_fault(91.0), is_fault(21.7))
print(sensorlib.__all__)

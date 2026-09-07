"""Exercise 02 -- Predict what imports do.

Replace each `...` with the value you expect, then run the file.

    uv run 10_modules/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

# ruff: noqa: I001 -- the imports in this file are deliberately repeated and out of
# order, because their order and repetition is what the file is about.

import collections
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(MODULE))

# TODO: how many times does sensorlib.limits run its top-level code?
import sensorlib.limits  # noqa: E402
import sensorlib.limits  # noqa: E402, F811

assert ("sensorlib.limits" in sys.modules) == ...


# TODO: `from x import y` against `x.y` -- one object or two?
from sensorlib.parsing import to_reading  # noqa: E402
import sensorlib.parsing  # noqa: E402

assert (sensorlib.parsing.to_reading is to_reading) == ...


# TODO: what is __name__ inside an imported module, and inside this file?
assert sensorlib.parsing.__name__ == ...
assert __name__ == ...


# TODO: what does a package's __file__ point at?
assert Path(sensorlib.__file__).name == ...


# TODO: reading a missing key from a defaultdict
grouped = collections.defaultdict(list)
before = len(grouped)
grouped["TH-99"]

assert (len(grouped) - before) == ...


# TODO: and from a Counter
counts = collections.Counter(["TH-04"])

assert counts["TH-77"] == ...
assert ("TH-77" in counts) == ...

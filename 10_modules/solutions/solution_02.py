"""Solution 02 -- Predict what imports do.

sys.modules      is True, and sensorlib/limits.py printed exactly once. The second
                 import found the name already there and handed the existing module
                 object straight back -- import is a one-off, and the cache is what
                 makes it one.
to_reading       is one object. `from x import y` binds the same object that `x.y`
                 reaches; the difference is only whether the module name stays in
                 your file. (It matters later: if x rebinds y, a from-imported name
                 still points at the old object.)
__name__         inside an imported module is its dotted name, 'sensorlib.parsing'.
                 In the file that was started it is '__main__' -- which is the whole
                 of what the main guard tests.
__file__         on a package points at its __init__.py. As far as import is
                 concerned, that file IS the package.
defaultdict      gains a key: reading a missing one creates it. That is how
                 grouped[tag].append(value) works without a setdefault, and it is
                 why a lookup can change the dict.
Counter          does not. A missing key counts zero and is not inserted, so `in`
                 stays False. Two containers from the same module, two different
                 answers to the same question -- worth knowing which is which.
"""

# ruff: noqa: I001 -- the imports in this file are deliberately repeated and out of
# order, because their order and repetition is what the file is about.

import collections
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(MODULE))

import sensorlib.limits  # noqa: E402
import sensorlib.limits  # noqa: E402, F811

assert ("sensorlib.limits" in sys.modules) is True


from sensorlib.parsing import to_reading  # noqa: E402
import sensorlib.parsing  # noqa: E402

assert (sensorlib.parsing.to_reading is to_reading) is True


assert sensorlib.parsing.__name__ == "sensorlib.parsing"
assert __name__ == "__main__"


assert Path(sensorlib.__file__).name == "__init__.py"


grouped = collections.defaultdict(list)
before = len(grouped)
grouped["TH-99"]

assert (len(grouped) - before) == 1


counts = collections.Counter(["TH-04"])

assert counts["TH-77"] == 0
assert ("TH-77" in counts) is False

# Your test suite

Put one or more `test_*.py` files in this folder. They import from `sensorlib`:

```python
import pytest
from sensorlib.parsing import ParseError, mean, parse_line, readings_above
```

`uv run pytest 15_testing/tests/test_exercise_09.py` then checks two things:

1. your tests **pass** against `../../sensorlib/`, the correct version;
2. your tests **fail** against each folder in `../../mutants/`, which hold the same
   library with one thing changed each.

The second one is the point. A suite that passes everywhere tests nothing, and the
failure message names which bug got past you.

One detail about the import: your suite writes `from sensorlib.parsing import ...`
with no `sys.path` line at all. The runner puts the right directory on the import
path before it starts — the correct one on the first run, a broken one on each of the
others. That is how the same suite can be pointed at four different libraries.

Read `../../sensorlib/parsing.py` first — the docstrings are the contract, and the
bugs are all violations of something written down there.

"""Exercise 05 -- Write a report and read it back.

Write the two lines in `lines` to `report`, one per line. Then append a line
reading `end`. Then print three things:

  1. the whole file read back, as a repr so the newlines are visible
  2. whether it exists, and its name
  3. the string FileExistsError, by trying to open it again with mode "x"

Expected output:

    'TH-04;91.0\nTH-02;88.4\nend\n'
    True report.txt
    FileExistsError

Hint: `write()` takes a string and adds no newline of its own. Mode "w" truncates,
"a" appends, "x" refuses to touch a file that exists. The temporary folder is made
for you -- nothing you write here lands in the repository.
"""

import tempfile
from pathlib import Path

work = Path(tempfile.mkdtemp())
report = work / "report.txt"

lines = ["TH-04;91.0", "TH-02;88.4"]

# TODO: write, append, then three prints

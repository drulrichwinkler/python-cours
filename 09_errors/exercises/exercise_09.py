"""Exercise 09 (bonus) -- Parse, log, carry on.

Same job as exercise 01, but the rows that fail are reported rather than counted.
Write `read_values(path)` which logs one WARNING per unparseable row -- naming the
line number in the file, so the header is line 1 and the first reading is line 2 --
and one INFO at the end saying how many of how many were read.

The logger is set up for you to write into a string, so that the output can be
checked. Do not use `print` for the log lines.

Expected output:

    [21.7, 23.1, 22.8]
    WARNING readings: line 3: 'n/a' is not a reading
    WARNING readings: line 5: '' is not a reading
    INFO readings: read 3 of 5

Hint: `enumerate(reader, start=2)` numbers the rows the way the file does. Pass the
values as arguments -- `log.warning("line %d: %r is not a reading", number, raw)` --
not as an f-string: that way they are only formatted if the message is emitted.
"""

import csv
import io
import logging
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

stream = io.StringIO()
handler = logging.StreamHandler(stream)
handler.setFormatter(logging.Formatter("%(levelname)s %(name)s: %(message)s"))

log = logging.getLogger("readings")
log.handlers = [handler]
log.setLevel(logging.INFO)


# TODO: write the function


values = read_values(DATA / "readings.csv")

print(values)
print(stream.getvalue(), end="")

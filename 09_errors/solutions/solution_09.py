"""Solution 09 (bonus) -- Parse, log, carry on."""

import csv
import io
import logging
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

stream = io.StringIO()  # a log destination that can be printed, so the output is checkable
handler = logging.StreamHandler(stream)
handler.setFormatter(logging.Formatter("%(levelname)s %(name)s: %(message)s"))

log = logging.getLogger("readings")
log.handlers = [handler]
log.setLevel(logging.INFO)


def read_values(path):
    values = []
    with open(path, newline="", encoding="utf-8") as fh:
        for number, row in enumerate(csv.DictReader(fh, delimiter=";"), start=2):
            try:
                values.append(float(row["value"]))
            except ValueError:
                # Arguments rather than an f-string: they are only formatted if the
                # message is emitted at all.
                log.warning("line %d: %r is not a reading", number, row["value"])
    log.info("read %d of %d", len(values), number - 1)
    return values


values = read_values(DATA / "readings.csv")

print(values)
print(stream.getvalue(), end="")

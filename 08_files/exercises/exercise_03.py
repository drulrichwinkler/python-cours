"""Exercise 03 -- Repair a hand-rolled CSV reader.

`read_rows` splits each line on the semicolon. `data/tricky.csv` has a field with a
semicolon *inside* it, in quotes -- so one row comes back with four fields instead
of three, and the note is cut in half.

Run it, look at the row that is wrong, then rewrite the function with the `csv`
module. Do not change anything below it.

Expected output:

    3 ['tag', 'value', 'note']
    3 ['TH-04', '91.0', 'over limit; check cable']
    3 ['TH-09', '23.1', 'ok']

Hint: `csv.reader(fh, delimiter=";")` over a file opened with `newline=""`. The
quotes are handled for you, and they do not appear in the result.
"""

from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def read_rows(path):
    # TODO: the whole function is the bug -- splitting cannot see quotes
    text = path.read_text(encoding="utf-8")
    return [line.split(";") for line in text.splitlines()]


rows = read_rows(DATA / "tricky.csv")

for row in rows:
    print(len(row), row)

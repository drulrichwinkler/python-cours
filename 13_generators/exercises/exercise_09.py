"""Exercise 09 (bonus) -- Reading a log without holding it.

Two generators over a log with one unparseable line:

  - `parsed(text)`: a `(tag, value)` pair per line that converts, skipping the rest
  - `faults(pairs, limit)`: only the pairs above the limit

Then five prints, as below. Note the last two: each one walks `parsed(RAW)` again
from the beginning, which is fine because each call builds a new generator.

Expected output:

    [('TH-04', 91.0), ('TH-04', 88.4)]
    [('TH-01', 21.7), ('TH-04', 91.0)]
    246.2
    5 of 6 lines converted
    ['TH-01', 'TH-04', 'TH-09']

Hint: `line.partition(";")` returns three parts -- before, the separator, after -- so
`tag, _, raw = ...` takes it apart in one line. Grouping at the end is module 06's
`setdefault`. The sum is rounded to one decimal place.
"""

import io
import itertools

RAW = "TH-01;21.7\nTH-04;91.0\nTH-04;n/a\nTH-09;23.1\nTH-04;88.4\nTH-01;22.0\n"


# TODO: the two generators


print(list(faults(parsed(RAW), 85.0)))
print(list(itertools.islice(parsed(RAW), 2)))
print(round(sum(value for _, value in parsed(RAW)), 1))
print(len(list(parsed(RAW))), "of 6 lines converted")

by_tag = {}
for tag, value in parsed(RAW):
    by_tag.setdefault(tag, []).append(value)

print(sorted(by_tag))

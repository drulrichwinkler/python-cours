"""Solution 09 (bonus) -- Reading a log without holding it."""

import io
import itertools

RAW = "TH-01;21.7\nTH-04;91.0\nTH-04;n/a\nTH-09;23.1\nTH-04;88.4\nTH-01;22.0\n"


def parsed(text):
    """(tag, value) for every line that converts, one at a time."""
    for line in io.StringIO(text):
        tag, _, raw = line.rstrip("\n").partition(";")
        try:
            yield tag, float(raw)
        except ValueError:
            continue


def faults(pairs, limit):
    for tag, value in pairs:
        if value > limit:
            yield tag, value


print(list(faults(parsed(RAW), 85.0)))
print(list(itertools.islice(parsed(RAW), 2)))
print(round(sum(value for _, value in parsed(RAW)), 1))  # module 02: floats again
print(len(list(parsed(RAW))), "of 6 lines converted")

by_tag = {}
for tag, value in parsed(RAW):
    by_tag.setdefault(tag, []).append(value)

print(sorted(by_tag))

"""Exercise 03 -- Repair a counter.

`count_tags` is meant to return how often each tag appears. It raises instead, on
the first tag it sees.

Run it, read the error, then fix the line. Do not change anything below the
function.

Expected output:

    {'TH-04': 3, 'TH-01': 1}

Hint: `counts[tag] += 1` reads the key before it writes it. There is nothing to
read the first time. `.get(key, 0)` supplies the starting value.
"""


def count_tags(log):
    counts = {}
    for tag, _ in log:
        counts[tag] += 1  # TODO: the bug is in this line
    return counts


log = [("TH-04", 91.0), ("TH-01", 21.7), ("TH-04", 88.0), ("TH-04", 90.1)]

print(count_tags(log))

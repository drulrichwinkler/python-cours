"""Solution 06 -- Pass a function as an argument.

`sorted(seq, key=f)` calls f on every item and sorts by the results. The function
is passed as a value -- not called, so no brackets after its name.

`by_reading` and the lambda are the same object in different clothes. Give it a
name when the name explains something ("by reading"), use a lambda when it does
not. `reverse=True` beats sorting and then reversing: one pass instead of two, and
it stays stable for equal keys.
"""

log = [("TH-04", 91.0), ("TH-01", 21.7), ("TH-09", 23.1)]


def by_reading(entry: tuple[str, float]) -> float:
    """Return the reading of a log entry, for use as a sort key."""
    return entry[1]


print(sorted(log, key=lambda entry: entry[0]))
print(sorted(log, key=by_reading))
print(sorted(log, key=by_reading, reverse=True))

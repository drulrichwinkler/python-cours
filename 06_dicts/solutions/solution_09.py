"""Solution 09 (bonus) -- A report out of a log."""


def report(log, limit):
    """Return {tag: highest reading} for the tags that went above `limit`."""
    highest = {}
    for tag, value in log:
        if value > limit:
            # A tag may exceed the limit more than once; keep the worst.
            highest[tag] = max(highest.get(tag, value), value)
    return highest


log = [
    ("TH-01", 21.7),
    ("TH-04", 91.0),
    ("TH-09", 23.1),
    ("TH-04", 88.0),
    ("TH-02", 99.9),
    ("TH-01", 22.4),
]

faults = report(log, 85.0)
print(faults)
print(sorted(faults))
print(sorted(faults.keys() & {"TH-02", "TH-09"}))
print(len(log))

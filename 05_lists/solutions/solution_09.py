"""Solution 09 (bonus) -- A window out of a log."""


def report(log, window):
    """Return the faults in the last `window` entries, worst first."""
    recent = log[-window:]  # a slice is a new list -- log stays as it was
    faults = [(tag, value) for tag, value in recent if value > 85]
    return sorted(faults, key=lambda item: item[1], reverse=True)


log = [
    ("TH-01", 21.7),
    ("TH-04", 91.0),
    ("TH-09", 23.1),
    ("TH-02", 88.4),
    ("TH-07", 22.8),
    ("TH-03", 99.9),
]

print(report(log, 4))
print(report(log, 2))
print(len(log))

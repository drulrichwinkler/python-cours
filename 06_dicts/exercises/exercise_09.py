"""Exercise 09 (bonus) -- A report out of a log.

Write `report(log, limit)` returning a dict that maps each tag which went above
`limit` to its **highest** reading. Tags that stayed below do not appear. `log`
must not change.

Expected output:

    {'TH-04': 91.0, 'TH-02': 99.9}
    ['TH-02', 'TH-04']
    ['TH-02']
    6

Hint: one loop, one `if`, and one line in the body. A tag can exceed the limit more
than once, so the body has to compare against what is already in the dict --
`highest.get(tag, value)` gives you something to compare with on the first hit.
"""


# TODO: write the function

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

"""Exercise 09 (bonus) -- A window out of a log.

Write `report(log, window)` which looks at the last `window` entries of `log` and
returns the ones above 85, highest reading first. `log` itself must not change.

Expected output:

    [('TH-03', 99.9), ('TH-02', 88.4)]
    [('TH-03', 99.9)]
    6

Hint: three steps, one line each -- a slice for the window, a comprehension for the
condition, `sorted(..., key=..., reverse=True)` for the order. Unpacking the pair in
the comprehension header (`for tag, value in recent`) reads better than `item[1]`.
"""


# TODO: write the function

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

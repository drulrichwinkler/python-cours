"""Exercise 09 (bonus) -- The hourly summary.

For each hour in the log, print how many readings it holds and their average,
rounded to one decimal place. The log is already in order.

Expected output:

    14: 3 readings, avg 22.4
    15: 2 readings, avg 24.1

Hint: `for timestamp, reading in log:` unpacks each pair in the loop header, so
you never index into it. `timestamp[:2]` is the hour -- slicing is module 05, and
this is a taste of it. Collect per hour first, then print; two loops read better
here than one clever one.
"""

log = [
    ("14:05", 21.7),
    ("14:10", 23.1),
    ("14:15", 22.4),
    ("15:00", 24.0),
    ("15:30", 24.2),
]

# TODO

"""Exercise 03 -- Repair a shared default.

`add_reading` is meant to start a fresh log whenever it is called without one.
It does not: the second call continues the first one's list.

Run it, look at the output, and fix the function. Do not change the calls.

Expected output:

    [21.7]
    [23.1]
    [21.7, 99.9]

Hint: the default expression runs once, when the def runs. Default to None and
build the list inside.
"""


def add_reading(reading, log=[]):  # TODO: the bug is in this line
    log.append(reading)
    return log


first = add_reading(21.7)
print(first)
print(add_reading(23.1))
print(add_reading(99.9, first))

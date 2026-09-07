"""Exercise 05 -- A sorted copy, and the original left alone.

Write `hottest(log, count)` returning the `count` highest readings, highest first.
The caller's list must be in its original order afterwards -- the second print
proves it.

Expected output:

    [91.0, 23.1, 22.4]
    [21.7, 91.0, 22.4, 23.1, 19.4]

Hint: `log.sort()` sorts the caller's list in place and returns None. `sorted(log)`
builds a new list. One of the two is wrong here for two separate reasons.
"""


# TODO: write the function

log = [21.7, 91.0, 22.4, 23.1, 19.4]

print(hottest(log, 3))
print(log)

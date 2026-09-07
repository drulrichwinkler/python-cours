"""Solution 05 -- A sorted copy, and the original left alone."""


def hottest(log, count):
    """Return the `count` highest readings, highest first, without touching `log`."""
    # sorted() builds a new list. log.sort() would sort the caller's list in place
    # and return None -- which is exactly what this function must not do.
    return sorted(log, reverse=True)[:count]


log = [21.7, 91.0, 22.4, 23.1, 19.4]

print(hottest(log, 3))
print(log)

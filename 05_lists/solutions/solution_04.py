"""Solution 04 -- Unpacking."""


def endpoints(values):
    """Return (first, last, everything in between) for a sequence of at least two."""
    first, *middle, last = values  # * takes what is left over, always as a list
    return first, last, middle


readings = [21.7, 22.0, 22.4, 23.1, 21.9]

first, last, rest = endpoints(readings)
print(first, last)
print(rest)

a, b = "TH-04", "TH-09"
a, b = b, a
print(a, b)

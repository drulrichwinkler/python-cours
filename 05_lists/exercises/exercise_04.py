"""Exercise 04 -- Unpacking.

Write `endpoints(values)` which RETURNS three things, in this order: the first
entry, the last entry, and a list of everything in between. Take the sequence apart
in a single assignment -- no indexing, no slicing.

The two lines about `a` and `b` are a second task: swap them without a temporary
name.

Expected output:

    21.7 21.9
    [22.0, 22.4, 23.1]
    TH-09 TH-04

Hint: `first, *middle, last = values` is one assignment. The starred name collects
what is left over and is always a list, even when it collects nothing.
"""


# TODO: write the function

readings = [21.7, 22.0, 22.4, 23.1, 21.9]

low, high, rest = endpoints(readings)
print(low, high)
print(rest)

a, b = "TH-04", "TH-09"
# TODO: swap a and b in one line
print(a, b)

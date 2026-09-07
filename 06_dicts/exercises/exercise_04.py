"""Exercise 04 -- Loop over pairs, and sort by value.

Two loops over the same dict.

First: one line per entry, tag and reading, the reading to one decimal place, in
the dict's own order. Then a blank line. Then: the same entries again, highest
reading first, tag and reading separated by a space.

Expected output:

    TH-01: 21.7
    TH-04: 91.0
    TH-09: 23.1
    TH-02: 88.4

    TH-04 91.0
    TH-02 88.4
    TH-09 23.1
    TH-01 21.7

Hint: `for tag, value in readings.items()` takes the pair apart in the loop header.
For the second loop, `sorted` takes `.items()` and a `key=` that picks the second
slot of the pair -- both from module 05.
"""

readings = {"TH-01": 21.7, "TH-04": 91.0, "TH-09": 23.1, "TH-02": 88.4}

# TODO: the first loop

# TODO: the blank line and the second loop

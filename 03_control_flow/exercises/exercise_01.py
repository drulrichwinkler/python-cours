"""Exercise 01 -- Classify a reading.

A sensor reading is

    below range   under -40
    plausible     -40 to 85 inclusive
    above limit   over 85

Print the classification for each of the three readings below, one per line, in
the format shown.

Expected output:

    21.7 plausible
    -55.0 below range
    91.0 above limit

Hint: exercise 06 of module 02 asked the same question as four boolean lines,
one per group. Here you get one line per reading instead. Keep both and compare
which of the two says what you meant.
"""

# TODO: for each of these, print the reading and its classification
readings = [21.7, -55.0, 91.0]

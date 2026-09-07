"""Exercise 06 -- defaultdict, and the trap in it.

Group the readings by tag with `collections.defaultdict`, then print four lines:

  1. the result as an ordinary dict
  2. whether it is an instance of dict
  3. how many keys there were before and after reading the key "TH-99" -- just
     reading it, on a line of its own, without printing it
  4. the keys afterwards, sorted

Expected output:

    {'TH-04': [91.0, 88.0], 'TH-01': [21.7]}
    True
    2 3
    ['TH-01', 'TH-04', 'TH-99']

Hint: `defaultdict(list)` -- the argument is a function that builds the default, not
the default itself. Line 3 is the trap: reading a missing key creates it, which is
exactly how `.append` works without a `setdefault`.
"""

import collections

log = [("TH-04", 91.0), ("TH-01", 21.7), ("TH-04", 88.0)]

# TODO: group, then four prints

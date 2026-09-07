"""Exercise 05 -- Counter.

Module 06 counted with `counts[tag] = counts.get(tag, 0) + 1`. Do the same job with
`collections.Counter` and print four lines:

  1. the counter itself
  2. the single most common entry, as `most_common` returns it
  3. the count for TH-04 and the count for TH-77, separated by a space
  4. the tags, sorted

Expected output:

    Counter({'TH-04': 3, 'TH-01': 1, 'TH-09': 1})
    [('TH-04', 3)]
    3 0
    ['TH-01', 'TH-04', 'TH-09']

Hint: `Counter` takes any iterable and counts what comes out of it, so a generator
expression over the tags is the whole construction. Line 3 is worth predicting before
you run it: a `Counter` is a `dict`, and this is one of the few places one does not
raise on a missing key.
"""

import collections

log = [("TH-04", 91.0), ("TH-01", 21.7), ("TH-04", 88.0), ("TH-09", 23.1), ("TH-04", 90.2)]

# TODO: build the counter, then four prints

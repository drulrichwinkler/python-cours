"""Exercise 01 -- Read a record.

`sensor` is written for you. Print five things, one per line and in this order:

  1. the tag
  2. the high limit, out of the nested dict
  3. whether "calibrated" is a key -- as True or False
  4. the value of "calibrated", or the string unknown if there is none
  5. the keys, sorted

Expected output:

    TH-04
    85.0
    False
    unknown
    ['limits', 'tag', 'unit']

Hint: `in` on a dict asks about keys. `.get(key, default)` is the lookup that does
not raise. `sorted(d)` sorts the keys -- looping a dict gives keys, and so does
handing one to a function that wants a sequence.
"""

sensor = {
    "tag": "TH-04",
    "unit": "C",
    "limits": {"low": -20.0, "high": 85.0},
}

# TODO: five prints

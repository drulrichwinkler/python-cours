"""Exercise 09 (bonus) -- A class that holds a log.

Write `Log`, which collects readings for one tag:

  - a class attribute `unit`, "C"
  - `__init__(tag)`, with an empty list of readings
  - `add(celsius)`, which appends and returns the object, so calls can be chained
  - `highest`, a property: the largest reading, or None when there are none
  - `faults`, a property: the readings above 85, as a list
  - `from_pairs(tag, pairs)`, a classmethod building a log from (tag, value) pairs,
    taking only the pairs whose tag matches
  - a `__repr__` as in the expected output

Expected output:

    Log(tag='TH-04', readings=[91.0, 23.1])
    91.0 [91.0]
    C C
    Log(tag='TH-04', readings=[88.0, 90.2])
    None

Hint: `return self` from `add` is what makes `Log("TH-04").add(91.0).add(23.1)`
work. Line 3 shows the class attribute read through the class and through an
instance. The readings list must be per instance -- exercise 03 is the reason.
"""


# TODO: the class

log = Log("TH-04").add(91.0).add(23.1)

print(log)
print(log.highest, log.faults)
print(Log.unit, log.unit)

pairs = [("TH-04", 88.0), ("TH-01", 21.7), ("TH-04", 90.2)]
print(Log.from_pairs("TH-04", pairs))
print(Log("TH-09").highest)

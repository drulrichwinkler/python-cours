"""Exercise 09 (bonus) -- A log that is a sequence.

Put the two halves of this module together.

  - `Reading`, a frozen dataclass with a tag and a value
  - `Log`, a dataclass with a tag and a list of Readings, which
      * has `add(celsius)` appending a Reading and returning itself
      * works with `len`, with `for`, and with `in` -- where `in` asks about a
        **value**, not about a Reading
      * has a `faults` property: the Readings above 85

Expected output:

    3
    True False
    [Reading(tag='TH-04', celsius=91.0), Reading(tag='TH-04', celsius=88.4)]
    [91.0, 23.1, 88.4]
    True False
    1

Hint: `any(reading.celsius == celsius for reading in self.readings)` is the whole of
`__contains__`. The last line is the frozen dataclass in a set -- two equal Readings
are one entry.
"""


# TODO: the imports and the two classes

log = Log("TH-04").add(91.0).add(23.1).add(88.4)

print(len(log))
print(91.0 in log, 0.0 in log)
print(log.faults)
print([reading.celsius for reading in log])
print(bool(log), bool(Log("TH-09")))
print(len({Reading("TH-04", 91.0), Reading("TH-04", 91.0)}))

"""Exercise 05 -- A dataclass.

Write `Reading` as a `@dataclass` with a tag, a value in Celsius, and a unit
defaulting to "C". Add a read-only `is_fault`, true above 85.

You write no `__init__`, no `__repr__` and no `__eq__`.

Expected output:

    Reading(tag='TH-04', celsius=91.0, unit='C')
    True
    False
    True False

Hint: `from dataclasses import dataclass`, then `@dataclass` above the class. The
fields are declared by annotating them -- `tag: str` -- and this is the one place
where an annotation does something rather than merely documenting. `@property` works
exactly as it did in module 11.
"""


# TODO: the import and the class

reading = Reading("TH-04", 91.0)

print(reading)
print(reading == Reading("TH-04", 91.0))
print(reading == Reading("TH-09", 91.0))
print(reading.is_fault, Reading("TH-01", 21.7).is_fault)

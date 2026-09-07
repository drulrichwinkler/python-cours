"""Exercise 06 -- Alternative constructors.

There is no constructor overloading. Give `Reading` two `@classmethod`s that build
one a different way, and a `@staticmethod` that needs neither the instance nor the
class.

  - `from_fahrenheit(value)`
  - `from_row(row)`, taking a dict like the ones `csv.DictReader` produces
  - `unit()`, returning "C"

Expected output:

    Reading(celsius=21.7)
    Reading(celsius=100.0)
    Reading(celsius=23.1)
    C
    Precise

Hint: a classmethod's first parameter is `cls`, the class itself. Build with
`cls(...)`, not `Reading(...)` -- the last line of the output is what that
difference buys.
"""


class Reading:
    def __init__(self, celsius):
        self.celsius = celsius

    # TODO: the two classmethods and the staticmethod

    def __repr__(self):
        return f"Reading(celsius={self.celsius:.1f})"


class Precise(Reading):
    pass


print(Reading(21.7))
print(Reading.from_fahrenheit(212))
print(Reading.from_row({"value": "23.1"}))
print(Reading.unit())
print(type(Precise.from_fahrenheit(212)).__name__)

"""Solution 06 -- Alternative constructors."""


class Reading:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, value):
        # cls, not Reading: a subclass calling this gets a subclass back.
        return cls((value - 32) / 1.8)

    @classmethod
    def from_row(cls, row):
        return cls(float(row["value"]))

    @staticmethod
    def unit():
        return "C"

    def __repr__(self):
        return f"Reading(celsius={self.celsius:.1f})"


class Precise(Reading):
    pass


print(Reading(21.7))
print(Reading.from_fahrenheit(212))
print(Reading.from_row({"value": "23.1"}))
print(Reading.unit())
print(type(Precise.from_fahrenheit(212)).__name__)

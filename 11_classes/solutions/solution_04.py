"""Solution 04 -- A computed attribute."""


class Reading:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        # Read like an attribute, computed on every access -- no call site changes.
        return self.celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) / 1.8

    @property
    def is_fault(self):
        return self.celsius > 85


reading = Reading(21.7)

print(round(reading.fahrenheit, 2))
print(reading.is_fault)

reading.fahrenheit = 212
print(reading.celsius)
print(reading.is_fault)

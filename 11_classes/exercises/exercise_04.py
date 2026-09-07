"""Exercise 04 -- A computed attribute.

`Reading` holds a temperature in Celsius. Add two things that are read like
attributes and computed on access:

  - `fahrenheit`, which also accepts assignment and converts back
  - `is_fault`, read-only, true above 85

Expected output:

    71.06
    False
    100.0
    True

Hint: `@property` above the getter; `@fahrenheit.setter` above a method of the same
name for the assignment. Note there are no parentheses at any call site below --
that is the whole point of the exercise.
"""


class Reading:
    def __init__(self, celsius):
        self.celsius = celsius

    # TODO: fahrenheit, its setter, and is_fault


reading = Reading(21.7)

print(round(reading.fahrenheit, 2))
print(reading.is_fault)

reading.fahrenheit = 212
print(reading.celsius)
print(reading.is_fault)

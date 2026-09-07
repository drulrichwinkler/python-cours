"""Solution 05 -- A dataclass."""

from dataclasses import dataclass


@dataclass
class Reading:
    # The annotations are what declares the fields -- this is the one place a type
    # annotation is not merely notation.
    tag: str
    celsius: float
    unit: str = "C"

    @property
    def is_fault(self):
        return self.celsius > 85


reading = Reading("TH-04", 91.0)

print(reading)
print(reading == Reading("TH-04", 91.0))
print(reading == Reading("TH-09", 91.0))
print(reading.is_fault, Reading("TH-01", 21.7).is_fault)

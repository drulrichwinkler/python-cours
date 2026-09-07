"""Exercise 03 -- Repair a forgotten super().

Run this. It raises `AttributeError: 'Sensor' object has no attribute 'tag'` -- and
the line it names is not the line that is wrong.

Expected output:

    TH-04 in C
    ['tag', 'unit']

Hint: Java would have inserted the call for you, or refused to compile. Python does
neither, so the object was built without a tag and nothing said so until `describe`
asked for it.
"""


class Device:
    def __init__(self, tag):
        self.tag = tag


class Sensor(Device):
    def __init__(self, tag, unit):
        self.unit = unit  # TODO: something is missing above this line

    def describe(self):
        return f"{self.tag} in {self.unit}"


sensor = Sensor("TH-04", "C")

print(sensor.describe())
print(sorted(vars(sensor)))

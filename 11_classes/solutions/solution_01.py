"""Solution 01 -- A class with a repr."""


class Sensor:
    def __init__(self, tag, unit="C"):
        # These two lines CREATE the attributes. There is no declaration anywhere.
        self.tag = tag
        self.unit = unit

    def describe(self):
        return f"{self.tag} in {self.unit}"

    def __repr__(self):
        # By convention a repr looks like the expression that would rebuild the
        # object. !r puts the quotes around the strings.
        return f"Sensor(tag={self.tag!r}, unit={self.unit!r})"


sensor = Sensor("TH-04")

print(sensor.describe())
print(sensor)
print([sensor, Sensor("TH-09", "F")])
print(sensor.__dict__)

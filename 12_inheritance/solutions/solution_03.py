"""Solution 03 -- Repair a forgotten super()."""


class Device:
    def __init__(self, tag):
        self.tag = tag


class Sensor(Device):
    def __init__(self, tag, unit):
        # The parent's __init__ does not run unless it is called. Without this
        # line the object has `unit` and no `tag`, and nothing complains until
        # describe() reaches for it.
        super().__init__(tag)
        self.unit = unit

    def describe(self):
        return f"{self.tag} in {self.unit}"


sensor = Sensor("TH-04", "C")

print(sensor.describe())
print(sorted(vars(sensor)))

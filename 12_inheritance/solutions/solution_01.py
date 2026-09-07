"""Solution 01 -- Inheritance, and the call that is not automatic."""


class Device:
    def __init__(self, tag):
        self.tag = tag

    def describe(self):
        return f"device {self.tag}"


class Sensor(Device):
    def __init__(self, tag, unit):
        # Not automatic: leave this out and self.tag is never set, with no error
        # until something reads it.
        super().__init__(tag)
        self.unit = unit

    def describe(self):
        return super().describe() + f" ({self.unit})"


sensor = Sensor("TH-04", "C")

print(sensor.describe())
print(sorted(vars(sensor)))
print(isinstance(sensor, Device), issubclass(Sensor, Device))
print(Device("TH-09").describe())

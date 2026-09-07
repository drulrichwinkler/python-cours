"""Solution 09 (bonus) -- A class that holds a log."""


class Log:
    unit = "C"  # a class attribute, and immutable, so sharing it is fine

    def __init__(self, tag):
        self.tag = tag
        self.readings = []  # per instance, because it changes

    def add(self, celsius):
        self.readings.append(celsius)
        return self  # returning self lets calls be chained

    @property
    def highest(self):
        return max(self.readings) if self.readings else None

    @property
    def faults(self):
        return [value for value in self.readings if value > 85]

    @classmethod
    def from_pairs(cls, tag, pairs):
        log = cls(tag)
        for other_tag, value in pairs:
            if other_tag == tag:
                log.add(value)
        return log

    def __repr__(self):
        return f"Log(tag={self.tag!r}, readings={self.readings})"


log = Log("TH-04").add(91.0).add(23.1)

print(log)
print(log.highest, log.faults)
print(Log.unit, log.unit)

pairs = [("TH-04", 88.0), ("TH-01", 21.7), ("TH-04", 90.2)]
print(Log.from_pairs("TH-04", pairs))
print(Log("TH-09").highest)

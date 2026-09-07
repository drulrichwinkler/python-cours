"""Solution 09 (bonus) -- A log that is a sequence."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Reading:
    tag: str
    celsius: float


@dataclass
class Log:
    tag: str
    readings: list[Reading] = field(default_factory=list)

    def add(self, celsius):
        self.readings.append(Reading(self.tag, celsius))
        return self

    def __len__(self):
        return len(self.readings)

    def __iter__(self):
        return iter(self.readings)

    def __contains__(self, celsius):
        # `in` asks about a value, not about a Reading -- worth deciding on purpose.
        return any(reading.celsius == celsius for reading in self.readings)

    @property
    def faults(self):
        return [reading for reading in self.readings if reading.celsius > 85]


log = Log("TH-04").add(91.0).add(23.1).add(88.4)

print(len(log))
print(91.0 in log, 0.0 in log)
print(log.faults)
print([reading.celsius for reading in log])
print(bool(log), bool(Log("TH-09")))
print(len({Reading("TH-04", 91.0), Reading("TH-04", 91.0)}))

"""Solution 06 -- Frozen, and a default that is not shared."""

from dataclasses import asdict, dataclass, field


@dataclass(frozen=True, order=True)
class Reading:
    celsius: float
    tag: str = "?"


@dataclass
class Log:
    tag: str
    # `= []` is an error on a dataclass field. default_factory says "call this to
    # make the default", which is module 04's fix, declared.
    readings: list[float] = field(default_factory=list)


print(sorted([Reading(91.0, "TH-04"), Reading(21.7, "TH-01")]))
print(len({Reading(91.0, "TH-04"), Reading(91.0, "TH-04")}))
print(asdict(Reading(91.0, "TH-04")))

a, b = Log("TH-04"), Log("TH-09")
a.readings.append(91.0)
print(a.readings, b.readings, a.readings is b.readings)

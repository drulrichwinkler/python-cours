"""Solution 06 -- The package underneath all five frameworks."""

from sensorreport import LIMIT, Reading, faults, load_readings, summarise

readings = load_readings()

print(len(readings), sum(1 for r in readings if r.value is None))

for summary in summarise(readings):
    print(
        f"{summary.location:<10}{summary.readings:>3}{summary.usable:>4}"
        f"{summary.mean:>8}{summary.highest:>7}{summary.faults:>3}"
    )

print(LIMIT)
print([(r.tag, r.value) for r in faults(readings)])
# A frozen dataclass, module 12: the slots make the attribute names checkable and
# frozen means a reading that has happened cannot be edited.
print(Reading("TH-01", 21.7, "°C", "Hall", "2026-03-01T08:00").is_fault)

"""Solution 09 (bonus) -- The hourly summary.

Two loops, on purpose. The first collects, the second reports. Trying to do both
in one pass means printing the summary of an hour only once the next hour has
started, plus a final flush after the loop -- which is where that kind of code
goes wrong.

`hours` is a plain list of pairs here. Module 06 introduces the dictionary, which
is what this really wants to be, and the same task comes back there in three
lines.
"""

log = [
    ("14:05", 21.7),
    ("14:10", 23.1),
    ("14:15", 22.4),
    ("15:00", 24.0),
    ("15:30", 24.2),
]

hours: list[tuple[str, list[float]]] = []

for timestamp, reading in log:
    hour = timestamp[:2]
    if hours and hours[-1][0] == hour:
        hours[-1][1].append(reading)
    else:
        hours.append((hour, [reading]))

for hour, values in hours:
    average = sum(values) / len(values)
    print(f"{hour}: {len(values)} readings, avg {average:.1f}")

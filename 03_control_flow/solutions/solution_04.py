"""Solution 04 -- Number the log lines.

`enumerate(seq, start=1)` counts from one. Without `start` it counts from zero,
and adding one by hand is the version that eventually gets it wrong.
"""

readings = [21.7, 23.1, 22.4]

for position, reading in enumerate(readings, start=1):
    print(f"{position}: {reading}")

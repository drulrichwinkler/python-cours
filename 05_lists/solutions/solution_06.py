"""Solution 06 -- The loop as a comprehension."""

readings = [21.7, 23.1, 91.0, 19.4, 22.8]

labelled = [f"{r:.1f} C" for r in readings if r < 90]

print(labelled)

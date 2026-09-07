"""Solution 06 -- Build the line with join."""

fields = ["TH-04", "91.0", "C"]
readings = [21.7, 91.0, 23.1]

print(";".join(fields))
print(";".join(f"{r:.1f}" for r in readings))

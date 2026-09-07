"""Solution 05 -- A table."""

readings = [("TH-04", 91.037), ("TH-1", 5.5), ("TH-09", 23.14)]

print(f"{'tag':<8}{'value':>9}")
print("-" * 17)
for tag, value in readings:
    print(f"{tag:<8}{value:>9.2f}")

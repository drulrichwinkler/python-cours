"""Solution 04 -- Loop over pairs, and sort by value."""

readings = {"TH-01": 21.7, "TH-04": 91.0, "TH-09": 23.1, "TH-02": 88.4}

for tag, value in readings.items():
    print(f"{tag}: {value:.1f}")

print()

# sorted() on .items() gets pairs; the key function picks the second slot.
for tag, value in sorted(readings.items(), key=lambda pair: pair[1], reverse=True):
    print(tag, value)

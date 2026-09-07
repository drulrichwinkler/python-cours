"""Solution 06 -- defaultdict, and the trap in it."""

import collections

log = [("TH-04", 91.0), ("TH-01", 21.7), ("TH-04", 88.0)]

grouped = collections.defaultdict(list)  # the argument is a function that builds the default
for tag, value in log:
    grouped[tag].append(value)

print(dict(grouped))
print(isinstance(grouped, dict))

# Reading a missing key CREATES it. That is how the append above works without a
# setdefault, and it is why a lookup can change the dict.
before = len(grouped)
grouped["TH-99"]
print(before, len(grouped))
print(sorted(grouped))

"""Solution 05 -- Counter."""

import collections

log = [("TH-04", 91.0), ("TH-01", 21.7), ("TH-04", 88.0), ("TH-09", 23.1), ("TH-04", 90.2)]

counts = collections.Counter(tag for tag, _ in log)

print(counts)
print(counts.most_common(1))
print(counts["TH-04"], counts["TH-77"])  # a missing key counts zero rather than raising
print(sorted(counts))

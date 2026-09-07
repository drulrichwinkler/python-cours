"""Solution 03 -- Repair a counter."""


def count_tags(log):
    counts = {}
    for tag, _ in log:
        # counts[tag] += 1 reads the key before it writes it, so the first
        # occurrence of a tag raises KeyError. get supplies the starting value.
        counts[tag] = counts.get(tag, 0) + 1
    return counts


log = [("TH-04", 91.0), ("TH-01", 21.7), ("TH-04", 88.0), ("TH-04", 90.1)]

print(count_tags(log))

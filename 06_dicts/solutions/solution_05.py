"""Solution 05 -- Group readings by tag."""


def group(log):
    """Return {tag: [values, in the order they arrived]}."""
    grouped = {}
    for tag, value in log:
        # setdefault inserts [] when the tag is new and returns the list that is
        # now in the dict -- so the append lands in the dict either way.
        grouped.setdefault(tag, []).append(value)
    return grouped


log = [("TH-04", 91.0), ("TH-01", 21.7), ("TH-04", 88.0), ("TH-09", 23.1)]

by_tag = group(log)
print(by_tag)
print(by_tag["TH-04"])
print(sorted(by_tag))

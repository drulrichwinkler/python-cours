"""Exercise 05 -- Group readings by tag.

Write `group(log)` returning a dict that maps each tag to a list of its readings,
in the order they arrived. A tag that appears three times gets a list of three.

Expected output:

    {'TH-04': [91.0, 88.0], 'TH-01': [21.7], 'TH-09': [23.1]}
    [91.0, 88.0]
    ['TH-01', 'TH-04', 'TH-09']

Hint: `grouped.setdefault(tag, []).append(value)` is the whole loop body.
`setdefault` puts the empty list in when the tag is new and hands back the list
that is now in the dict -- so the append lands in the dict either way.
"""


# TODO: write the function

log = [("TH-04", 91.0), ("TH-01", 21.7), ("TH-04", 88.0), ("TH-09", 23.1)]

by_tag = group(log)
print(by_tag)
print(by_tag["TH-04"])
print(sorted(by_tag))

"""Exercise 06 -- Frozen, and a default that is not shared.

Two dataclasses:

  - `Reading`, frozen and ordered, with `celsius` first and `tag` defaulting to "?"
  - `Log`, with a tag and a list of readings that starts empty

Expected output:

    [Reading(celsius=21.7, tag='TH-01'), Reading(celsius=91.0, tag='TH-04')]
    1
    {'celsius': 91.0, 'tag': 'TH-04'}
    [91.0] [] False

Hint: `@dataclass(frozen=True, order=True)`. Frozen makes it hashable, which is what
line 2 needs -- and `order=True` compares the fields in the order they are declared,
which is why `celsius` comes first. On `Log`, `= []` raises: use
`field(default_factory=list)`. `asdict` comes from the same module.
"""


# TODO: the imports and the two classes

print(sorted([Reading(91.0, "TH-04"), Reading(21.7, "TH-01")]))
print(len({Reading(91.0, "TH-04"), Reading(91.0, "TH-04")}))
print(asdict(Reading(91.0, "TH-04")))

a, b = Log("TH-04"), Log("TH-09")
a.readings.append(91.0)
print(a.readings, b.readings, a.readings is b.readings)

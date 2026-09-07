"""Exercise 01 -- A class with a repr.

Write `Sensor`, taking a tag and a unit that defaults to "C". Give it `describe()`,
returning a line like `TH-04 in C`, and a `__repr__` that looks like the expression
that would rebuild the object.

Expected output:

    TH-04 in C
    Sensor(tag='TH-04', unit='C')
    [Sensor(tag='TH-04', unit='C'), Sensor(tag='TH-09', unit='F')]
    {'tag': 'TH-04', 'unit': 'C'}

Hint: `!r` in an f-string asks for the repr of a value, which is what puts the quotes
around the strings. The third line is a list, and a list always shows the repr of what
is in it -- so if you write only `__str__`, that line will not match.
"""


# TODO: the class

sensor = Sensor("TH-04")

print(sensor.describe())
print(sensor)
print([sensor, Sensor("TH-09", "F")])
print(sensor.__dict__)

"""Exercise 04 -- A type that works with for, in and len.

Give `Log` the methods that make the calls below work. Nothing is inherited and
nothing is declared -- each piece of syntax needs its own method.

Expected output:

    3
    [21.7, 91.0, 23.1]
    True False
    21.7 23.1
    91.0 [21.7, 23.1, 91.0]
    True False

Hint: `__len__`, `__iter__`, `__contains__`, `__getitem__`. `__iter__` can return
`iter(self.readings)` -- it has to hand back an iterator, not a list. The last line
needs no work: with `__len__` and no `__bool__`, an empty object is already falsy.
"""


class Log:
    def __init__(self, readings):
        self.readings = readings

    # TODO: the four methods


log = Log([21.7, 91.0, 23.1])

print(len(log))
print([value for value in log])
print(91.0 in log, 0.0 in log)
print(log[0], log[-1])
print(max(log), sorted(log))
print(bool(log), bool(Log([])))

"""Exercise 05 -- Equality, and what it costs.

Give `Reading` a `__repr__`, an `__eq__` comparing tag and value, and whatever else
is needed for the last two lines to work.

Expected output:

    True False
    False
    1
    [Reading(tag='TH-04', celsius=91.0)]

Hint: `__eq__` should return `NotImplemented` -- not False -- when the other operand
is not a Reading. And run the file with only `__eq__` written first: the error you
get is module 06's rule about dict keys being enforced.
"""


class Reading:
    def __init__(self, tag, celsius):
        self.tag = tag
        self.celsius = celsius

    # TODO: __repr__, __eq__, and the one more that line 3 of the output needs


a = Reading("TH-04", 91.0)
b = Reading("TH-04", 91.0)

print(a == b, a is b)
print(a == "TH-04")
print(len({a, b}))
print(sorted({a, b}, key=lambda r: r.celsius))

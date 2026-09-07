"""Solution 02 -- Predict what classes do.

b.seen           is ['TH-01', 'TH-04']. `seen` was assigned in the class body, so
                 there is one list and every instance reaches the same one. This is
                 module 04's mutable default argument, one floor up.
a.kind           is 'hygrometer' and b.kind and Sensor.kind are both 'thermometer'.
                 Assignment writes to the instance -- a property with a setter is
                 the exception -- so it created a new attribute on `a` that shadows
                 the class one. Reading looks at the instance first and the class
                 second; writing does not.
a.__dict__       is ['kind', 'tag'] -- the instance carries only what was assigned
                 to it, which after the line above includes its own `kind`.
hasattr(a, ...)  is False. `b.calibrated = True` created an attribute on that one
                 object. Nothing was declared anywhere, and nothing else knows.
vars(m)          is ['_Mangled__hidden']. Two leading underscores are rewritten with
                 the defining class in front. That is collision protection between a
                 class and its subclasses, not privacy -- the name is still there.
Reading == ...   is False. The default __eq__ is identity, as in Java. Two objects
                 with equal contents are not equal until you say what equal means.
hash(...)        raises TypeError. Defining __eq__ sets __hash__ to None, so the
                 class stops being usable as a dict key or in a set. That is module
                 06's rule -- equal objects must hash equal -- being enforced,
                 because Python cannot guess which fields you meant.
"""


class Sensor:
    kind = "thermometer"
    seen = []

    def __init__(self, tag):
        self.tag = tag
        Sensor.seen.append(tag)


a = Sensor("TH-01")
b = Sensor("TH-04")

assert b.seen == ["TH-01", "TH-04"]


a.kind = "hygrometer"

assert a.kind == "hygrometer"
assert b.kind == "thermometer"
assert Sensor.kind == "thermometer"


assert sorted(a.__dict__) == ["kind", "tag"]


b.calibrated = True

assert hasattr(a, "calibrated") is False


class Mangled:
    def __init__(self):
        self.__hidden = 1


m = Mangled()

assert list(vars(m)) == ["_Mangled__hidden"]


class Reading:
    def __init__(self, celsius):
        self.celsius = celsius


assert (Reading(21.7) == Reading(21.7)) is False


class Compared:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        return isinstance(other, Compared) and self.celsius == other.celsius


try:
    hash(Compared(21.7))
    outcome = "hashable"
except TypeError:
    outcome = "TypeError"

assert outcome == "TypeError"

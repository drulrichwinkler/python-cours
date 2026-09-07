"""Exercise 02 -- Predict what classes do.

Replace each `...` with the value you expect, then run the file.

    uv run 11_classes/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""


class Sensor:
    kind = "thermometer"
    seen = []

    def __init__(self, tag):
        self.tag = tag
        Sensor.seen.append(tag)


a = Sensor("TH-01")
b = Sensor("TH-04")

# TODO: one list, or one per object?
assert b.seen == ...


# TODO: what does assigning to a class attribute through an instance do?
a.kind = "hygrometer"

assert a.kind == ...
assert b.kind == ...
assert Sensor.kind == ...


# TODO: which attributes does the instance itself carry?
assert sorted(a.__dict__) == ...


# TODO: an attribute nobody declared
b.calibrated = True

assert hasattr(a, "calibrated") == ...


# TODO: name mangling -- what is the attribute actually called?
class Mangled:
    def __init__(self):
        self.__hidden = 1


m = Mangled()

assert list(vars(m)) == ...


# TODO: == on a class that says nothing about it
class Reading:
    def __init__(self, celsius):
        self.celsius = celsius


assert (Reading(21.7) == Reading(21.7)) == ...


# TODO: and what defining __eq__ does to hashing
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

assert outcome == ...

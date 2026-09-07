"""Exercise 02 -- Predict what inheritance and dataclasses do.

Replace each `...` with the value you expect, then run the file.

    uv run 12_inheritance/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

from dataclasses import dataclass, field


# TODO: the parent's __init__ is not called for you
class Device:
    def __init__(self, tag):
        self.tag = tag


class Forgot(Device):
    def __init__(self, tag):
        self.extra = 1


assert hasattr(Forgot("TH-04"), "tag") == ...


# TODO: super() follows the MRO of the object's type, not the class it is written in
class A:
    def who(self):
        return "A"


class B(A):
    def who(self):
        return "B->" + super().who()


class C(A):
    def who(self):
        return "C->" + super().who()


class D(B, C):
    pass


assert [cls.__name__ for cls in D.__mro__] == ...
assert D().who() == ...
assert B().who() == ...


# TODO: __len__ with no __bool__
class Sized:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n


assert bool(Sized(0)) == ...


# TODO: iteration with only __getitem__
class OnlyGetitem:
    def __getitem__(self, index):
        return ["a", "b"][index]


assert list(OnlyGetitem()) == ...


# TODO: what a dataclass writes, and what it costs
@dataclass
class Reading:
    tag: str
    celsius: float


assert (Reading("TH-04", 91.0) == Reading("TH-04", 91.0)) == ...

try:
    {Reading("TH-04", 91.0)}
    outcome = "hashable"
except TypeError:
    outcome = "TypeError"

assert outcome == ...


# TODO: a mutable default on a dataclass field
try:

    @dataclass
    class Bad:
        items: list = []

    made = "fine"
except ValueError:
    made = "ValueError"

assert made == ...


# TODO: and the version that works
@dataclass
class Good:
    items: list = field(default_factory=list)


first, second = Good(), Good()
first.items.append(1)

assert second.items == ...

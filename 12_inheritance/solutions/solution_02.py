"""Solution 02 -- Predict what inheritance and dataclasses do.

Forgot           has no tag: False. Java inserts an implicit super() call and will
                 not compile without one; Python does neither, so the attribute is
                 simply absent until something reads it and raises somewhere else.
D.__mro__        is ['D', 'B', 'C', 'A', 'object'], and D().who() is 'B->C->A'.
                 super() inside B.who reached C -- a class B does not inherit from.
                 It walks the MRO of the object's type, which is why the same line
                 gives 'B->A' for a B() and 'B->C->A' for a D().
bool(Sized(0))   is False. With __len__ and no __bool__, an object is falsy when its
                 length is zero. That is free and occasionally surprising.
OnlyGetitem      iterates to ['a', 'b']. With no __iter__, iteration falls back to
                 calling __getitem__ with 0, 1, 2 ... until IndexError stops it.
Reading == ...   is True: a dataclass writes __eq__ over all the fields. And it is
                 unhashable for the reason module 11 gave -- defining __eq__ sets
                 __hash__ to None. frozen=True is the declarative fix.
items: list = [] raises ValueError. Module 04's mutable default argument, and here
                 the language refuses outright rather than sharing one list.
                 field(default_factory=list) is the same fix, declared: second.items
                 is [], its own.
"""

from dataclasses import dataclass, field


class Device:
    def __init__(self, tag):
        self.tag = tag


class Forgot(Device):
    def __init__(self, tag):
        self.extra = 1


assert hasattr(Forgot("TH-04"), "tag") is False


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


assert [cls.__name__ for cls in D.__mro__] == ["D", "B", "C", "A", "object"]
assert D().who() == "B->C->A"
assert B().who() == "B->A"


class Sized:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n


assert bool(Sized(0)) is False


class OnlyGetitem:
    def __getitem__(self, index):
        return ["a", "b"][index]


assert list(OnlyGetitem()) == ["a", "b"]


@dataclass
class Reading:
    tag: str
    celsius: float


assert (Reading("TH-04", 91.0) == Reading("TH-04", 91.0)) is True

try:
    {Reading("TH-04", 91.0)}
    outcome = "hashable"
except TypeError:
    outcome = "TypeError"

assert outcome == "TypeError"


try:

    @dataclass
    class Bad:
        items: list = []

    made = "fine"
except ValueError:
    made = "ValueError"

assert made == "ValueError"


@dataclass
class Good:
    items: list = field(default_factory=list)


first, second = Good(), Good()
first.items.append(1)

assert second.items == []

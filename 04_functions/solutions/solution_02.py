"""Solution 02 -- Predict what functions do.

the second def   rebinds the name. There is no overloading, so area(3) reaches
                 the two-parameter version and raises TypeError.
collect(3)       returns [1, 2, 3]. The default list was created once, when the
                 def ran, and every call that omits it appends to that one list.
data             is [1, 99]. mutate reached the caller's list; rebind only moved
                 its own local name.
nothing()        is None. There is no void -- a function that falls off the end
                 returns None, and so does a bare `return`.
"""


def area(side):
    return side * side


def area(width, height):  # noqa: F811 -- rebinding the name is the point
    return width * height


try:
    area(3)
    outcome = "worked"
except TypeError:
    outcome = "TypeError"

assert outcome == "TypeError"


def collect(item, bucket=[]):  # a mutable default -- the trap is the exercise
    bucket.append(item)
    return bucket


collect(1)
collect(2)
assert collect(3) == [1, 2, 3]


def mutate(values):
    values.append(99)


def rebind(values):
    values = [0]  # noqa: F841 -- the unused rebinding is the point


data = [1]
mutate(data)
rebind(data)
assert data == [1, 99]


def nothing():
    pass


assert nothing() is None

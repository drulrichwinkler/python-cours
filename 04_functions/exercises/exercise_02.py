"""Exercise 02 -- Predict what functions do.

Replace each `...` with the value you expect, then run the file.

    uv run 04_functions/exercises/exercise_02.py

Nothing printed means every prediction was right.

All four are places where Python differs from C or Java: what a second def does,
when a default is evaluated, what a caller sees, and what a bare return gives.

There is no "Expected output" section here: what is checked is your prediction.
"""


# TODO: a second def with the same name -- what happens to the first?
def area(side):
    return side * side


def area(width, height):  # noqa: F811 -- rebinding the name is the point
    return width * height


try:
    area(3)
    outcome = "worked"
except TypeError:
    outcome = "TypeError"

assert outcome == ...


# TODO: the default is one object, shared by every call that omits it
def collect(item, bucket=[]):  # noqa: B006 -- the trap is the exercise
    bucket.append(item)
    return bucket


collect(1)
collect(2)
assert collect(3) == ...


# TODO: which of the two reaches the caller?
def mutate(values):
    values.append(99)


def rebind(values):
    values = [0]  # noqa: F841 -- the unused rebinding is the point


data = [1]
mutate(data)
rebind(data)
assert data == ...


# TODO: a function that falls off the end returns what?
def nothing():
    pass


assert nothing() is ...

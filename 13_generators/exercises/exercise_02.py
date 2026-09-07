"""Exercise 02 -- Predict what iterators and generators do.

Replace each `...` with the value you expect, then run the file.

    uv run 13_generators/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

import itertools


# TODO: calling a function with `yield` in it -- what comes back, and what has run?
def counting():
    counting.body_ran = True
    yield 1


counting.body_ran = False
generator = counting()

assert counting.body_ran == ...
assert type(generator).__name__ == ...


# TODO: a generator is used up
def readings():
    yield 21.7
    yield 91.0


values = readings()

assert list(values) == ...
assert list(values) == ...


# TODO: an iterable against an iterator
numbers = [1, 2]
iterator = iter(numbers)

assert (iter(numbers) is numbers) == ...
assert (iter(iterator) is iterator) == ...


# TODO: range is lazy, but it is not an iterator
assert (iter(range(3)) is range(3)) == ...
assert [list(range(2)), list(range(2))] == ...


# TODO: what a `return` inside a generator does
def with_return():
    yield 1
    return "done"


assert list(with_return()) == ...


# TODO: groupby groups CONSECUTIVE equal items
grouped = [(key, list(group)) for key, group in itertools.groupby([1, 1, 2, 1])]

assert [key for key, _ in grouped] == ...

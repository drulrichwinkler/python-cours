"""Solution 02 -- Predict what iterators and generators do.

counting()       ran none of the body: body_ran is still False, and what came back
                 is a 'generator'. A function containing `yield` builds one when
                 called; the body starts at the first next().
list(values)     is [21.7, 91.0] the first time and [] the second. A generator is
                 used up, and the second pass does not raise -- which is the trap:
                 a function that walks its argument twice works on a list and
                 silently returns nothing on a generator.
iter(numbers)    is not `numbers`: a list is an iterable, and iter() hands back a
                 separate list_iterator. iter(iterator) IS the iterator -- that is
                 what makes an iterator usable in a for loop.
range            is lazy but not an iterator: iter(range(3)) is a new object each
                 time, and range can be walked twice. Laziness and single-use are
                 two different properties.
with_return()    is [1]. The return value is not yielded; it goes into the
                 StopIteration, where only `yield from` picks it up. A caller doing
                 the obvious thing never sees it.
groupby          gives keys [1, 2, 1] -- it groups CONSECUTIVE equal items, like
                 the Unix uniq it is named after. Sort first if you meant all of
                 them.
"""

import itertools


def counting():
    counting.body_ran = True
    yield 1


counting.body_ran = False
generator = counting()

assert counting.body_ran is False
assert type(generator).__name__ == "generator"


def readings():
    yield 21.7
    yield 91.0


values = readings()

assert list(values) == [21.7, 91.0]
assert list(values) == []


numbers = [1, 2]
iterator = iter(numbers)

assert (iter(numbers) is numbers) is False
assert (iter(iterator) is iterator) is True


assert (iter(range(3)) is range(3)) is False
assert [list(range(2)), list(range(2))] == [[0, 1], [0, 1]]


def with_return():
    yield 1
    return "done"


assert list(with_return()) == [1]


grouped = [(key, list(group)) for key, group in itertools.groupby([1, 1, 2, 1])]

assert [key for key, _ in grouped] == [1, 2, 1]

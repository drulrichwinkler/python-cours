"""Solution 06 -- yield from, and an endless generator."""

import itertools


def lines_of(name):
    yield f"{name}:1"
    yield f"{name}:2"


def files(names):
    for name in names:
        yield from lines_of(name)  # one flat stream out of several


def rising(start):
    value = start
    while True:  # never ends on its own -- the consumer decides
        yield value
        value += 1


print(list(files(["a.log", "b.log"])))
print(list(itertools.islice(rising(10), 3)))

taken = []
for number in rising(0):
    if number > 3:
        break
    taken.append(number)

print(taken)
print(list(itertools.pairwise([1, 2, 3])))

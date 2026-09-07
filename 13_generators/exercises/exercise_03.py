"""Exercise 03 -- Repair a function that walks twice.

`summarise` returns how many readings there are and the largest. It works on a list
and raises on a generator. Run it and read the error: by the time `max` is reached,
there is nothing left to look at.

Expected output:

    (3, 91.0)
    (3, 91.0)

Hint: `len()` walks the values, and then `max()` finds nothing left. There are two
defensible fixes: take a `list(values)` first, or make a single pass keeping a count
and a running maximum. Either is fine.
"""


def summarise(values):
    return len(list(values)), max(values)  # TODO: this walks the argument twice


def readings():
    yield 21.7
    yield 91.0
    yield 23.1


print(summarise(readings()))
print(summarise([21.7, 91.0, 23.1]))

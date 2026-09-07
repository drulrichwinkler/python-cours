"""Exercise 04 -- The same iterator, twice over.

Write the countdown twice: once as a class with `__iter__` and `__next__`, once as a
generator function. Both count down from `start` to 1.

Expected output:

    [3, 2, 1]
    [3, 2, 1]
    True
    generator

Hint: the class keeps its state in an attribute and raises `StopIteration` when there
is nothing left. The generator keeps its state in the paused function, and needs
neither -- running off the end is how a generator stops.
"""


# TODO: class Countdown


# TODO: def countdown

print(list(Countdown(3)))
print(list(countdown(3)))
print(list(Countdown(3)) == list(countdown(3)))
print(type(countdown(3)).__name__)

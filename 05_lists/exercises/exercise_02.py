"""Exercise 02 -- Predict what lists and tuples do.

Replace each `...` with the value you expect, then run the file.

    uv run 05_lists/exercises/exercise_02.py

Nothing printed means every prediction was right.

All five are consequences of one fact: a name holds a reference, and a list can
change while a tuple cannot.

There is no "Expected output" section here: what is checked is your prediction.
"""

import copy

# TODO: two names, one list -- and the same two lines with an int
a = [1, 2]
b = a
b.append(3)

x = 1
y = x
y += 1

assert a == ...
assert x == ...


# TODO: += appends to a list and rebuilds a tuple. Which alias sees the change?
lst = [1, 2]
lst_alias = lst
lst += [3]

t = (1, 2)
t_alias = t
t += (3,)

assert lst_alias == ...
assert t_alias == ...


# TODO: copy.copy makes a new outer list. What about the rows inside it?
readings = [[21.7], [23.1]]
shallow = copy.copy(readings)
shallow[0].append(99.9)

assert readings == ...


# TODO: three rows, one assignment
grid = [[0] * 3] * 3
grid[0][0] = 9

assert grid == ...


# TODO: what does a method that changes the list hand back?
values = [23.1, 21.7]
result = values.sort()

assert result is ...
assert values == ...

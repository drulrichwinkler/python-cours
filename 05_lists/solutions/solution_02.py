"""Solution 02 -- Predict what lists and tuples do.

a                is [1, 2, 3]. `b = a` copied the reference; `append` changed the
                 one list both names refer to. `y = x` shared the int in exactly
                 the same way, but `y += 1` built a new int and rebound `y`, so x
                 stayed 1. Nothing about assignment differs -- only what the
                 object allows.
lst_alias        is [1, 2, 3]: `+=` on a list is `extend`, so the object itself
                 grew. t_alias is (1, 2): a tuple has no in-place add, so
                 `t += (3,)` built a new tuple and rebound `t` alone.
readings         is [[21.7, 99.9], [23.1]]. copy.copy built a new outer list
                 holding the same two row objects. Only copy.deepcopy would have
                 copied the rows.
grid             is [[9, 0, 0], [9, 0, 0], [9, 0, 0]]. `[row] * 3` repeated the
                 reference, so there is one row and three ways to reach it.
result           is None, and values is [21.7, 23.1]. Every list method that
                 mutates returns None -- pop is the exception, and it returns the
                 item, not the list.
"""

import copy

a = [1, 2]
b = a
b.append(3)

x = 1
y = x
y += 1

assert a == [1, 2, 3]
assert x == 1


lst = [1, 2]
lst_alias = lst
lst += [3]

t = (1, 2)
t_alias = t
t += (3,)

assert lst_alias == [1, 2, 3]
assert t_alias == (1, 2)


readings = [[21.7], [23.1]]
shallow = copy.copy(readings)
shallow[0].append(99.9)

assert readings == [[21.7, 99.9], [23.1]]


grid = [[0] * 3] * 3
grid[0][0] = 9

assert grid == [[9, 0, 0], [9, 0, 0], [9, 0, 0]]


values = [23.1, 21.7]
result = values.sort()

assert result is None
assert values == [21.7, 23.1]

"""Exercise 04 -- A decorator with an argument.

Write `repeat(times)`, so that a decorated function is called `times` times and the
results come back as a list.

Expected output:

    ['p', 'p', 'p']
    [42, 42]
    ping
    ['q', 'q']

Hint: three levels. The outer function takes `times`, the middle takes the function,
the inner takes the call's arguments. `@repeat(3)` means `ping = repeat(3)(ping)` --
which is what the last line writes out. Keep `@functools.wraps` on the wrapper.
"""

import functools  # noqa: F401

# TODO: repeat


@repeat(3)
def ping():
    return "p"


@repeat(2)
def double(value):
    return value * 2


def plain():
    return "q"


print(ping())
print(double(21))
print(ping.__name__)
print(repeat(2)(plain)())

"""Exercise 03 -- Repair a decorator.

Three things are wrong with `loud`. Run it and the first one appears immediately;
fix that and the next shows up.

Expected output:

    3
    7
    add | Add two numbers.

Hint: a wrapper has to (a) accept whatever the function accepts, including keyword
arguments, (b) hand back what the function returned, and (c) not throw away the
function's identity. One line from `functools` fixes the third.
"""

import functools  # noqa: F401 -- you will need this


def loud(function):
    # TODO: three things are wrong in these four lines
    def wrapper():
        function()

    return wrapper


@loud
def add(a, b):
    """Add two numbers."""
    return a + b


print(add(1, 2))
print(add(b=3, a=4))
print(add.__name__, "|", add.__doc__)

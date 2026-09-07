"""Solution 03 -- Repair a decorator."""

import functools


def loud(function):
    @functools.wraps(function)  # without this, add.__name__ is "wrapper"
    def wrapper(*args, **kwargs):
        # Two things were missing: the arguments have to be passed on, and the
        # result has to be returned -- a wrapper that forgets gives back None.
        result = function(*args, **kwargs)
        return result

    return wrapper


@loud
def add(a, b):
    """Add two numbers."""
    return a + b


print(add(1, 2))
print(add(b=3, a=4))
print(add.__name__, "|", add.__doc__)

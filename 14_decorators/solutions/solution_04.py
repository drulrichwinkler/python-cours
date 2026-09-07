"""Solution 04 -- A decorator with an argument."""

import functools


def repeat(times):  # takes the argument, returns the decorator
    def decorator(function):  # takes the function, returns the wrapper
        @functools.wraps(function)
        def wrapper(*args, **kwargs):  # takes the call's arguments
            return [function(*args, **kwargs) for _ in range(times)]

        return wrapper

    return decorator


@repeat(3)
def ping():
    return "p"


@repeat(2)
def double(value):
    return value * 2


print(ping())
print(double(21))
print(ping.__name__)


def plain():
    return "q"


# Written out: the brackets after repeat are a call that returns the decorator.
print(repeat(2)(plain)())

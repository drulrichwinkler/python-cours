"""Exercise 02 -- Predict what decorators do.

Replace each `...` with the value you expect, then run the file.

    uv run 14_decorators/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

import functools


# TODO: what does a plain wrapper do to the name and the docstring?
def bare(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@bare
def add(a, b):
    """Add two numbers."""
    return a + b


assert add.__name__ == ...
assert add.__doc__ is ...


# TODO: and with functools.wraps
def wrapped(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@wrapped
def subtract(a, b):
    """Subtract two numbers."""
    return a - b


assert subtract.__name__ == ...
assert subtract.__wrapped__.__name__ == ...


# TODO: a wrapper that forgets to return
def forgetful(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)

    return wrapper


@forgetful
def multiply(a, b):
    return a * b


assert multiply(2, 3) is ...


# TODO: in which order does a stack apply?
def tag(label):
    def decorator(function):
        @functools.wraps(function)
        def wrapper():
            return f"{label}({function()})"

        return wrapper

    return decorator


@tag("top")
@tag("bottom")
def base():
    return "base"


assert base() == ...


# TODO: when does the decorator itself run?
applied = []


def noting(function):
    applied.append(function.__name__)
    return function


@noting
def first():
    pass


@noting
def second():
    pass


assert applied == ...


# TODO: cache counts what reaches the function, not what the caller asked for
@functools.cache
def doubled(value):
    doubled.reached += 1
    return value * 2


doubled.reached = 0
doubled(1)
doubled(1)
doubled(2)

assert doubled.reached == ...

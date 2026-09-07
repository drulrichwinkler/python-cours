"""Solution 02 -- Predict what decorators do.

add.__name__     is 'wrapper' and add.__doc__ is None. `@bare` rebound the name to
                 the wrapper, so everything that reads the function's identity --
                 help(), a traceback, a documentation tool -- sees the wrapper.
subtract         keeps its name because functools.wraps copied it, and
                 __wrapped__ is the original, which wraps leaves behind as a way
                 back.
multiply(2, 3)   is None. The wrapper called the function and did not return the
                 result. Nothing raises; the function simply stops producing
                 values, which is the easiest decorator bug to write.
base()           is 'top(bottom(base))'. A stack applies from the def outwards --
                 base = tag("top")(tag("bottom")(base)) -- so the one nearest the
                 def ends up innermost, and the one at the top runs first.
applied          is ['first', 'second']. A decorator runs at import time, when the
                 def is executed, not when the function is called. That is what
                 makes a registry possible (exercise 09) and why an expensive
                 decorator body costs you on every import.
doubled.reached  is 2. The cache sits above the function, so the second call with
                 1 was answered without reaching it. Three calls, two arrivals.
"""

import functools


def bare(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@bare
def add(a, b):
    """Add two numbers."""
    return a + b


assert add.__name__ == "wrapper"
assert add.__doc__ is None


def wrapped(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@wrapped
def subtract(a, b):
    """Subtract two numbers."""
    return a - b


assert subtract.__name__ == "subtract"
assert subtract.__wrapped__.__name__ == "subtract"


def forgetful(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)

    return wrapper


@forgetful
def multiply(a, b):
    return a * b


assert multiply(2, 3) is None


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


assert base() == "top(bottom(base))"


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


assert applied == ["first", "second"]


@functools.cache
def doubled(value):
    doubled.reached += 1
    return value * 2


doubled.reached = 0
doubled(1)
doubled(1)
doubled(2)

assert doubled.reached == 2

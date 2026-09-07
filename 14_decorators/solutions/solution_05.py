"""Solution 05 -- Stacking, and the order."""

import functools


def tagged(label):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            return f"{label}({function(*args, **kwargs)})"

        return wrapper

    return decorator


# Applied from the def outwards: base = outer(inner(base)). The one nearest the def
# wraps first and ends up innermost.
@tagged("outer")
@tagged("inner")
def base():
    return "base"


print(base())
print(tagged("outer")(tagged("inner")(lambda: "base"))())
print(base.__name__)

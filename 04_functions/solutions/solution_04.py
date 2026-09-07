"""Solution 04 -- Keyword-only arguments.

Everything after the bare `*` can only be passed by name. It costs the caller six
characters and buys two things: `scale(21.7, 1.8)` cannot be read the wrong way
round, and `factor` can never be filled by accident from a positional argument
that was meant for something else.

The rule of thumb: make a parameter keyword-only when its meaning is not obvious
from the call site. `scale(21.7, 1.8)` says nothing; `scale(21.7, factor=1.8)`
says everything.
"""


def scale(value: float, *, factor: float, precision: int = 1) -> float:
    """Multiply a value by a factor and round the result."""
    return round(value * factor, precision)


print(scale(21.7, factor=1.8))
print(scale(21.7, factor=1.8, precision=3))

try:
    scale(21.7, 1.8)
    print("no error")
except TypeError:
    print("TypeError")

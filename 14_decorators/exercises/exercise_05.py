"""Exercise 05 -- Stacking, and the order.

Write `tagged(label)`, which wraps the result in `label(...)`. Then work out from the
expected output which way round a stack of two applies.

Expected output:

    outer(inner(base))
    outer(inner(base))
    base

Hint: the second line is the same thing written out by hand -- write it as nested
calls and see which order gives the same string as the decorated version. The third
line is what `@functools.wraps` is for.
"""

import functools  # noqa: F401

# TODO: tagged


@tagged("outer")
@tagged("inner")
def base():
    return "base"


print(base())
# TODO: the same thing as nested calls, on a lambda that returns "base"
print(base.__name__)

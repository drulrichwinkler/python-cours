"""Exercise 06 -- The same thing with a decorator.

Write `section(name)` as a generator-based context manager: the same two lines, this
time without a class and without the exception name in the second one.

Expected output:

    -> reading
       in reading
    <- reading
    -> parsing
    <- parsing
    caught: bad line

Hint: `@contextlib.contextmanager` above a function that prints, then `yield`s, then
prints. The `yield` is where the with-block runs, and what it yields is what `as`
binds. Wrap it in `try` / `finally`, or the second print will not happen when the
block raises.
"""

import contextlib

# TODO: the function


with section("reading") as label:
    print("   in", label)

try:
    with section("parsing"):
        raise ValueError("bad line")
except ValueError as err:
    print("caught:", err)

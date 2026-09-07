"""Exercise 05 -- A context manager as a class.

Write `Section`, a class that can be used in a `with`. On entering it prints an
arrow, the name, and binds itself to `as`. On leaving it prints the other arrow, the
name, and in brackets either the name of the exception class or the word `nothing`.
The exception must carry on to the caller.

Expected output:

    -> reading
       in reading
    <- reading (nothing)
    -> parsing
    <- parsing (ValueError)
    caught: bad line

Hint: `__init__(self, name)`, `__enter__(self)` returning `self`, and
`__exit__(self, exc_type, exc, traceback)`. The three arguments of `__exit__` are
`None` when the block ended normally. Return `False` so the exception is not
swallowed. Three spaces before `in`.
"""


# TODO: the class

with Section("reading") as section:
    print("   in", section.name)

try:
    with Section("parsing"):
        raise ValueError("bad line")
except ValueError as err:
    print("caught:", err)

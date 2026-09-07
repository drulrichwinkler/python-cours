"""Solution 06 -- The same thing with a decorator."""

import contextlib


@contextlib.contextmanager
def section(name):
    print(f"-> {name}")
    try:
        yield name  # the with-block runs here; this is what `as` binds
    finally:
        # finally, not a plain line: this half has to run when the block raised.
        print(f"<- {name}")


with section("reading") as label:
    print("   in", label)

try:
    with section("parsing"):
        raise ValueError("bad line")
except ValueError as err:
    print("caught:", err)

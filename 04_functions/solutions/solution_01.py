"""Solution 01 -- A function with a docstring and a default.

Note that it returns rather than prints. A function that prints can only ever be
used one way; a function that returns can be printed, joined, tested or written to
a file -- which is why every test in this course calls something and inspects what
came back.
"""


def describe(tag: str, reading: float, unit: str = "C") -> str:
    """Return a one-line description of a reading."""
    return f"{tag}: {reading} {unit}"


print(describe("TH-04", 21.7))
print(describe("TH-09", 71.6, unit="F"))
print("docstring:", describe.__doc__)

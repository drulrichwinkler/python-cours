"""Solution 01 -- A function with a docstring and a default.

It returns rather than prints -- which is what every test in this course checks:
it calls something and inspects what came back.
"""


def describe(tag: str, reading: float, unit: str = "C") -> str:
    """Return a one-line description of a reading."""
    return f"{tag}: {reading} {unit}"


print(describe("TH-04", 21.7))
print(describe("TH-09", 71.6, unit="F"))
print("docstring:", describe.__doc__)

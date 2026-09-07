"""Exercise 01 -- A function with a docstring and a default.

Write `describe(tag, reading, unit="C")` so that it RETURNS -- not prints -- a
line like

    TH-04: 21.7 C

Give it a one-line docstring. The calls at the bottom are already written.

Expected output:

    TH-04: 21.7 C
    TH-09: 71.6 F
    docstring: Return a one-line description of a reading.

Hint: the docstring is the first statement in the body, and afterwards it is
available as `describe.__doc__`.
"""


# TODO: write the function

print(describe("TH-04", 21.7))
print(describe("TH-09", 71.6, unit="F"))
print("docstring:", describe.__doc__)

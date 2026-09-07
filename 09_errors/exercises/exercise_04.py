"""Exercise 04 -- An exception of your own.

Define `ParseError`, an exception class of your own, and write `to_reading(raw)`
which returns a float or raises `ParseError` -- with the original `ValueError` named
as its cause.

Expected output:

    21.7
    ParseError - not a reading: 'n/a'
    cause: ValueError
    True

Hint: `class ParseError(Exception):` and a docstring is the whole class. Inside the
`except ValueError as err:` clause, `raise ParseError(...) from err` is what sets the
cause. `{raw!r}` in the f-string puts the quotes there.
"""


# TODO: the class


# TODO: the function

print(to_reading("21.7"))

try:
    to_reading("n/a")
except ParseError as err:
    print(type(err).__name__, "-", err)
    print("cause:", type(err.__cause__).__name__)

print(issubclass(ParseError, Exception))

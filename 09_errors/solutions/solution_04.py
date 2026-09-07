"""Solution 04 -- An exception of your own."""


class ParseError(Exception):
    """Raised when a field cannot be read as a reading."""


def to_reading(raw):
    try:
        return float(raw)
    except ValueError as err:
        # `from err` says the connection is deliberate: Python prints the original
        # under "The above exception was the direct cause of the following".
        raise ParseError(f"not a reading: {raw!r}") from err


print(to_reading("21.7"))

try:
    to_reading("n/a")
except ParseError as err:
    print(type(err).__name__, "-", err)
    print("cause:", type(err.__cause__).__name__)

print(issubclass(ParseError, Exception))

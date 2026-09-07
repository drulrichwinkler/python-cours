"""Turning fields from the log into numbers."""


class ParseError(Exception):
    """Raised when a field cannot be read as a reading."""


def to_reading(raw):
    """Return `raw` as a float, or raise ParseError naming what was wrong."""
    try:
        return float(raw)
    except ValueError as err:
        raise ParseError(f"not a reading: {raw!r}") from err

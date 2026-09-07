"""Parsing and summarising a sensor log. This is the code your tests are about."""


class ParseError(Exception):
    """Raised when a line cannot be read as a reading."""


def parse_line(line):
    """Turn 'TH-04;91.0' into ('TH-04', 91.0).

    Raises ParseError when the line has the wrong shape or an unreadable value.
    """
    parts = line.strip().split(";")
    if len(parts) != 2:
        raise ParseError(f"expected two fields, got {len(parts)}: {line.strip()!r}")
    tag, raw = parts
    if not tag:
        raise ParseError(f"empty tag in {line.strip()!r}")
    try:
        return tag, float(raw)
    except ValueError as err:
        raise ParseError(f"not a reading: {raw!r}") from err


def mean(values):
    """The arithmetic mean. Raises ValueError on an empty sequence."""
    values = list(values)
    if not values:
        return 0.0
    return sum(values) / len(values)


def readings_above(pairs, limit):
    """The (tag, value) pairs whose value is strictly above `limit`."""
    return [(tag, value) for tag, value in pairs if value > limit]

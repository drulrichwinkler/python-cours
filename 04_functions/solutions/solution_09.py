"""Solution 09 (bonus) -- A formatter with optional fields.

`**fields` collects whatever keyword arguments were passed into a dict, and since
Python 3.7 a dict keeps insertion order -- so the fields come out in the order the
caller wrote them, which is what makes the output predictable enough to test.

Building a list and joining it beats appending to a string: one allocation instead
of one per field, and no leading-space problem to work around.
"""


def line(tag: str, reading: float, **fields: str) -> str:
    """Return a log line with any number of extra key=value fields."""
    parts = [tag, str(reading)]
    for key, value in fields.items():
        parts.append(f"{key}={value}")
    return " ".join(parts)


print(line("TH-04", 21.7))
print(line("TH-04", 21.7, unit="C"))
print(line("TH-04", 91.0, unit="C", status="fault"))

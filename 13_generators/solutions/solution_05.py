"""Solution 05 -- A lazy pipeline."""

import io

RAW = "tag;value\nTH-01;21.7\nTH-04;n/a\nTH-09;23.1\nTH-02;88.4\n"


def rows(text):
    lines = iter(io.StringIO(text))
    header = next(lines).rstrip("\n").split(";")
    for line in lines:
        yield dict(zip(header, line.rstrip("\n").split(";")))


def readings(rows_):
    for row in rows_:
        try:
            yield float(row["value"])
        except ValueError:
            continue


def above(values, limit):
    for value in values:
        if value > limit:
            yield value


pipeline = above(readings(rows(RAW)), 85.0)

print(type(pipeline).__name__)
print(list(pipeline))
print(round(sum(readings(rows(RAW))), 1))  # module 02: floats do not add exactly
print(max(readings(rows(RAW))))

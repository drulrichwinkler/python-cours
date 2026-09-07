"""Exercise 05 -- A lazy pipeline.

Three generators, each pulling from the one before it. Nothing may build a list of
the whole input.

  - `rows(text)`: one dict per data line, using the first line as the field names
  - `readings(rows_)`: the values as floats, skipping what does not convert
  - `above(values, limit)`: only the values above the limit

Expected output:

    generator
    [88.4]
    133.2
    88.4

Hint: `io.StringIO(text)` behaves like an open file -- iterating it yields lines,
newline included, so `.rstrip("\\n")` before splitting. `next(lines)` takes the header
before the loop starts. Line 3 is rounded to one decimal place, because floats do not
add exactly (module 02).
"""

import io

RAW = "tag;value\nTH-01;21.7\nTH-04;n/a\nTH-09;23.1\nTH-02;88.4\n"


# TODO: the three generators


pipeline = above(readings(rows(RAW)), 85.0)

print(type(pipeline).__name__)
print(list(pipeline))
print(round(sum(readings(rows(RAW))), 1))
print(max(readings(rows(RAW))))

"""Exercise 06 -- Build the line with join.

This loop is the shape to avoid -- it builds a whole new string on every pass and
then has to remove the separator it added too many times:

    line = ""
    for field in fields:
        line += field + ";"
    line = line.removesuffix(";")

Write both lines with `join` instead. The second one has floats in it, so the
pieces have to be made into strings on the way in, with one decimal place each.

Expected output:

    TH-04;91.0;C
    21.7;91.0;23.1

Hint: `";".join(fields)` for the first. For the second, a generator expression goes
straight into `join`: `";".join(f"{r:.1f}" for r in readings)`.
"""

fields = ["TH-04", "91.0", "C"]
readings = [21.7, 91.0, 23.1]

# TODO: two prints

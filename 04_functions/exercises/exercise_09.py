"""Exercise 09 (bonus) -- A formatter with optional fields.

Write `line(tag, reading, **fields)` returning a log line: the tag and reading
first, then every extra field as `key=value`, in the order they were passed.

Expected output:

    TH-04 21.7
    TH-04 21.7 unit=C
    TH-04 91.0 unit=C status=fault

Hint: `**fields` collects surplus keyword arguments into a dict, and a dict keeps
insertion order. Build the pieces in a list and join them with a space.
"""


# TODO: write the function

print(line("TH-04", 21.7))
print(line("TH-04", 21.7, unit="C"))
print(line("TH-04", 91.0, unit="C", status="fault"))

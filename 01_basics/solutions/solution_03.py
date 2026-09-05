"""Solution 03 -- Repair broken code.

The error was:

    TypeError: unsupported operand type(s) for -: 'int' and 'str'

reported on the line  distance = limit - reading .

Why: `reading` holds text, not a number, and you cannot subtract text from a
number. The fix is one conversion. The text itself stays untouched, as required.

The many nines at the end are not a bug -- see exercise 08 (c).
"""

reading = "21.7"
limit = 25

distance = limit - float(reading)
print(f"Distance to limit: {distance}")

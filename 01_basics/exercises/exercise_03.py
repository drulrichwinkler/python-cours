"""Exercise 03 -- Repair broken code.

This program crashes. Run it, READ THE TRACEBACK, and fix it.

The reading arrives as text from a file -- you may not change the first line.

Expected output:

    Distance to limit: 3.3000000000000007

Yes, really. Section 9 of explore.ipynb explains why.

Note for yourself: which error type does Python report, and on which line?
"""

reading = "21.7"  # <- do not change
limit = 25

distance = limit - reading  # TODO: the bug is here
print(f"Distance to limit: {distance}")

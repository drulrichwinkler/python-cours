"""Exercise 04 -- Repair broken code.

This crashes. Fix it WITHOUT an if and without changing the value of `count`.

Expected output:

    False

Hint: with `and`, Python evaluates the left side first -- and if that already
settles the result, it never looks at the right side at all. The order here is
not style, it is the whole trick.

Note for yourself: which error type does Python report?
"""

total = 0
count = 0

print(total / count > 10)  # TODO: the bug is here

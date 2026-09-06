"""Exercise 04 -- Repair broken code.

This crashes. Fix it WITHOUT an if and without changing the value of `count`.

Expected output:

    False

Hint: `and` short-circuits, exactly like `&&`. Put the guard on the left.

Note for yourself: which error type does Python report?
"""

total = 0
count = 0

print(total / count > 10)  # TODO: the bug is here

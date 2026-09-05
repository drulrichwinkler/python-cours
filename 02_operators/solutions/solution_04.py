"""Solution 04 -- Repair broken code.

The error was:

    ZeroDivisionError: division by zero

The fix is to put the guard BEFORE the division. With `and`, if the left side is
false the result is already settled and Python never evaluates the right side.
That is short-circuit evaluation, and it is a promise of the language, not an
optimisation you are lucky to get.

Swap the two sides and it crashes again -- try it.
"""

total = 0
count = 0

print(count != 0 and total / count > 10)

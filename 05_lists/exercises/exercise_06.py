"""Exercise 06 -- The loop as a comprehension.

This loop works:

    labelled = []
    for r in readings:
        if r < 90:
            labelled.append(f"{r:.1f} C")

Write the same thing as a single list comprehension. One line, one name bound.

Expected output:

    ['21.7 C', '23.1 C', '19.4 C', '22.8 C']

Hint: `[expression for name in sequence if condition]` -- the expression comes
first, the `for` in the middle, the condition last. The f-string keeps one decimal
place: `f"{r:.1f} C"`.
"""

readings = [21.7, 23.1, 91.0, 19.4, 22.8]

# TODO: bind `labelled` to the comprehension

print(labelled)

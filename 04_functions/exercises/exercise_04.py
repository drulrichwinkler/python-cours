"""Exercise 04 -- Keyword-only arguments.

Write `scale(value, *, factor, precision=1)` which multiplies and rounds:

    scale(21.7, factor=1.8)              -> 39.1
    scale(21.7, factor=1.8, precision=3) -> 39.06

`factor` must be keyword-only -- `scale(21.7, 1.8)` has to raise TypeError.

Expected output:

    39.1
    39.06
    TypeError

Hint: everything after a bare `*` in the signature can only be passed by name.
The calls at the bottom are already written, including the one that must fail.
"""


# TODO: write the function

print(scale(21.7, factor=1.8))
print(scale(21.7, factor=1.8, precision=3))

try:
    scale(21.7, 1.8)
    print("no error")
except TypeError:
    print("TypeError")

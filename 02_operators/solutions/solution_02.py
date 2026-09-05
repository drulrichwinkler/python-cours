"""Solution 02 -- Predicting precedence.

2 ** 3 ** 2 is 512, because ** is evaluated right to left: 2 ** (3 ** 2) = 2 ** 9.
-3 ** 2 is -9, because ** binds more tightly than the minus sign: -(3 ** 2).

The other three: 2 + 3 * 4 is 14 (multiplication first), (2 + 3) * 4 is 20, and
10 - 4 - 3 is 3 because subtraction is evaluated left to right.
"""

from course import check

check(
    "512",
    "94f8607915dff25f013e45fc0642fb9830b0fb25ab0ab46d477eaf1061def379",
    "Not (2**3)**2. The other way round.",
)
check(
    "-9",
    "d5c534fde62beb89c745a59952c8efed8b7523cbd047e682782e4367de9ea3bf",
    "The power is applied first, the minus afterwards.",
)

print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 ** 2)  # fmt: skip
print(-3 ** 2)  # fmt: skip
print(10 - 4 - 3)

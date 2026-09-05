"""Exercise 02 -- Predicting precedence.

Fill in your predictions BEFORE you run the file.

Hint: two of the five lines surprise almost everyone. For ** it is worth asking
which side Python reads from -- and how tightly a minus sign binds.

No "Expected output" section here on purpose: what is checked is your prediction.
"""

# check() is a helper of this course. It compares your prediction against a
# checksum, so it can say right or wrong without the answer being readable
# anywhere in this repository. `from X import Y` is module 10.
from course import check

# TODO: what is  2 ** 3 ** 2 ?
check(
    "...",
    "94f8607915dff25f013e45fc0642fb9830b0fb25ab0ab46d477eaf1061def379",
    "Not (2**3)**2. The other way round.",
)

# TODO: what is  -3 ** 2 ?
check(
    "...",
    "d5c534fde62beb89c745a59952c8efed8b7523cbd047e682782e4367de9ea3bf",
    "The power is applied first, the minus afterwards.",
)

# Only then run this:
print(2 + 3 * 4)
print((2 + 3) * 4)
# The comment `# fmt: skip` tells the code formatter to leave this line alone.
# Without it the tool would rewrite  2 ** 3 ** 2  as  2**3**2  and  -3 ** 2  as
# -(3**2) -- correct, but it would give the answer away before you predicted it.
print(2 ** 3 ** 2)  # fmt: skip
print(-3 ** 2)  # fmt: skip
print(10 - 4 - 3)

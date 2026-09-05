"""Exercise 02 -- Predict the types.

Write down what the four print() lines below produce -- BEFORE you run the file.
check() tells you whether you are right without revealing the answer.

Hint: write the line exactly as Python prints it, angle brackets and quotes
included.

This exercise has no "Expected output" section on purpose: what it checks is your
prediction, not the program's output.
"""

# check() is a helper of this course. It compares your prediction against a
# checksum, so it can say right or wrong without the answer being readable
# anywhere in this repository. `from X import Y` is module 10.
from course import check

# TODO: replace the dots with your prediction for  type(21.7)
check(
    "...",
    "ec15c2bad4367dd8e12539fc1cc9b70b3e6f04d8c07fad82072a535827db73f1",
    "The value is 21.7 -- a number with a decimal point.",
)

# Only then run this:
print(type(21.7))
print(type("21.7"))
print(type(21))
print(type(True))

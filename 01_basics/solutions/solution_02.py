"""Solution 02 -- Predict the types.

The answer is  <class 'float'>  -- 21.7 has a decimal point, so it is a float,
not an int.

Worth noticing in the last line of the program: bool is a special kind of int in
Python. True behaves like 1 in arithmetic, False like 0. You rarely need this,
but it explains why  True + True  is 2 (see module 02).
"""

# check() compares a prediction against a checksum -- see 00_setup.
from course import check

check(
    "<class 'float'>",
    "ec15c2bad4367dd8e12539fc1cc9b70b3e6f04d8c07fad82072a535827db73f1",
    "The value is 21.7 -- a number with a decimal point.",
)

print(type(21.7))
print(type("21.7"))
print(type(21))
print(type(True))

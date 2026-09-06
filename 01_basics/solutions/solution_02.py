"""Solution 02 -- Predict the types.

The third line is the one worth pausing on: "21.7" in quotes is text that looks
like a number. That distinction is what exercise 03 crashes on.

And the fourth: bool is a special kind of int in Python. True behaves like 1 in
arithmetic and False like 0, which is why True + True is 2 (see module 02).
"""

assert type(21.7) is float
assert type("21.7") is str
assert type(21) is int
assert type(True) is bool

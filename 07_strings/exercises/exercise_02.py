"""Exercise 02 -- Predict what strings do.

Replace each `...` with the value you expect, then run the file.

    uv run 07_strings/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

# TODO: two literals, and the same characters assembled while the program runs
name = "TH-04"
from_source = "TH-04"
built = "".join(["TH", "-04"])

assert (name is from_source) == ...
assert (name is built) == ...
assert (name == built) == ...


# TODO: a method with nothing to do
tag = "TH-04"

assert (tag.strip() is tag) == ...
assert (tag.upper() is tag) == ...


# TODO: no argument against one space
line = "  a b   c  "

assert line.split() == ...
assert len(line.split(" ")) == ...


# TODO: join needs strings
try:
    ";".join(["a", 1])
    outcome = "worked"
except Exception as err:
    outcome = type(err).__name__

assert outcome == ...


# TODO: what len counts, and what encode counts
word = "Übergabe"

assert len(word) == ...
assert len(word.encode("utf-8")) == ...


# TODO: a slice of a string, against a slice of a list
text = "TH-04"
values = [1, 2]

assert (text[:] is text) == ...
assert (values[:] is values) == ...

"""Exercise 02 -- Predict the precedence.

Replace each `...` with the value you expect, then run the file.

    uv run 02_operators/exercises/exercise_02.py

Nothing printed means every prediction was right.

Two of the five surprise almost everyone. For `**` it is worth asking which side
Python starts from, and how tightly a minus sign binds compared with a power.

There is no "Expected output" section here on purpose: what is checked is your
prediction.
"""

# TODO: replace each ... with the value you expect
assert 2 + 3 * 4 == ...
assert (2 + 3) * 4 == ...
assert 2 ** 3 ** 2 == ...  # fmt: skip
assert -3 ** 2 == ...  # fmt: skip
assert 10 - 4 - 3 == ...

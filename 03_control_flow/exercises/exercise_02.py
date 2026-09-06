"""Exercise 02 -- Predict the loop.

Replace each `...` with the value you expect, then run the file.

    uv run 03_control_flow/exercises/exercise_02.py

Nothing printed means every prediction was right.

Three of these are about things C and Java do differently: how far `range` goes,
what happens to the loop variable afterwards, and when a loop's `else` runs.

There is no "Expected output" section here: what is checked is your prediction.
"""

# TODO: how many values does range(0, 10, 3) yield, and what is the last one?
assert len(range(0, 10, 3)) == ...
assert list(range(0, 10, 3))[-1] == ...

# TODO: what is bound to i after the loop?
for i in range(3):
    pass
assert i == ...

# TODO: the loop finishes without break -- does the else run?
log = []
for value in [21.7, 23.1]:
    if value > 85:
        log.append("stopped")
        break
else:
    log.append("completed")
assert log == ...

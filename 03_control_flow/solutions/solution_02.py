"""Solution 02 -- Predict the loop.

range(0, 10, 3)   yields 0, 3, 6, 9 -- four values, stopping before 10.
i after the loop  is 2. Python has no block scope: the name outlives the loop,
                  where C and Java would have discarded it.
the else          runs, because the loop was never broken out of. Read `else`
                  on a loop as "no break".
"""

assert len(range(0, 10, 3)) == 4
assert list(range(0, 10, 3))[-1] == 9

for i in range(3):
    pass
assert i == 2

log = []
for value in [21.7, 23.1]:
    if value > 85:
        log.append("stopped")
        break
else:
    log.append("completed")
assert log == ["completed"]

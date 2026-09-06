"""Solution 03 -- Repair a translated loop.

The error was:

    IndexError: list index out of range

`range(len(times) + 1)` runs one step too far -- the classic off-by-one, and the
reason it happened is that the loop was translated instead of rewritten.

`zip` removes the index altogether, and with it the possibility of the bug: it
walks both sequences in step and stops at the shorter one. If the two lists ever
get different lengths, this prints fewer lines instead of crashing.
"""

times = ["14:05", "14:10", "14:15"]
readings = [21.7, 23.1, 22.4]

for time, reading in zip(times, readings):
    print(time, reading)

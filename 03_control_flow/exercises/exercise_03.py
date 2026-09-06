"""Exercise 03 -- Repair a translated loop.

Someone ported this from C and kept the indexed loop. It crashes.

Run it, read the traceback, and fix it -- but not by patching the index. Rewrite
it as the Python idiom: `zip` walks two sequences in step and stops at the
shorter one.

Expected output:

    14:05 21.7
    14:10 23.1
    14:15 22.4

Hint: `for a, b in zip(seq1, seq2):` gives you one item from each per turn.
"""

times = ["14:05", "14:10", "14:15"]
readings = [21.7, 23.1, 22.4]

# TODO: rewrite these two lines
for i in range(len(times) + 1):
    print(times[i], readings[i])

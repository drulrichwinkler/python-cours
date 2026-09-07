"""Exercise 01 -- Slicing a log.

Print five slices of `readings`, one per line and in this order:

  1. the last three
  2. the first three
  3. everything except the first and the last
  4. every second entry, starting at the first
  5. the whole list, reversed

Write no loop and no `len()`. Each line is one `print` with one slice in it.

Expected output:

    [91.0, 22.8, 21.9]
    [21.7, 22.0, 22.4]
    [22.0, 22.4, 23.1, 91.0, 22.8]
    [21.7, 22.4, 91.0, 21.9]
    [21.9, 22.8, 91.0, 23.1, 22.4, 22.0, 21.7]

Hint: the form is `seq[start:stop:step]`, `stop` is excluded, and all three parts
may be left out. A negative index counts from the end; a negative step walks
backwards.
"""

readings = [21.7, 22.0, 22.4, 23.1, 91.0, 22.8, 21.9]

# TODO: five prints

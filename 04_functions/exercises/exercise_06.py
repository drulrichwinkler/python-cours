"""Exercise 06 -- Pass a function as an argument.

Sort the log three ways and print each result on its own line:

  1. by tag, alphabetically
  2. by reading, lowest first
  3. by reading, highest first

Expected output:

    [('TH-01', 21.7), ('TH-04', 91.0), ('TH-09', 23.1)]
    [('TH-01', 21.7), ('TH-09', 23.1), ('TH-04', 91.0)]
    [('TH-04', 91.0), ('TH-09', 23.1), ('TH-01', 21.7)]

Hint: `sorted(seq, key=f)` calls `f` on each item and sorts by what it returns.
Write the key as a named function at least once -- a lambda is the same thing
without a name.
"""

log = [("TH-04", 91.0), ("TH-01", 21.7), ("TH-09", 23.1)]

# TODO

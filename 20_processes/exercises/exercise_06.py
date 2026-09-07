"""Exercise 06 -- The package underneath all five frameworks.

`sensorreport` is an installed package of this repository, so it imports from
anywhere with no `sys.path` line. Print five things:

  1. how many readings there are and how many are unreadable, separated by a space
  2. one line per location: the name padded to 10, then readings in a field of 3,
     usable in 4, mean in 8, highest in 7 and faults in 3
  3. the limit above which a reading is a fault
  4. the faults as a list of (tag, value) pairs, worst first
  5. whether a Reading of 21.7 is a fault

Expected output:

    50 3
    Hall       20  18   22.12   23.9  0
    Office     10   9   22.34   23.1  0
    Test rig   20  20   32.83   93.5  3
    85.0
    [('TH-04', 93.5), ('TH-04', 93.2), ('TH-02', 88.4)]
    False

Hint: `from sensorreport import LIMIT, Reading, faults, load_readings, summarise`.
Those are the same numbers as module 18's pandas summary and module 19's SQL query,
computed a third way. A `Reading` takes tag, value, unit, location and at, and has an
`is_fault` property.
"""

# TODO: the import, then the prints

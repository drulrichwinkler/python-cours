"""Exercise 06 -- Two days of tags.

Print five things about the two sets, one per line and in this order:

  1. the tags seen on both days, sorted
  2. the tags seen only today, sorted
  3. the tags seen on exactly one of the two days, sorted
  4. how many distinct tags there are altogether
  5. whether every tag of today also appeared yesterday -- as True or False

Expected output:

    ['TH-04', 'TH-09']
    ['TH-01', 'TH-12']
    ['TH-01', 'TH-11', 'TH-12']
    5
    False

Hint: `&` `-` `^` `|` and `<=`. Print sets through `sorted()`: a set has no order,
and a set of strings usually prints in a different arrangement from one run to the
next.
"""

today = {"TH-01", "TH-04", "TH-09", "TH-12"}
yesterday = {"TH-04", "TH-09", "TH-11"}

# TODO: five prints

"""Exercise 05 -- A table.

Print a heading, a rule, and one line per reading. The tag goes in a field eight
wide, left-aligned; the value in a field nine wide with two decimals. The heading
uses the same widths, but `value` is right-aligned to sit over its column. The rule
is seventeen dashes.

Expected output:

    tag         value
    -----------------
    TH-04       91.04
    TH-1         5.50
    TH-09       23.14

Hint: a string multiplied by a number repeats it. In the heading the words are
strings, so they need the alignment written out -- text is left-aligned by default
and numbers are not.
"""

readings = [("TH-04", 91.037), ("TH-1", 5.5), ("TH-09", 23.14)]

# TODO: the heading, the rule, and the loop

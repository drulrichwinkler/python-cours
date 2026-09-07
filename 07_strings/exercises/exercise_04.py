"""Exercise 04 -- Take a line apart and put it back together.

Four prints, in this order:

  1. the three fields, split on the semicolon, each one stripped of its spaces,
     as a list
  2. tag, value and unit on one line, the value as a float with one decimal
  3. the three stripped fields joined with a pipe
  4. what `.split()` with no argument makes of the original line

Expected output:

    ['TH-04', '91.0', 'C']
    TH-04 91.0 C
    TH-04|91.0|C
    ['TH-04', ';', '91.0', ';', 'C']

Hint: a list comprehension over `line.split(";")` does the stripping in one line.
Unpack the result into three names (module 05). `.join` is a method on the
separator. The fourth line needs no work -- print it and read what it did.
"""

line = "  TH-04 ; 91.0 ; C  "

# TODO: four prints

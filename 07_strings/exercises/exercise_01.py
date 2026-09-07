"""Exercise 01 -- A report line.

Print four lines with f-strings, in this order:

  1. the tag in a field ten wide, left-aligned, then the value in a field eight
     wide with two decimals, then a space and C
  2. the tag centred in a field fifteen wide, padded with asterisks
  3. the value as a percentage of the limit, one decimal place, then " of the limit"
  4. the debugging form that prints the name `value` and its value together

Expected output:

    TH-04        91.04 C
    *****TH-04*****
    107.1% of the limit
    value=91.037

Hint: the format spec goes after a colon. `<` `>` `^` align, a character before
them is the padding, `.2f` fixes the decimals, `.1%` multiplies by 100 and adds the
sign. The fourth line is `f"{value=}"`.
"""

tag = "TH-04"
value = 91.037
limit = 85.0

# TODO: four prints

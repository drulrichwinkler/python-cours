# Solution 08 — Explaining

**a) Why does `int(3.9)` give `3` and not `4`?**
Because `int()` truncates instead of rounding: it throws away everything after
the decimal point. If you want rounding, `round(3.9)` gives `4`. Two different
jobs, two different functions.

**b) Why does `int("3.9")` fail with a `ValueError` when `int(3.9)` works?**
`int(3.9)` receives a *number* and is allowed to truncate it. `int("3.9")`
receives *text* and has to interpret it first — and `int()` can only interpret
text that spells out a whole number. `"3.9"` does not. The way round is
`int(float("3.9"))`: first read the text as a decimal number, then truncate.

**c) Why is `0.1 + 0.2 == 0.3` false?**
`0.1` cannot be represented exactly in binary, in the same way ⅓ cannot be
represented exactly in decimal — `0.3333...` never terminates. So the computer
stores a value a hair away from `0.1`, and adding makes the deviation visible:
`0.30000000000000004`.

This is not a Python quirk. Every language with floating point numbers behaves
this way, because they all follow the same IEEE 754 standard.

Two practical consequences:

- Never compare floats with `==`. Compare the difference against a tolerance.
- Never store money as a float. Use integer cents, or `decimal.Decimal`.

"""Exercise 01 -- A function is a value.

No decorators yet. Five prints, in this order:

  1. `converter(21.7)`, where `converter` is another name for the conversion function
  2. the result of applying each of `celsius_to_fahrenheit`, `abs` and `round` to -2.5,
     as a list
  3. `apply_twice(celsius_to_fahrenheit, 0)` -- a function taking a function
  4. `double(21)` and `scaler(3)(21)`, separated by a space, where `scaler(n)` returns
     a function that multiplies by n
  5. the `__name__` of `double` and the type name of `double`, separated by a space

Expected output:

    71.06
    [27.5, 2.5, -2]
    89.6
    42 63
    scale function

Hint: `converter = celsius_to_fahrenheit` with no brackets binds the function itself.
`scaler` returns its inner function -- a closure over `factor`, which is module 04.
Line 5 shows that the returned object carries the inner function's name, not the
name you bound it to.
"""


def celsius_to_fahrenheit(value):
    return value * 1.8 + 32


# TODO: apply_twice, scaler, then five prints

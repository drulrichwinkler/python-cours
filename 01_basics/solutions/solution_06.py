"""Solution 06 -- Unit conversion.

Without the format spec this would print 21.999999999999996. That is the same
floating point effect as in exercise 08 (c), not a mistake in the formula.
"""

fahrenheit = 71.6
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit} degrees Fahrenheit is {celsius:.1f} degrees Celsius.")

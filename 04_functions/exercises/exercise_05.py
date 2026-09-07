"""Exercise 05 -- Return three values.

Write `summarise(readings)` returning the lowest, the highest and the mean, in
that order. The caller unpacks them into three names.

Expected output:

    low 21.7
    high 23.1
    mean 22.4

Hint: `return a, b, c` builds a tuple; `low, high, mean = summarise(...)` takes it
apart. Round the mean to one decimal place in the f-string, not in the function.
"""

readings = [21.7, 23.1, 22.4]

# TODO: write the function


low, high, mean = summarise(readings)
print("low", low)
print("high", high)
print(f"mean {mean:.1f}")

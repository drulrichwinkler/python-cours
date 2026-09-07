"""Solution 05 -- Return three values.

`return a, b, c` builds a tuple and the assignment takes it apart. In C this needs
pointer out-parameters, in Java a small class or an array -- here it is the
ordinary way to answer a question that has three parts.

The rounding lives at the call site because the function's job is the number, not
its appearance. A function that rounds has thrown away precision its caller might
have wanted.
"""

readings = [21.7, 23.1, 22.4]


def summarise(values: list[float]) -> tuple[float, float, float]:
    """Return the lowest, highest and mean of the readings."""
    return min(values), max(values), sum(values) / len(values)


low, high, mean = summarise(readings)
print("low", low)
print("high", high)
print(f"mean {mean:.1f}")

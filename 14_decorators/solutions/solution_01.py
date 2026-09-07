"""Solution 01 -- A function is a value."""


def celsius_to_fahrenheit(value):
    return value * 1.8 + 32


def apply_twice(function, value):
    return function(function(value))


def scaler(factor):
    def scale(value):
        return value * factor  # a closure over `factor` -- module 04

    return scale


converter = celsius_to_fahrenheit  # no call: the function itself

print(converter(21.7))
print([f(-2.5) for f in [celsius_to_fahrenheit, abs, round]])
print(apply_twice(celsius_to_fahrenheit, 0))

double = scaler(2)
print(double(21), scaler(3)(21))
print(double.__name__, type(double).__name__)

"""Solution 01 -- Your first function, with a type hint.

Note that there is no print() here. The function hands its result back with
`return`, and the test calls it and inspects the value. That is the normal shape
of testable code -- printing is for people, returning is for programs.

Modules 01 to 03 print instead, because `return` needs functions and those come
in module 04. From then on the exercises look like this one.
"""


def to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

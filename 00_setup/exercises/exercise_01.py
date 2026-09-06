"""Exercise 01 -- Your first function, with a type hint.

Functions and type hints belong to module 04. They are here because a function is
the smallest thing a test can call and an annotation the smallest thing a checker
can check -- this module is a tour of the tooling, not a lesson about the language.

THE TASK

Complete the function below so that it converts a temperature in Celsius to
Fahrenheit:

    Fahrenheit = Celsius * 9 / 5 + 32

Replace the line `return 0.0` with the real calculation.

HOW YOU KNOW YOU ARE DONE -- three checks, in this order:

    uv run pytest 00_setup      does it compute the right thing?
    uv run mypy                 do the types line up?
    uv run ruff check .         is the style clean?

All three green means done. No one to ask.

ABOUT THE SIGNATURE

    def to_fahrenheit(celsius: float) -> float:

Unlike C or Java, Python does not enforce that annotation while running -- the
interpreter ignores it, and nothing stops the function from returning a string.
`mypy` is the separate tool that checks whether you kept the promise. Try breaking
it on purpose once you are done: return `"warm"` and run `uv run mypy`.
"""


def to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return 0.0  # TODO: the real calculation

"""Exercise 01 -- Your first function, with a type hint.

This module is a guided tour of the tools, not a lesson about the language. You
are not expected to understand every line yet -- functions arrive in module 04
and type hints in module 04 as well. What you practise here is the workflow.

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

READING THE SIGNATURE

    def to_fahrenheit(celsius: float) -> float:

  - `celsius: float`  -- this function expects a floating point number
  - `-> float`        -- and it hands one back

Python does NOT enforce this while running. It is a promise to the reader, and
`mypy` is the tool that checks whether you keep it. Try breaking it on purpose
once you are done: return `"warm"` instead of a number and run `uv run mypy`.
"""


def to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return 0.0  # TODO: the real calculation

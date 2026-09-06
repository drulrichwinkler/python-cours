"""Tests for exercise 01 -- your first function.

Read this file. Every test in this course is built the same way: call something,
then state what it should have produced.

You will not have met most of this syntax yet -- that is expected. Every line
that is new carries a comment saying what it does. You need to be able to READ
this, not to write it.
"""

from pathlib import Path  # Path represents a file path as an object, not as text

import pytest  # the test runner: it finds every function whose name starts with test_

from course.checks import load_module  # a helper of this course: imports a .py file by path

# __file__ is the path of THIS file. .resolve() turns it into a full path with no
# ".." in it. .parent goes up one folder -- twice, because this file sits in
# 00_setup/tests/, and we want 00_setup/ itself.
MODULE = Path(__file__).resolve().parent.parent

# The / operator joins path parts. Path knows what a folder separator looks like
# on your system, so the same line works on Windows and on macOS.
EXERCISE = MODULE / "exercises" / "exercise_01.py"
SOLUTION = MODULE / "solutions" / "solution_01.py"

# A list of pairs: each entry is (input, expected result). Square brackets make a
# list, round brackets a pair. Lists are module 05.
CASES = [
    (0.0, 32.0),  # freezing point
    (100.0, 212.0),  # boiling point
    (-40.0, -40.0),  # the one temperature where both scales agree
    (21.5, 70.7),  # an ordinary room
]


# A name starting with _ is a hint to the reader: "helper, not a test".
# pytest ignores it because it does not start with test_.
def _check(path: Path) -> None:
    # Load the file and pull the function out of it by name.
    to_fahrenheit = load_module(path).to_fahrenheit

    # `for celsius, expected in CASES` unpacks each pair into two names at once.
    # Python does that for any sequence of the right length.
    for celsius, expected in CASES:
        actual = to_fahrenheit(celsius)

        # `assert` is the heart of every test: "this must be true, or stop here".
        # pytest.approx allows a tiny rounding difference -- see the 0.1 + 0.2
        # surprise in 01_basics. Comparing floats with plain == is a trap.
        # The text after the comma is only shown when the assert fails.
        assert actual == pytest.approx(expected), (
            f"to_fahrenheit({celsius}) gave {actual}, expected {expected}"
        )


# A test is an ordinary function whose name begins with test_.
# "-> None" says it hands nothing back (module 04).
def test_solution_is_correct() -> None:
    """The model solution must pass the same tests you do."""
    _check(SOLUTION)


# A line starting with @ is a decorator: a label stuck onto the function below it.
# This one marks the test as YOURS, so the automated build can skip it -- it is
# supposed to be red until you fill the exercise in. Decorators are module 14.
@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have finished the exercise. That is the point."""
    _check(EXERCISE)

"""Tests for exercise 01 -- your first function.

Read this file. It is short on purpose, and every test in this course is built
the same way: call something, then assert what it should have produced.
"""

from pathlib import Path

import pytest

from course.checks import load_module

MODULE = Path(__file__).resolve().parent.parent
EXERCISE = MODULE / "exercises" / "exercise_01.py"
SOLUTION = MODULE / "solutions" / "solution_01.py"

# celsius -> expected fahrenheit
CASES = [
    (0.0, 32.0),  # freezing point
    (100.0, 212.0),  # boiling point
    (-40.0, -40.0),  # the one temperature where both scales agree
    (21.5, 70.7),  # an ordinary room
]


def _check(path: Path) -> None:
    to_fahrenheit = load_module(path).to_fahrenheit
    for celsius, expected in CASES:
        actual = to_fahrenheit(celsius)
        assert actual == pytest.approx(expected), (
            f"to_fahrenheit({celsius}) gave {actual}, expected {expected}"
        )


def test_solution_is_correct() -> None:
    """The model solution must pass the same tests you do."""
    _check(SOLUTION)


@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have filled in the exercise. That is the point."""
    _check(EXERCISE)

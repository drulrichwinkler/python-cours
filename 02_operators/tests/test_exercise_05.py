"""Tests for exercise 05 -- range check."""

from pathlib import Path

import pytest

from course.checks import assert_output

MODULE = Path(__file__).resolve().parent.parent
EXERCISE = MODULE / "exercises" / "exercise_05.py"
SOLUTION = MODULE / "solutions" / "solution_05.py"


def test_solution_matches_the_brief() -> None:
    """The model solution must produce exactly what the exercise promises."""
    assert_output(SOLUTION, spec_file=EXERCISE)


@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have finished the exercise. That is the point."""
    assert_output(EXERCISE)

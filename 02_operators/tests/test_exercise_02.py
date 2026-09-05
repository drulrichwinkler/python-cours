"""Tests for exercise 02 -- predicting precedence."""

from pathlib import Path

import pytest

from course.checks import assert_predictions

MODULE = Path(__file__).resolve().parent.parent
EXERCISE = MODULE / "exercises" / "exercise_02.py"
SOLUTION = MODULE / "solutions" / "solution_02.py"


def test_solution_matches_the_brief() -> None:
    """The model solution must produce exactly what the exercise promises."""
    assert_predictions(SOLUTION)


@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have finished the exercise. That is the point."""
    assert_predictions(EXERCISE)

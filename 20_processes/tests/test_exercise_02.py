"""Tests for exercise 02 -- predict what a process does."""

from pathlib import Path

import pytest

from course.checks import assert_runs

MODULE = Path(__file__).resolve().parent.parent

EXERCISE = MODULE / "exercises" / "exercise_02.py"
SOLUTION = MODULE / "solutions" / "solution_02.py"


def test_solution_matches_the_brief() -> None:
    """The model solution must produce exactly what the exercise promises."""
    assert_runs(SOLUTION)


@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have finished the exercise. That is the point."""
    assert_runs(EXERCISE)

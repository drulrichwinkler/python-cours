"""Tests for exercise 03 -- repair three views.

You are meant to read this file: it says exactly what your exercise has to do.

Nothing here starts a server. `app.test_client()` sends requests into the
application directly, which is how Flask applications are actually tested.
"""

from pathlib import Path

import pytest

from course.checks import assert_output

MODULE = Path(__file__).resolve().parent.parent

EXERCISE = MODULE / "exercises" / "exercise_03.py"
SOLUTION = MODULE / "solutions" / "solution_03.py"


def test_solution_matches_the_brief() -> None:
    """The model solution must produce exactly what the exercise promises."""
    assert_output(SOLUTION, spec_file=EXERCISE)


@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have finished the exercise. That is the point."""
    assert_output(EXERCISE)

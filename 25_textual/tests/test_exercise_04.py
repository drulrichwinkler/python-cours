"""Tests for exercise 04 -- a reactive attribute.

You are meant to read this file: it says exactly what your exercise has to do.

The count in the last line is 2 for two assignments, and `init=False` in `app.py`
is what makes it 2 rather than 3.
"""

from pathlib import Path

import pytest

from course.checks import assert_output

# __file__ is the path of this file; .resolve() makes it absolute and
# .parent.parent walks up from tests/ to the module folder.
MODULE = Path(__file__).resolve().parent.parent

EXERCISE = MODULE / "exercises" / "exercise_04.py"
SOLUTION = MODULE / "solutions" / "solution_04.py"


def test_solution_matches_the_brief() -> None:
    """The model solution must produce exactly what the exercise promises."""
    assert_output(SOLUTION, spec_file=EXERCISE)


@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have finished the exercise. That is the point."""
    assert_output(EXERCISE)

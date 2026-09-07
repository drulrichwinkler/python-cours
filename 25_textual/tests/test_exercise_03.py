"""Tests for exercise 03 -- the handler nobody calls.

You are meant to read this file: it says exactly what your exercise has to do.

Ships red, and the symptom is the whole lesson: no exception, no warning, and the
second line of output identical to the first.
"""

from pathlib import Path

import pytest

from course.checks import assert_output

# __file__ is the path of this file; .resolve() makes it absolute and
# .parent.parent walks up from tests/ to the module folder.
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

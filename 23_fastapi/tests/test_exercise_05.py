"""Tests for exercise 05 -- bounds in the model.

You are meant to read this file: it says exactly what your exercise has to do.

The four bodies are fixed and the four expected lines are fixed. What you write is
the model -- which is the whole argument of the module: the model is the code.
"""

from pathlib import Path

import pytest

from course.checks import assert_output

# __file__ is the path of this file; .resolve() makes it absolute and
# .parent.parent walks up from tests/ to the module folder.
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

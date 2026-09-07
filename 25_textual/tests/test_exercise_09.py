"""Tests for exercise 09 -- one app, everything at once.

You are meant to read this file: it says exactly what your exercise has to do.

The six prints at the bottom of the exercise are written already. What you write is
the class -- the bindings, the reactive, the action and the redraw.
"""

from pathlib import Path

import pytest

from course.checks import assert_output

# __file__ is the path of this file; .resolve() makes it absolute and
# .parent.parent walks up from tests/ to the module folder.
MODULE = Path(__file__).resolve().parent.parent

EXERCISE = MODULE / "exercises" / "exercise_09.py"
SOLUTION = MODULE / "solutions" / "solution_09.py"


def test_solution_matches_the_brief() -> None:
    """The model solution must produce exactly what the exercise promises."""
    assert_output(SOLUTION, spec_file=EXERCISE)


@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have finished the exercise. That is the point."""
    assert_output(EXERCISE)

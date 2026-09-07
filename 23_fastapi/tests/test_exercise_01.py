"""Tests for exercise 01 -- the annotation is the parser.

You are meant to read this file: it says exactly what your exercise has to do.

Nothing here starts a server. `TestClient` calls the application in this process --
the same shape as Flask's `test_client()` in module 21, and for the same reason: a
test that needs a port is a test that fails when the port is busy.
"""

from pathlib import Path

import pytest

from course.checks import assert_output

# __file__ is the path of this file; .resolve() makes it absolute and
# .parent.parent walks up from tests/ to the module folder.
MODULE = Path(__file__).resolve().parent.parent

EXERCISE = MODULE / "exercises" / "exercise_01.py"
SOLUTION = MODULE / "solutions" / "solution_01.py"


def test_solution_matches_the_brief() -> None:
    """The model solution must produce exactly what the exercise promises."""
    assert_output(SOLUTION, spec_file=EXERCISE)


@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have finished the exercise. That is the point."""
    assert_output(EXERCISE)

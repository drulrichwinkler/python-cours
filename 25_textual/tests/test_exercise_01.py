"""Tests for exercise 01 -- the app, read without a terminal.

You are meant to read this file: it says exactly what your exercise has to do.

No terminal is involved. `run_test()` draws the screen into memory, which is why
these tests run in continuous integration where module 24's needed xvfb and a
graphical session.
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

"""Tests for exercise 02 -- predict what pytest does.

You are meant to read this file: it says exactly what your exercise has to do.
This is also the module about writing files like this one, so read it twice.
"""

from pathlib import Path  # Path represents a file path as an object, not as text

import pytest  # the test runner: it finds every function whose name starts with test_

from course.checks import assert_runs  # a helper of this course -- see 00_setup

# __file__ is the path of THIS file. .resolve() turns it into a full path with no
# ".." in it. .parent goes up one folder -- twice, because this file sits in
# 15_testing/tests/, and we want 15_testing/ itself.
MODULE = Path(__file__).resolve().parent.parent

# The / operator joins path parts. Path knows what a folder separator looks like
# on your system, so the same line works on Windows and on macOS.
EXERCISE = MODULE / "exercises" / "exercise_02.py"
SOLUTION = MODULE / "solutions" / "solution_02.py"


def test_solution_matches_the_brief() -> None:
    """The model solution must produce exactly what the exercise promises."""
    assert_runs(SOLUTION)


# @pytest.mark.your_turn marks this test as YOURS, so the automated build can skip
# it -- it is supposed to be red in a fresh copy. The mark is declared in
# pyproject.toml, which is what stops a typo in the name from being silently
# ignored.
@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have finished the exercise. That is the point."""
    assert_runs(EXERCISE)

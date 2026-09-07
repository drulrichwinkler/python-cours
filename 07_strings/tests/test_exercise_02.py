"""Tests for exercise 02 -- predict what strings do.

You are meant to read this file: it says exactly what your exercise has to do.
Anything in here you have not met yet is explained in a comment on the line
where it shows up. You do not need to be able to write this code -- only to
read it.
"""

from pathlib import Path  # Path represents a file path as an object, not as text

import pytest  # the test runner: it finds every function whose name starts with test_

from course.checks import assert_runs  # a helper of this course -- see 00_setup

# __file__ is the path of THIS file. .resolve() turns it into a full path with no
# ".." in it. .parent goes up one folder -- twice, because this file sits in
# 07_strings/tests/, and we want 07_strings/ itself.
MODULE = Path(__file__).resolve().parent.parent

# The / operator joins path parts. Path knows what a folder separator looks like
# on your system, so the same line works on Windows and on macOS.
EXERCISE = MODULE / "exercises" / "exercise_02.py"
SOLUTION = MODULE / "solutions" / "solution_02.py"


# A test is an ordinary function whose name begins with test_. That naming is how
# pytest finds it. The "-> None" says the function hands nothing back (module 04).
def test_solution_matches_the_brief() -> None:
    """The model solution must produce exactly what the exercise promises."""
    assert_runs(SOLUTION)


# A line starting with @ is a decorator: a label stuck onto the function below it.
# This one marks the test as YOURS, so the automated build can skip it -- it is
# supposed to be red in a fresh copy. Decorators are module 14.
@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have finished the exercise. That is the point."""
    assert_runs(EXERCISE)

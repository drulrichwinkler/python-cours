"""Tests for exercise 04 -- two tables, joined.

You are meant to read this file: it says exactly what your exercise has to do.

These tests need `data/readings.db`, which is a build artefact rather than a
committed file. Run `uv run 19_sql/build_db.py` once if they cannot find it.
"""

from pathlib import Path  # Path represents a file path as an object, not as text

import pytest  # the test runner: it finds every function whose name starts with test_

from course.checks import assert_output  # a helper of this course -- see 00_setup

# __file__ is the path of THIS file. .resolve() turns it into a full path with no
# ".." in it. .parent goes up one folder -- twice, because this file sits in
# 19_sql/tests/, and we want 19_sql/ itself.
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

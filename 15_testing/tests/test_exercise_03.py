"""Tests for exercise 03 -- repair three tests that cannot fail.

This one does not compare an output. Your exercise is three tests, so what is
checked is whether they can fail: the file is run against the correct library and
against each broken copy in `mutants/`, and every broken copy has to make it fail.

That is the same check as exercise 09, on a smaller scale, and it is the only kind
of check that can tell a real test from one that merely passes.
"""

from pathlib import Path

import pytest

from course.checks import assert_file_finds_bugs, assert_output

MODULE = Path(__file__).resolve().parent.parent

EXERCISE = MODULE / "exercises" / "exercise_03.py"
SOLUTION = MODULE / "solutions" / "solution_03.py"

CORRECT = MODULE  # sensorlib/ sits here
MUTANTS = sorted((MODULE / "mutants").iterdir())  # one folder per planted bug


def test_solution_finds_every_bug() -> None:
    """The model answer must pass on the correct library and fail on all three."""
    assert_output(SOLUTION, spec_file=EXERCISE)
    assert_file_finds_bugs(SOLUTION, CORRECT, MUTANTS)


@pytest.mark.your_turn
def test_your_tests_can_fail() -> None:
    """Red until each of your three tests demands something. The message says which."""
    assert_output(EXERCISE)
    assert_file_finds_bugs(EXERCISE, CORRECT, MUTANTS)

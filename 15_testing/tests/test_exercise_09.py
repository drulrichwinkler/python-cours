"""Tests for exercise 09 -- write the suite.

This one is different from every other test in the course. Your exercise is a
test suite, so what is checked is not an output: it is whether your tests pass
on the correct library AND fail on each broken one.

A suite that passes everywhere tests nothing, which is the point of the module.
"""

from pathlib import Path

import pytest

from course.checks import assert_suite_finds_bugs

MODULE = Path(__file__).resolve().parent.parent

CORRECT = MODULE  # sensorlib/ sits here
MUTANTS = sorted((MODULE / "mutants").iterdir())  # one folder per planted bug


def test_solution_finds_every_bug() -> None:
    """The model suite must pass on the correct code and fail on all three mutants."""
    assert_suite_finds_bugs(MODULE / "solutions" / "suite", CORRECT, MUTANTS)


@pytest.mark.your_turn
def test_your_suite_finds_every_bug() -> None:
    """Red until your suite catches all three. The message names the ones it missed."""
    assert_suite_finds_bugs(MODULE / "exercises" / "suite", CORRECT, MUTANTS)

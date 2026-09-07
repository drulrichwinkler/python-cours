"""Tests for exercise 09 -- a window, tested without a click.

You are meant to read this file: it says exactly what your exercise has to do.

`invoke()` is the whole test strategy of this module. There is no mouse, there is no
click, and the button's command is called directly -- see the README on why there is
no test client for tkinter.
"""

import sys
from pathlib import Path

import pytest

from course.checks import assert_output

sys.path.append(str(Path(__file__).resolve().parent.parent))

from display import has_display  # noqa: E402

# __file__ is the path of this file; .resolve() makes it absolute and
# .parent.parent walks up from tests/ to the module folder.
MODULE = Path(__file__).resolve().parent.parent

EXERCISE = MODULE / "exercises" / "exercise_09.py"
SOLUTION = MODULE / "solutions" / "solution_09.py"

# tkinter needs a graphical session, and this test opens one. On a machine without a
# screen -- a server, a container, a CI runner -- the tests below skip rather than
# fail. `xvfb-run -a uv run pytest 24_tkinter` runs them anyway on Linux, which is
# what this repository does in continuous integration.
needs_a_window = pytest.mark.skipif(
    not has_display(),
    reason="no display: run `xvfb-run -a uv run pytest 24_tkinter` on a headless machine",
)


@needs_a_window
def test_solution_matches_the_brief() -> None:
    """The model solution must produce exactly what the exercise promises."""
    assert_output(SOLUTION, spec_file=EXERCISE)


@needs_a_window
@pytest.mark.your_turn
def test_your_solution() -> None:
    """Red until you have finished the exercise. That is the point."""
    assert_output(EXERCISE)

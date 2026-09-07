"""A test suite for sensorlib.parsing -- the model answer to exercise 09.

Every test here is one claim about the code. Together they catch all three bugs
in `mutants/`, which is what the check in tests/test_exercise_09.py verifies.
"""

import pytest
from sensorlib.parsing import ParseError, mean, parse_line, readings_above


def test_parse_line_splits_tag_and_value():
    assert parse_line("TH-04;91.0") == ("TH-04", 91.0)


def test_parse_line_ignores_surrounding_whitespace():
    assert parse_line("  TH-04;91.0\n") == ("TH-04", 91.0)


def test_parse_line_rejects_a_missing_field():
    with pytest.raises(ParseError):
        parse_line("TH-04")


def test_parse_line_rejects_an_empty_tag():
    # Catches bug_02, where the check for an empty tag was dropped.
    with pytest.raises(ParseError):
        parse_line(";91.0")


def test_parse_line_rejects_an_unreadable_value():
    with pytest.raises(ParseError) as info:
        parse_line("TH-04;n/a")
    assert "n/a" in str(info.value)  # the message names what was wrong


def test_mean_of_three():
    assert mean([1.0, 2.0, 3.0]) == 2.0


def test_mean_needs_approx_for_thirds():
    # 0.1 + 0.2 != 0.3 (module 02), so an exact comparison would fail here.
    assert mean([0.1, 0.2]) == pytest.approx(0.15)


def test_mean_of_nothing_raises():
    # Catches bug_03, where an empty sequence quietly returned 0.0.
    with pytest.raises(ValueError):
        mean([])


def test_mean_accepts_a_generator():
    assert mean(value for value in [1.0, 3.0]) == 2.0


def test_readings_above_keeps_only_higher():
    pairs = [("TH-01", 21.7), ("TH-04", 91.0)]
    assert readings_above(pairs, 85.0) == [("TH-04", 91.0)]


def test_readings_above_is_strict_at_the_limit():
    # Catches bug_01, where `>` had become `>=`.
    assert readings_above([("TH-04", 85.0)], 85.0) == []


def test_readings_above_on_nothing():
    assert readings_above([], 85.0) == []

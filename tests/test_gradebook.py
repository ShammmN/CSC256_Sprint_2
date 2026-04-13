# test_gradebook.py
import pytest
from unittest.mock import Mock
from src.gradebook import calculate_average, get_letter_grade, is_passing, format_report


def test_calculate_average_basic():
    assert calculate_average([80, 90, 100]) == 90.0


def test_calculate_average_single():
    # expects 85.0 -- will raise ZeroDivisionError due to bug in calculate_average
    assert calculate_average([85]) == 85.0


def test_get_letter_grade_A():
    assert get_letter_grade(95) == "A"


def test_get_letter_grade_F():
    # BUG IN TEST: asserts "F" but function returns None for scores below 60
    # test is wrong -- it should catch the missing else, but instead it hides it
    assert get_letter_grade(50) == "F"


def test_is_passing_boundary():
    # passes 60 -- will return False due to > instead of >=
    assert is_passing(60) == False


def test_format_report_runs():
    result = format_report("Alice", [85, 90, 95])
    assert "Alice" in result

"""
Basic tests for calculator.py — run with: pytest test_calculator.py
"""

import pytest
from calculator import add, subtract, multiply, divide, calculate


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_calculate_dispatches_correctly():
    assert calculate("+", 2, 2) == 4
    assert calculate("-", 2, 2) == 0
    assert calculate("*", 2, 2) == 4
    assert calculate("/", 2, 2) == 1


def test_calculate_invalid_operator_raises():
    with pytest.raises(ValueError):
        calculate("%", 2, 2)

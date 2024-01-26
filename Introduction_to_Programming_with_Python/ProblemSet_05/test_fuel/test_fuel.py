from fuel import convert, gauge
import pytest


def test_convert_valid_fraction():
    assert convert("5/10") == 50


def test_convert_invalid_fraction_not_integers():
    with pytest.raises(ValueError, match="Invalid fraction format or values"):
        convert("3.5/2")


def test_convert_invalid_fraction_x_greater_than_y():
    with pytest.raises(ValueError, match="Invalid fraction format or values"):
        convert("8/4")


def test_convert_invalid_fraction_y_is_zero():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")


def test_gauge_less_than_or_equal_to_1():
    assert gauge(1) == "E"


def test_gauge_greater_than_or_equal_to_99():
    assert gauge(99) == "F"


def test_gauge_between_1_and_99():
    assert gauge(50) == "50%"

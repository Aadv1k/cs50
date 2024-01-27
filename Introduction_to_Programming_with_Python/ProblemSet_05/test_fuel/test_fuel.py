import pytest
from fuel import convert, gauge


def test_convert_valid_fraction():
    result = convert("3/5")
    assert result == 60


def test_convert_invalid_fraction_non_integer():
    with pytest.raises(ValueError):
        convert("2.5/3")


def test_convert_invalid_fraction_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/3")


def test_convert_invalid_fraction_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")


def test_gauge_e_grade():
    result = gauge(1)
    assert result == "E"


def test_gauge_f_grade():
    result = gauge(99)
    assert result == "F"


def test_gauge_percentage_grade():
    result = gauge(75)
    assert result == "75%"


def main():
    pytest.main(['-v', __file__])


if __name__ == "__main__":
    main()

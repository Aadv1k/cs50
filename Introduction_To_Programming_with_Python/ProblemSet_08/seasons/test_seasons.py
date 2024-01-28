import sys
import pytest
from seasons import calculate_time_in_minutes_as_word

def test_valid_timeframes():
    d1 = "1999-01-01"
    d2 = "2000-01-01"
    ans = "Five hundred twenty-five thousand, six hundred minutes"

    assert ans == calculate_time_in_minutes_as_word(d1, d2)

    d1 = "1998-01-01"
    ans = "One million, fifty-one thousand, two hundred minutes"

    assert ans == calculate_time_in_minutes_as_word(d1, d2)

def test_invalid_timeframes():
    with pytest.raises(ValueError):
        calculate_time_in_minutes_as_word("invalid", "invalid")

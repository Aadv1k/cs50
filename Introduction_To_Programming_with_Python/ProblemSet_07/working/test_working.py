import pytest
from working import convert

def test_valid_12_hour_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM") 
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")  
    with pytest.raises(ValueError):
        convert("9 AM to 13 PM")  

import pytest
from response import validate_email

def test_valid_email():
    assert validate_email("malan@harvard.edu") == "Valid"
    assert validate_email("user@example.com") == "Valid"
    assert validate_email("john.doe123@domain.org") == "Valid"

def test_invalid_email():
    assert validate_email("malan@@@harvard.edu") == "Invalid"
    assert validate_email("user@example") == "Invalid"
    assert validate_email("john.doe@com") == "Invalid"
    assert validate_email("invalid.email@.com") == "Invalid"

def test_mistyped_email():
    assert validate_email("john.doe@domain..com") == "Invalid"
    assert validate_email("user@.example.com") == "Invalid"

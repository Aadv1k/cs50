import pytest
from numb3rs import validate

def test_valid_ipv4():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True

def test_invalid_ipv4():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("256.0.0.1") == False
    assert validate("192.168.1.1.1") == False

def test_edge_cases():
    # Minimum valid IPv4 address
    assert validate("0.0.0.0") == True

    # Maximum valid IPv4 address
    assert validate("255.255.255.255") == True

    # Valid IPv4 addresses with leading zeros
    assert validate("001.002.003.004") == True
    assert validate("010.020.030.040") == True

    # Valid IPv4 addresses with spaces
    assert validate(" 127.0.0.1 ") == True
    assert validate("   192.168.1.1   ") == True

def test_mixed_formats():
    # Valid IPv4 addresses in mixed formats
    assert validate("192.168.1.001") == True
    assert validate("   010.020.030.040   ") == True

def test_invalid_formats():
    # Invalid IPv4 formats
    assert validate("256.0.0.1") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("192.168.1.1.1") == False

if __name__ == "__main__":
    pytest.main()

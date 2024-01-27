from plates import is_valid


def main():
    test_min_max_characters()
    test_start_with_two_letters()
    test_number_zero()
    test_number_zero()
    test_special_chars()


def test_min_max_characters():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False


def test_start_with_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("2") == False


def test_numbers_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_number_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_special_chars():
    assert is_valid("????") == False


if __name__ == "__main__":
    main()

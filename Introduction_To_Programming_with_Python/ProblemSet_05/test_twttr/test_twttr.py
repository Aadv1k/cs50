from twttr import shorten


def test_shorten_no_vowels():
    assert shorten("hello") == "hll"


def test_shorten_with_vowels():
    assert shorten("Python") == "Pythn"


def test_shorten_empty_string():
    assert shorten("") == ""


def test_shorten_all_vowels():
    assert shorten("AEIOUaeiou") == ""


def test_shorten_capitalized_vowels():
    assert shorten("AEIOU") == ""


def test_shorten_lowercase_vowels():
    assert shorten("aeiou") == ""


def test_shorten_with_numbers():
    assert shorten("hello123") == "hll123"


def test_shorten_printing_in_uppercase():
    assert shorten("HELLO") == "HLL"


def test_shorten_with_punctuation():
    assert shorten("Hello, World") == "Hll, Wrld"

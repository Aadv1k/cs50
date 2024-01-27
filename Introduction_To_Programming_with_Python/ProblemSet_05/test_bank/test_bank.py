import bank


def test_value_starts_with_hello():
    assert bank.value("Hello, World!") == 0


def test_value_starts_with_h():
    assert bank.value("Hi there!") == 20


def test_value_default_case():
    assert bank.value("What's up?") == 100


def test_value_case_insensitive():
    assert bank.value("HELLO, Everyone!") == 0

from plates import is_valid
import pytest


def test_valid_plate():
    assert is_valid("ABC123")


def test_invalid_plate_too_short():
    assert not is_valid("AB123")


def test_invalid_plate_too_long():
    assert not is_valid("ABCDE12345")


def test_invalid_plate_invalid_characters():
    assert not is_valid("ABC#123")


def test_invalid_plate_missing_letters():
    assert not is_valid("123456")

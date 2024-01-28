import pytest
from um import count

def test_single_um():
    assert count("um") == 1

def test_um_with_punctuation():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_multiple_um():
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3

def test_case_insensitivity():
    assert count("Um, uM, uM.") == 3

def test_no_um():
    assert count("Hello, world!") == 0
    assert count("The quick brown fox jumps over the lazy dog.") == 0

def test_um_within_words():
    assert count("humble umbrella") == 0
    assert count("drum") == 0

def test_um_as_whole_word():
    assert count("umbrella") == 0
    assert count("album") == 0

from src.game import validate_guess

def test_empty_input():
    valid, msg = validate_guess("", [])
    assert valid is False
    assert msg == "empty"

def test_multiple_characters():
    valid, msg = validate_guess("ab", [])
    assert valid is False
    assert msg == "multiple"

def test_non_alpha():
    valid, msg = validate_guess("7", [])
    assert valid is False
    assert msg == "nonalpha"

def test_repeated_letter():
    valid, msg = validate_guess("a", ["a"])
    assert valid is False
    assert msg == "repeat"

def test_valid_letter():
    valid, msg = validate_guess("a", [])
    assert valid is True
    assert msg == "a"

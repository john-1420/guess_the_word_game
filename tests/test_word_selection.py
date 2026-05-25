import json
from pathlib import Path
from src.gameplay.words import select_word

def load_words():
    data_path = Path(__file__).resolve().parents[1] / "data" / "words.json"
    with open(data_path, "r") as f:
        return json.load(f)

def test_select_word_valid_category_and_difficulty():
    words = load_words()
    word = select_word("animals", "easy")
    assert word in words["animals"]["easy"]

def test_select_word_other_difficulty():
    words = load_words()
    word = select_word("food", "hard")
    assert word in words["food"]["hard"]

def test_invalid_category_raises_keyerror():
    try:
        select_word("invalid_category", "easy")
        assert False, "Expected KeyError"
    except KeyError:
        assert True

def test_invalid_difficulty_raises_keyerror():
    try:
        select_word("animals", "invalid_diff")
        assert False, "Expected KeyError"
    except KeyError:
        assert True
import json
from pathlib import Path
from src.game import select_word

def load_words():
    """Helper to load the JSON word lists for comparison."""
    data_path = Path(__file__).resolve().parents[1] / "data" / "words.json"
    with open(data_path, "r") as f:
        return json.load(f)

def test_level_1_word_selection():
    words = load_words()
    word = select_word(1)
    assert word in words["normal"]

def test_level_2_word_selection():
    words = load_words()
    word = select_word(2)
    assert word in words["advanced"]

def test_invalid_level_raises_error():
    try:
        select_word(999)
        assert False, "Expected ValueError for invalid level"
    except ValueError:
        assert True

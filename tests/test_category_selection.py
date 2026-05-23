from src.gameplay.words import select_word

def test_select_word_returns_string(config):
    word = select_word("animals", "easy")
    assert isinstance(word, str)
    assert len(word) > 0

def test_select_word_valid_category(config):
    word = select_word("food", "normal")
    assert word.isalpha()

def test_select_word_difficulty_levels(config):
    for diff in ["easy", "normal", "hard"]:
        word = select_word("animals", diff)
        assert isinstance(word, str)
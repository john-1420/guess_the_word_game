from src.gameplay.core import GuessGame

def test_full_round_scoring(monkeypatch, config):
    # Force the word to "cat"
    monkeypatch.setattr("src.gameplay.core.select_word", lambda c, d: "cat")

    # Simulate user input: c, a, t
    inputs = iter(["c", "a", "t"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    score = GuessGame(config, "animals", "easy")
    assert score > 0
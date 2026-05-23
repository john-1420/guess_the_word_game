from src.persistence.highscores import save_highscore, load_highscores
from pathlib import Path
import json

def test_highscore_persistence(tmp_path, monkeypatch):
    fake_path = tmp_path / "highscores.json"
    monkeypatch.setattr("src.persistence.highscores.HIGHSCORE_PATH", fake_path)

    save_highscore("Alice", 30)
    save_highscore("Bob", 40)

    data = load_highscores()

    assert len(data["scores"]) == 2
    assert data["scores"][0]["score"] == 40  # highest first
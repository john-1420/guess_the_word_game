from src.persistence.highscores import load_highscores, save_highscore
from pathlib import Path
import json

def test_highscore_save_and_load(tmp_path, monkeypatch):
    # Redirect highscores.json to a temporary file
    fake_path = tmp_path / "highscores.json"
    monkeypatch.setattr(
        "src.persistence.highscores.HIGHSCORE_PATH",
        fake_path
    )

    save_highscore("John", 50)
    data = load_highscores()

    assert len(data["scores"]) == 1
    assert data["scores"][0]["name"] == "John"
    assert data["scores"][0]["score"] == 50
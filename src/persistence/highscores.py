# High score loading and saving

import json
from pathlib import Path
from datetime import datetime

HIGHSCORE_PATH = Path(__file__).resolve().parents[2] / "data" / "highscores.json"

def load_highscores():
    """
    Load highscores.json, return structure:
    {
        "scores": [
            {"name": "...", "score": 123, "date": "2025-05-01"},
            ...
        ]
    }
    """
    if not HIGHSCORE_PATH.exists():
        return {"scores": []}

    with open(HIGHSCORE_PATH, "r") as f:
        return json.load(f)


def save_highscore(name, score):
    """
    Append a new high score entry and save back to highscores.json.
    """

    data = load_highscores()

    entry = {
        "name": name,
        "score": score,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    data["scores"].append(entry)

    # Sort by score descending
    data["scores"].sort(key=lambda x: x["score"], reverse=True)

    with open(HIGHSCORE_PATH, "w") as f:
        json.dump(data, f, indent=4)
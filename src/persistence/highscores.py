# High score loading and saving

import json
from pathlib import Path
from datetime import datetime

HIGHSCORE_PATH = Path(__file__).resolve().parents[2] / "data" / "highscores.json"


def load_highscores():
    """
    Load the high score data from highscores.json.

    Returns:
        dict: A dictionary with the structure:
            {
                "scores": [
                    {"name": str, "score": int, "date": "YYYY-MM-DD"},
                    ...
                ]
            }

    Notes:
        - If the file does not exist, an empty structure is returned.
        - No sorting is applied here; scores are returned as stored.
    """
    if not HIGHSCORE_PATH.exists():
        return {"scores": []}

    with open(HIGHSCORE_PATH, "r") as f:
        return json.load(f)


def save_highscore(name, score):
    """
    Save a new high score entry to highscores.json.

    Parameters:
        name (str): The player's name.
        score (int): The player's total score for the session.

    Behaviour:
        - Loads existing high scores.
        - Appends a new entry with the current date.
        - Sorts all scores in descending order.
        - Writes the updated list back to highscores.json.
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
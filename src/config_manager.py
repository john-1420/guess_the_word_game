import json
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "settings.json"

DEFAULT_CONFIG = {
    "default_difficulty": "normal",
    "default_category": "animals",
    "attempts": {
        "easy": 12,
        "normal": 10,
        "hard": 8
    },
    "colour_output": True,
    "logging_level": "INFO"
}

def load_config():
    """
    Load game configuration from config/settings.json.
    Returns a dictionary with configuration values.
    Falls back to safe defaults if the file is missing or corrupted.
    """

    if not CONFIG_PATH.exists():
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_PATH, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        with open(CONFIG_PATH, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG


def save_config(config):
    """
    Save the given configuration dictionary to config/settings.json.
    Ensures the directory exists and writes JSON in a clean, formatted way.
    """

    if not isinstance(config, dict):
        raise ValueError("Config must be a dictionary")

    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

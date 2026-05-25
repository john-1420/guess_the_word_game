# Configuration File Structure

The game uses a JSON configuration file located at:

```
config/settings.json
```

This file controls difficulty behaviour, colour output, logging, and scoring.

---

## Structure

```json
{
  "default_difficulty": "normal",
  "default_category": "animals",

  "colour_output": true,
  "logging_level": "INFO",

  "attempts": {
    "easy": 12,
    "normal": 10,
    "hard": 8
  },

  "hint_penalty": {
    "easy": 1,
    "normal": 2,
    "hard": 3
  },

  "scoring": {
    "difficulty_multiplier": {
      "easy": 1,
      "normal": 2,
      "hard": 3
    }
  }
}

```

### Field Descriptions

default_difficulty
The difficulty selected automatically when starting a new game.

default_category
The category pre‑selected when starting a new game.

colour_output
Enables or disables colourised terminal output.

logging_level
Controls verbosity:

- "INFO" — standard gameplay logs

- "DEBUG" — includes chosen words and internal details

attempts
Number of attempts per difficulty.

hint_penalty
Attempts deducted when the player uses a hint.

scoring.difficulty_multiplier
Multiplier applied to attempts remaining when calculating score.

Editing the Config

Users can modify the config manually or through the in‑game Settings menu.
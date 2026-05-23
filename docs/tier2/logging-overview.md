# Logging Overview

The game uses Python’s built‑in logging module to record gameplay events, errors, and debugging information.

Logs are stored in:

```
logs/game.log
```

---

## Logging Levels

The logging level is controlled by `settings.json`:

- **INFO** — default, logs major events  
- **DEBUG** — logs detailed internal information  

---

## What Gets Logged

### Gameplay Events
- Game start and end  
- Selected difficulty  
- Selected category  
- User guesses  
- Hint usage  
- Round score  

### Debug Information (DEBUG mode only)
- The chosen word  
- Internal scoring calculations  

### Errors
- Any unhandled exceptions  
- File loading issues  
- Invalid configuration  

---

## Purpose of Logging

Logging helps with:

- Debugging gameplay issues  
- Analysing player behaviour  
- Testing and verifying game logic  
- Tracking errors in production environments  

---

## Example Log Entries

```
2026-05-21 14:32:10 [INFO] Selected difficulty: normal
2026-05-21 14:32:12 [DEBUG] Chosen word: elephant
2026-05-21 14:32:20 [INFO] User guessed: e
2026-05-21 14:32:45 [INFO] Round score: 18
```
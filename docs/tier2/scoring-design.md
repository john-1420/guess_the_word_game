# Scoring System Design

The scoring system rewards efficient guessing while applying penalties for using hints.  
All scoring behaviour is fully configurable through `settings.json`.

---

## Overview

Each round produces a score based on:

- Attempts remaining
- Difficulty multiplier
- Number of hints used
- Hint penalty per difficulty

The final score is always **non‑negative**.

---

## Formula

```
base_score = attempts_left * difficulty_multiplier
penalty = hints_used * hint_penalty
final_score = max(base_score - penalty, 0)
```

---

## Difficulty Multipliers

Defined in `settings.json`:

| Difficulty | Multiplier |
|-----------|------------|
| easy      | 1×         |
| normal    | 2×         |
| hard      | 3×         |

Higher difficulty = higher reward.

---

## Hint Penalties

Hints reveal a random letter but cost attempts.

Example (configurable):

| Difficulty | Penalty per hint |
|-----------|------------------|
| easy      | 1                |
| normal    | 2                |
| hard      | 3                |

---

## Example Calculations

### Example 1 — Normal Difficulty
- Attempts left: 6  
- Multiplier: 2  
- Hints used: 1  
- Hint penalty: 2  

```
base_score = 6 * 2 = 12
penalty = 1 * 2 = 2
final_score = 10
```

### Example 2 — Hard Difficulty, many hints
- Attempts left: 3  
- Multiplier: 3  
- Hints used: 2  
- Hint penalty: 3  

```
base_score = 3 * 3 = 9
penalty = 2 * 3 = 6
final_score = 3
```

---

## Design Goals

- Reward skillful play  
- Encourage guessing over hint‑spamming  
- Scale difficulty meaningfully  
- Keep scoring transparent and predictable  
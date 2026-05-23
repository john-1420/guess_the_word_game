# Score calculation logic

import logging

def calculate_score(attempts_left, difficulty, hints_used, config):
    """
    Calculate the player's score for a single round.

    Parameters:
        attempts_left (int): Number of attempts remaining at the end of the round.
        difficulty (str): Difficulty level ("easy", "normal", "hard").
        hints_used (int): Total number of hints used during the round.
        config (dict): Configuration settings containing scoring multipliers
                       and hint penalties.

    Returns:
        int: The final score for the round (never negative).

    Scoring Formula:
        base_score = attempts_left * difficulty_multiplier
        penalty = hints_used * hint_penalty
        final_score = max(base_score - penalty, 0)

    Notes:
        - Difficulty multipliers and hint penalties are defined in settings.json.
        - All scoring events are logged for debugging and analytics.
    """

    multiplier = config["scoring"]["difficulty_multiplier"][difficulty]
    base_score = attempts_left * multiplier

    penalty = hints_used * config["hint_penalty"][difficulty]

    final_score = base_score - penalty
    final_score = max(final_score, 0)

    logging.info(
        f"Score calculated: {final_score} "
        f"(difficulty={difficulty}, attempts_left={attempts_left}, hints_used={hints_used})"
    )

    return final_score
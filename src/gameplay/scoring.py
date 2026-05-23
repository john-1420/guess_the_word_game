# Score calculation logic

import logging

def calculate_score(attempts_left, difficulty, hints_used, config):
    """
    Calculate round score using config-driven multipliers and penalties.
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
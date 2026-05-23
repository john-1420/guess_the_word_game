# Input validation and user input handling

from src.ui.display import apply_color, YELLOW
import logging


def validate_guess(guess, guessed_letters):
    """
    Validate a single-character guess.
    Returns (valid: bool, result: str)
    """

    guess = guess.strip().lower()

    if guess == "":
        return False, "empty"

    if len(guess) > 1:
        return False, "multiple"

    if not guess.isalpha():
        return False, "nonalpha"

    if guess in guessed_letters:
        return False, "repeat"

    return True, guess


def get_user_input(guessed_letters, config):
    """
    Prompt the user for a valid guess or 'hint'.
    """

    while True:
        guess = input("Please type in a letter (or type 'hint' for help): ").strip().lower()

        if guess == "hint":
            logging.info("User requested a hint")
            return "hint"

        valid, result = validate_guess(guess, guessed_letters)

        if not valid:
            if result == "empty":
                print(apply_color("Did you forget something? :o", YELLOW, config))
            elif result == "multiple":
                print(apply_color("Type ONE letter please.", YELLOW, config))
            elif result == "nonalpha":
                print(apply_color("Only letters are allowed!", YELLOW, config))
            elif result == "repeat":
                print(apply_color("That letter has been used already!", YELLOW, config))
            continue

        # Valid guess
        guessed_letters.append(result)
        logging.info(f"User guessed: {result}")
        return result
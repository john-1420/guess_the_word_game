# Input validation and user input handling

from src.ui.display import apply_color, YELLOW
import logging


def validate_guess(guess, guessed_letters):
    """
    Validate a player's guess and classify any invalid input.

    Parameters:
        guess (str): The raw user input to validate.
        guessed_letters (list[str]): Letters already guessed in this round.

    Returns:
        tuple:
            - bool: True if the guess is valid, False otherwise.
            - str: Either the cleaned guess (lowercase) or an error code:
                   "empty", "multiple", "nonalpha", "repeat".

    Behaviour:
        - Ensures the guess is non-empty.
        - Ensures only one character is entered.
        - Ensures the guess is alphabetic.
        - Ensures the letter has not been guessed before.
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
    Prompt the user for a valid letter guess or the 'hint' command.

    Parameters:
        guessed_letters (list[str]): Letters already guessed in this round.
        config (dict): Configuration settings for colour output.

    Returns:
        str: Either a valid single-letter guess or the string "hint".

    Behaviour:
        - Accepts the special command "hint".
        - Validates all other input using validate_guess().
        - Prints colour-coded feedback for invalid input.
        - Appends valid guesses to guessed_letters.
        - Logs all user actions.
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
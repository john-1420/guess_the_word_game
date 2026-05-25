# Core gameplay loop (GuessGame) and attempt/hint logic

import time
import logging

from src.gameplay.words import select_word, reveal_random_letter
from src.gameplay.input import get_user_input
from src.gameplay.scoring import calculate_score
from src.ui.display import apply_color, update_display, GREEN, RED, YELLOW

def GuessGame(config, category, difficulty):
    """
    Run a single round of the Guess The Word game.

    Parameters:
        config (dict): Configuration settings loaded from settings.json.
                       Includes attempts per difficulty, hint penalties,
                       colour mode, and logging level.
        category (str): The selected word category (e.g., "animals", "food").
        difficulty (str): The chosen difficulty level ("easy", "normal", "hard").

    Returns:
        int: The player's score for this round, calculated using:
             - attempts remaining
             - difficulty multiplier
             - number of hints used

    Gameplay Flow:
        - Selects a random word based on category + difficulty.
        - Initializes attempts and hint counters.
        - Displays the hidden word as underscores.
        - Repeatedly prompts the user for input:
            * Normal letter guesses
            * "hint" command to reveal a random letter (with penalty)
        - Updates the displayed word after each guess.
        - Ends the round when:
            * The word is fully revealed, or
            * Attempts reach zero.
        - Calculates and returns the round score.

    Notes:
        - All user interactions (guesses, hints, results) are logged.
        - Hint penalties and attempt scaling are defined in settings.json.
    """

    # Select word
    word = select_word(category, difficulty)
    logging.debug(f"Chosen word: {word}")

    attempts = config["attempts"][difficulty]
    hints_used = 0

    # Initial display
    word_display = "_" * len(word)
    update_display(word_display, config)

    guessed = []

    while attempts > 0:
        guess = get_user_input(guessed, config)
        logging.info(f"User guessed: {guess}")

        # -------------------------
        # HINT HANDLING
        # -------------------------
        if guess == "hint":
            hints_used += 1
            penalty = config["hint_penalty"][difficulty]
            attempts -= penalty

            print(apply_color(
                f"\nHint used! Revealing a letter... (-{penalty} attempts)",
                YELLOW, config
            ))

            word_display = reveal_random_letter(word, word_display)
            update_display(word_display, config)

            # Word completed by hint
            if word_display == word:
                time.sleep(2)
                print(apply_color(f"\nThe word is {word}!", GREEN, config))
                print(apply_color("Well done!", GREEN, config))

                round_score = calculate_score(attempts, difficulty, hints_used, config)
                logging.info(f"Round score: {round_score}")
                print(f"Score for this round: {round_score}")
                return round_score

            # Out of attempts after hint
            if attempts <= 0:
                time.sleep(2)
                print(apply_color(f"\nNo attempts left! The word was {word}", RED, config))

                round_score = calculate_score(attempts, difficulty, hints_used, config)
                logging.info(f"Round score: {round_score}")
                print(f"Score for this round: {round_score}")
                return round_score

            continue

        # -------------------------
        # NORMAL GUESS HANDLING
        # -------------------------
        from src.gameplay.check import check_guess  # We'll move this in Wave 6 if needed

        word_display, attempts, correct = check_guess(guess, word, word_display, attempts)

        if not correct:
            if attempts > 0:
                print(apply_color(f"Try again. Attempts left: {attempts}", RED, config))
            else:
                time.sleep(2)
                print(apply_color(f"\nNo attempts left! The word was {word}", RED, config))

                round_score = calculate_score(attempts, difficulty, hints_used, config)
                logging.info(f"Round score: {round_score}")
                print(f"Score for this round: {round_score}")
                return round_score

        else:
            # Word completed by correct guess
            if word_display == word:
                time.sleep(2)
                print(apply_color(f"\nThe word is {word}!", GREEN, config))
                print(apply_color("Well done!", GREEN, config))

                round_score = calculate_score(attempts, difficulty, hints_used, config)
                logging.info(f"Round score: {round_score}")
                print(f"Score for this round: {round_score}")
                return round_score

        update_display(word_display, config)
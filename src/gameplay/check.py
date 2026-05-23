def check_guess(guess, word, word_display, attempts):
    """
    Evaluate a player's guessed letter and update game state accordingly.

    Parameters:
        guess (str): The letter guessed by the player.
        word (str): The target word the player is trying to guess.
        word_display (str): The current revealed state of the word (e.g., "_p_l_").
        attempts (int): The number of attempts remaining before the guess.

    Returns:
        tuple:
            - str: Updated word display after applying the guess.
            - int: Updated number of attempts remaining.
            - bool: True if the guess was correct, False otherwise.

    Behaviour:
        - If the guess is in the word, all matching positions are revealed.
        - If incorrect, one attempt is deducted.
    """

    correct = guess in word

    if correct:
        # Reveal all matching letters
        new_display = list(word_display)
        for i, letter in enumerate(word):
            if letter == guess:
                new_display[i] = guess
        return "".join(new_display), attempts, True

    else:
        # Wrong guess → lose 1 attempt
        attempts -= 1
        return word_display, attempts, False
def check_guess(guess, word, word_display, attempts):
    """
    Check if the guessed letter is in the word.
    Returns updated (word_display, attempts, correct)
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
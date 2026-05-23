# Word selection and letter reveal logic

import json
import random
import logging
from pathlib import Path


def select_word(category, difficulty):
    """
    Select a random word from the words.json file based on category and difficulty.

    Parameters:
        category (str): The chosen word category (e.g., "animals", "food").
        difficulty (str): The difficulty level ("easy", "normal", "hard").

    Returns:
        str: A randomly selected word in lowercase.

    Behaviour:
        - Loads words.json from the data directory.
        - Retrieves the list of words for the given category and difficulty.
        - Chooses one word at random.
        - Logs the chosen word at DEBUG level.
    """
    data_path = Path(__file__).resolve().parents[2] / "data" / "words.json"

    with open(data_path, "r") as f:
        words = json.load(f)

    word_list = words[category][difficulty]
    word = random.choice(word_list).lower()

    logging.debug(f"Chosen word: {word}")
    return word


def reveal_random_letter(word, word_display):
    """
    Reveal one random hidden letter in the displayed word.

    Parameters:
        word (str): The full target word.
        word_display (str): The current display state (e.g., "_p_l_").

    Returns:
        str: Updated word display with one hidden letter revealed.

    Behaviour:
        - Finds all indices where the display still shows "_".
        - Randomly selects one of those positions.
        - Reveals the corresponding letter from the actual word.
        - If no hidden letters remain, returns the display unchanged.
    """
    hidden_indices = [i for i, ch in enumerate(word_display) if ch == "_"]

    if not hidden_indices:
        return word_display  # nothing to reveal

    index = random.choice(hidden_indices)
    letter = word[index]

    new_display = list(word_display)
    new_display[index] = letter

    return "".join(new_display)
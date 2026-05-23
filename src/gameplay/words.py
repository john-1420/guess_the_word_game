# Word selection and letter reveal logic

import json
import random
import logging
from pathlib import Path


def select_word(category, difficulty):
    """
    Load words.json and select a random word from the given category/difficulty.
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
    Reveal one random hidden letter in the word.
    """

    hidden_indices = [i for i, ch in enumerate(word_display) if ch == "_"]

    if not hidden_indices:
        return word_display  # nothing to reveal

    index = random.choice(hidden_indices)
    letter = word[index]

    new_display = list(word_display)
    new_display[index] = letter

    return "".join(new_display)

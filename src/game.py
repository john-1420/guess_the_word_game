#In this program the user is required to guess every letter of a given unknown word.
#Date: 23/03/2023
#Written by: John Razak
#Updated: 21/05/2026
#=============================================

from pathlib import Path
from src.config_manager import load_config, save_config
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)

import time
import random
import json
import logging

GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

def apply_color(text, color, config):
    if config.get("colour_output", True):
        return f"{color}{text}{RESET}"
    return text

# Create logs directory if missing
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "game.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,  # default, will be overridden by config
    format="%(asctime)s [%(levelname)s] %(message)s",
    filemode="a"
)

def load_highscores():
    path = Path(__file__).parent.parent / "data" / "highscores.json"

    if not path.exists():
        return {"scores": []}

    with open(path, "r") as f:
        return json.load(f)

def save_highscore(name, score):
    path = Path(__file__).parent.parent / "data" / "highscores.json"

    data = load_highscores()

    entry = {
        "name": name,
        "score": score,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    data["scores"].append(entry)

    # Sort by score descending
    data["scores"] = sorted(data["scores"], key=lambda x: x["score"], reverse=True)

    # Keep only top 10
    data["scores"] = data["scores"][:10]

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

#This function returns a word based on the category and difficulty the user selected.
def select_word(category, difficulty):
    data_path = Path(__file__).parent.parent / "data" / "words.json"
    with open(data_path, "r") as f:
        words = json.load(f)

    word_list = words[category][difficulty]
    return random.choice(word_list)

def validate_guess(guess, char_check):
    """
    Validate a guessed character without requiring user input.
    Used for automated testing.

    Args:
        guess (str): The raw user input.
        char_check (list[str]): Letters already guessed.

    Returns:
        tuple:
            bool: True if valid, False otherwise.
            str: Error message or cleaned guess.
    """
    guess = guess.strip().lower()

    if guess == "":
        return False, "empty"

    if len(guess) > 1:
        return False, "multiple"

    if not guess.isalpha():
        return False, "nonalpha"

    if guess in char_check:
        return False, "repeat"

    return True, guess

#This function handles the error trapping part, for when the user: presses enter, types two or more letters, types a number or types a character that has already been evaluated.
def get_user_input(char_check, config):
    """
    Prompt the user for a single valid letter guess.
    """

    while True:
        guess = input("Please type in a letter (or type 'hint' for help): ").strip().lower()

        if guess == "hint":
            return "hint"

        valid, result = validate_guess(guess, char_check)

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

        # valid guess
        char_check.append(result)
        return result

#This function checks if the guess was correct or not and it returns the word to be displayed, the number of tries and a boolean for if the word has been guessed.
def check_guess(guess, word, word_display, tries):
    """
    Evaluate the user's guess and update the game state.

    Args:
        guess (str): The letter guessed by the user.
        word (str): The target word to guess.
        word_display (str): The current display string with revealed letters.
        tries (int): Number of remaining attempts.

    Returns:
        tuple:
            str: Updated display string.
            int: Updated number of tries.
            bool: True if the guess was correct, False otherwise.
    """

    correct = False

    # Reveal letters
    new_display = list(word_display)
    for i, letter in enumerate(word):
        if letter == guess:
            new_display[i] = guess
            correct = True

    updated_display = "".join(new_display)

    # If incorrect, reduce tries
    if not correct:
        tries -= 1

    return updated_display, tries, correct

#This function prints the updated word after the guess has been made
def update_display(word_display, config):
    """
    Display the current state of the word to the user.
    """
    text = " ".join(word_display)
    print(apply_color("\n" + text, CYAN, config))

def reveal_random_letter(word, word_display):
    """
    Reveal one random hidden letter in the word.
    """
    hidden_indices = [i for i, ch in enumerate(word_display) if ch == "_"]

    if not hidden_indices:
        return word_display  # nothing to reveal

    index = random.choice(hidden_indices)
    letter = word[index]

    # rebuild the display string with the revealed letter
    new_display = list(word_display)
    new_display[index] = letter

    return "".join(new_display)

def calculate_score(attempts_left, difficulty, hints_used, config):
    multiplier = config["scoring"]["difficulty_multiplier"][difficulty]
    base_score = attempts_left * multiplier

    penalty = hints_used * config["hint_penalty"][difficulty]

    final_score = base_score - penalty
    return max(final_score, 0)

#This function operates the main part of the game. Based on the difficulty and category choosed by the user, it will fetch a word from one of the two lists and prompt the user to guess each letter until the word is completed or there are no tries left.
def GuessGame(config, category, difficulty):
    word = select_word(category, difficulty)
    logging.debug(f"Chosen word: {word}")
    attempts = config["attempts"][difficulty]
    hints_used = 0

    word_display = "_" * len(word)
    update_display(word_display, config)

    guessed = []

    while attempts > 0:
        guess = get_user_input(guessed, config)
        logging.info(f"User guessed: {guess}")

        # HINT HANDLING
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

            if word_display == word:
                time.sleep(2)
                print(apply_color(f"\nThe word is {word}!", GREEN, config))
                print(apply_color("Well done!", GREEN, config))
                round_score = calculate_score(attempts, difficulty, hints_used, config)
                print(f"Score for this round: {round_score}")
                return round_score

            if attempts <= 0:
                time.sleep(2)
                print(apply_color(f"\nNo attempts left! The word was {word}", RED, config))
                round_score = calculate_score(attempts, difficulty, hints_used, config)
                print(f"Score for this round: {round_score}")
                return round_score

            continue

        # NORMAL GUESS HANDLING
        word_display, attempts, correct = check_guess(guess, word, word_display, attempts)

        if not correct:
            if attempts > 0:
                print(apply_color(f"Try again. Attempts left: {attempts}", RED, config))
            else:
                time.sleep(2)
                print(apply_color(f"\nNo attempts left! The word was {word}", RED, config))
                round_score = calculate_score(attempts, difficulty, hints_used, config)
                print(f"Score for this round: {round_score}")
                return round_score
        else:
            if word_display == word:
                time.sleep(2)
                print(apply_color(f"\nThe word is {word}!", GREEN, config))
                print(apply_color("Well done!", GREEN, config))
                round_score = calculate_score(attempts, difficulty, hints_used, config)
                print(f"Score for this round: {round_score}")
                return round_score

        update_display(word_display, config)

#Prints the rules of the game.
def choose_difficulty(config):
    valid = ["easy", "normal", "hard"]
    while True:
        difficulty = input("Choose difficulty (easy, normal, hard): ").lower().strip()
        if difficulty in valid:
            return difficulty
        print(apply_color("Invalid choice. Please choose easy, normal, or hard.", YELLOW, config))

def select_category(words_data, config):
    categories = list(words_data.keys())

    print("\nAvailable categories:")
    for i, cat in enumerate(categories, start=1):
        print(f"[{i}] {cat.capitalize()}")

    while True:
        choice = input("Choose a category by number: ").strip()

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(categories):
                return categories[index]

        print(apply_color("Invalid choice. Please select a valid category number.", YELLOW, config))

def main_menu(config):
    print(apply_color("\nMAIN MENU", CYAN, config))
    print(apply_color("[1] Play Game", MAGENTA, config))
    print(apply_color("[2] View High Scores", MAGENTA, config))
    print(apply_color("[3] Settings", MAGENTA, config))
    print(apply_color("[4] Exit", MAGENTA, config))

    while True:
        choice = input("Choose an option: ").strip()
        if choice in ["1", "2", "3", "4"]:
            return choice
        print(apply_color("Invalid choice.", YELLOW, config))

def display_highscores(config):
    data = load_highscores()

    print(apply_color("\n=== HIGH SCORES ===", CYAN, config))
    if not data["scores"]:
        print(apply_color("No high scores yet.", YELLOW, config))
        return

    for i, entry in enumerate(data["scores"], start=1):
        print(apply_color(
            f"{i}. {entry['name']} - {entry['score']} pts ({entry['date']})",
            MAGENTA, config
        ))

def settings_menu(config):
    while True:
        print(apply_color("\n=== SETTINGS ===", CYAN, config))
        print(f"{MAGENTA}[1]{RESET} Toggle Colour Mode (currently: {config['colour_output']})")
        print(f"{MAGENTA}[2]{RESET} Toggle Logging Level (currently: {config['logging_level']})")
        print(f"{MAGENTA}[3]{RESET} Save & Return")
        print(f"{MAGENTA}[4]{RESET} Cancel")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            config["colour_output"] = not config["colour_output"]
            print(apply_color(f"Colour mode set to {config['colour_output']}", GREEN, config))

        elif choice == "2":
            config["logging_level"] = "DEBUG" if config["logging_level"] == "INFO" else "INFO"
            print(apply_color(f"Logging level set to {config['logging_level']}", GREEN, config))

        elif choice == "3":
            save_config(config)
            print(apply_color("Settings saved!", GREEN, config))
            return

        elif choice == "4":
            print(apply_color("Changes discarded.", YELLOW, config))
            return

        else:
            print(apply_color("Invalid choice.", YELLOW, config))

def main():
    config = load_config()

    # Apply logging level
    level = logging.DEBUG if config["logging_level"] == "DEBUG" else logging.INFO
    logging.getLogger().setLevel(level)

    print(apply_color("Welcome to GUESS THE WORD game! Hope you enjoy it! ;)\n", CYAN, config))
    time.sleep(2)

    print("Now... Let's get to know you better, shall we?\n")
    name = input("How shall I call you? ")
    time.sleep(2)

    print(apply_color(f"Nice to meet you, {name}!\n", GREEN, config))
    time.sleep(2)

    total_score = 0

    while True:
        choice = main_menu(config)

        if choice == "1":
            config = load_config()

            data_path = Path(__file__).parent.parent / "data" / "words.json"
            with open(data_path, "r") as f:
                words_data = json.load(f)

            category = select_category(words_data, config)
            logging.info(f"Selected category: {category}")
            difficulty = choose_difficulty(config)
            logging.info(f"Selected difficulty: {difficulty}")

            logging.info("Game started")
            round_score = GuessGame(config, category, difficulty)
            logging.info("Game ended")
            total_score += round_score
            logging.info(f"Round score: {round_score}")
            logging.info(f"Total score: {total_score}")

            print(f"Total score so far: {total_score}")
            time.sleep(2)

        elif choice == "2":
            display_highscores(config)
            time.sleep(2)

        elif choice == "3":
            config = load_config()
            settings_menu(config)
            time.sleep(1)

        elif choice == "4":
            print(f"\nYour final total score is: {total_score}")

            if total_score > 0:
                save_highscore(name, total_score)
                print("Your score has been saved to the high scores!")
            else:
                print("No score to save.")

            print("Thanks for playing! :)")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.exception("Unhandled exception occurred")
        raise
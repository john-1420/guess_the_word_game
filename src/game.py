#In this program the user is required to guess every letter of a given unknown word.
#Date: 23/03/2023
#Written by: John Razak
#Updated: 21/05/2026
#=============================================

import json
import time
import logging
from pathlib import Path

from src.config_manager import load_config, save_config
from src.gameplay.core import GuessGame
from src.ui.menu import main_menu, display_highscores, settings_menu
from src.ui.display import apply_color, YELLOW, CYAN, GREEN
from src.persistence.highscores import save_highscore

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

            data_path = Path(__file__).resolve().parents[1] / "data" / "words.json"
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
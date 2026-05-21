#In this program the user is required to guess every letter of a given unknown word.
#Date: 23/03/2023
#Written by: John Razak
#Updated: 19/05/2026
#=============================================

from src.config_manager import load_config, save_config

import time
import random
import json
from pathlib import Path

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
def get_user_input(char_check):
    """
    Prompt the user for a single valid letter guess.

    Ensures the input is:
    - non-empty
    - a single character
    - alphabetic
    - not previously guessed

    Args:
        char_check (list[str]): List of letters already guessed.

    Returns:
        str: A validated lowercase letter.
    """

    while True:
        guess = input("Please type in a letter (or type 'hint' for help): ").strip().lower()

        if guess == "hint":
            return "hint"

        valid, result = validate_guess(guess, char_check)

        if not valid:
            if result == "empty":
                print("Did you forget something? :o\n")
            elif result == "multiple":
                print("Type ONE letter please.\n")
            elif result == "nonalpha":
                print("Only letters are allowed!\n")
            elif result == "repeat":
                print("That letter has been used already!\n")
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
def update_display(word_display):
    """
    Display the current state of the word to the user.

    Args:
        word_display (str): The string showing revealed and hidden letters.
    """

    print("\n", " ".join(word_display))

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

#This function operates the main part of the game. Based on the difficulty and category choosed by the user, it will fetch a word from one of the two lists and prompt the user to guess each letter until the word is completed or there are no tries left.
def GuessGame(config, category, difficulty):
    word = select_word(category, difficulty) # updated selector
    attempts = config["attempts"][difficulty]

    word_display = "_" * len(word)
    update_display(word_display)

    guessed = []

    while attempts > 0:
        guess = get_user_input(guessed)

        # HINT HANDLING
        if guess == "hint":
            penalty = config["hint_penalty"][difficulty]
            attempts -= penalty

            print(f"\nHint used! Revealing a letter... (-{penalty} attempts)")
            word_display = reveal_random_letter(word, word_display)
            update_display(word_display)

            # ⭐ NEW: Check if the word is now complete
            if word_display == word:
                print(f"\nThe word is {word}!")
                print("Well done!")
                break

            if attempts <= 0:
                print(f"\nNo attempts left! The word was {word}")
                break

            continue
        
        # NORMAL GUESS HANDLING
        word_display, attempts, correct = check_guess(guess, word, word_display, attempts)

        if not correct:
            if attempts > 0:
                print(f"Try again. You have {attempts} attempts left.")
            else:
                print(f"\nSorry, no attempts left. The word was {word}")
                break
        else:
            # After revealing a letter
            if word_display == word:
                print(f"\nThe word is {word}!")
                print("Well done!")
                break

        update_display(word_display)

#Prints the rules of the game.
def choose_difficulty(config):
    valid = ["easy", "normal", "hard"]
    while True:
        difficulty = input("Choose difficulty (easy, normal, hard): ").lower().strip()
        if difficulty in valid:
            return difficulty
        print("Invalid choice. Please choose easy, normal, or hard.")

def select_category(words_data):
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

        print("Invalid choice. Please select a valid category number.")

def main():
    #Prints a welcome message.
    print("Hello there! This is the ##GUESS THE WORD## game! Hope you enjoy it! ;)\n")

    time.sleep(2)

    print("Now..Let's get to know you better, shall we?\n")

    #Accepts a name from the user.
    name=input("How shall I call you?")

    time.sleep(2)

    print("\nNice to meet you", name, "!\n")

    time.sleep(2)

    #Setting a loop to enable the user to play multiple times.
    play_again="y"
    while play_again=="y":

        config = load_config()

        # Load words.json once
        data_path = Path(__file__).parent.parent / "data" / "words.json"
        with open(data_path, "r") as f:
            words_data = json.load(f)

        category = select_category(words_data)
        difficulty = choose_difficulty(config)

        GuessGame(config, category, difficulty)

        time.sleep(3)

        #Prompts the user to choose wether to continue playing or to exit.
        play_again=input("\nDo you want to continue? (Y or any key to exit):\n")
        play_again=play_again.lower()

    print("Thanks for playing! :)")

if __name__ == "__main__":
    main()
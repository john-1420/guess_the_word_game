#In this program the user is required to guess every letter of a given unknown word.
#Date: 23/03/2023
#Written by: John Razak
#Updated: 19/05/2026
#=============================================

import time
import random
import json
from pathlib import Path

#This function returns a word based on the level the user selected.
def select_word(level):
    """
    Select a random word based on the chosen difficulty level.

    Args:
        level (int): Difficulty level selected by the user (1 = normal, 2 = advanced).

    Returns:
        str: A randomly selected word from the appropriate word list.

    Raises:
        ValueError: If an invalid level is provided.
    """

    # Load JSON file
    data_path = Path(__file__).parent.parent / "data" / "words.json"
    with open(data_path, "r") as f:
        words = json.load(f)

    if level == 1:
        return random.choice(words["normal"])
    elif level == 2:
        return random.choice(words["advanced"])
    else:
        raise ValueError("Invalid level selected")

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
        guess = input("Please type in a letter: ").strip().lower()

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

#This function operates the main part of the game. Based on the level choosed by the user, it will fetch a word from one of the two lists and prompt the user to guess each letter until the word is completed or there are no tries left.
def GuessGame(level):
    """
    Run a full round of the Guess The Word game.

    Handles:
    - word selection
    - user input loop
    - guess checking
    - display updates
    - win/lose conditions

    Args:
        level (int): Difficulty level selected by the user.
    """

    #It runs when level==1. Essentially it chooses a random word from a list (normalGame) and display it for the user two see how many charecters there are, and set the tries to 10.
    if level==1 :
        word = select_word(level)
        word_display=""
        for letter in word:
            word_display=word_display +"_"
        update_display(word_display)
        tries=10
        char_check=[]
        while tries!=0:
            guess = get_user_input(char_check)
            #In this part the user's letter is being compared to each letter of the word and if there is a correspondence the letter is unveiled, else a message is being displayed and the number of tries reduces by one. This goes on until the word is guessed or the are no tries left.
            word_display, tries, correct = check_guess(guess, word, word_display, tries)
            if not correct:
                if tries > 0:
                    print("Try again. You have,", tries, "tries left")
                else:
                    print("\nSorry, no lives left. The word was,", word)
                    break
            else:
                if word_display == word:
                    print("\nThe word is,", word, "!")
                    print("Well done! :)")
                    break
            update_display(word_display)
    #It runs when level==2. It works just like when level==1, only difference being the word is being fetched from a different list (advanceGame).
    elif level==2 :
        word = select_word(level)
        word_display=""
        for letter in word:
            word_display=word_display +"_"
        update_display(word_display)
        tries=10
        char_check=[]
        while tries!=0:
            guess = get_user_input(char_check)
            #In this part the user's letter is being compared to each letter of the word and if there is a correspondence the letter is unveiled, else a message is being displayed and the number of tries reduces by one. This goes on until the word is guessed or the are no tries left.
            word_display, tries, correct = check_guess(guess, word, word_display, tries)
            if not correct:
                if tries > 0:
                    print("Try again. You have,", tries, "tries left")
                else:
                    print("\nSorry, no lives left. The word was,", word)
                    break
            else:
                if word_display == word:
                    print("\nThe word is,", word, "!")
                    print("Well done! :)")
                    break
            update_display(word_display)
    else:
        #Error trapping for when the user does not select any of the available levels.
        print("Ooops! You didn't select any of the available levels!")

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

    #Prints the rules of the game.
    print(
    """

            Available levels for you to play:

            PRESS 1 OR 2 ON THE KEYBOARD

        [1]=NORMAL: You will have to guess a word that can
                have up to 8 characters.

        [2]=ADVANCE: You will have to guess a word that can
                have up to 10 characters.

        ##ATTENTION! You will have only 10 attempts
                to guess each letter of the word.##


                                            """)

    time.sleep(3)
    #Setting a loop to enable the user to play multiple times.
    play_again="y"
    while play_again=="y":

        #Error trapping for when the user does not type a digit.
        while True:
            try:
                level=int(input("Which level do you want to play? [1] or [2]"))
                break
            except ValueError:
                print("Please type either 1 or 2.\n")

        #Prints a message to the screen when the condition is met and makes a function call, starting the game.
        if level==1 or level==2 :
            print("\nAlright! Let's start!")

        GuessGame(level)

        time.sleep(3)

        #Prompts the user to choose wether to continue playing or to exit.
        play_again=input("\nDo you want to continue? (Y or any key to exit):\n")
        play_again=play_again.lower()

    print("Thanks for playing! :)")

if __name__ == "__main__":
    main()
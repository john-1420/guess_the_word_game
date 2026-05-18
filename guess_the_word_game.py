#In this program the user is required to guess every letter of a given unknown word.
#Date: 23/03/2023
#Written by: John Razak
#=============================================

#This function operates the main part of the game. Based on the level choosed by the user, it will fetch a word from one of the two lists and prompt the user to guess each letter until the word is completed or there are no tries left.
def GuessGame():
    #It runs when level==1. Essentially it chooses a random word from a list (normalGame) and display it for the user two see how many charecters there are, and set the tries to 10.
    if level==1 :
        import random
        word=random.choice(normalGame)
        word_display=""
        for letter in word:
            word_display=word_display +"_"
        print(" ".join(word_display))
        tries=10
        #This is the error trapping part, for when the user: presses enter, types two or more letters, types a number or types a character that has already been evaluated.
        char_check=[]
        while tries!=0:
            i=True
            while i==True :
                guess=input("Please type in a letter:").strip()
                if guess=="":
                    print("Did you forget something? :o\n")
                elif len(guess)>1:
                    print("Type ONE letter please.\n")
                elif not guess.isalpha():
                    print("Only letters are allowed!\n")
                else:
                    i=False
                    guess=guess.lower()
                    while True:
                        if guess in char_check:
                            print("That letter has been used already!\n")
                            guess=input("Please type in a letter:").lower()
                        else:
                            char_check.append(guess)
                            break
            #In this part the user's letter is being compared to each letter of the word and if there is a correspondence the letter is unveiled, else a message is being displayed and the number of tries reduces by one. This goes on until the word is guessed or the are no tries left.
            for i in range(len(word)):
                if word[i]==guess:
                    word_display=word_display[0:i]+guess+word_display[i+1:]
            if guess not in word:
                tries=tries-1
                if tries>0:
                    print("Try again. You have,", tries, "tries left")
                else:
                    time.sleep(2)
                    print("\nSorry, no lives left. The word was, ", word, ". Better luck next time! :(")
                    break
            if word_display==word:
                print("\nThe word is, ", word, "!")
                time.sleep(2)
                print("Well done! :)")
                break
            print("\n", " ".join(word_display))

    #It runs when level==2. It works just like when level==1, only difference being the word is being fetched from a different list (advanceGame).
    elif level==2 :
        import random
        word=random.choice(advancedGame)
        word_display=""
        for letter in word:
            word_display=word_display +"_"
        print(" ".join(word_display))
        tries=10
        char_check=[]
        while tries!=0:
            i=True
            while i==True :
                guess=input("Please type in a letter:").strip()
                if guess=="":
                    print("Did you forget something? :o\n")
                elif len(guess)>1:
                    print("Type ONE letter please.\n")
                elif not guess.isalpha():
                    print("Only letters are allowed!\n")
                else:
                    i=False
                    guess=guess.lower()
                    while True:
                        if guess in char_check:
                            print("That letter has been used already!\n")
                            guess=input("Please type in a letter:").lower()
                        else:
                            char_check.append(guess)
                            break

            for i in range(len(word)):
                if word[i]==guess:
                    word_display=word_display[0:i]+guess+word_display[i+1:]
            if guess not in word:
                tries=tries-1
                if tries>0:
                    print("Try again. You have,", tries, "tries left")
                else:
                    time.sleep(2)
                    print("\nSorry, no lives left. The word was, ", word,". Better luck next time! :(")
                    break
            if word_display==word:
                print("\nThe word is, ", word, "!")
                time.sleep(2)
                print("Well done! :)")
                break
            print("\n"," ".join(word_display))

    else:
        #Error trapping for when the user does not select any of the available levels.
        print("Ooops! You didn't select any of the available levels!")



import time

#Creating two lists with the words for the game.
normalGame=["weak", "head", "burial", "tip", "chorus", "page", "mark", "score"]

advancedGame=["bike", "innovation", "up", "abolish", "iron", "floor", "economist", "stain"]

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

    GuessGame()

    time.sleep(3)

    #Prompts the user to choose wether to continue playing or to exit.
    play_again=input("\nDo you want to continue? (Y or any key to exit):\n")
    play_again=play_again.lower()

print("Thanks for playing! :)")

"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from
the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken,
and when the game ends, print this out.
"""

import random

randNum = random.randint(1, 9)
userGuess = input("Guess a number between 1-9: ")


def validate_input(guess):
    if 1 <= int(guess) <= 9:
        return True
    else:
        return False


def game():
    randNum = random.randint(1, 9)
    userGuess = input("Guess a number between 1-9: ")

    if validate_input(userGuess) is False:
        input("Invalid entry. Press a key to try again: ")
        game()
    else:
        if userGuess == randNum:
            print("You got it! The computer chose {}!".format(randNum))
        elif userGuess < randNum:
            print("Ooo...a little low there. Try again with a new number!")
            game()
        elif userGuess > randNum:
            print("You guessed too high! Try again with a new number!")
            game()


game()

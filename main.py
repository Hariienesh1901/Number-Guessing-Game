# This is a simple number guessing game.

# Import the random module.
from random import randint
from colorama import Fore, Style

# Asking user required questions.
startRange = int(input(Fore.LIGHTBLUE_EX + "Enter the starting range: "))
endRange = int(input(Fore.LIGHTBLUE_EX + "Enter the ending range: "))
attempts = int(input(Fore.LIGHTBLUE_EX + "Enter the number of attempts: "))

# Generating a random number.
randomNumber = randint(startRange, endRange)

# Calculating the number of attempts.
tries = 0

# Looping the game if they have more attempts.
while tries < attempts:
    # Ask user to guess the number.
    guess = int(input(Fore.LIGHTCYAN_EX + "Guess the number: "))

    if guess == randomNumber:
        print(f"{Fore.GREEN} You guessed the number! In {tries} tries.")
        tries += 1
        break
    elif guess > randomNumber:
        print(Fore.MAGENTA + "Your guess is too high!")
        tries += 1
    else:
        print(Fore.MAGENTA + "Your guess is too low!")
        tries += 1

# If they don't have any more attempts, tell them they lost.
else:
    print(Fore.RED + "You lost!")

import random

startRange = int(input("Enter the starting range: "))
endRange = int(input("Enter the ending range: "))
attempt = int(input("Enter the number of attempts: "))

randomNumber = random.randint(startRange, endRange)

tries = 0

while tries < attempt:
    guess = int(input("Enter your guess: "))
    tries += 1
    if guess == randomNumber:
        print(f"You guessed the correct number! In {tries} tries.")
        break
    elif guess < randomNumber:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")
else:
    print("You are out of tries!")
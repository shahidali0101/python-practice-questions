"""  
Number Guessing Game

Description:
A simple command-line game where the user tries to guess
a randomly generated number between 1 and 50.

Features:
- Random number generation 
- Hint system (higher/lower)
- Attempt counter

"""

import random

# Generate random number
JACKPOT_NUMBER = random.randint(1, 50)

# Attempt counter
attempts = 1

# User input
guess = int(input("Enter a number between 1 and 50: "))

# Game loop
while guess != JACKPOT_NUMBER:

    if guess < JACKPOT_NUMBER:
        print("Guess higher ")
    else:
        print("Guess lower ")

    guess = int(input("Enter a number between 1 and 50: "))
    attempts += 1

# Win message
print("\n🎉 Congratulations! You guessed it right!")
print(f"You took {attempts} attempt(s) to win.")


import random

print(" Dice Guessing Game")
print("Guess a number from 1 to 6. Type 'q' to quit.\n")

while True:
    dice = random.randint(1, 6)
    user = input("Enter your guess (1-6): ")

    if user.lower() == 'q':
        print("Thanks for playing! 👋")
        break

    if not user.isdigit():
        print("Please enter a valid number.\n")
        continue

    user = int(user)

    if user < 1 or user > 6:
        print("Number must be between 1 and 6.\n")
        continue

    print(f"Computer rolled: {dice}")

    if dice == user:
        print("🎉 You won!!\n")
        break
    else:
        print("❌ Computer won! Try again.\n")




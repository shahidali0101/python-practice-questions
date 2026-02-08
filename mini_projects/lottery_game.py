

import random
import time

sct = random.randint(1, 100)

print("Welcome to Lottery Game!")
time.sleep(1)
 
for i in range(5):
    user = int(input("Please enter a number: "))
    print("Checking your number...")
    time.sleep(1.5)

    if user == sct:
        print("🎉 You won the lottery!")
        break
    else:
        print("❌ Better luck next time")
        time.sleep(1)

print("🏆 Lottery number was:", sct)

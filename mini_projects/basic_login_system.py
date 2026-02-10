"""
Simple Login System in Python

Features:
- Basic email validation
- Password verification
- Retry option for incorrect password

Author: Shahid Ali
"""

# Take email input from user
email = input("Enter your email here: ")

# Check if email contains '@'
if '@' not in email:
    print("Your email is invalid")

else:
    # Take password input
    password = input("Enter your password here: ")

    # Stored correct credentials
    CORRECT_EMAIL = "shahids.user@gmail.com"
    CORRECT_PASSWORD = "654123"

    # Case 1: Correct email and password
    if email == CORRECT_EMAIL and password == CORRECT_PASSWORD:
        print("Welcome! You are successfully logged in")

    # Case 2: Correct email but wrong password
    elif email == CORRECT_EMAIL and password != CORRECT_PASSWORD:
        print("Your password is incorrect")
        password = input("Enter your password again: ")

        if password == CORRECT_PASSWORD:
            print("You are successfully logged in")
        else:
            print("Still incorrect password")

    # Case 3: Incorrect email
    else:
        print("Incorrect User ID or password")


   

print("   Calculator   ")
print("_" * 30)

print("press  +  to Add") 
print("press  -  to Subtract") 
print("press  *  to Multiply") 
print("press  /  to Divide")   
print("press  !  to Factorial")
print("_" * 30)

choose = input("Press to calculate (+ - * / !) : ")

# Factorial
if choose == "!":
    user = int(input("Enter number to find factorial: "))
    fact = 1
    for i in range(1, user + 1):
        fact = fact * i
    print("The factorial is:", fact)

# Other operations
elif choose in ["+", "-", "*", "/"]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choose == "+":
        print("Result:", num1 + num2)

    elif choose == "-":
        print("Result:", num1 - num2)

    elif choose == "*":
        print("Result:", num1 * num2)

    elif choose == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result:", num1 / num2)

else:
    print("Invalid Operator")

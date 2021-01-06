#!/usr/bin/env python3

# defining operations
operators = ["+", "-", "/", "*"]


# calculating functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


def multiply(x, y):
    return x * y


# input request from user with validation
def asknumber():
    try:
        userchoice = float(input("Input a number\n"))
        return userchoice
    except:
        print("NaN mah dude")
        asknumber()


def askoperand():
    userchoice = input(f"Choose operand {operators}\n")
    if userchoice in operators:
        return userchoice
    else:
        print("Not an valid operand mah dude")
        askoperand()


# While loop

while True:
    userx = asknumber()
    usery = asknumber()
    operand = askoperand()
    if operand == "+":
        print(userx, operand, usery, "=", add(userx, usery))
    elif operand == "-":
        print(userx, operand, usery, "=", subtract(userx, usery))
    elif operand == "/":
        print(userx, operand, usery, "=", divide(userx, usery))
    elif operand == "*":
        print(userx, operand, usery, "=", multiply(userx, usery))
    else:
        print("something went wrong")
    calcagain = input("Do you want to calculate again? [Y/N]")
    if calcagain.upper() == "Y":
        print("Okay more math")
    elif calcagain.upper() == "N":
        print("Okay dueces")
        break
    else:
        print("Invalid input. We do more math now.")




import sys

try:
    print(0/0)

except ZeroDivisionError:
    print("You can't divide by zero!")
# Spits out "You can't divide by zero!"


# print(1/0)
# Spits out "ZeroDivisionError: division by zero"


try:
    number = int(input("Enter a number between 1 - 10  :"))

except ValueError:
    print("Error ~ Please input a numeric value")
    sys.exit()
    # sys.exit() Stops Python.

print(f"{number}, Thank you for your submission.")

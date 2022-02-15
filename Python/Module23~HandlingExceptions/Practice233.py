import sys

try:
    number = int(input("Enter a number between 1 - 10  :"))

except ValueError:
    print("Error ~ Please input a numeric value")
    sys.exit()
    # sys.exit() Stops Python.

else:
    if number > 10:
        print("Error ~ Please input Number less than 11")
        sys.exit()
    elif number < 0:
        print("Error ~ Please input Number more than 0")
        sys.exit()


print(f"{number}, Thank you for your submission.")

# Error Checking

text = input("Give me a Number:  ")
try:
    num = int(text)
    print("The number you gave is:  ", num)
except ValueError:
    print("Please input a numeric value (1-999)")

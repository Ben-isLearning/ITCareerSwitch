# Create 3 variables and assign them the values of 10, 20 and 30.
# Only use 1 line of code.

a, b, c = 10, 20, 30
print(a, b, c)

# Prints 10 20 30


# Create 4 variables and assign them the values of 33, "car" 2.158 and "hey".
# Only use 1 line of code.

aa, bb, cc, dd = 33, "car", 2.158, "hey"
print(aa, bb, cc, dd)
# Prints 333 car 2.158 hey


# Create multiple assignment operator and create 3 key/value pairs using
# (Dave, 41; Bob, 28; Mark, 38)
# Loop through these
# Print using an F-string.

ages = {"Dave": '41', "Bob": '22', "Mark": '38'}
for key, value in ages.items():
    print(f"{key} is {value} years old")

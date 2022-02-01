# Create a variable and assign it the integer value of 15.
# Then have the code display the type of variable used.

variable = 15
print(type(variable))
# Prints <class 'int'>


# Create a variable and assign it the float value of 6.1234
# Then have the code display the type of variable used.

float_value = 6.1234
print(type(float_value))
# Prints <class 'float'>


# Create a variable and assign it a Boolean value, so when you print the variable,
# You get a value of True returned.

bool_value = True
print(bool_value)
# Prints True


# Create 3 string variables.
# Concatenate them together.

this = "abc"
one = "def"
pls = "ghi"

print(this + " " + one + " " + pls)
# This is Old-school Concatenation

print(f"{this} {one} {pls}")
# This is new-school Concatenation

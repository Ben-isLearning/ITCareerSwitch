fruit = ["apple", "banana"]
alpha = ["apple", "banana"]
beta = fruit

print(f"{fruit} {alpha} {beta}")
# All 3 lists print the same values.

print(fruit is beta)
# True ~ variable "fruit" and variable "beta" are the same object.

print(fruit is alpha)
# False ~ variable "fruit" and variable "alpha" are NOT the same object.

print("------------------")

print(fruit is not beta)
# False ~ variable "fruit" and variable "beta" are the same object.

print(fruit is not alpha)
# True ~ variable "fruit" and variable "alpha" are NOT the same object.

# is          True if both are the same       a is b
# is not      True if both are NOT the same   a is not c
